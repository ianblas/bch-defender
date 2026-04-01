# Wrong Address

## Summary

A BCH payment sent to the wrong address is not the same thing as a delayed payment.

If the destination was wrong, the main issue is misdelivery, not BCH speed.

## Why It Matters

People often hope a wrong-address payment can be reversed automatically.

In self-custodial BCH usage, that is usually not how it works.

Support should explain the situation clearly without creating false hope.

## What to Verify

### 1. Confirm the destination address used

Do not rely on memory. Check the actual BCH transaction details.

### 2. Confirm whether the transaction was broadcast and confirmed

If the BCH transaction already exists on-chain, the situation is more serious.

### 3. Confirm who controls the destination address

Recovery options depend heavily on whether the recipient is known or cooperative.

## Step-by-Step Guidance

### 1. Verify the destination on-chain

Use the transaction record to confirm exactly where the BCH was sent.

### 2. Explain that BCH transactions are generally not reversible by default

This is normal self-custodial behavior, not a BCH defect.

### 3. Determine whether any recovery path exists

Possible recovery is more likely if:

- the recipient is known
- the receiving service cooperates
- the user controls the destination keys

## Common Causes

- copied the wrong address
- pasted an old address
- user rushed the send flow
- poor destination verification before sending

## Common Mistakes

- promising reversal too early
- treating a wrong-address send as if it were still pending
- failing to confirm the destination on-chain
- blaming BCH for normal self-custodial finality

## Short Answer

If BCH was sent to the wrong address, first verify the destination on-chain. If the transaction is real, automatic reversal is usually not available, so any recovery depends on who controls the destination.