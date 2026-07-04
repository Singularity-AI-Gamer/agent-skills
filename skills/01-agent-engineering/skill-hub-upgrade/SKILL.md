---
name: skill-hub-upgrade
description: Maintain Ethan's Skill-hub by finding each skill's original upstream repository, comparing local content with the upstream version, upgrading only evidence-backed open-source skills, and updating the upstream source index for future skills. Use whenever the user asks to check, update, audit, or upgrade Skill-hub skills.
---

# Skill-hub Upgrade

Use this skill to keep Skill-hub aligned with verified upstream skill sources without overwriting local or self-made skills on weak evidence.

## Evidence Rules

- Do not upgrade a skill unless the original upstream is verified by at least one strong signal: an explicit URL in the skill, exact directory/content match against a repository, official vendor repository, or a prior source entry in `_meta/skill-upstreams.json`.
- If evidence is incomplete, report known facts, candidate hypotheses, verification paths, and optional temporary mitigation. Mark the conclusion as unverified.
- Treat self-made, project-private, and locally adapted skills as manual unless their source entry explicitly permits automatic mirroring.
- Preserve the user's working tree. Check `git status --short` before edits and never revert unrelated changes.

## Source Index

Read `_meta/skill-upstreams.json` before auditing. For every new skill, add or update one entry:

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

## Upgrade Workflow

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

## Helper Script

Run the read-only audit helper when you need a quick source-index check:

```powershell
.\skills\01-agent-engineering\skill-hub-upgrade\scripts\check_upstreams.ps1
```

The helper reports missing local paths, missing upstream paths, upstream commits, and file-level drift counts. It does not modify Skill-hub.

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
