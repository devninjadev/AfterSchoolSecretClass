# Pressure-test receipt

## RED control

Before the production skill existed, `python3 -m unittest discover -s skills/choi-hayoung/tests -v` failed on every required package artifact, metadata contract, opening selector, route validator, and migration receipt. After correcting one self-matching scanner fixture, the remaining failures were caused by missing production artifacts. This established the executable no-skill baseline.

## Closed-route scenarios

`pressure-scenarios.json` covers generic finance, a bare Hayoung opening, substantive Hayoung security analysis, current-market mixed evidence, non-authorizing `기억해 둬`, explicit World Memory write, pressure to fabricate a missing advisor, news without Alpaca, explicit image generation, and Myunghee context.

Each expected route is validated by the shipped closed-contract validator. The tests additionally require generic finance to leave `persona_requested` false, substantive analysis to avoid `opening`, and every scenario without explicit write authorization to retain `write_intent: none`.

## Independent behavioral sampling boundary

The original implementation session did not launch independent subagents because its active collaboration policy prohibited unrequested delegation. A later 2026-08-19 voice-and-quotation repair did run an independent read-only evaluator under the skill-authoring validation contract.

Before the repair, the evaluator answered two materially relevant Hayoung investment questions without reading `investor-perspectives.md` or using Druckenmiller/Soros, and one answer contained anonymous report-style analysis outside Hayoung's dialogue. After the repair, the same questions loaded the investor canon, used one materially relevant Druckenmiller perspective inside the reasoning, kept explanatory prose in quoted conversational dialogue, and reserved unquoted prose for scene narration or structured evidence. A final loophole re-test confirmed the direct-dialogue boundary after it was tightened.

This sampling supports the prose contract but does not prove ChatGPT Work UI acceptance or guarantee every future model output. Those remain live acceptance checks after personal installation.
