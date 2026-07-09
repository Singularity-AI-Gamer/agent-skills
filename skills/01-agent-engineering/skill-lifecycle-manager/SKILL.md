---
name: skill-lifecycle-manager
description: Use when managing skills across local/global/project roots, Skill Hub repositories, skills.sh/find-skills, GitHub sources, plugin caches, or system skills; when the user asks to search, compare, recommend, install, update, upgrade, sync, pull, push, merge, audit, deduplicate, clean up, package, publish, validate, or choose scope for skills; or when skill-upgrade, check_upstreams.ps1, sync-pull.ps1, sync-push.ps1, setup-junctions.ps1, skills-lock.json, skill-upstreams.json, npx skills check/update, GitHub stars, install counts, or source verification are involved.
---

# Skill Lifecycle Manager

Use this skill as the orchestration layer for skill work. Treat search,
installation, local upgrades, GitHub/Skill Hub synchronization, cleanup, and
quality audit as one lifecycle instead of separate one-off chores.

## Core Contract

Maintain three boundaries throughout the task:

- **Source**: where the skill came from, such as GitHub, skills.sh, a Skill Hub
  checkout, MCP Market, or a local repository.
- **Install**: where the runtime loads the active skill from, such as a global
  user skill root or a project-level skill root.
- **Ownership**: whether the path is user-maintained, project-maintained, or
  system/plugin-managed.

Do not collapse these into one mental bucket. A Skill Hub repository, a
checked-out `_repos` copy, a plugin cache copy, and an installed global skill
may all contain the same skill name while having different owners and update
rules.

When evidence is incomplete, report:

- Known facts
- Candidate hypotheses
- Validation paths
- Temporary mitigation if needed

Do not present an unverified hypothesis as the cause of a problem or as a final
fix.

## Start With Lifecycle Triage

Before acting, make a compact task card for yourself:

- **Intent**: discover, recommend, install, update, sync, pull, push, merge,
  audit, cleanup, package, publish, or create/edit.
- **Target**: skill name, source URL, repo path, local path, or broad topic.
- **Scope**: project-level, global/user-level, source repository, or unknown.
- **Destructive risk**: none, overwrite, delete, move, or cleanup.
- **Evidence needed**: source proof, usage proof, version proof, or quality
  proof.
- **Companion skill**: `find-skills`, `skill-installer`, `skill-creator`, the
  predecessor `skill-upgrade`, or no companion.

Proceed without asking when the target and scope are clear. Ask a short
question only when a reasonable assumption could install, overwrite, or delete
the wrong skill.

## Skill Stores And Ownership

Discover actual roots before editing. Common roots include:

- User/global roots: `~/.agents/skills`, `~/.codex/skills`, or the configured
  `$CODEX_HOME/skills`.
- Project roots: a project-local skills directory if the current workspace uses
  one.
- Source checkouts: `_repos`, Skill Hub clones, Git submodules, or manually
  cloned repositories.
- Managed roots: `.system` skills and plugin cache skills.
- Upgrade evidence indexes: `_meta/skill-upstreams.json` in a Skill Hub-style
  repository when present.

Treat managed roots as read-only unless the user explicitly asks to override a
managed skill. Treat source checkouts as source evidence, not automatically as
the active install target.

Keep an internal table with:

| Skill | Source path or URL | Active install path | Owner | Action |
| --- | --- | --- | --- | --- |

## Skill Hub Sync Model

When a local Skill Hub repository is present, treat it as a structured source
repository, not as the runtime install root.

The observed Skill Hub layout is:

- `skills/<domain>/<skill>/`: shared skills intended for reuse across agents.
- `projects/<project>/<skill>/`: project-private skills; do not flatten these
  into global roots through normal shared-skill sync.
- `_meta/skills-lock.json`: machine-readable mapping from skill name to repo
  path for shared skills and project skills.
