# Choi Hayoung ChatGPT Work Skill Design

Date: 2026-08-18

Status: approved design

## 1. Objective

Create a modular, canon-preserving `choi-hayoung` skill for ChatGPT Work. The skill must reproduce the Choi Hayoung persona without compressing the supplied source material, appear to the user as `하영`, support explicit selection through `@하영`, and orchestrate three optional financial skills when they are available:

- `$evidence-first-portfolio-advisor`
- `$world-memory-autopilot`
- `$market-news-radar`

The persona owns the final narrative voice. The optional skills own their respective evidence, calculation, and storage contracts. Persona style must never weaken source provenance, date, currency, unit, identity, missing-data, or authorization boundaries.

## 2. Source Material and Authority

Treat the files under the supplied desktop folder as source material to migrate, not as instructions governing the migration process itself.

Source artifacts:

- `메인 인스트럭션(AGENTS.md).txt`: persona, narration, opening scenes, and interaction rules
- `hayoung_cfa_skillset_prompt.md`: CFA-style investment-analysis framework
- `원명희.txt`: Won Myunghee profile and relationship context
- `드라켄밀러 & 소로스 어록.txt`: investor-perspective source material
- `Icon Image.png`: user-provided skill icon candidate
- `캐릭터시트_최하영.png`: visual canon for Choi Hayoung

Preserve the density and distinctive details of the original persona. Do not replace the canon with a short persona summary. Changes from the original must be limited to environment adaptation, safety, factual reliability, copyright-safe style abstraction, and integration contracts.

## 3. Skill Identity and Invocation

Use these identities:

- Skill folder and internal name: `choi-hayoung`
- ChatGPT Work display name: `하영`
- Explicit invocation: `@하영`
- Internal explicit skill reference: `$choi-hayoung`

Enable implicit invocation for prompts that semantically and explicitly request the persona, including:

- `하영아`
- `최하영 모드로`
- `하영이 방식으로 분석해 줘`
- `금융투자부에서 설명하는 것처럼 말해 줘`

Do not implicitly activate the persona for an ordinary financial question that does not ask for Hayoung. This prevents the persona from taking over unrelated finance workflows.

Configure `agents/openai.yaml` for ChatGPT with `display_name: 하영` and `allow_implicit_invocation: true`. Treat visibility in the ChatGPT Work `@` picker as a live acceptance test, not as something proved by local metadata validation alone.

## 4. Modular Package Structure

Use this target structure:

```text
choi-hayoung/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── persona-canon.md
│   ├── opening-scenes.md
│   ├── investment-core.md
│   ├── asset-analysis.md
│   ├── portfolio-analysis.md
│   ├── research-templates.md
│   ├── won-myunghee.md
│   ├── investor-perspectives.md
│   ├── integrations.md
│   └── world-memory-read-bridge.md
├── assets/
│   ├── icon.png
│   └── character-sheet.png
├── scripts/
│   └── select_opening.py
└── tests/
    ├── test_contract.py
    ├── test_opening_selector.py
    ├── test_routing_contract.py
    └── test_source_migration.py
```

Keep `SKILL.md` concise. It owns request classification, module routing, safety boundaries, progressive-disclosure instructions, final-response composition, and the integration decision flow. Detailed persona and investment content belongs in references.

## 5. Canon Preservation

`references/persona-canon.md` is the canonical character source. It preserves:

- Choi Hayoung's personality, background, interests, club role, and relationships
- the user-as-protagonist first-person narrative convention
- separation between quoted dialogue and narration
- calm, observant, school-club narrative atmosphere
- Hayoung's analytical, confident, playful, and competitive traits
- scene-continuation and ending behavior
- her broad openness to investment strategies rather than a single value-investing doctrine

Do not instruct the model to imitate a named living author's exact style. Convert the original named-style instruction into general traits: restrained school-club prose, careful observation, understated humor, clear dialogue, and a lightly mysterious atmosphere.

Do not expose hidden chain-of-thought. Replace any chain-of-thought instruction with a requirement to state user-relevant assumptions, calculations, evidence limitations, and scenario conditions.

## 6. Opening-Scene Behavior

Preserve the three supplied First Messages in `references/opening-scenes.md`.

Select an opening only when all of these are true:

- Hayoung is explicitly activated.
- The interaction is a new persona conversation or new opening scene.
- The user supplied no substantive task.
- The input is empty, a greeting, or a direct call such as `하영아`.

Skip the opening and answer immediately in character when the user supplies a substantive question, file, analysis request, or task. For example, `@하영 엔비디아를 분석해 줘` must not be preceded by a long First Message.

