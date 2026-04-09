# LEP2P Run Selection

## Purpose

This document shows how to select the right run type when working with the LEP2P-derived expansions.

## Selection Rules

### Use the merchant manifest when:

- the prompt change affects merchant setup
- the change affects xPub or receive-flow explanation
- the change affects refund-role or treasury-role clarity

Recommended manifest:

- `runner/run-manifest.lep2p-merchant.example.json`

### Use the comparative manifest when:

- the prompt change affects BCH vs BTC framing
- the change affects Nano, Monero, stablecoin, CBDC, or PoS comparisons
- the change affects anti-tribal tone stability across objections

Recommended manifest:

- `runner/run-manifest.lep2p-comparative.example.json`

### Use the privacy manifest when:

- the prompt change affects Tor, I2P, IPFS, CashFusion, or privacy-tool explanations
- the change affects confusion handling around privacy versus storage versus access tools
- the change affects network-resilience or censorship-resistance answers

Recommended manifest:

- `runner/run-manifest.lep2p-privacy.example.json`

## Practical Rule

If a prompt change touches multiple areas, start with the most directly affected slice first.

Then run the neighboring slice to check for regressions.

## Example

If you change `prompts/privacy-and-network.md`, run:

1. the LEP2P privacy manifest first
2. then confusion-related cases if the wording could affect tool distinction

This keeps iteration targeted while still catching cross-area regressions.
