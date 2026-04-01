# Fake Payment Proof

## Summary

A screenshot is not the same thing as a BCH payment.

If a customer shows a payment screen but the merchant cannot see the transaction, support should verify the BCH transaction itself.

## Why It Matters

A merchant can lose money by trusting the wrong evidence.

At checkout, pressure and politeness can cause staff to accept:

- a screenshot
- an incomplete send screen
- a wallet view that does not prove the BCH transaction was actually broadcast

A good BCH support standard is simple: verify the transaction, not the story.

## What to Verify

### 1. Ask whether there is a BCH transaction ID

A real transaction should be traceable.

### 2. Check whether the transaction is visible in the merchant wallet or BCH block explorer

If the merchant cannot see the BCH transaction, do not treat it as received.

### 3. Confirm the destination and amount

Even a real transaction may have been sent to the wrong place or for the wrong amount.

## Step-by-Step Guidance

### 1. Do not rely on a screenshot alone

A screenshot may show only that the customer opened the wallet or started the send flow.

### 2. Ask for the transaction ID or visible transaction record

If the transaction exists, it should be possible to verify it.

### 3. Check the merchant side before completing the sale

If the payment is not visible in the merchant wallet or verifiable on-chain, do not mark it as received.

## Common Causes

- customer never finished the send flow
- customer showed the wrong screen
- customer misunderstood what counts as proof
- intentional fraud attempt

## Common Mistakes

- accepting a screenshot as proof of payment
- skipping transaction verification under pressure
- confusing a send screen with an actual BCH transaction
- completing the sale before the payment is visible

## Short Answer

A screenshot is not proof of a BCH payment. Verify the transaction itself in the merchant wallet or on-chain before treating the payment as received.