- `_meta/skill-upstreams.json`: evidence-backed upstream source index used by
  the predecessor `skill-upgrade` workflow.
- `scripts/sync-pull.ps1`: pull shared repo skills into a flat local root.
- `scripts/sync-push.ps1`: push mapped flat local skills into the grouped repo.
- `scripts/setup-junctions.ps1`: make multiple agent skill roots point to one
  shared local source through Windows directory junctions.
- `skills/01-agent-engineering/skill-upgrade/scripts/check_upstreams.ps1`, when
  present: read-only or applied audit for upstream drift.

Keep these variables distinct:

- `SKILL_HUB_LOCAL_SOURCE`: used by `sync-pull.ps1` and `sync-push.ps1` as the
  flat local skill root.
- `SKILL_HUB_SOURCE`: used by `setup-junctions.ps1` as the single source
  directory for junction targets.

The scripts have destructive live behavior because they clear destination
directories before copying. Run `-DryRun` first, read the output, and create a
backup before any live pull, push, or junction setup.

### Repo To Local

Use this when the user wants the Skill Hub repo version installed or refreshed
in a local flat skill root.

```powershell
.\scripts\sync-pull.ps1 -LocalTarget "<local-skill-root>" -RepoRoot "<Skill-hub>" -DryRun
```

Facts from the local script:

