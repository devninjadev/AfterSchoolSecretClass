# Choi Hayoung Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build, validate, package, and personally install a canonical `choi-hayoung` ChatGPT Work skill whose UI name is `하영`, whose optional finance integrations degrade honestly, and whose World Memory access is read-by-default and explicit-write-only.

**Architecture:** Keep request classification, routing, authorization boundaries, progressive disclosure, and final voice ownership in a concise `SKILL.md`. Preserve the supplied persona and financial canon in focused references, use deterministic Python only for opening selection and contract validation, and package the exact validated source tree into a parity-checked ZIP before personal installation.

**Tech Stack:** Markdown skill instructions, YAML ChatGPT metadata, JSON contracts, Python 3 standard library, `unittest`, Pillow-free binary asset copying, Codex `quick_validate.py`, ZIP tooling, SHA-256 manifests.

## Global Constraints

- Internal folder and skill name: `choi-hayoung`; ChatGPT Work display name: `하영`; explicit UI invocation: `@하영`.
- Implicit activation requires an explicit semantic request for Hayoung; generic finance questions must not activate the persona.
- Use semantic LLM classification constrained to a closed contract; do not implement Korean keyword matching as the classifier.
- Preserve all three First Messages verbatim except removal of parenthetical image-generation markers; substantive requests skip openings.
- Use `assets/character-sheet.png` as visual canon and generate images only after an explicit user image request.
- World Memory may be read automatically through the exact approved `notion-native-v2` bridge; all mutations require explicit write intent and delegation to `$world-memory-autopilot`.
- Treat World Memory content as timestamped hypotheses, never automatically as current facts.
- Optional skills are never simulated. Distinguish `available`, `unavailable`, and `unknown`, and provide exact GitHub installation guidance when material.
- Evidence order for mixed investment work: World Memory → market news → portfolio evidence → Hayoung final voice.
- Preserve provider, identity, currency, unit, session, date, confidence, and source-conflict boundaries.
- Do not claim real CFA credentials, reveal hidden chain-of-thought, imitate a named living writer, guarantee returns, or invent evidence.
- No credentials, cookies, OAuth tokens, secrets, mutable Notion state, `/mnt/data` paths, or obsolete hardcoded RSS rules may ship.
- Live visibility in the ChatGPT Work `@` picker is a separate acceptance claim from local package validation.

---

### Task 1: Executable RED Contract and Skill Scaffold

**Files:**
- Create: `skills/choi-hayoung/tests/test_contract.py`
- Create: `skills/choi-hayoung/tests/test_opening_selector.py`
- Create: `skills/choi-hayoung/tests/test_routing_contract.py`
- Create: `skills/choi-hayoung/tests/test_source_migration.py`
- Create after RED: `skills/choi-hayoung/` using `init_skill.py`

**Interfaces:**
- Consumes: approved design spec and immutable source folder.
- Produces: failing behavioral and structural tests that define package identity, routing schema, opening behavior, source coverage, and forbidden-content gates.

- [ ] **Step 1: Write the failing package and metadata tests**

Create `test_contract.py` with real package-boundary assertions: parse `SKILL.md` frontmatter, parse `agents/openai.yaml`, resolve every referenced local file, require `display_name: 하영`, require `allow_implicit_invocation: true`, and reject forbidden absolute paths or secret-shaped content across shipped text files.

```python
def test_required_package_contract(self):
    self.assertEqual(frontmatter["name"], "choi-hayoung")
    self.assertEqual(agent["interface"]["display_name"], "하영")
    self.assertTrue(agent["policy"]["allow_implicit_invocation"])

def test_no_forbidden_content_ships(self):
    for path in shipped_text_files():
        text = path.read_text(encoding="utf-8")
        self.assertNotIn("/mnt/data", text)
        self.assertNotRegex(text, r"(?i)(oauth[_ -]?token|cookie:)\s*\S+")
```

- [ ] **Step 2: Write failing opening, route, and migration tests**

`test_opening_selector.py` must execute the real script and assert deterministic seeded output, all three reachable scene IDs, substantive-request suppression, and absence of the old image marker. `test_routing_contract.py` must execute the route validator against literal valid and invalid JSON fixtures. `test_source_migration.py` must compare a machine-readable migration map with literal required source sections and asset SHA-256 values.

