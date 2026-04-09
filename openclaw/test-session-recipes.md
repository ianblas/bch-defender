# Test Session Recipes

## Purpose

This document gives simple, repeatable test-session recipes for BCH Defender inside OpenClaw.

## Recipe 1: Merchant Operations Session

### Ask

- How do I start accepting BCH in my business?
- Should my staff be able to send refunds?
- Why would I use an xPub in a POS flow?

### Expected Runtime Shape

- profile: Merchant Operations Agent
- dominant skill: `bch_merchant_ops`
- prompt stack: `system` + `merchant` + `merchant-operations`

### Expected Follow-Up Evaluation

- manifest: `runner/run-manifest.lep2p-merchant.example.json`
- slices: merchant operations

## Recipe 2: Comparative Objections Session

### Ask

- Why not BTC?
- Why not Nano?
- Why not Monero?

### Expected Runtime Shape

- profile: Comparative Objections Agent
- dominant skill: `bch_comparative_objections`
- prompt stack: `system` + `objections` + `comparative-objections`

### Expected Follow-Up Evaluation

- manifest: `runner/run-manifest.lep2p-comparative.example.json`
- slices: comparative objections

## Recipe 3: Privacy and Network Session

### Ask

- What is CashFusion for?
- Why would a BCH user care about Tor or I2P?
- Is IPFS the same thing as privacy?

### Expected Runtime Shape

- profile: Privacy and Network Agent
- dominant skill: `bch_privacy_network`
- prompt stack: `system` + `knowledge` + `privacy-and-network`

### Expected Follow-Up Evaluation

- manifest: `runner/run-manifest.lep2p-privacy.example.json`
- slices: privacy and infrastructure

## Recipe 4: Record Anchoring Session

### Ask

- What is OP_RETURN useful for?
- Can BCH timestamp a document?
- Why anchor a hash instead of storing the whole file?

### Expected Runtime Shape

- profile: Record Anchoring Agent
- dominant skill: `bch_record_anchoring`
- prompt stack: `system` + `knowledge` + `record-anchoring`

### Expected Follow-Up Evaluation

- use the record-anchoring slice guidance from `iteration/lep2p-slices.md`

## Rule

A recipe is successful when the session shape, dominant skill, and evaluation path all line up clearly.