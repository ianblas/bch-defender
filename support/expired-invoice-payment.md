# Expired Invoice Payment

## Summary

Sometimes a customer sends BCH after the intended checkout window has already expired.

That should be treated as an operational exception, not as a normal completed payment flow.

## Why It Matters

When a payment arrives after the intended window, confusion can follow.

The merchant may not know whether to:

- accept it normally
- refund it
- reconcile it manually

Support should treat this as a timing exception rather than a BCH failure.

## What to Verify

### 1. Confirm that the BCH payment was sent after the intended checkout window

A late payment may still be real, but it may no longer match the original request conditions.

### 2. Check the BCH transaction ID, amount, and destination

Verify the actual transaction before deciding what to do.

### 3. Determine the merchant policy for expired payments

The business should know whether it prefers manual reconciliation, completion, or refund.

## Step-by-Step Guidance

### 1. Verify the transaction first

Do not treat the payment as imaginary just because the invoice or quote expired.

### 2. Separate payment validity from payment timing

A real BCH payment can still be real even if it arrived outside the intended checkout window.

### 3. Resolve it as an exception

The merchant may need to:

- reconcile it manually
- ask the customer to complete a difference
- refund it according to policy

## Common Causes

- customer waited too long to send
- stale checkout screen
- customer used an old quote
- merchant and customer were out of sync about timing

## Common Mistakes

- treating a late BCH payment as a normal on-time checkout
- ignoring the actual transaction details
- improvising a refund without policy
- blaming BCH for a timing exception

## Short Answer

If a BCH payment arrives after the intended invoice or checkout window, verify the transaction and treat it as a timing exception that may require manual reconciliation or refund.