# Wrong Amount

## Summary

Sometimes the BCH payment arrives, but the amount is wrong.

This may mean the customer sent too little or too much.

That is not a protocol failure. It is a checkout exception.

## Why It Matters

If the amount is wrong, staff can make the situation worse by improvising.

Typical mistakes include:

- accepting an underpayment as if it were complete
- refunding an overpayment to an unverified address
- blaming BCH when the real issue was timing or user error

## What to Verify

### 1. Compare the expected BCH amount with the received BCH amount

Use the actual checkout request and the actual received payment.

### 2. Check whether the price changed during checkout

A stale quote or expired payment window can produce a mismatch.

### 3. Determine whether this is an underpayment or an overpayment

The response depends on which kind of mismatch occurred.

## Step-by-Step Guidance

### 1. Do not call it complete until the amount issue is understood

A wrong-amount payment is not the same thing as a normal BCH payment.

### 2. If the customer paid too little

The merchant should follow a simple rule:

- complete the missing difference
- or resolve it as an exception or refund

### 3. If the customer paid too much

Confirm the excess carefully.

If a refund is needed, use a verified BCH refund address and return only the excess unless the merchant has another policy.

### 4. Record what happened

The business should know:

- expected amount
- received amount
- reason for the difference if known
- any refund sent

## Common Causes

- stale BCH quote
- customer typed the wrong amount
- customer paid after the intended checkout window
- customer got confused during checkout

## Common Mistakes

- treating an underpayment as close enough
- refunding an overpayment without address verification
- assuming the wrong amount means BCH failed
- resolving the case without a clear merchant rule

## Short Answer

If the BCH amount is wrong, first compare the expected amount with the received amount. Then treat the case as an underpayment or overpayment exception instead of a normal completed checkout.