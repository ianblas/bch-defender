# LEP2P Subroutes

## Purpose

This document refines BCH Defender routing with more concrete subroutes inspired by recurring LEP2P themes.

## Merchant-Oriented Subroutes

### `merchant_setup`
Use when the user wants to begin accepting BCH with minimal friction.

### `merchant_treasury`
Use when the user is asking about control of funds, multisig, or owner/operator separation.

### `merchant_refund_roles`
Use when the user is asking who should be allowed to issue refunds or control business outflows.

## Comparative Subroutes

### `compare_btc`
Use for BCH versus BTC, SegWit, Lightning, or Bitcoin-identity comparisons.

### `compare_privacy_coin`
Use for BCH versus Monero or privacy-first comparisons.

### `compare_fee_free`
Use for BCH versus Nano or similar fee-free instant-payment narratives.

### `compare_state_or_stable`
Use for stablecoin, CBDC, custodial, or permissioned-money comparisons.

### `compare_pos_or_contract_chain`
Use for proof-of-stake, smart-contract, or throughput-first chain comparisons.

## Privacy and Infrastructure Subroutes

### `privacy_tooling`
Use for CashFusion and transaction-privacy questions.

### `network_privacy`
Use for Tor, I2P, censorship resistance, and network-access questions.

### `distributed_storage_and_access`
Use for IPFS or similar content-access and storage discussions.

## Record and Data Subroutes

### `record_anchoring`
Use for OP_RETURN, hashes, timestamps, and notary-style discussions.

## Routing Rule

Prefer the most specific subroute that captures the user's actual need.

If ambiguity creates risk, keep the primary route but add escalation as a secondary label.
