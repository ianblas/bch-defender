# Skill Regression Checks

## Purpose

This document defines simple regression checks for BCH Defender's first OpenClaw skills.

## Core Rule

A skill should not be judged only by whether it answers its own favorite question well.

It should also be checked for nearby regressions in:

- BCH framing
- safety
- clarity
- role separation
- scope discipline

## By Skill

### `bch_merchant_ops`

Check for regressions in:

- wallet safety language
- refund-role separation
- xPub explanation discipline
- pressure toward unnecessary setup complexity

Use after changes with:

- `runner/run-manifest.lep2p-merchant.example.json`
- merchant slices from `iteration/lep2p-slices.md`

### `bch_comparative_objections`

Check for regressions in:

- tribal or mocking tone
- failure to admit real tradeoffs
- collapse of all comparisons into the same template
- weak BCH use-case framing

Use after changes with:

- `runner/run-manifest.lep2p-comparative.example.json`
- comparative slices from `iteration/lep2p-slices.md`

### `bch_privacy_network`

Check for regressions in:

- confusing Tor, I2P, IPFS, and CashFusion
- magical privacy claims
- weak tool-scope explanation
- failure to connect privacy to BCH practice and resilience

Use after changes with:

- `runner/run-manifest.lep2p-privacy.example.json`
- privacy slices from `iteration/lep2p-slices.md`

### `bch_record_anchoring`

Check for regressions in:

- confusing hash anchoring with raw storage
- overstating legal certainty
- treating anchoring and storage as the same thing
- losing practical clarity for builders and ordinary users

Use after changes with:

- record-anchoring evaluation guidance from `iteration/lep2p-slices.md`
- `evaluations/record-anchoring-rubric.md`

## Practical Rule

When a skill changes, first run its direct slice.

Then run one neighboring slice to check whether the wording change caused collateral regressions.