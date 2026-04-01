# QR Not Scanning

## Summary

Sometimes a BCH payment does not fail because of BCH at all.

The customer simply cannot scan the QR code reliably.

This is a normal checkout friction case and should be handled calmly.

## Why It Matters

At a live checkout, a QR scan failure can create unnecessary confusion.

People may assume:

- the wallet is broken
- the merchant setup is wrong
- BCH is not working

But in many cases the issue is simpler:

- low screen brightness
- bad camera focus
- awkward distance or angle
- incompatible wallet QR handling
- address-format confusion

A good BCH support answer keeps the checkout moving without improvisation.

## What to Verify

### 1. Check brightness, focus, and distance

A dim screen or poor camera focus can prevent a normal scan.

### 2. Make the QR easier to scan

If needed, enlarge the QR or hold the device more steadily.

### 3. Confirm the customer is using a BCH wallet

Do not assume the app understands BCH correctly.

### 4. Check whether the wallet supports the address format being shown

Some BCH wallets and services present addresses differently.

### 5. Check whether the QR may include something the wallet does not parse well

In some cases the wallet handles a plain BCH address better than a full payment request.

## Step-by-Step Guidance

### 1. Improve the scan conditions first

Raise brightness, steady the device, and let the customer try again.

### 2. Confirm the app is a BCH wallet

If the customer is in the wrong wallet or wrong asset flow, fix that first.

### 3. Use a fallback instead of forcing repeated scans

If the QR still fails, show:

- the BCH address
- the amount separately

Then ask the customer to confirm both visually before sending.

### 4. Keep the process simple

Do not turn a scan problem into a technical debate.

The goal is a successful BCH payment, not a perfect QR experience.

## Common Causes

- low brightness
- poor focus
- awkward scanning angle
- customer is in the wrong wallet
- wallet does not interpret the QR well
- BCH address-format confusion

## Common Mistakes

- assuming BCH itself failed
- asking the customer to keep retrying without changing anything
- improvising under pressure
- skipping visual confirmation when using the address as fallback

## Short Answer

If the BCH QR does not scan, improve the scan conditions first. If that still fails, show the BCH address and amount separately and ask the customer to confirm both before sending.