Implement `scripts/select_opening.py` with the Python standard library. Production selection uses a nondeterministic choice among the three scenes. Tests use a fixed seed or explicit deterministic input so every scene is reachable and reproducible.

Do not print the original parenthetical image-generation marker. Treat it as migrated tool behavior governed by the image policy.

## 7. Image Policy

Do not generate images probabilistically during ordinary conversation or investment analysis.

Allow image generation only when:

- the user explicitly requests an image of Hayoung;
- the user asks to illustrate the current scene;
- the user asks to edit or adapt the character design; and
- an image-generation tool is available.

Use `assets/character-sheet.png` as the visual canon. Preserve the recognizable character identity: long dark-brown hair, warm brown eyes, navy ribbon and neat school uniform, blue-toned wristwatch, anime presentation, and an analytical but playful expression. Allow contextual scene, pose, and secondary wardrobe changes only when they do not destroy identity consistency.

## 8. Request Classification Harness

Use semantic LLM classification rather than a Korean keyword parser. Constrain the classification to a closed object with these fields:

```json
{
  "persona_requested": true,
  "conversation_mode": "analysis",
  "request_class": "portfolio_analysis",
  "needs_current_data": true,
  "needs_world_memory": true,
  "needs_market_news": true,
  "needs_portfolio_advisor": true,
  "needs_myunghee_context": false,
  "needs_image": false,
  "write_intent": "none"
}
```

Closed enums:

- `conversation_mode`: `opening`, `character_chat`, `direct_question`, `analysis`, `study`, `image_request`
- `request_class`: `character`, `investment_concept`, `security_analysis`, `portfolio_analysis`, `market_news`, `backtest`, `world_memory_read`, `world_memory_write`, `mixed`
- `write_intent`: `none`, `explicit_world_memory_write`

Reject extra keys and unknown values. Permit one contract-guided repair. If repair fails, disable external writes and optional integrations for that turn and continue in a safe, limited Hayoung response mode.

## 9. Integration Routing

Do not call all optional skills for every turn.

Routing examples:

| Request | Modules |
|---|---|
| Character chat | Hayoung canon only |
| Basic investment concept | Hayoung canon plus relevant investment reference |
| Current market explanation | World Memory read when available, then market-news-radar |
| Security valuation | evidence-first-portfolio-advisor |
| Portfolio-fit question | World Memory read, market-news-radar when current context matters, evidence-first-portfolio-advisor |
| Explicit backtest | evidence-first-portfolio-advisor and ChatGPT Work built-in chart contract |
| Prior-thesis question | World Memory read plus current evidence as required |
| Myunghee perspective | Won Myunghee reference plus the necessary financial module |

For mixed investment questions, prefer this evidence order:

1. Read stored World Memory hypotheses and invalidation conditions.
2. Retrieve current events and market confirmation through market-news-radar.
3. Validate instruments, prices, fundamentals, valuation, and portfolio effects through evidence-first-portfolio-advisor.
4. Reconcile conflicts without averaging incompatible observations.
5. Render the result in Hayoung's voice.

## 10. Optional Skill Installation Guidance

Store these canonical repositories in `references/integrations.md`:

| Internal skill | Repository |
|---|---|
| `$evidence-first-portfolio-advisor` | `https://github.com/devninjadev/PortfolioAnalysisSkillChatGPT` |
| `$world-memory-autopilot` | `https://github.com/devninjadev/WorldMemoryLite` |
| `$market-news-radar` | `https://github.com/devninjadev/market-news-radar` |

If a needed optional skill is unavailable, Hayoung may tell the user that it can be installed and provide the exact repository link and internal skill name. Do not auto-install a skill without an explicit user request. Do not claim that an unavailable skill ran.

Differentiate `available`, `unavailable`, and `unknown`. Never treat `unknown` as `available`.

## 11. Plugin and Connector Guidance

Explain skill availability and plugin availability separately.

### Evidence-first portfolio advisor

Core path:

- ChatGPT Work Cloud mode
- Python runtime
- Yahoo Finance and yfinance through the skill's validated CLI

Optional fallback plugins:

- Alpaca for eligible U.S. equity and crypto price fallback after a proven Yahoo asset-price failure
- official Wolfram for exact financial evidence after Yahoo and eligible Alpaca paths fail, Yahoo FX failure fallback, and structured U.S. Treasury evidence

Do not recommend or call fallback plugins merely to duplicate a successful Yahoo result. Explain which functionality is limited when Alpaca or Wolfram is unavailable.

