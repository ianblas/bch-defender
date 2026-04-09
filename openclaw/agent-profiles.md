# Agent Profiles

## Purpose

This document defines the first practical agent profiles for BCH Defender inside OpenClaw.

## Profile 1: Merchant Operations Agent

### Main Use

- merchant onboarding
- BCH acceptance setup
- pricing and refund-role clarity
- xPub, receive-flow, and multisig context

### Main Inputs

- `prompts/system.md`
- `prompts/merchant.md`
- `prompts/merchant-operations.md`
- relevant `routing/` files

### Default Skill

- `skills/bch_merchant_ops/`

## Profile 2: Comparative Objections Agent

### Main Use

- BCH vs BTC
- BCH vs Nano
- BCH vs Monero
- BCH vs stablecoins or CBDCs
- BCH vs PoS or smart-contract narratives

### Main Inputs

- `prompts/system.md`
- `prompts/objections.md`
- `prompts/comparative-objections.md`
- relevant `routing/` files

### Default Skill

- `skills/bch_comparative_objections/`

## Profile 3: Privacy and Network Agent

### Main Use

- CashFusion
- Tor and I2P
- privacy scope clarification
- censorship-resistant access and resilience

### Main Inputs

- `prompts/system.md`
- `prompts/knowledge.md`
- `prompts/privacy-and-network.md`
- relevant `routing/` files

### Default Skill

- `skills/bch_privacy_network/`

## Profile 4: Record Anchoring Agent

### Main Use

- OP_RETURN
- hashes and timestamps
- lightweight notary-style use cases
- anchoring versus storage clarification

### Main Inputs

- `prompts/system.md`
- `prompts/knowledge.md`
- `prompts/record-anchoring.md`
- relevant `routing/` files

### Default Skill

- `skills/bch_record_anchoring/`

## General Rule

These profiles should be treated as focused entry points.

They do not replace the broader BCH Defender prompt stack. They make runtime behavior easier to organize and control.