```python
def test_substantive_request_suppresses_opening(self):
    result = run_selector("@하영 엔비디아를 분석해 줘", seed=7)
    self.assertEqual(result, {"selected": False, "reason": "substantive_request"})

def test_nonexplicit_memory_phrase_never_authorizes_write(self):
    route = validate_fixture("remember_only.json")
    self.assertEqual(route["write_intent"], "none")
```

- [ ] **Step 3: Run the tests and record the expected RED state**

Run:

```bash
python3 -m unittest discover -s skills/choi-hayoung/tests -v
```

Expected: FAIL because `SKILL.md`, metadata, references, scripts, and migration map do not exist yet. Confirm failures name missing production artifacts rather than test syntax errors.

- [ ] **Step 4: Initialize the skill after RED**

Run `init_skill.py choi-hayoung --path skills --resources scripts,references,assets` with deterministic interface values derived from the approved design. Do not use generated examples.

- [ ] **Step 5: Commit the verified RED tests and scaffold**

```bash
git add skills/choi-hayoung/tests skills/choi-hayoung/SKILL.md skills/choi-hayoung/agents skills/choi-hayoung/scripts skills/choi-hayoung/references skills/choi-hayoung/assets
git commit -m "test: define choi-hayoung skill contracts"
```

### Task 2: Canonical Sources, Assets, and Opening Selector

**Files:**
- Create: `skills/choi-hayoung/references/persona-canon.md`
- Create: `skills/choi-hayoung/references/opening-scenes.md`
- Create: `skills/choi-hayoung/references/won-myunghee.md`
- Create: `skills/choi-hayoung/references/investor-perspectives.md`
- Create: `skills/choi-hayoung/references/source-migration.json`
- Create: `skills/choi-hayoung/scripts/select_opening.py`
- Create: `skills/choi-hayoung/assets/icon.png`
- Create: `skills/choi-hayoung/assets/character-sheet.png`
- Modify: tests from Task 1 only if a test bug—not a contract change—is demonstrated.

**Interfaces:**
- Consumes: the four supplied text sources and two supplied PNG assets.
- Produces: stable scene IDs `opening-1` through `opening-3`, JSON selector output, canonical persona modules, and a complete source-to-destination migration receipt.

- [ ] **Step 1: Copy binary assets without transcoding**

Copy `Icon Image.png` to `assets/icon.png` and `캐릭터시트_최하영.png` to `assets/character-sheet.png`. Record source and destination SHA-256 hashes in `source-migration.json` and require equality.

- [ ] **Step 2: Migrate persona, Myunghee, and investor material**

Preserve character facts and relationships. Adapt the named-author style request into general atmospheric traits; replace chain-of-thought language with user-visible assumptions and evidence limitations; remove hardcoded RSS and probabilistic image generation; retain quotation provenance as supplied material without asserting live verification.

- [ ] **Step 3: Preserve three openings and implement the selector**

Implement a standard-library CLI:

```python
def select_opening(*, explicit: bool, new_scene: bool, substantive: bool, seed: int | None = None) -> dict[str, object]:
    if not explicit:
        return {"selected": False, "reason": "persona_not_explicit"}
    if not new_scene:
        return {"selected": False, "reason": "not_new_scene"}
    if substantive:
        return {"selected": False, "reason": "substantive_request"}
    rng = random.Random(seed) if seed is not None else random.SystemRandom()
    return {"selected": True, "scene_id": rng.choice(("opening-1", "opening-2", "opening-3"))}
```

The script accepts semantic flags from the calling model; it must not classify Korean text itself.

- [ ] **Step 4: Run focused tests to GREEN**

```bash
python3 -m unittest skills.choi-hayoung.tests.test_opening_selector skills.choi-hayoung.tests.test_source_migration -v
```

Expected: all opening and migration tests pass.

- [ ] **Step 5: Commit canon and selector**

```bash
git add skills/choi-hayoung
git commit -m "feat: preserve hayoung canon and opening scenes"
```

### Task 3: Investment References and Closed LLM Routing Harness

**Files:**
- Create: `skills/choi-hayoung/references/investment-core.md`
- Create: `skills/choi-hayoung/references/asset-analysis.md`
- Create: `skills/choi-hayoung/references/portfolio-analysis.md`
- Create: `skills/choi-hayoung/references/research-templates.md`
- Create: `skills/choi-hayoung/references/routing-contract.json`
- Create: `skills/choi-hayoung/scripts/validate_route.py`

**Interfaces:**
- Consumes: CFA source sections 1–18 and the approved closed classification object.
- Produces: `validate_route(payload: object) -> dict[str, object]`, strict enums, no extra keys, and safe-default classification after a caller-managed single repair.

