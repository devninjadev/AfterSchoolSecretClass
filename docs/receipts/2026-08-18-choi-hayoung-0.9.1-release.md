# Choi Hayoung 0.9.1 release receipt

Date: 2026-08-18 Asia/Seoul

## Scope

- Preserve Hayoung as a comprehensive investment persona.
- Relax the former blanket quotation-verification rule for ordinary character dialogue.
- Require source verification for precise attribution, dates, events, formal publication, and decision-critical evidence.
- Correct the signature quotation canon: Hayoung quotes Stanley Druckenmiller and George Soros. Warren Buffett and Ray Dalio belong to Myunghee's signature canon, although Hayoung may still compare their analytical frameworks when relevant.
- Add a primary-source registry for Soros and Druckenmiller without changing the immutable `v0.9.0` release.

## Reproducible package identity

- Source path: `skills/choi-hayoung`
- Git skill-tree object: `f41219bacb27ae1b1e0fe19b504b5840fcf57e27`
- Release archive: `choi-hayoung-0.9.1.zip`
- Archive SHA-256: `047f3c4be39b65ef91fd3b8cef3c7f0c7e8e60a5c4390e8a717fa19f522d14c9`
- Archive layout: one top-level `choi-hayoung/` directory

The candidate archive was generated from tracked files with `git archive`. Its file list and per-file SHA-256 values matched the tracked source tree before tests were run. Python bytecode caches were excluded from both the tracked archive and the comparison contract.

## Local verification

- Source contract suite: 17 tests, 0 failures.
- Extracted contract suite: 17 tests, 0 failures.
- Personal-install contract suite: 17 tests, 0 failures.
- Official skill validation on source, extraction, and personal install: `Skill is valid!`.
- ZIP CRC validation: no compressed-data errors.
- Tracked source-to-extraction file list and SHA-256 comparison: identical.
- Extraction-to-personal-install file list and SHA-256 comparison: identical.
- Personal install target: `/Users/jundochang/.codex/skills/choi-hayoung`.
- Recoverable pre-update backup: `/private/tmp/choi-hayoung-install-backup.J4DmVK/choi-hayoung`.

## Publication gates

Before declaring the release complete:

- tag the exact release commit as `v0.9.1`;
- publish the ZIP and checksum without altering `v0.9.0`;
- redownload both public assets to a fresh directory;
- verify checksum, ZIP CRC, skill validation, all 17 tests, source parity, remote branch commit, peeled tag commit, and release flags.

