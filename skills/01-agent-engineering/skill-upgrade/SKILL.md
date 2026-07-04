---
name: skill-upgrade
description: Use when a user asks to audit, compare, or upgrade Skill Hub repositories or local SKILL.md directories against original upstream sources, especially when source evidence may be incomplete.
---

# Skill Upgrade

Use this skill to keep a Skill Hub repository or a user's local skill installation aligned with verified upstream skill sources without overwriting local, self-made, or project-specific skills on weak evidence.

## Evidence Rules

- Do not upgrade a skill unless the original upstream is verified by at least one strong signal: an explicit URL in the skill, exact directory/content match against a repository, official vendor repository, or a prior source entry in `_meta/skill-upstreams.json`.
- If evidence is incomplete, report known facts, candidate hypotheses, verification paths, and optional temporary mitigation. Mark the conclusion as unverified.
- Treat self-made, project-private, and locally adapted skills as manual unless their source entry explicitly permits automatic mirroring.
- Preserve the user's working tree. Check `git status --short` before edits and never revert unrelated changes.

## Choose the Mode

| Mode | Use when | Main evidence source |
|---|---|---|
| Skill Hub repository | The current workspace has `skills/`, `projects/`, and `_meta/skill-upstreams.json`. | The source index plus normalized upstream directory comparison. |
| Local installation | The user asks to check `~/.codex/skills`, `~/.agents/skills`, project skill folders, or another local skill root. | Git remotes in `_repos`, explicit upstream URLs, and optional source-index files. |
| Mixed | The user asks to upgrade both a Skill Hub and installed local skills. | Run repository mode first, then local mode, and keep the results separate. |

## Source Index

In a Skill Hub repository, read `_meta/skill-upstreams.json` before auditing. For every new skill, add or update one entry:

- `name`: skill frontmatter name.
- `path`: local repository path ending with `/`.
- `classification`: `open-source`, `self`, `local`, `candidate`, or `unknown`.
- `upstream.url`: repository URL when verified.
- `upstream.path`: directory path inside upstream repository.
- `upstream.ref`: branch, tag, or commit used for comparison.
- `lastChecked.commit`: upstream commit SHA checked.
- `updatePolicy`: `mirror`, `mapped`, `manual`, or `none`.
- `notes`: short reason for the classification or mapping.

Use `candidate` only when a likely source exists but has not been proven safe for overwrite.

For local installations, prefer a compatible source-index file when it exists. If it does not exist, create an inventory report first and upgrade only git-backed repositories that can fast-forward cleanly.

## Repository Workflow

1. Confirm repo state with `git status --short`, current branch, remote, and default branch.
2. Enumerate `skills/**/SKILL.md` and `projects/**/SKILL.md`; compare the set with `_meta/skill-upstreams.json`.
3. For missing entries, inspect `SKILL.md`, README files, licenses, and embedded GitHub links. Then search by exact skill name and one unique phrase from the skill body.
4. For verified source entries, fetch upstream at the recorded ref and compare normalized file hashes, ignoring `.git`, line-ending differences, and UTF-8 BOM.
5. Upgrade only entries whose `updatePolicy` allows it:
   - `mirror`: replace the local skill directory with upstream content.
   - `mapped`: apply the declared path mapping and preserve documented local adaptations.
   - `manual`: do not overwrite; produce a diff summary and recommendation.
   - `none`: record as current or not externally updateable.
6. After edits, update `_meta/skill-upstreams.json` with the checked commit and result.
7. Run `scripts/build-indexes.ps1` if any skill was added, removed, renamed, or had frontmatter `name` or `description` changed.
8. Validate with JSON parsing, frontmatter scan, and `git diff --check`.
9. Final output must list upgraded skills, current/no-op skills, unverified candidates, and whether source-index coverage improved.

## Local Installation Workflow

1. Enumerate all configured skill roots. Default roots are `~/.codex/skills` and `~/.agents/skills`; include project-specific roots only when the user names them.
2. For each `SKILL.md`, record the skill name, directory, whether it is inside a git repository, git remote, branch, HEAD commit, and any embedded GitHub URLs.
3. Fast-forward git-backed upstream repositories only when the worktree is clean and the upstream branch is ahead. Do not rewrite history, merge, or stash.
4. For copied standalone skills, use a source index or explicit upstream URL plus full directory comparison before replacing files.
5. For candidates or local/self skills, do not overwrite. Report known facts, unverified hypotheses, and verification paths.
6. Re-scan after upgrades and summarize upgraded repositories, current repositories, dirty/blocked repositories, and unverified standalone skills.

## Helper Script

Run the helper in repository mode:

```powershell
.\skills\01-agent-engineering\skill-upgrade\scripts\check_upstreams.ps1 -Mode Repo
```

Run it against local skill roots:

```powershell
.\skills\01-agent-engineering\skill-upgrade\scripts\check_upstreams.ps1 -Mode Local
.\skills\01-agent-engineering\skill-upgrade\scripts\check_upstreams.ps1 -Mode Local -SkillRoots "$HOME\.codex\skills","$HOME\.agents\skills" -Apply
```

Without `-Apply`, the helper does not change skill content; local mode may fetch git metadata to check whether a source repository is behind. With `-Apply`, repository mode mirrors only entries whose source index permits automatic update, and local mode only fast-forwards clean git-backed source repositories.

## Output Format

Use this concise structure:

```markdown
已升级:
- skill-name: upstream repo/path @ commit, reason

已确认当前:
- skill-name: no drift

未证实/不自动覆盖:
- skill-name: known facts; candidate hypothesis; next verification path

索引建议:
- whether `_meta/skill-upstreams.json` coverage is sufficient and what remains
```
