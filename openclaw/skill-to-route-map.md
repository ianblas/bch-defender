# Skill-to-Route Map

## Purpose

This document maps BCH Defender routes and subroutes to the first core OpenClaw skills.

## Merchant Skill

Skill:

- `skills/bch_merchant_ops/`

Use when the dominant need is:

- merchant onboarding
- BCH acceptance setup
- QR/POS flow clarity
- xPub receiving context
- refund-role separation
- multisig or shared-control context

Primary route:

- `merchant`

Typical subroutes:

- `merchant_setup`
- `merchant_treasury`
- `merchant_refund_roles`

## Comparative Skill

Skill:

- `skills/bch_comparative_objections/`

Use when the dominant need is:

- BCH versus BTC comparison
- BCH versus Nano comparison
- BCH versus Monero comparison
- BCH versus stablecoin, CBDC, PoS, or other comparative objection

Primary route:

- `objections`

Typical subroutes:

- `compare_btc`
- `compare_privacy_coin`
- `compare_fee_free`
- `compare_state_or_stable`
- `compare_pos_or_contract_chain`

## Privacy Skill

Skill:

- `skills/bch_privacy_network/`

Use when the dominant need is:

- CashFusion explanation
- Tor or I2P explanation
- privacy-tool scope clarification
- censorship-resistant or resilient access explanation
- IPFS or distributed access questions when privacy/access distinctions matter

Primary route:

- `knowledge`

Typical subroutes:

- `privacy_tooling`
- `network_privacy`
- `distributed_storage_and_access`

## Record Skill

Skill:

- `skills/bch_record_anchoring/`

Use when the dominant need is:

- OP_RETURN explanation
- hashes and timestamps
- anchoring versus storage clarification
- notary-style BCH explanation

Primary route:

- `knowledge`

Typical subroute:

- `record_anchoring`

## Rule

Choose one dominant skill first.

Only layer additional logic when the secondary concern is strong enough to improve the answer rather than dilute it.