# Won Myunghee Skill and Hayoung 0.9.1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish Hayoung `v0.9.1` with contextual quotation rules and primary sources, then build, install, validate, and release the independent `won-myunghee` `v0.9.0` skill.

**Architecture:** Keep the current checkout as the Hayoung repository and create `repositories/won-myunghee/` as an independently initialized Git repository excluded through the parent `.git/info/exclude`. Reuse Hayoung's validated package shapes and deterministic routing/opening scripts, but keep Myunghee's canon, CFP modules, source registry, tests, installation, remote, and release history independent.

**Tech Stack:** Markdown skill contracts, YAML ChatGPT metadata, JSON closed routing contracts, Python 3 standard-library scripts and `unittest`, Git/GitHub CLI, SHA-256, ZIP.

## Global Constraints

- Hayoung is objectively a comprehensive persona; Myunghee may subjectively see her as fast and tactical but must not reduce her to short-term trading.
- Keep signature quotation canons disjoint: Hayoung quotes Stanley Druckenmiller and George Soros; Myunghee quotes Warren Buffett and Ray Dalio. This does not prevent either comprehensive persona from comparing other investors' frameworks as analysis.
- Myunghee internal name is `won-myunghee`, display name is `명희`, invocation is `@명희`, initial release is `v0.9.0`.
- Hayoung's contextual-quotation correction is released as `v0.9.1`; existing `v0.9.0` assets remain immutable.
- Casual character dialogue may naturally use supplied quotation canon; precise wording, attribution, date, event, publication-grade use, and decision-critical quotations require source verification.
- Both skills include substantial real-source registries; no fabricated precise citation, date, document title, or source link.
- Use LLM semantic classification with deterministic closed-schema validation; do not implement a Korean keyword parser.
- `기억해 둬`, `참고해`, and preference statements never authorize a World Memory write.
- Do not automatically invoke every integration, install dependencies, generate images, or mutate World Memory.
- Do not include OAuth tokens, cookies, client secrets, mutable Notion state, desktop absolute paths, legacy hard-coded RSS URLs, or old ChatGPT GPT links.
- Do not modify or commit the existing user-owned `vendor/` directory.
- Build release ZIPs from tracked source at the tagged commit and verify public assets after redownload.

---

### Task 1: Complete and release Hayoung 0.9.1

**Files:**
- Modify: `skills/choi-hayoung/SKILL.md`
- Modify: `skills/choi-hayoung/references/persona-canon.md`
- Create: `skills/choi-hayoung/references/source-registry.md`
- Modify: `skills/choi-hayoung/tests/test_contract.py`
- Modify: `README.md`
- Create: `docs/receipts/2026-08-18-choi-hayoung-0.9.1-release.md`

**Interfaces:**
- Consumes: existing Hayoung package, tests, personal installation, GitHub repository and `v0.9.0` release.
- Produces: contextual quotation policy, source registry, `v0.9.1` tag, public `choi-hayoung-0.9.1.zip` and checksum.

- [x] **Step 1: Verify the failing quotation/source-registry contract was observed**

Recorded two RED states: the original contextual-policy contract failed because `source-registry.md` and policy markers were absent; the later persona-source separation contract failed because Hayoung's registry incorrectly included Buffett and Dalio. The corrected contract requires Druckenmiller and Soros and rejects Berkshire/Principles entries in Hayoung's signature registry.

- [ ] **Step 2: Run the completed Hayoung contracts**

Run:

```bash
python3 -m unittest discover -s skills/choi-hayoung/tests -p 'test_*.py' -v
python3 /Users/jundochang/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/choi-hayoung
```

Expected: all 17 tests pass and `Skill is valid!`.

- [ ] **Step 3: Update public version documentation**

Change README installation asset to `choi-hayoung-0.9.1.zip`, current release to `0.9.1`, and describe the contextual quotation policy plus primary-source registry.

- [ ] **Step 4: Commit release metadata**

```bash
git add README.md docs/receipts/2026-08-18-choi-hayoung-0.9.1-release.md
git commit -m "docs: prepare choi-hayoung 0.9.1 release"
```

- [ ] **Step 5: Build and validate the tracked package**

Create a temporary tracked-source archive containing `skills/choi-hayoung` under top-level `choi-hayoung/`. Generate `choi-hayoung-0.9.1.sha256`, run `unzip -tq`, extract fresh, run official validation and all 17 tests, and compare file lists and SHA-256 with source.

