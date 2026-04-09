# LEP2P Recommended Flows

## Purpose

This document gives practical paths for using the LEP2P-derived material without needing to reconstruct the order of previous PRs.

## Flow 1: Merchant Improvement

Use this flow when improving merchant onboarding, setup, treasury-role clarity, or POS guidance.

Recommended path:

1. `faq/merchant-faq-lep2p.md`
2. `playbooks/accepting-bch-in-business.md`
3. `prompts/merchant-operations.md`
4. `datasets/lep2p-merchant-and-adoption.jsonl`
5. `evaluations/merchant-operations-rubric.md`
6. `runner/run-manifest.lep2p-merchant.example.json`

## Flow 2: Comparative Objection Improvement

Use this flow when improving BCH vs BTC, Nano, Monero, stablecoin, CBDC, or PoS answers.

Recommended path:

1. `objections/`
2. `prompts/comparative-objections.md`
3. `datasets/lep2p-comparative-objections.jsonl`
4. `evaluations/objections-rubric.md`
5. `runner/run-manifest.lep2p-comparative.example.json`

## Flow 3: Privacy and Infrastructure Improvement

Use this flow when improving Tor, I2P, IPFS, CashFusion, privacy practice, or resilience explanations.

Recommended path:

1. `faq/knowledge-faq-lep2p.md`
2. `playbooks/privacy-and-network-access.md`
3. `prompts/privacy-and-network.md`
4. `datasets/lep2p-privacy-and-infrastructure.jsonl`
5. `evaluations/privacy-and-infrastructure-rubric.md`
6. `runner/run-manifest.lep2p-privacy.example.json`

## Flow 4: Record Anchoring Improvement

Use this flow when improving OP_RETURN, hashes, timestamps, and notary-style BCH explanations.

Recommended path:

1. `knowledge/`
2. `playbooks/notary-and-record-anchoring.md`
3. `prompts/record-anchoring.md`
4. relevant cases in `datasets/lep2p-privacy-and-infrastructure.jsonl`
5. `evaluations/record-anchoring-rubric.md`

## Practical Rule

If you are unsure where to start, begin with the FAQ or playbook, then move toward prompts, datasets, evaluations, and runner manifests in that order.