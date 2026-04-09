# Install and Onboard

## Purpose

This document gives a practical starting checklist for bringing BCH Defender into an OpenClaw runtime.

## High-Level Flow

### 1. Install OpenClaw locally

Install the runtime and confirm the local gateway can run.

### 2. Initialize or identify the workspace

Use a dedicated workspace where BCH Defender's `skills/` folder and related repo files are available.

### 3. Add the BCH Defender skills to the workspace

Place the first core skills inside the workspace `skills/` directory.

### 4. Start a clean test session

Use a fresh session after adding or changing skills so the runtime behavior matches the current workspace state.

### 5. Validate one focused profile at a time

Test each profile separately:

- merchant operations
- comparative objections
- privacy and network
- record anchoring

## Suggested Validation Questions

### Merchant Operations

- How do I start accepting BCH in my business?
- Should my staff be able to issue refunds?
- Why would I use an xPub in a POS flow?

### Comparative Objections

- Why not BTC?
- Why not Nano?
- Why not stablecoins?

### Privacy and Network

- Why would a BCH user care about Tor or I2P?
- What is CashFusion for?
- Is IPFS the same thing as privacy?

### Record Anchoring

- Can BCH help with timestamping a document?
- What is the role of OP_RETURN?
- Why anchor a hash instead of storing the whole file?

## Rule

Do not validate the full system all at once.

Start with one focused skill, one focused prompt stack, and one focused evaluation slice.