- [ ] **Step 6: Update the personal installation**

Replace only `/Users/jundochang/.codex/skills/choi-hayoung` with the verified package contents, then compare its file list and per-file SHA-256 to the extracted archive.

- [ ] **Step 7: Push and publish immutably**

Push `main`, create annotated tag `v0.9.1` at exact `HEAD`, push the tag, and create `Choi Hayoung Skill 0.9.1` with ZIP and checksum assets. Do not alter `v0.9.0`.

- [ ] **Step 8: Redownload and verify public assets**

Download to a fresh `/private/tmp` directory, verify checksum, ZIP CRC, official validation, 17 tests, source parity, remote `main`, peeled tag commit, and release flags.

---

### Task 2: Initialize the independent Myunghee repository and RED contracts

**Files:**
- Modify local-only: `.git/info/exclude`
- Create independent repository: `repositories/won-myunghee/.git/`
- Create: `repositories/won-myunghee/skills/won-myunghee/tests/test_contract.py`
- Create: `repositories/won-myunghee/skills/won-myunghee/tests/test_opening_selector.py`
- Create: `repositories/won-myunghee/skills/won-myunghee/tests/test_routing_contract.py`
- Create: `repositories/won-myunghee/skills/won-myunghee/tests/test_cfp_routing.py`
- Create: `repositories/won-myunghee/skills/won-myunghee/tests/test_relationship_canon.py`
- Create: `repositories/won-myunghee/skills/won-myunghee/tests/test_source_migration.py`

**Interfaces:**
- Consumes: approved design and baseline pressure evidence.
- Produces: independent Git identity and failing tests that specify the Myunghee package before production files exist.

- [ ] **Step 1: Exclude and initialize the independent repository**

Append `/repositories/won-myunghee/` to the parent `.git/info/exclude`, create the directory, run `git init -b main`, and set origin to `https://github.com/devninjadev/TheEasygoingSageoftheEconomicResearchClub.git`.

- [ ] **Step 2: Write package and metadata RED tests**

Test exact name `won-myunghee`, `display_name: "명희"`, `$won-myunghee` default prompt, icon paths, implicit invocation, required reference/script/assets, and absence of forbidden values.

- [ ] **Step 3: Write opening RED tests**

Define a wished-for `choose_opening(persona_explicit: bool, new_scene: bool, has_substantive_request: bool) -> str | None`. Assert a bare explicit call returns the canonical scene and substantive requests return `None`.

- [ ] **Step 4: Write closed route RED tests**

Define exact fields and enums from the design. Assert valid round-trip, extra-key rejection, unknown-enum rejection, `기억해 둬` fixture with `write_intent: none`, and safe default disabling integrations, image, and writes.

- [ ] **Step 5: Write CFP and relationship RED tests**

Assert retirement/tax/insurance routes carry correct freshness and jurisdiction fields. Assert objective `하영은 종합형` and subjective `명희에게 속도형·전술형으로 보임` coexist while `하영은 단타밖에 모른다` is absent.

- [ ] **Step 6: Run RED suite**

```bash
python3 -m unittest discover -s skills/won-myunghee/tests -p 'test_*.py' -v
```

Expected: failures caused by absent production files and functions, not syntax errors.

- [ ] **Step 7: Commit RED contracts**

```bash
git add skills/won-myunghee/tests
git commit -m "test: define won-myunghee skill contracts"
```

---

### Task 3: Implement the Myunghee core package and make base contracts GREEN

**Files:**
- Create: `repositories/won-myunghee/skills/won-myunghee/SKILL.md`
- Create: `repositories/won-myunghee/skills/won-myunghee/agents/openai.yaml`
- Create: `repositories/won-myunghee/skills/won-myunghee/scripts/select_opening.py`
- Create: `repositories/won-myunghee/skills/won-myunghee/scripts/validate_route.py`
- Create: `repositories/won-myunghee/skills/won-myunghee/references/routing-contract.json`
- Create: `repositories/won-myunghee/skills/won-myunghee/references/persona-canon.md`
- Create: `repositories/won-myunghee/skills/won-myunghee/references/opening-scene.md`
- Create: `repositories/won-myunghee/skills/won-myunghee/references/relationship-canon.md`
- Create: `repositories/won-myunghee/skills/won-myunghee/assets/icon.png`
- Create: `repositories/won-myunghee/skills/won-myunghee/assets/character-sheet.png`

