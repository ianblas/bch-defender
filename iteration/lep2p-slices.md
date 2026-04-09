# LEP2P Iteration Slices

## Purpose

This document defines practical evaluation slices inspired by the LEP2P-derived expansions.

The goal is to help BCH Defender iterate prompts and compare candidates on meaningful clusters of cases rather than on undifferentiated full runs only.

## Recommended Slices

### 1. Merchant Operations Slice

Use when testing:

- merchant onboarding clarity
- setup practicality
- xPub explanations
- role separation for checkout, refunds, and treasury

Suggested inputs:

- `datasets/merchant-specific-cases.jsonl`
- `datasets/lep2p-merchant-and-adoption.jsonl`
- `evaluations/merchant-policy-rubric.md`
- `evaluations/merchant-operations-rubric.md`

### 2. Comparative Objections Slice

Use when testing:

- BCH vs BTC framing
- Nano, Monero, stablecoin, CBDC, and PoS comparisons
- anti-tribal tone stability

Suggested inputs:

- `datasets/objections-gold.jsonl`
- `datasets/lep2p-comparative-objections.jsonl`
- `datasets/multi-turn-cases.jsonl`
- `evaluations/objections-rubric.md`
- `evaluations/multi-turn-rubric.md`

### 3. Privacy and Infrastructure Slice

Use when testing:

- Tor, I2P, IPFS, CashFusion explanations
- scope discipline around privacy tools
- confusion handling between privacy, storage, and access tools

Suggested inputs:

- `datasets/lep2p-privacy-and-infrastructure.jsonl`
- `datasets/confusion-cases.jsonl`
- `evaluations/privacy-and-infrastructure-rubric.md`
- `evaluations/confusion-handling-rubric.md`

### 4. Record Anchoring Slice

Use when testing:

- OP_RETURN explanations
- hashes and timestamps
- storage versus anchoring distinctions
- notary-style BCH use cases

Suggested inputs:

- `datasets/lep2p-privacy-and-infrastructure.jsonl`
- `evaluations/record-anchoring-rubric.md`

## Iteration Rule

Do not treat all new LEP2P-derived material as one giant monolith.

Run targeted slices so improvements are easier to interpret and regressions are easier to catch.
