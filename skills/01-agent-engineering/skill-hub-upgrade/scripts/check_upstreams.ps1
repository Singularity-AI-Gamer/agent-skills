[CmdletBinding()]
param(
    [string]$RepoRoot,
    [string]$IndexPath,
    [string]$WorkDir
)

$ErrorActionPreference = "Stop"

if (-not $RepoRoot) {
    $RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..")).Path
}
if (-not $IndexPath) {
    $IndexPath = Join-Path $RepoRoot "_meta\skill-upstreams.json"
}
if (-not $WorkDir) {
    $WorkDir = Join-Path $env:TEMP "skillhub-upstream-audit"
}

if (-not (Test-Path $IndexPath)) {
    throw "Missing source index: $IndexPath"
}

New-Item -ItemType Directory -Force -Path $WorkDir | Out-Null

function Get-RepoSlug([string]$Url) {
    $u = $Url.TrimEnd("/")
    $u = $u -replace "^https://github.com/", ""
    $u = $u -replace "\.git$", ""
    return ($u -replace "[^A-Za-z0-9_.-]+", "_")
}

function Update-UpstreamRepo([object]$Entry) {
    $url = $Entry.upstream.url
    if (-not $url) { return $null }

    $slug = Get-RepoSlug $url
    $target = Join-Path $WorkDir $slug
    if (Test-Path (Join-Path $target ".git")) {
        git -C $target fetch --depth=1 origin $Entry.upstream.ref | Out-Null
        git -C $target checkout --force FETCH_HEAD | Out-Null
    } else {
        git clone --depth 1 --branch $Entry.upstream.ref $url $target | Out-Null
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

$index = Get-Content $IndexPath -Raw -Encoding UTF8 | ConvertFrom-Json
$results = @()

foreach ($entry in @($index.sources)) {
    if ($entry.classification -ne "open-source") { continue }

    $localPath = Join-Path $RepoRoot ($entry.path -replace "/", "\")
    $result = [ordered]@{
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

        $result.upstreamCommit = (git -C $repoPath rev-parse HEAD).Trim()
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
    } catch {
        $result.status = "error: $($_.Exception.Message)"
    }

    $results += [pscustomobject]$result
}

$results | ConvertTo-Json -Depth 6