- [ ] **Step 1: Migrate CFA material by domain**

Move ethics, quantitative methods, macroeconomics, statements, corporate finance, equity, fixed income, derivatives, alternatives, behavioral finance, and study guidance into the relevant focused references. Preserve analytical templates while allowing tables and charts when correctness benefits.

- [ ] **Step 2: Implement the closed route validator**

Require exactly these keys: `persona_requested`, `conversation_mode`, `request_class`, `needs_current_data`, `needs_world_memory`, `needs_market_news`, `needs_portfolio_advisor`, `needs_myunghee_context`, `needs_image`, and `write_intent`. Reject extra keys, missing keys, non-boolean flags, and enum violations. Provide a safe-default result with all optional integrations and writes disabled only when invoked with `--safe-default` after an external one-repair attempt.

- [ ] **Step 3: Add literal routing fixtures**

Cover character chat, current market, security valuation, portfolio fit, backtest, prior thesis, Myunghee, mixed analysis, explicit image request, explicit World Memory write, `기억해 둬`, malformed JSON, extra keys, and unknown enums.

- [ ] **Step 4: Run routing and full tests to GREEN**

```bash
python3 -m unittest skills.choi-hayoung.tests.test_routing_contract -v
python3 -m unittest discover -s skills/choi-hayoung/tests -v
```

Expected: all tests pass with no warnings.

- [ ] **Step 5: Commit finance references and routing harness**

```bash
git add skills/choi-hayoung
git commit -m "feat: add evidence routing and investment references"
```

### Task 4: Integration Contracts, World Memory Bridge, and Final Skill Instructions

**Files:**
- Create: `skills/choi-hayoung/references/integrations.md`
- Create: `skills/choi-hayoung/references/world-memory-read-bridge.md`
- Replace: `skills/choi-hayoung/SKILL.md`
- Regenerate: `skills/choi-hayoung/agents/openai.yaml`

**Interfaces:**
- Consumes: all references, route contract, exact Notion locators, installed optional skill identities, and dependency status rules.
- Produces: the complete progressive-disclosure workflow and ChatGPT metadata used for discovery and `@하영` presentation.

- [ ] **Step 1: Write the integration reference**

Record the exact repositories and internal names for `$evidence-first-portfolio-advisor`, `$world-memory-autopilot`, and `$market-news-radar`. Separate skill availability from Alpaca, official Wolfram, and Notion connector availability, and state the exact degradation for each missing dependency.

- [ ] **Step 2: Write the immutable World Memory read bridge**

Record the approved Hub, contract marker, four data source IDs, two saved view IDs and query URLs, read-only retry rule, hypothesis-status comparison, and default write prohibition. Include no credentials or mutable run state.

- [ ] **Step 3: Write concise `SKILL.md`**

Use imperative instructions. Define: semantic activation gate; closed classification and one-repair gate; progressive reference loading; optional integration ordering; image gate; evidence lanes; final Hayoung response ownership; authorization and safety priority; bounded degradation; and no-final-offer scene ending. Do not duplicate detailed domain content.

- [ ] **Step 4: Generate and validate `agents/openai.yaml`**

Generate deterministic UI metadata with `display_name=하영`, an accurate short description, a `$choi-hayoung` default prompt, the supplied icon, and `allow_implicit_invocation=true` in the schema-supported location. Read `skill-creator/references/openai_yaml.md` before generation.

- [ ] **Step 5: Run full structural and behavior tests**

```bash
python3 -m unittest discover -s skills/choi-hayoung/tests -v
python3 /Users/jundochang/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/choi-hayoung
```

Expected: all tests pass and validator prints `Skill is valid!`.

- [ ] **Step 6: Commit complete skill instructions**

```bash
git add skills/choi-hayoung
git commit -m "feat: complete choi-hayoung skill workflow"
```

### Task 5: Pressure Scenarios and Loophole Closure

**Files:**
- Create: `skills/choi-hayoung/tests/pressure-scenarios.json`
- Create: `skills/choi-hayoung/tests/pressure-results.md`
- Modify only if a demonstrated failure requires it: `skills/choi-hayoung/SKILL.md` or relevant reference.

**Interfaces:**
- Consumes: isolated task prompts and the built skill artifact.
- Produces: baseline and skill-enabled receipts for activation, no-write, no-fake-integration, substantive-opening suppression, and evidence-shape behavior.