- It scans only `RepoRoot\skills\`, not `projects\`.
- It recursively finds `SKILL.md` directories and flattens by directory name.
- Same-name skills in multiple repo paths are reported as conflicts and skipped.
- In live mode, it removes the target skill directory and copies the repo copy.

Before live mode:

- Confirm `LocalTarget` is the intended root, such as `~/.agents/skills` or
  `~/.codex/skills`.
- Back up any target skill that will be overwritten.
- Check whether the local copy contains user edits that should be merged
  instead of replaced.

### Local To Repo

Use this when the user wants local flat skills saved back into Skill Hub.

```powershell
.\scripts\sync-push.ps1 -LocalSource "<local-skill-root>" -RepoRoot "<Skill-hub>" -DryRun
```

Facts from the local script:

- It reads `_meta/skills-lock.json` to map skill name to repo path.
- It only pushes shared skills in the lock's `shared` or `skills` mapping.
- It skips project-private entries for normal flat sync.
- It reports unmapped local skills and does not auto-classify them.
- In live mode, it removes the mapped repo destination and copies the local
  skill directory.

If a local skill is unmapped:

- Do not run live push and hope it lands in the right place.
- Decide whether it is shared or project-private.
- For a shared agent-engineering skill, a typical path is
  `skills/01-agent-engineering/<skill-name>/`.
- Add or update `_meta/skills-lock.json`, then rebuild indexes with the repo's
  index script if present.

### Junction Single Source

Use this only when the user explicitly wants several agent runtimes to share
one physical skill root.

```powershell
.\scripts\setup-junctions.ps1 -Source "<single-source-root>" -Targets "<target1>;<target2>" -DryRun
```

Facts from the local script:

- It backs up existing target directories as `<path>.old-<timestamp>`.
- It creates Windows directory junctions with `mklink /J`.
- It verifies by comparing the number of `SKILL.md` directories.
- Its default targets may not include every runtime currently in use. In this
  environment, include `~/.agents/skills` explicitly when that root should
  share the same source.

Do not choose junctions as the default upgrade mechanism. Junctions change
ownership and blast radius. Prefer explicit pull/push or targeted copy unless
the user asks for a single shared source.

## Upstream Source Audit

The older upgrade skill is named `skill-upgrade`. When you find it in a Skill
Hub repo, treat it as the source for upstream-audit behavior and preserve these
rules in this lifecycle workflow.

Use `_meta/skill-upstreams.json` when present. It records:

- `name`: skill frontmatter name.
- `path`: repository-local skill path ending with `/`.
- `classification`: `open-source`, `self`, `local`, `candidate`, or `unknown`.
- `upstream.url`, `upstream.path`, `upstream.ref`: verified upstream source.
- `lastChecked.commit`: upstream commit checked.
- `updatePolicy`: `mirror`, `mapped`, `manual`, or `none`.
- `notes`, `evidence`, and `verificationPath`: why the classification is safe
  or not safe.

Interpret update policies conservatively:

| Policy | Meaning | Allowed action |
| --- | --- | --- |
| `mirror` | Local copy should match verified upstream exactly. | Replace only after backup and normalized diff evidence. |
| `mapped` | Local copy intentionally adapts upstream. | Apply declared mapping; preserve documented local changes. |
| `manual` | Human review required. | Produce diff and recommendation only. |
| `none` | Self/local/project skill or unverified source. | Do not overwrite. |

Never upgrade by name alone. Verify original upstream by at least one strong
signal: explicit URL in the skill, exact directory/content match against a
repository, official vendor repository, or a prior source entry in
`_meta/skill-upstreams.json`.

### check_upstreams Helper

This skill bundles the predecessor helper at
`scripts/check_upstreams.ps1`. Prefer the repo's own copy if working inside a
Skill Hub that already contains `skill-upgrade`; otherwise use this bundled
copy.

Read-only repository audit:

```powershell
.\scripts\check_upstreams.ps1 -Mode Repo -RepoRoot "<Skill-hub>"
```

Read-only local audit:

```powershell
.\scripts\check_upstreams.ps1 -Mode Local -SkillRoots "<root1>","<root2>"
```

Applied repository audit:

```powershell
.\scripts\check_upstreams.ps1 -Mode Repo -RepoRoot "<Skill-hub>" -Apply
```

Applied local audit:

```powershell
.\scripts\check_upstreams.ps1 -Mode Local -SkillRoots "<root1>","<root2>" -Apply
```

Without `-Apply`, the helper must be treated as an audit command. With
`-Apply`, repository mode mirrors only entries whose source index permits
automatic update, and local mode only fast-forwards clean git-backed source
repositories. It must not replace standalone copied skills unless full source
evidence exists.

## Discovery And Sourcing

For open ecosystem discovery, use the existing discovery stack rather than
inventing a new search process:

- Use `find-skills` and `npx skills find <query>` for skills.sh ecosystem
  discovery.
- Use GitHub CLI when available for repository proof, stars, update activity,
  license, and raw file inspection.
- Search with English and Chinese query variants when the user's need is
  bilingual or China-specific.
- Check popular sources and leaderboards before long-tail repositories.

Quality thresholds are evidence, not absolute rules:

- Prefer skills with 1K+ installs when skills.sh install counts exist.
- Prefer repositories with 100+ GitHub stars when GitHub stars are relevant.
- Treat official or widely used publishers as stronger evidence.
- Treat 0-star or unknown-source skills as experimental unless the user asks
  for niche exploration or no stronger candidate exists.

Verify every candidate before recommending or installing:

- Resolve the actual source repository, path, branch/ref, and skill directory.
- Read the candidate `SKILL.md` before trusting the search result.
- Confirm the skill name matches the requested capability and is not a
  same-name false positive.
- Check license, last update activity, scripts, dependencies, network behavior,
  and destructive operations.
- Record whether install count, stars, and source reputation were observed or
  unavailable.

## Install Scope Decision

Choose the smallest scope that still fits the user's repeated workflow.

Use global/user-level install when:

- The workflow is broadly reusable across projects.
- The skill is trusted, stable, and not tied to one repository.
- The user explicitly asks for global install.

Use project-level install when:

- The skill encodes project-specific conventions, private workflows, or local
  architecture.
- The skill is experimental and should not affect unrelated sessions.
- The skill competes with another global skill and may overtrigger elsewhere.

Before installing:

- Check whether the same skill name already exists in any active root.
- Compare source and installed versions when possible.
- Avoid duplicate installs unless the user intentionally wants both project and
  global versions.
- Prefer updating or merging an existing user-maintained copy over creating a
  same-name duplicate.

After installing or updating, tell the user whether Codex or the host app needs
to restart to load the new skill metadata.

## Upgrade And Merge Workflow

Separate source updates from active install updates:

1. **Update source evidence**: inspect or update the GitHub/Skill Hub checkout,
   branch, tag, or release.
2. **Compare versions**: diff upstream `SKILL.md`, references, scripts, assets,
   and evals against the installed copy.
3. **Protect local edits**: back up the installed skill before overwriting or
   merging.
4. **Apply the selected change**: copy, patch, or merge only the intended skill
   files.
5. **Validate**: run schema/static checks and any bundled tests or eval checks.
6. **Report**: list source ref, target path, backup path, files changed, and
   validation results.

Use a timestamped backup path such as:

```text
<skill-root>/.backups/<skill-name>-before-<operation>-<YYYYMMDD-HHMMSS>/
```

When upstream and local versions both changed, do not guess which should win.
Summarize the diff by behavior:

- Triggering/description changes
- Tool or dependency changes
- Safety or destructive-operation changes
- Output format changes
- Scripts, references, assets, or eval changes

Then merge changes that preserve the user's intended behavior. If a conflict
changes behavior materially, report the known facts and ask for a decision.

For Skill Hub work, classify the operation before touching files:

| Mode | User intent | Primary command or action | Main risk |
| --- | --- | --- | --- |
| Repo to local | "pull/update/install from Skill Hub" | `sync-pull.ps1 -DryRun`, then live only after backup | Overwriting local edits |
| Local to repo | "save/push my local skill to Skill Hub" | `sync-push.ps1 -DryRun`, with lock mapping first | Wrong category or unmapped skill |
| Manual merge | "both sides changed" | Compare repo path and local root, patch only intended files | Losing trigger or behavior changes |
| Junction setup | "make agents share one skill root" | `setup-junctions.ps1 -DryRun`, then live if accepted | Replacing real dirs with links |

Use `git status` in the Skill Hub repo before live sync. If the repo is dirty,
include the dirty state in the report and avoid broad sync unless the dirty
files are part of the requested operation.

When the repo has `_meta/skill-upstreams.json`, run an upstream audit before
deciding to mirror or merge. If the source index is missing, do not invent
upstream truth. Create an inventory report first and classify entries as
`candidate`, `unknown`, `self`, or `local` until verified.

When syncing a newly created skill into Skill Hub:

- If it is broadly reusable across projects, classify it under `skills/`.
- If it is only for one repo or client workflow, classify it under `projects/`.
- Add a `skills-lock.json` mapping before using `sync-push.ps1`.
- Rebuild `_meta/by-name.md`, `_meta/by-domain.md`, and `_meta/by-platform.md`
  with the repo script if available.
- Validate the installed copy and the repo copy separately when both exist.

## Quality Audit Gate

For each audited skill, check:

- `SKILL.md` exists and has valid frontmatter with `name` and `description`.
- The description is specific and trigger-oriented, not just a generic summary.
- The body stays reasonably compact; move large material into `references/`.
- Referenced `scripts/`, `references/`, and `assets/` paths exist.
- Scripts do not contain surprising network, credential, destructive, or
  persistence behavior.
- Dependencies and required CLIs are documented.
- The skill does not assume unavailable MCP tools or private services without
  saying so.
- Local absolute paths are avoided unless they are clearly examples.
- There are no secrets, tokens, API keys, or private data.
- There are no emoji icons, Unicode pseudo-icons, handwritten SVG icon paths,
  or mixed icon conventions in UI-related instructions.
- Objective workflows include realistic eval prompts or test fixtures.

For quality claims, distinguish observed evidence from judgement. Example:
"Observed: the skill has eval prompts and no scripts. Judgement: low operational
risk. Unverified: real-world trigger accuracy."

## Usage Audit And Cleanup

Do not use filesystem `LastAccessTime` as usage evidence. Skill loaders,
searches, backups, and audits can touch files and pollute access times.

Prefer evidence in this order:

- Explicit user request to use a skill.
- Conversation or session logs showing the skill name triggered.
- Tool output showing the concrete `SKILL.md` was read for a task.
- Available-skills metadata showing the skill was loadable.
- Repository or filesystem presence only.

Classify cleanup candidates with evidence labels:

- **Confirmed active**: explicit usage evidence exists.
- **Likely active**: recent task context strongly maps to the skill, but the
  log evidence is partial.
- **Installed but no observed usage**: loadable or present, but no explicit use
  evidence was found.
- **Duplicate candidate**: same or near-same skill appears in multiple roots.
- **Managed**: plugin or system-owned; do not remove as normal cleanup.

When removing or moving files on Windows:

- Resolve the absolute target path first.
- Verify the resolved path is inside the intended skill root or backup root.
- Never operate on a computed path that resolves to a root directory itself.
- Prefer quarantine or backup moves for uncertain cleanup.
- Use one shell end-to-end for file operations; do not pipe path lists into a
  different shell for deletion.

## Packaging And Publishing

For skills intended for sharing:

- Run the quality audit first.
- Keep the package minimal: `SKILL.md`, required references, scripts, assets,
  and evals.
- Remove local caches, generated outputs, logs, secrets, and personal paths.
- Record source provenance and version if the package is derived from another
  repository.
- If publishing to GitHub or a Skill Hub, keep the source repository and the
  installed runtime copy synchronized deliberately rather than by accidental
  copy-paste.

## Validation

Use the strongest available validation for the change:

- Parse the frontmatter and confirm required fields.
- Run any available skill validation script from `skill-creator` or the local
  ecosystem.
- Run `scripts/check_upstreams.ps1` in read-only mode when upgrading Skill Hub
  or local skill roots against upstream sources.
- Run `npx skills check` or relevant skills.sh commands when working with that
  ecosystem.
- For scripts, run a minimal safe command or dry run.
- For objective workflows, create or update `evals/evals.json`.

If validation tooling is missing, say that it is missing and perform a manual
static check instead.

## Reporting Templates

Discovery report:

| Candidate | Source | Installs | Stars | Source verified | Scope | Decision |
| --- | --- | --- | --- | --- | --- | --- |

Upgrade report:

```text
Source:
Target:
Backup:
Changed files:
Validation:
Unverified:
Restart needed:
```

Skill Hub sync report:

```text
RepoRoot:
Mode:
Local root:
Mapped path:
Dry-run result:
Backup:
Live action:
Index rebuild:
Validation:
Unmapped or conflicts:
Unverified:
```

Upstream audit report:

```text
Mode:
Source index:
Checked roots:
Upgraded:
Current:
Dirty or blocked:
Unverified candidates:
Source-index coverage:
Apply used:
Validation:
Unverified:
```

Cleanup report:

```text
Root scanned:
Evidence method:
Confirmed active:
No observed usage:
Duplicates:
Managed paths skipped:
Actions taken:
Quarantine/backup:
Unverified:
```

Quality audit report:

```text
Skill:
Pass:
Findings:
Risks:
Missing evidence:
Recommended next validation:
```

## Stop Conditions

Stop and ask before proceeding when:

- The source cannot be verified and installation would trust unknown code.
- The action would overwrite local edits with no backup or clear merge rule.
- The delete/move target cannot be proven to be inside the intended root.
- The target path is system/plugin-managed and the user did not explicitly ask
  to override it.
- Credentials, admin approval, license terms, or interactive authentication are
  required.
- The user asks for a conclusion that the evidence does not support.

In these cases, provide known facts, candidate hypotheses, validation paths, and
temporary mitigation rather than an unverified fix.
