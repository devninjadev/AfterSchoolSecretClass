# Pressure-test receipt

## RED control

Before the production skill existed, `python3 -m unittest discover -s skills/choi-hayoung/tests -v` failed on every required package artifact, metadata contract, opening selector, route validator, and migration receipt. After correcting one self-matching scanner fixture, the remaining failures were caused by missing production artifacts. This established the executable no-skill baseline.

## Closed-route scenarios

`pressure-scenarios.json` covers generic finance, a bare Hayoung opening, substantive Hayoung security analysis, current-market mixed evidence, non-authorizing `기억해 둬`, explicit World Memory write, pressure to fabricate a missing advisor, news without Alpaca, explicit image generation, and Myunghee context.

Each expected route is validated by the shipped closed-contract validator. The tests additionally require generic finance to leave `persona_requested` false, substantive analysis to avoid `opening`, and every scenario without explicit write authorization to retain `write_intent: none`.

## Independent behavioral sampling boundary

This implementation session did not launch independent subagents because the active collaboration policy prohibited unrequested subagent delegation. Therefore this file does not claim fresh-agent prose compliance or ChatGPT Work UI acceptance. Those remain live acceptance checks after personal installation. The deterministic tests prove the route contract and authorization fixtures, not the behavior of an unseen production model.
