# LEP2P Manifests and Slices Index

## Purpose

This document gives one place to find the LEP2P-oriented runner manifests and iteration slices.

## Runner Manifests

### Merchant

- `runner/run-manifest.lep2p-merchant.example.json`
- use for merchant setup, xPub explanation, refund-role clarity, and multisig context

### Privacy / Infrastructure

- `runner/run-manifest.lep2p-privacy.example.json`
- use for Tor, I2P, IPFS, CashFusion, privacy-tool distinction, and resilience explanations

### Comparative Objections

- `runner/run-manifest.lep2p-comparative.example.json`
- use for BCH vs BTC, Nano, Monero, stablecoins, CBDCs, and PoS comparisons

## Iteration Slices

- `iteration/lep2p-slices.md`

Recommended slices include:

- merchant operations
- comparative objections
- privacy and infrastructure
- record anchoring

## Selection Rule

Pick the manifest that most directly matches the behavior being changed.

Then use the related slice guidance to decide whether a second neighboring run is needed for regression checking.