**Interfaces:**
- Consumes: exact tests from Task 2 and supplied source images/text.
- Produces: discoverable `@명희` skill, closed route validator, deterministic opening gate, persona and relationship canon.

- [ ] **Step 1: Scaffold with official initializer**

Run `init_skill.py won-myunghee --path repositories/won-myunghee/skills --resources scripts,references,assets` with exact interface strings from the design. Remove all generated placeholders before validation.

- [ ] **Step 2: Implement route validation**

Create a standard-library validator that loads the JSON contract, requires exact keys and types, rejects unknown enums and extra keys, and exposes a safe-default object with every optional need false and `write_intent: none`.

- [ ] **Step 3: Implement opening selection**

Return the canonical opening only when persona is explicit, scene is new, and no substantive request exists. The script accepts flags and never classifies Korean text.

- [ ] **Step 4: Migrate persona and relationship canon**

Preserve dense character details and the five relationship stages. Encode objective Hayoung ground truth separately from Myunghee's subjective view. Replace exact living-writer/artist imitation with general style traits.

- [ ] **Step 5: Copy and validate visual canon**

Copy the supplied 512×512 icon and 1536×1024 character sheet. Record SHA-256 and assert image presence, size, and metadata paths.

- [ ] **Step 6: Run base GREEN tests**

Run package, opening, routing, and relationship tests until all pass; run official `quick_validate.py`.

- [ ] **Step 7: Commit core package**

```bash
git add skills/won-myunghee
git commit -m "feat: establish won-myunghee persona and routing"
```

---

### Task 4: Add CFP modules, integrations, source registry, and pressure contracts

**Files:**
- Create: `repositories/won-myunghee/skills/won-myunghee/references/cfp-core.md`
- Create: `repositories/won-myunghee/skills/won-myunghee/references/cashflow-and-debt.md`
- Create: `repositories/won-myunghee/skills/won-myunghee/references/insurance-and-risk.md`
- Create: `repositories/won-myunghee/skills/won-myunghee/references/tax-retirement-estate.md`
- Create: `repositories/won-myunghee/skills/won-myunghee/references/investment-and-portfolio.md`
- Create: `repositories/won-myunghee/skills/won-myunghee/references/financial-psychology.md`
- Create: `repositories/won-myunghee/skills/won-myunghee/references/investor-perspectives.md`
- Create: `repositories/won-myunghee/skills/won-myunghee/references/source-registry.md`
- Create: `repositories/won-myunghee/skills/won-myunghee/references/integrations.md`
- Create: `repositories/won-myunghee/skills/won-myunghee/references/world-memory-read-bridge.md`
- Create: `repositories/won-myunghee/skills/won-myunghee/references/source-migration.json`
- Create: `repositories/won-myunghee/skills/won-myunghee/tests/pressure-scenarios.json`
- Create: `repositories/won-myunghee/skills/won-myunghee/tests/test_pressure_scenarios.py`
- Create: `repositories/won-myunghee/skills/won-myunghee/tests/pressure-results.md`

**Interfaces:**
- Consumes: core routing and canon from Task 3, supplied CFP/quotation sources, exact personal World Memory bridge copied from the verified Hayoung package.
- Produces: progressive-disclosure CFP knowledge, optional integration routing, official-source lookup registry, migration receipt, deterministic pressure expectations.

- [ ] **Step 1: Split CFP source by decision domain**

Map goals/process/ethics into `cfp-core.md`; cash flow and debt into its module; insurance into its module; tax/retirement/estate into its jurisdiction-sensitive module; investment and portfolio into its module; behavior and family conflict into `financial-psychology.md`.

- [ ] **Step 2: Add contextual quotation canon**

Allow natural conversational use of supplied Buffett/Dalio canon. Require source checks only for precise attribution, formal/public use, or decision-critical evidence; prohibit invented precise citations.

- [ ] **Step 3: Add primary and official source registry**

