# Runtime Routing

## Purpose

This document maps BCH Defender routing decisions to concrete OpenClaw runtime profiles and prompt stacks.

## Core Rule

Routing should choose the smallest focused runtime profile that matches the user's real need.

## Primary Route Mapping

### Merchant

Default profile:

- Merchant Operations Agent

Default prompt stack:

- `prompts/system.md`
- `prompts/merchant.md`
- add `prompts/merchant-operations.md` when setup, xPub, refund-role, or multisig context matters

Typical subroutes:

- `merchant_setup`
- `merchant_treasury`
- `merchant_refund_roles`

### Objections

Default profile:

- Comparative Objections Agent

Default prompt stack:

- `prompts/system.md`
- `prompts/objections.md`
- add `prompts/comparative-objections.md` when the user is comparing BCH with another system

Typical subroutes:

- `compare_btc`
- `compare_privacy_coin`
- `compare_fee_free`
- `compare_state_or_stable`
- `compare_pos_or_contract_chain`

### Knowledge

Default profile depends on subroute.

#### Privacy / infrastructure knowledge

Profile:

- Privacy and Network Agent

Prompt stack:

- `prompts/system.md`
- `prompts/knowledge.md`
- `prompts/privacy-and-network.md`

Subroutes:

- `privacy_tooling`
- `network_privacy`
- `distributed_storage_and_access`

#### Record anchoring knowledge

Profile:

- Record Anchoring Agent

Prompt stack:

- `prompts/system.md`
- `prompts/knowledge.md`
- `prompts/record-anchoring.md`

Subroute:

- `record_anchoring`

## Escalation Rule

If routing adds escalation, keep the same dominant profile but tighten the response style.

Do not switch to a broader or more aggressive runtime profile automatically.

## Practical Rule

When a question touches multiple areas, choose the dominant route first.

Then add secondary labels or prompt layers only if they materially improve the answer without creating confusion.