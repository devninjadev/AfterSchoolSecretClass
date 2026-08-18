# Choi Hayoung 0.9.2 release receipt

Date: 2026-08-19 Asia/Seoul

## Scope and version

- Repository: `https://github.com/devninjadev/AfterSchoolSecretClass`
- Previously published latest release: `v0.9.1`
- Release version: `0.9.2`
- Behavior change commit: `99c72b140ac08ad91abb5bac78cc3d1bbc842760`
- Git skill-tree object: `eb97ab3c163ef094662bbbcb5baeb1559f51bb23`

Version `0.9.2` distinguishes scene narration, Hayoung's user-directed dialogue, third-party speech, and structured evidence by semantic role. Report-style endings remain valid in narration and evidence structures, while Hayoung's own dialogue is recast into natural conversational Korean even after tool use. It also loads a relevant Druckenmiller or Soros perspective when that perspective materially clarifies the user's investment question and connects it to Hayoung's interpretation and current evidence.

## Package identity

- Archive: `choi-hayoung-0.9.2.zip`
- Archive SHA-256: `a2024cbb5107b606af98e2b716522c52da063a0733f8a2d3bbec5cbbcdc594b7`
- Layout: one top-level `choi-hayoung/` directory.
- Build input: tracked `skills/choi-hayoung` tree only.
- Reproducibility: file order is sorted, entry times are normalized to 1980-01-01, and ZIP extended attributes are omitted.

## Behavior verification

- A fresh-context tool-assisted market probe retained Hayoung's conversational direct speech instead of copying report-style tool prose.
- A semantic-role probe allowed `-이다` narration while rejecting an unquoted anonymous-analysis loophole for Hayoung's user-directed explanation.
- A relevant market-liquidity probe naturally used one Druckenmiller perspective, interpreted it in Hayoung's voice, and kept current evidence separate from authority.

## Pre-publication verification

- Source suite: 19 tests, 0 failures.
- Official skill validation on source: `Skill is valid!`.
- ZIP CRC: no compressed-data errors.
- The release candidate was generated from the recorded tracked skill tree and will be revalidated after public download.

## Publication and installation gate

Publish only if remote `main` and the annotated `v0.9.2` tag resolve to the intended release commit and the GitHub Release is non-draft and non-prerelease. After publication, download the public ZIP and checksum into fresh staging, repeat checksum, CRC, validation, tests, and source parity checks, then replace `/Users/jundochang/.codex/skills/choi-hayoung` from that verified public extraction.