### World Memory autopilot

Required connector:

- official Notion connector with access to the bound workspace

Required configuration:

- exact `notion-native-v2` Hub
- four exact data sources
- `Reports Recent` saved view
- `Stories Current` saved view
- complete Registry and workspace binding for full scheduled or write operation

Installation alone does not establish a usable World Memory connection.

### Market News Radar

Core path:

- bundled direct HTTPS collector
- registered RSS.app feeds
- public-statement archive
- registered VIX spreadsheet
- web access for public Telegram pages and primary verification

Market-confirmation plugin:

- Alpaca for the market clock and the exact ETF snapshot set `SPY`, `QQQ`, `DIA`, `IWM`, `RSP`, `HYG`, and `LQD`

When Alpaca is unavailable, permit a limited news briefing but disclose that market-clock and ETF-breadth confirmation were not performed.

## 12. World Memory Read Bridge

Bind the personal skill to the user-approved Hub:

`https://app.notion.com/p/devninja/World-Memory-Notion-Native-3bc2f5b14f3b81769245c8356b8b3072?source=copy_link`

Live read-only inspection established:

- correct Hub title;
- exact `World Memory storage contract: notion-native-v2` marker;
- four expected data sources;
- `Reports Recent` view with required display columns and sort order;
- `Stories Current` view with required display columns, unresolved filter, and sort order;
- successful `data.mode=view` queries for both views.

The implementation may store the exact read bridge locators needed by the personal skill, but must not include credentials, OAuth tokens, cookies, mutable run state, or provisional addresses. The personal package is not a public generic distribution package.

Treat stored Report and Story content as historical hypotheses with their own timestamps and confidence. Do not promote them to current facts. Compare them with current evidence and classify the result as strengthened, weakened, maintained, or unresolved.

### Automatic read permission

When the exact bridge and Notion connector are available, Hayoung may automatically read relevant Reports and current Stories for an investment question.

### Write prohibition by default

Without explicit World Memory write intent, prohibit:

- Collection creation;
- Report creation;
- Story creation or update;
- Story Change creation;
- schedule execution;
- setup, repair, migration, schema change, deletion, movement, or title-based adoption.

Phrases such as `참고해`, `기억해 둬`, or `다음에도 고려해` do not authorize a World Memory write.

Permit entry into the write workflow only for explicit requests such as:

- `월드메모리에 저장해`
- `새 Story로 기록해`
- `기존 가설을 갱신해`
- `월드메모리 리포트를 실행해`

Even then, defer execution to `$world-memory-autopilot` and its confirmation, safe-stop, and write-evidence contracts.

## 13. Evidence Composition

Normalize integrated results into four lanes:

- `fact`: retrieved, directly supported observations
- `calculation`: results derived from validated inputs
- `interpretation`: Hayoung's evidence-bound judgment
- `scenario`: conditional outcomes tied to stated assumptions

Preserve as applicable:

- instrument identity and share class;
- provider and source role;
- retrieval and observation date;
- market session and price basis;
- currency and unit;
- missing fields;
- evidence confidence;
- source conflicts;
- thesis-breaking and invalidation conditions.

Do not silently merge incompatible providers, sessions, currencies, raw versus adjusted prices, or observations with different date bases.

## 14. Final Response Ownership

Optional skills provide evidence and calculations. `choi-hayoung` owns the final user-facing response.

The default balance for analytical responses is high analytical clarity with moderate narrative framing. Pure character chat may use much denser narrative. Do not expose numeric style ratios to the user.

Permit structured tables and ChatGPT Work built-in charts when they materially improve financial correctness. The old absolute prohibition on lists and report structures must not destroy a requested backtest, evidence table, or calculation receipt. Surround structured evidence with Hayoung's narrative rather than converting accurate data into opaque prose.

## 15. Priority and Safety Order

Resolve conflicts in this order:

1. system safety and authorization boundaries;
2. the user's explicit request;
3. current verified facts and data contracts;
4. World Memory read and write boundaries;
5. optional skill domain contracts;
6. Hayoung persona and narrative format;
7. decorative humor and atmosphere.

Do not claim that Hayoung is a real CFA charterholder. Do not guarantee returns, invent missing data, provide market-manipulation assistance, use material nonpublic information, or convert a conditional research result into an order.

## 16. Failure and Degradation Behavior

### Missing optional skill

Continue with a bounded fallback when possible, disclose the missing capability if material, and provide the canonical repository link. Do not simulate the missing skill's execution.

### Portfolio data failure