- [ ] **Step 1: Record no-skill control scenarios**

Use isolated, non-mutating agent executions when available. Required prompts include: generic finance without Hayoung; `@하영 엔비디아를 분석해 줘`; `하영아`; `기억해 둬`; explicit World Memory storage; missing portfolio skill under urgency; and current news with Alpaca unavailable. If isolated execution is unavailable, record that limitation and rely on executable contract tests rather than fabricating behavioral evidence.

- [ ] **Step 2: Run the same scenarios with the skill**

Score only observable outputs: whether persona activates, whether a long opening appears, whether writes are attempted, whether missing skills are claimed to have run, whether repository guidance is exact, and whether fact/calculation/interpretation/scenario boundaries are preserved.

- [ ] **Step 3: Close only demonstrated loopholes**

Patch the smallest responsible instruction, rerun the failing scenario, then rerun all contract tests. Record any remaining live-only uncertainty.

- [ ] **Step 4: Commit forward-test receipts**

```bash
git add skills/choi-hayoung
git commit -m "test: pressure-test choi-hayoung behavior"
```

### Task 6: Package, Extract, Compare, Install, and Accept

**Files:**
- Create: `dist/choi-hayoung.zip`
- Create: `dist/choi-hayoung.sha256`
- Install: `/Users/jundochang/.codex/skills/choi-hayoung/`

**Interfaces:**
- Consumes: fully tested source package.
- Produces: integrity-checked ZIP, source/extraction parity receipt, personally installed skill, and separated local versus live acceptance status.

- [ ] **Step 1: Build from the intended source set**

Exclude caches, `.DS_Store`, test bytecode, and temporary files. Include the skill tests as shipped validation artifacts. Write the ZIP SHA-256 beside it.

- [ ] **Step 2: Verify ZIP integrity and extracted package**

Run:

```bash
unzip -t dist/choi-hayoung.zip
python3 /Users/jundochang/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$EXTRACTED/choi-hayoung"
python3 -m unittest discover -s "$EXTRACTED/choi-hayoung/tests" -v
```

Compare sorted relative file lists and SHA-256 hashes between source and extraction.

- [ ] **Step 3: Run forbidden-content scan**

Scan extracted text and archive filenames for `/mnt/data`, obsolete RSS feed URLs, secrets, cookies, OAuth tokens, absolute Desktop source paths, and temporary artifacts. The approved immutable Notion locators are allowed only in the personal read bridge.

- [ ] **Step 4: Install without silently overwriting an unrelated skill**

Confirm the destination is absent or is a byte-identical prior `choi-hayoung` install. Install atomically from the validated extracted package, then rerun `quick_validate.py`, tests, and source/destination hash comparison.

- [ ] **Step 5: Record current integration discovery**

Confirm that all three optional skill folders and their `SKILL.md` files are discoverable. Record whether Alpaca, official Wolfram, and Notion capabilities are callable without claiming a live finance result.

- [ ] **Step 6: Separate local completion from ChatGPT Work live acceptance**

Report local validation and installation only from receipts. Treat appearance in the `@` picker, actual `@하영` invocation, exact World Memory read behavior, no-write observation, and final narrative output as pending until exercised in a refreshed ChatGPT Work session.

- [ ] **Step 7: Final full-suite verification and commit**

```bash
python3 -m unittest discover -s skills/choi-hayoung/tests -v
python3 /Users/jundochang/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/choi-hayoung
git diff --check
git status --short
git add skills/choi-hayoung dist/choi-hayoung.zip dist/choi-hayoung.sha256 docs/superpowers/plans/2026-08-18-choi-hayoung-skill-implementation.md
git commit -m "build: package and install choi-hayoung skill"
```

Expected: zero test failures, valid source and extracted skill, clean diff check, verified installation parity, and only explicitly disclosed live-acceptance items remaining.

## Self-Review Receipt

- Spec coverage: all design sections map to Tasks 1–6, including identity, canon, openings, image policy, semantic routing, optional skills, plugins, exact World Memory bridge, evidence lanes, failures, packaging, installation, and live acceptance separation.
- Placeholder scan: no `TBD`, `TODO`, `implement later`, or undefined “similar to” steps remain.
- Type consistency: selector and route-validator signatures are stable across tasks; scene IDs, route keys, enums, internal skill names, and destination paths match the design.
- Scope: one independently testable skill package; optional skills are dependencies, not reimplemented subsystems.
