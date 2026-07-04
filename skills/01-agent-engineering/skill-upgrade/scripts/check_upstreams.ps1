[CmdletBinding()]
param(
    [ValidateSet("Auto", "Repo", "Local")]
    [string]$Mode = "Auto",

    [string]$RepoRoot,
    [string]$IndexPath,
    [string[]]$SkillRoots,
    [string]$WorkDir,
    [switch]$Apply
)

$ErrorActionPreference = "Stop"

if (-not $RepoRoot) {
    $RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..")).Path
}
if (-not $IndexPath) {
    $IndexPath = Join-Path $RepoRoot "_meta\skill-upstreams.json"
}
if (-not $WorkDir) {
    $WorkDir = Join-Path $env:TEMP "skill-upstream-audit"
}
if ($Mode -eq "Auto") {
    if (Test-Path $IndexPath) { $Mode = "Repo" } else { $Mode = "Local" }
}

New-Item -ItemType Directory -Force -Path $WorkDir | Out-Null

function Invoke-Git {
    param(
        [Parameter(Mandatory = $true)][string[]]$GitArgs,
        [switch]$AllowFailure
    )

    $oldErrorActionPreference = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    try {
        $output = & git @GitArgs 2>&1
        $code = $LASTEXITCODE
    } finally {
        $ErrorActionPreference = $oldErrorActionPreference
    }
    if ($code -ne 0 -and -not $AllowFailure) {
        throw "git $($GitArgs -join ' ') failed: $($output -join "`n")"
    }
    return [pscustomobject]@{
        Code = $code
        Text = (($output | ForEach-Object { "$_" }) -join "`n").Trim()
    }
}

function Get-RepoSlug([string]$Url) {
    $u = $Url.TrimEnd("/")
    $u = $u -replace "^https://github.com/", ""
    $u = $u -replace "^git@github.com:", ""
    $u = $u -replace "\.git$", ""
    return ($u -replace "[^A-Za-z0-9_.-]+", "_")
}

function Update-UpstreamRepo([object]$Entry) {
    $url = $Entry.upstream.url
    if (-not $url) { return $null }

    $slug = Get-RepoSlug $url
    $target = Join-Path $WorkDir $slug
    $ref = $Entry.upstream.ref

    if (Test-Path (Join-Path $target ".git")) {
        $fetch = Invoke-Git -GitArgs @("-C", $target, "fetch", "--depth=1", "origin", $ref) -AllowFailure
        if ($fetch.Code -ne 0) {
            Invoke-Git -GitArgs @("-C", $target, "fetch", "--depth=1", "origin") | Out-Null
        }
        Invoke-Git -GitArgs @("-C", $target, "checkout", "--force", "FETCH_HEAD") | Out-Null
    } else {
        $clone = Invoke-Git -GitArgs @("clone", "--depth", "1", "--branch", $ref, $url, $target) -AllowFailure
        if ($clone.Code -ne 0) {
            Invoke-Git -GitArgs @("clone", "--depth", "1", $url, $target) | Out-Null
            Invoke-Git -GitArgs @("-C", $target, "fetch", "--depth=1", "origin", $ref) | Out-Null
            Invoke-Git -GitArgs @("-C", $target, "checkout", "--force", "FETCH_HEAD") | Out-Null
        }
    }

    return $target
}