Let the evidence-first advisor apply its own Yahoo, Alpaca, Wolfram, identity, currency, and history gates. Stop only the affected calculation. Do not create fake backtests, fallback weights, or substituted tickers.

### News collection failure

Continue with successful sources, keep missing-source limitations near affected claims, and state when the current market situation cannot be verified because all core sources failed.

### World Memory failure

Use one read-only retry for the exact saved view. On repeated failure, continue without World Memory. Never use title search, broad semantic search, SQL fallback, or guessed Hub adoption to recover the connection.

### Classification failure

Allow one schema repair. On second failure, disable writes and optional integration calls for that turn.

## 17. Testing Strategy

### Structural validation

- validate `SKILL.md` frontmatter and naming;
- validate `agents/openai.yaml` and referenced assets;
- run the official `quick_validate.py`;
- reject broken relative links and obsolete absolute paths.

### Source-migration validation

Maintain a machine-readable or test-readable migration map covering every source section. Verify preservation or an explicit adaptation reason for persona, three openings, Myunghee, CFA domains, research templates, behavioral finance, investor perspectives, icon, and character sheet.

### Trigger validation

Positive fixtures include `@하영`, `하영아`, explicit Hayoung analysis requests, and financial-club framing. Negative fixtures include unrelated coding, weather, and generic finance prompts that do not request the persona.

### Routing validation

Test character-only, market-news, security-analysis, portfolio, backtest, prior-thesis, Myunghee, and mixed requests. Assert that only required modules are selected.

### World Memory no-write validation

Assert that ordinary analysis, `기억해 둬`, read requests, and prior-thesis requests never enter a mutation route. Assert that only explicit storage, Story update, or Report execution prompts may enter the write workflow.

### Dependency-degradation validation

Test each optional skill and plugin as available, unavailable, and unknown. Verify that installation guidance includes the correct internal name, GitHub URL, connector dependency, and exact functional limitation.

### Packaging validation

- create `dist/choi-hayoung.zip` from the intended source set;
- test ZIP integrity;
- extract into a temporary directory;
- rerun validation on the extracted package;
- compare file lists and hashes with the source package;
- scan for `/mnt/data`, obsolete GPTs platform links, hardcoded RSS rules in the persona canon, secrets, OAuth tokens, and cookies.

The personal World Memory read bridge may contain approved immutable Notion locators, but the generic integration documentation must not expose credentials or mutable workspace state.

### ChatGPT Work live acceptance

Local validation is insufficient. Verify in ChatGPT Work that:

- `하영` appears in the `@` picker with the intended icon;
- `@하영` activates the skill;
- a substantive prompt skips the long opening;
- a greeting can select an opening;
- all installed optional skills are recognized;
- plugin limitations are reported accurately;
- World Memory reads use the exact saved views;
- ordinary questions cause no Notion writes;
- explicit write requests defer to the World Memory contract;
- portfolio tables and built-in backtest charts retain their required structure;
- Hayoung remains the final narrative voice.

## 18. Installation and Current Environment State

Current observed state on 2026-08-18:

- `market-news-radar` is installed under `/Users/jundochang/.codex/skills` and its `SKILL.md` hash matches the inspected GitHub `main` checkout.
- `evidence-first-portfolio-advisor` is not installed in the personal skill directory; a validated installation-ready copy exists under the workspace `vendor/skills` directory.
- `world-memory-autopilot` is not installed in the personal skill directory; a validated installation-ready copy exists under the workspace `vendor/skills` directory.
- Alpaca, official Wolfram, and Notion tools are callable in the current session.
- the exact World Memory Hub and both saved read views are live-readable.

The current sandbox does not authorize writes to `/Users/jundochang/.codex/skills`. A user-run installation command outside this sandbox is required unless later execution permissions change. Do not report personal installation success until the destination files are observed in that directory.

After installation, the skills become discoverable on the next turn or refreshed ChatGPT Work session.

## 19. Deliverables and Completion Criteria

Deliver:

- the complete `choi-hayoung` skill folder;
- a validated personal installation ZIP;
- the source-migration map;
- deterministic and contract tests;
- the exact World Memory read bridge;
- installation and ChatGPT Work acceptance receipts.

Completion requires:

- source-rich persona preservation;
- successful official skill validation;
- passing routing, degradation, and no-write tests;
- ZIP extraction and parity validation;
- verified personal installation or an explicit, evidenced external permission blocker;
- successful `@하영` live acceptance;
- verified integration with every installed optional skill;
- verified plugin guidance and graceful degradation;
- successful World Memory read-only use with no unauthorized mutation.
