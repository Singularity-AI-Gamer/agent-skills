---
name: github-desktop-release
description: "GitHub Actions Windows desktop installer qualification plus GitHub Release orchestration for already-qualified desktop artifacts. Use when Codex must build, qualify, or diagnose Windows installers in GitHub Actions, or must promote, publish, resume, or authoritatively verify a GitHub Release containing Windows and/or macOS assets from one frozen source SHA. Covers Windows acceptance receipts, same-byte cross-platform promotion, signing/notarization disclosure, and Release readback. Do not use this Skill to build or qualify Electron macOS installers in GitHub Actions; use electron-development for that platform stage. Also exclude local-only packaging, non-GitHub CI, mobile/container delivery, README-only work, and app-internal updater UI."
---

# GitHub Desktop Release

Treat a desktop release as a state machine, not a build command. Keep application implementation, platform qualification, artifact identity, and public GitHub Release state as separate evidence boundaries.

## Establish scope

1. Read the repository's `AGENTS.md`, domain docs, packaging configuration, workflows, release scripts, and tests. Use CodeGraph first when the project is indexed.
2. Record the repository, default branch, full source SHA, tag, version, requested platforms/architectures, signing policy, expected assets, and authorization boundary.
3. Use this Skill as the sole owner of Windows GitHub Actions qualification and of shared GitHub Release promotion/publication. Invoke `electron-development` for Electron macOS build and qualification; do not absorb that platform stage into this Skill.
4. Keep project facts in a repository release profile, not in this Skill. Read [references/release-profile.md](references/release-profile.md), then validate it:

   ```text
   node <skill-root>/scripts/validate-release-profile.mjs --profile <project-profile.json>
   ```

5. If Windows is in scope, run the read-only adapter scan without `-OutputPath`, then read [references/stack-adapters.md](references/stack-adapters.md) and the selected adapter:

   ```powershell
   & "<skill-root>\scripts\preflight-windows-release.ps1" -ProjectRoot "<project-root>"
   ```

6. If macOS is in scope, require a qualification artifact produced under `electron-development` from the same frozen SHA. Read [references/macos-qualification.md](references/macos-qualification.md) only to validate the artifact contract used by shared promotion; do not dispatch or own the macOS build/qualification job from this Skill.

Stop at a read-only plan when repository writes, workflow dispatch, tag creation, or Release publication are not authorized.

## Freeze before spending runner time

Read [references/release-contract.md](references/release-contract.md) and [references/evidence-contract.md](references/evidence-contract.md). Before the first release qualification:

1. Freeze the source SHA, tag/version, runner labels, application toolchains, workflow identities, exact artifact set, acceptance receipts, normalization rules, and promotion inputs.
2. 在 install、build 或 acceptance 前冻结并 hash contract。Link the immutable contract hash to every platform ledger and run.
3. Replay real platform receipts through the final consumer before dispatch:

   ```text
   node <skill-root>/scripts/replay-release-evidence.mjs --profile <project-profile.json> --evidence-root <real-fixtures>
   ```

4. Use real platform-produced bytes as positive fixtures. Build negative fixtures independently from the verifier. Read [references/receipt-replay.md](references/receipt-replay.md).
5. For first-time Windows infrastructure with no real fixtures, allow at most one non-publishing Windows canary to collect receipts. Freeze those bytes, add them to the replay set, fix locally, and only then start formal qualification. Any missing macOS canary belongs to `electron-development`.
6. Assign one end-to-end evidence owner and one independent adversarial reviewer. Read [references/agent-orchestration.md](references/agent-orchestration.md).

The dispatch gate is complete only when the profile is valid, the contract is frozen, every known real receipt shape replays green, negative cases fail, and no unexplained platform representation remains.

## Qualify Windows artifacts

Dispatch Windows qualification only after the release inputs are bound to the frozen SHA and contract meaning. When macOS is also requested, `electron-development` may run its independent macOS qualification in parallel against the same frozen SHA.

For Windows qualification:

1. Checkout the full frozen SHA with read-only permissions and `persist-credentials: false`.
2. Verify the runner image and application toolchain against the frozen contract.
3. 执行 stack 专属的 locked install, build/package, native/vendor checks, and packaged smoke.
4. 对 installer 做真实安装、launch/mount, quiet/error observation, upgrade-data retention, and uninstall/eject acceptance where the platform/package supports those operations. Record unsupported gates as explicit blocked scope, not silent success.
5. Record signing or notarization status, validation result, and unsigned/unnotarized distribution impact.
6. Upload only the exact contract asset set plus contract, ledger, manifest, checksums, receipts, and sanitized diagnostics.