function Get-NormalizedHashes([string]$Dir, [bool]$TrimTrailingWhitespace = $false) {
    $map = @{}
    if (-not (Test-Path $Dir)) { return $map }
    $resolvedDir = (Resolve-Path $Dir).Path
    Get-ChildItem -LiteralPath $Dir -Recurse -File -Force |
        Where-Object {
            $relForFilter = $_.FullName.Substring($resolvedDir.Length).TrimStart("\", "/")
            ($relForFilter -split '[\\/]') -notcontains ".git"
        } |
        ForEach-Object {
            $rel = $_.FullName.Substring($resolvedDir.Length).TrimStart("\", "/").Replace("\", "/")
            $bytes = [IO.File]::ReadAllBytes($_.FullName)
            $text = [Text.Encoding]::UTF8.GetString($bytes)
            $text = $text -replace "`r`n", "`n"
            if ($TrimTrailingWhitespace) {
                $text = $text -replace "[ `t]+(?=`n)", ""
                $text = $text -replace "(`n)+\z", "`n"
            }
            if ($text.Length -gt 0 -and $text[0] -eq [char]0xFEFF) { $text = $text.Substring(1) }
            $sha = [Security.Cryptography.SHA256]::Create()
            $hash = $sha.ComputeHash([Text.Encoding]::UTF8.GetBytes($text))
            $map[$rel] = ([BitConverter]::ToString($hash)).Replace("-", "").ToLowerInvariant()
        }
    return $map
}

function Assert-PathUnderRoot([string]$Path, [string]$Root) {
    $resolvedPath = (Resolve-Path -LiteralPath $Path).Path.TrimEnd("\", "/")
    $resolvedRoot = (Resolve-Path -LiteralPath $Root).Path.TrimEnd("\", "/")
    if (-not $resolvedPath.StartsWith($resolvedRoot, [StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing to modify path outside allowed root. Path=$resolvedPath Root=$resolvedRoot"
    }
}

function Sync-DirectoryMirror([string]$SourceDir, [string]$TargetDir, [string]$AllowedRoot) {
    Assert-PathUnderRoot -Path $TargetDir -Root $AllowedRoot
    if (-not (Test-Path $SourceDir)) { throw "Missing source directory: $SourceDir" }
    if (-not (Test-Path $TargetDir)) { New-Item -ItemType Directory -Force -Path $TargetDir | Out-Null }

    Get-ChildItem -LiteralPath $TargetDir -Force | ForEach-Object {
        Remove-Item -LiteralPath $_.FullName -Recurse -Force
    }
    Get-ChildItem -LiteralPath $SourceDir -Force | Where-Object { $_.Name -ne ".git" } | ForEach-Object {
        Copy-Item -LiteralPath $_.FullName -Destination $TargetDir -Recurse -Force
    }
}

function Invoke-RepoMode {
    if (-not (Test-Path $IndexPath)) {
        throw "Missing source index: $IndexPath"
    }

    $index = Get-Content $IndexPath -Raw -Encoding UTF8 | ConvertFrom-Json
    $results = @()
    $today = Get-Date -Format "yyyy-MM-dd"

    foreach ($entry in @($index.sources)) {
        if ($entry.classification -ne "open-source") { continue }

        $localPath = Join-Path $RepoRoot ($entry.path -replace "/", "\")
        $result = [ordered]@{
            mode = "repo"
            name = $entry.name
            path = $entry.path
            updatePolicy = $entry.updatePolicy
            upstream = $entry.upstream.url
            upstreamPath = $entry.upstream.path
            status = "unknown"
            upstreamCommit = $null
            missingLocalFiles = 0
            extraLocalFiles = 0
            changedFiles = 0
            applied = $false
        }

        if (-not (Test-Path $localPath)) {
            $result.status = "missing-local-path"
            $results += [pscustomobject]$result
            continue
        }

        try {
            $repoPath = Update-UpstreamRepo $entry
            if (-not $repoPath) {
                $result.status = "missing-upstream-url"
                $results += [pscustomobject]$result
                continue
            }

            $commit = (Invoke-Git -GitArgs @("-C", $repoPath, "rev-parse", "HEAD")).Text
            $result.upstreamCommit = $commit
            $upPath = Join-Path $repoPath ($entry.upstream.path -replace "/", "\")
            if (-not (Test-Path $upPath)) {
                $result.status = "missing-upstream-path"
                $results += [pscustomobject]$result
                continue
            }

            $trimTrailingWhitespace = $false
            if ($entry.PSObject.Properties["normalization"] -and
                $entry.normalization.PSObject.Properties["trimTrailingWhitespace"]) {
                $trimTrailingWhitespace = [bool]$entry.normalization.trimTrailingWhitespace
            }

            $local = Get-NormalizedHashes $localPath $trimTrailingWhitespace
            $up = Get-NormalizedHashes $upPath $trimTrailingWhitespace
            $localKeys = [System.Collections.Generic.HashSet[string]]::new([string[]]$local.Keys)
            $upKeys = [System.Collections.Generic.HashSet[string]]::new([string[]]$up.Keys)

            $missing = 0
            foreach ($k in $upKeys) { if (-not $localKeys.Contains($k)) { $missing++ } }
            $extra = 0
            foreach ($k in $localKeys) { if (-not $upKeys.Contains($k)) { $extra++ } }
            $changed = 0
            foreach ($k in $upKeys) {
                if ($localKeys.Contains($k) -and $local[$k] -ne $up[$k]) { $changed++ }
            }

            $result.missingLocalFiles = $missing
            $result.extraLocalFiles = $extra
            $result.changedFiles = $changed
            if (($missing + $extra + $changed) -eq 0) {
                $result.status = "current"
            } elseif ($entry.updatePolicy -eq "mapped") {
                $result.status = "mapped-drift"
            } else {
                $result.status = "drift"
            }

            if ($Apply -and $result.status -eq "drift" -and $entry.updatePolicy -eq "mirror") {
                Sync-DirectoryMirror -SourceDir $upPath -TargetDir $localPath -AllowedRoot $RepoRoot
                $result.status = "updated"
                $result.applied = $true
            }

            if ($entry.PSObject.Properties["lastChecked"]) {
                $entry.lastChecked.date = $today
                $entry.lastChecked.commit = $commit
            }
            if ($entry.PSObject.Properties["status"]) {
                $entry.status = $result.status
            }
        } catch {
            $result.status = "error: $($_.Exception.Message)"
        }

        $results += [pscustomobject]$result
    }

    if ($Apply) {
        $index.updated_at = $today
        $json = $index | ConvertTo-Json -Depth 12
        $enc = New-Object System.Text.UTF8Encoding($false)
        [IO.File]::WriteAllText($IndexPath, $json, $enc)
    }

    return [pscustomobject]@{
        mode = "repo"
        apply = [bool]$Apply
        indexPath = $IndexPath
        results = $results
    }
}

function Read-SkillName([string]$SkillFile) {
    $lines = Get-Content -LiteralPath $SkillFile -Encoding UTF8 -TotalCount 80
    foreach ($line in $lines) {
        if ($line -match '^\s*name\s*:\s*(.+?)\s*$') {
            return ($Matches[1].Trim().Trim('"').Trim("'"))
        }
    }
    return (Split-Path -Leaf (Split-Path -Parent $SkillFile))
}

function Find-GitRoot([string]$StartDir) {
    $dir = Get-Item -LiteralPath $StartDir
    while ($dir) {
        if (Test-Path (Join-Path $dir.FullName ".git")) { return $dir.FullName }
        $dir = $dir.Parent
    }
    return $null
}

function Get-GitHubUrls([string]$SkillFile) {
    $text = Get-Content -LiteralPath $SkillFile -Raw -Encoding UTF8
    $matches = [regex]::Matches($text, 'https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_./?#=&%-]+)?')
    return @($matches | ForEach-Object { $_.Value.TrimEnd(".", ")", "]") } | Select-Object -Unique)
}

function Get-DefaultSkillRoots {
    $homeDir = [Environment]::GetFolderPath("UserProfile")
    $candidates = @(
        (Join-Path $homeDir ".codex\skills"),
        (Join-Path $homeDir ".agents\skills")
    )
    return @($candidates | Where-Object { Test-Path $_ })
}

function Invoke-LocalMode {
    if (-not $SkillRoots -or $SkillRoots.Count -eq 0) {
        $SkillRoots = Get-DefaultSkillRoots
    }
    if (-not $SkillRoots -or $SkillRoots.Count -eq 0) {
        throw "No skill roots found. Pass -SkillRoots explicitly."
    }

    $skillFiles = @()
    foreach ($root in $SkillRoots) {
        if (-not (Test-Path $root)) { continue }
        $resolvedRoot = (Resolve-Path -LiteralPath $root).Path
        $skillFiles += Get-ChildItem -LiteralPath $resolvedRoot -Recurse -File -Filter "SKILL.md" -Force |
            Where-Object { ($_.FullName -split '[\\/]') -notcontains ".git" }
    }

    $skills = @()
    foreach ($file in $skillFiles) {
        $dir = Split-Path -Parent $file.FullName
        $gitRoot = Find-GitRoot $dir
        $skills += [pscustomobject]@{
            name = Read-SkillName $file.FullName
            path = $dir
            skillFile = $file.FullName
            gitRoot = $gitRoot
            embeddedGitHubUrls = Get-GitHubUrls $file.FullName
        }
    }

    $repoResults = @()
    $gitRoots = @($skills | Where-Object { $_.gitRoot } | Select-Object -ExpandProperty gitRoot -Unique)
    foreach ($gitRoot in $gitRoots) {
        $repoSkills = @($skills | Where-Object { $_.gitRoot -eq $gitRoot } | Select-Object -ExpandProperty name)
        $remote = (Invoke-Git -GitArgs @("-C", $gitRoot, "remote", "get-url", "origin") -AllowFailure).Text
        $branch = (Invoke-Git -GitArgs @("-C", $gitRoot, "rev-parse", "--abbrev-ref", "HEAD") -AllowFailure).Text
        $head = (Invoke-Git -GitArgs @("-C", $gitRoot, "rev-parse", "HEAD") -AllowFailure).Text
        $dirty = (Invoke-Git -GitArgs @("-C", $gitRoot, "status", "--short") -AllowFailure).Text
        $upstream = (Invoke-Git -GitArgs @("-C", $gitRoot, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}") -AllowFailure).Text
        if (-not $upstream -and $branch) { $upstream = "origin/$branch" }

        $status = "unknown"
        $behind = $null
        $newHead = $head
        $applied = $false
        try {
            if ($remote) { Invoke-Git -GitArgs @("-C", $gitRoot, "fetch", "origin", "--prune") | Out-Null }
            if ($upstream) {
                $behindText = (Invoke-Git -GitArgs @("-C", $gitRoot, "rev-list", "--count", "$head..$upstream") -AllowFailure).Text
                if ($behindText -match '^\d+$') { $behind = [int]$behindText }
            }

            if (-not $remote) {
                $status = "missing-origin-remote"
            } elseif ($dirty) {
                $status = "dirty-worktree"
            } elseif ($behind -gt 0) {
                $status = "behind"
                if ($Apply) {
                    Invoke-Git -GitArgs @("-C", $gitRoot, "pull", "--ff-only") | Out-Null
                    $newHead = (Invoke-Git -GitArgs @("-C", $gitRoot, "rev-parse", "HEAD")).Text
                    $status = "updated"
                    $applied = $true
                }
            } else {
                $status = "current"
            }
        } catch {
            $status = "error: $($_.Exception.Message)"
        }

        $repoResults += [pscustomobject]@{
            gitRoot = $gitRoot
            remote = $remote
            branch = $branch
            upstream = $upstream
            head = $head
            newHead = $newHead
            behind = $behind
            status = $status
            applied = $applied
            skills = $repoSkills
        }
    }

    $standalone = @($skills | Where-Object { -not $_.gitRoot } | ForEach-Object {
        [pscustomobject]@{
            name = $_.name
            path = $_.path
            status = if ($_.embeddedGitHubUrls.Count -gt 0) { "candidate-url-found" } else { "local-or-unknown" }
            embeddedGitHubUrls = $_.embeddedGitHubUrls
            verificationPath = if ($_.embeddedGitHubUrls.Count -gt 0) {
                "Compare full directory content against the linked repository/path before overwriting."
            } else {
                "Search exact frontmatter name and a unique phrase from SKILL.md before assigning an upstream."
            }
        }
    })

    return [pscustomobject]@{
        mode = "local"
        apply = [bool]$Apply
        skillRoots = $SkillRoots
        skillCount = @($skills).Count
        gitRepositoryCount = @($repoResults).Count
        standaloneCount = @($standalone).Count
        gitRepositories = $repoResults
        standaloneSkills = $standalone
    }
}

if ($Mode -eq "Repo") {
    Invoke-RepoMode | ConvertTo-Json -Depth 10
} else {
    Invoke-LocalMode | ConvertTo-Json -Depth 10
}