Keep the quotation canons disjoint. Hayoung uses Soros's direct essays and lectures plus a primary USC Druckenmiller transcript. Myunghee uses Berkshire letters and SEC filings plus Dalio's official Principles publications. Do not present Buffett or Dalio as Hayoung's representative voices, and do not present Soros or Druckenmiller as Myunghee's representative voices. Put SEC Investor.gov, FPSB practice/global standards, National Tax Service, National Pension Service, Ministry of Employment and Labor retirement-pension pages, National Health Insurance Service, Korean Law Information Center, Financial Supervisory Service/FINE, and insurance consumer portals in a separate general or professional evidence layer. Explain each source role and current-date boundary.

- [ ] **Step 4: Add optional integration and World Memory references**

Document exact repository URLs, available/unavailable/unknown status, Alpaca/Wolfram/Notion roles, the exact personal saved-view bridge, one read retry, and explicit-write delegation.

- [ ] **Step 5: Complete source migration receipt**

Map every supplied source domain to preserved, transformed, or excluded output and record both image hashes. Exclude saved HTML and legacy URLs from runtime payload while retaining coverage evidence.

- [ ] **Step 6: Add and run pressure contracts**

Encode scenarios for generic-finance nonactivation, substantive-opening suppression, non-write `기억해 둬`, Hayoung relationship nuance, casual quotation naturalness, precise-citation boundary, CFP product-first rejection, and safe degraded routes.

- [ ] **Step 7: Commit CFP and integration package**

```bash
git add skills/won-myunghee
git commit -m "feat: add CFP evidence and integration contracts"
```

---

### Task 5: Validate, document, package, and install Myunghee

**Files:**
- Create: `repositories/won-myunghee/README.md`
- Create: `repositories/won-myunghee/docs/receipts/2026-08-18-won-myunghee-installation.md`

**Interfaces:**
- Consumes: complete tracked Myunghee package.
- Produces: public documentation, tested release archive/checksum, personal installation parity, local acceptance receipt.

- [ ] **Step 1: Write README**

Document `@명희`, installation, comprehensive value/CFP behavior, optional skills, plugins, World Memory disclosure, Hayoung relationship, contextual quotation rule, official-source registry, and verification.

- [ ] **Step 2: Run full source validation**

Run all tests, official validation, forbidden-value scan, image metadata/hash checks, and `git diff --check`.

- [ ] **Step 3: Build from tracked source**

Use tracked `HEAD` to build `/private/tmp/won-myunghee-0.9.0.zip` with top-level `won-myunghee/` and a matching checksum file. Run ZIP CRC.

- [ ] **Step 4: Validate a fresh extraction**

Extract into a new temporary directory, run official validation and all tests, then compare file lists and per-file SHA-256 to tracked source.

- [ ] **Step 5: Install verified package**

Install at `/Users/jundochang/.codex/skills/won-myunghee`, then compare it file-for-file and hash-for-hash with the extracted release package.

- [ ] **Step 6: Record local receipt and commit**

Record commands, counts, hashes, limitations, and the distinction between local metadata and live `@` picker acceptance.

```bash
git add README.md docs/receipts/2026-08-18-won-myunghee-installation.md
git commit -m "build: package and install won-myunghee skill"
```

---

### Task 6: Publish and redownload-verify Myunghee 0.9.0

**Files:**
- No additional tracked package files unless verification reveals a tested defect.

**Interfaces:**
- Consumes: exact tested Myunghee `HEAD`, ZIP, checksum, remote repository.
- Produces: public `main`, annotated `v0.9.0`, GitHub Release and remote-asset verification receipt.

- [ ] **Step 1: Confirm remote is still safe to initialize**

Use GitHub plugin/API and `git ls-remote` to verify no unexpected commits, tags, or releases appeared. Stop on non-empty conflicting state.

- [ ] **Step 2: Push source and exact tag**

Push `main`, create annotated `v0.9.0` at exact `HEAD`, verify the peeled tag target, and push it.

- [ ] **Step 3: Create release**

Publish `Won Myunghee Skill 0.9.0` as non-draft, non-prerelease with `won-myunghee-0.9.0.zip` and checksum.

- [ ] **Step 4: Redownload public assets**

Download into a fresh temporary directory and verify checksum, ZIP CRC, official validation, full extracted tests, source parity, asset digest, remote `main`, peeled tag commit, release flags, and direct download URLs.

- [ ] **Step 5: Request live ChatGPT Work acceptance**

Ask the user to confirm `명희` and its icon appear in the `@` picker and that `@명희` activates the persona. Do not claim this before user confirmation.