Windows Electron/NSIS qualification must follow [references/electron-nsis.md](references/electron-nsis.md). A macOS qualification artifact is an external input owned by `electron-development`; validate it against [references/macos-qualification.md](references/macos-qualification.md) before promotion. Qualification success proves an Actions artifact, not a public Release.

Use [assets/electron-nsis-qualification.yml](assets/electron-nsis-qualification.yml) as the fail-closed Windows qualification starting point. The bundled [assets/macos-qualification.yml](assets/macos-qualification.yml) is retained only as a contract-compatible handoff template for `electron-development`; using it does not transfer macOS execution ownership to this Skill.

Promotion is shared infrastructure, not a project adapter. Copy [scripts/github-desktop-promotion.mjs](scripts/github-desktop-promotion.mjs) and [scripts/validate-release-profile.mjs](scripts/validate-release-profile.mjs) verbatim, with the same filenames, to `.release/scripts/`; then copy [assets/github-desktop-release-promotion.yml](assets/github-desktop-release-promotion.yml) to the repository workflow path declared by the profile. Do not reimplement profile validation, artifact selection, same-SHA/contract binding, manifest hashing, resume, upload, channel, or readback logic per project. Run the vendored script's offline tests when updating it:

```text
node <skill-root>/scripts/test-github-desktop-promotion.mjs
```

## Diagnose without cloud trial-and-error

Read [references/failure-classification.md](references/failure-classification.md) and [references/failure-playbook.md](references/failure-playbook.md).

1. Classify every failure as `product`, `build`, `acceptance`, `gate-false-positive`, or `promotion` before deciding whether a rebuild is justified.
2. Preserve the run URL/ID, attempt, head SHA, runner/toolchain, failing stage, contract, manifest, receipts, and the smallest sanitized log excerpt.
3. Change one falsifiable hypothesis at a time. Replay the complete real receipt set locally before another dispatch.
4. After two consecutive failures in the same stage, stop. Do not start a third run until a unified root cause, ranked alternatives, and local red-to-green replay exist.
5. Keep binary identity and normalized semantics separate: installer/DMG/ZIP/blockmap bytes use raw SHA-256; eligible UTF-8 text may additionally use newline-canonical SHA-256. Never compare cross-OS text raw hashes as semantic identity.

## Promote the qualified bytes

Read [references/github-release-state-machine.md](references/github-release-state-machine.md).

1. Accept only unique, unexpired qualification artifacts whose workflow, run ID, attempt, head SHA, contract, manifest, and platform all match.
2. Require every requested platform to qualify the same source SHA. Promotion may download and verify artifacts; it must not install, build, or substitute a same-named artifact.
3. Pass `qualification_runs_json` as an exact platform mapping of positive integer `runId`, `attempt`, and `artifactId`. The shared script verifies the profile's workflow and artifact name in addition to those immutable identities.
4. Require every schema-v2 manifest and run ledger to bind `contractRawBytesSha256` and `profileRawBytesSha256`. `release-contract.json` and `signing.evidencePath` must be members of the exact manifest/checksum set; every required platform must carry identical contract/profile raw-byte hashes, and the latter must equal the profile file used for promotion.
5. Verify the exact asset set, raw byte hashes, signing disclosures, tag availability, default-branch ancestry, and existing draft/tag/assets in a read-only job.
6. Grant `contents: write` only to the final publish job. Resume a partial draft only when its provenance is exact and every already uploaded asset is an exact subset by name, size, state, and GitHub `sha256:` digest; upload only the missing assets. Never overwrite or delete a mismatch.
7. After the final mutation, perform bounded authoritative readback of tag target, Release state, draft/prerelease/latest flags against the profile's release-channel policy, exact assets, uploaded state, platform digests, release notes, signing/notarization disclosures, and URL. A verified draft reports `draftVerified: true` and `publicationVerified: false`; only a verified non-draft public state may report publication success.

Workflow success is not publication success. A missing or unverifiable readback leaves the release incomplete.

## Report evidence states

Report `mode`, `frozen inputs`, `qualification by platform`, `failure classification`, `signing/notarization`, `promotion identity`, `authoritative readback`, `unverified/blocked`, and `next action`.

Use only these completion claims:

- `build-success`: packaging command produced an artifact.
- `qualification-success`: a platform artifact passed its frozen acceptance contract.
- `promotion-success`: qualified bytes were promoted without rebuilding.
- `publication-success`: authoritative GitHub readback matches the full release contract and the Release is not a draft.
