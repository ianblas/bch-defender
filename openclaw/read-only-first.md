# Read-Only First

## Purpose

This document explains how BCH Defender should apply a read-only-first approach inside OpenClaw.

## Core Idea

Many questions can be answered well without browsing actions or system execution.

The runtime should prove that read-only behavior is insufficient before using stronger tools.

## By Profile

### Merchant Operations Agent

Use read-only first for:

- setup explanations
- pricing logic
- refund-role guidance
- xPub and multisig explanation

Do not jump to browser actions just because a merchant topic sounds practical.

### Comparative Objections Agent

Use read-only almost always.

Comparative objections are usually reasoning-heavy, not action-heavy.

### Privacy and Network Agent

Use read-only first for:

- Tor, I2P, IPFS explanations
- CashFusion explanation
- privacy and resilience comparisons

Escalate only if the task genuinely requires checking or interacting with a live resource.

### Record Anchoring Agent

Use read-only first for:

- OP_RETURN explanation
- hash and timestamp explanation
- anchoring versus storage clarification

Do not treat record-anchoring questions as action tasks by default.

## When Read-Only Is Not Enough

Escalation beyond read-only can make sense when:

- a public fact must be verified rather than explained generally
- the user explicitly needs live confirmation
- the task is bounded and genuinely requires interaction rather than explanation

## When Read-Only Should Remain the Ceiling

Keep the ceiling at read-only when:

- the question is mostly conceptual
- the task is comparative or educational
- ambiguity is still high
- stronger tools would create pressure without adding clarity

## Rule

Read-only first is not about passivity.

It is about proving that stronger runtime capability is actually needed before using it.