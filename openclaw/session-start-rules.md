# Session Start Rules

## Purpose

This document defines how a BCH Defender session should start inside OpenClaw once routing and profile selection are available.

## Start Sequence

### 1. Identify the dominant route

Determine whether the user's main need is:

- merchant guidance
- comparative objection handling
- privacy/infrastructure knowledge
- record anchoring knowledge

### 2. Select one dominant profile

Pick the most relevant initial profile:

- Merchant Operations Agent
- Comparative Objections Agent
- Privacy and Network Agent
- Record Anchoring Agent

### 3. Assemble the prompt stack

Always start from:

- `prompts/system.md`

Then add the focused prompt layers required by the selected profile.

### 4. Add escalation only when needed

If the case is risky or ambiguous, tighten the response style.

Do not broaden the profile or widen confidence automatically.

### 5. Keep the session focused

A session should begin with one dominant skill and one dominant route.

Secondary concerns should only be layered if they improve the answer clearly.

## Examples

### Merchant setup question

- dominant route: `merchant`
- profile: Merchant Operations Agent
- prompts: `system` + `merchant` + `merchant-operations`
- likely skill: `bch_merchant_ops`

### BTC comparison question

- dominant route: `objections`
- profile: Comparative Objections Agent
- prompts: `system` + `objections` + `comparative-objections`
- likely skill: `bch_comparative_objections`

### Tor / CashFusion question

- dominant route: `knowledge`
- subroute: `privacy_tooling` or `network_privacy`
- profile: Privacy and Network Agent
- prompts: `system` + `knowledge` + `privacy-and-network`
- likely skill: `bch_privacy_network`

### OP_RETURN / timestamping question

- dominant route: `knowledge`
- subroute: `record_anchoring`
- profile: Record Anchoring Agent
- prompts: `system` + `knowledge` + `record-anchoring`
- likely skill: `bch_record_anchoring`

## Rule

A focused session is safer and easier to evaluate than a broad session that tries to activate every capability at once.