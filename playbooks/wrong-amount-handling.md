# Wrong Amount Handling

## Goal

Resolve BCH amount mismatches without treating them as normal completed payments.

## Core Rule

A wrong-amount BCH payment is an exception.

It must be handled deliberately as either an underpayment or an overpayment.

## First Checks

### 1. Compare the expected BCH amount with the received amount

Use the actual checkout request and actual payment record.

### 2. Determine whether the mismatch is underpayment or overpayment

The response depends on which kind of mismatch occurred.

### 3. Check whether the mismatch came from stale timing or user error

Examples include:

- stale quote
- late payment
- customer entered the wrong amount

## Handling Underpayment

### 1. Do not mark the sale complete automatically

An underpayment is not close enough by default.

### 2. Follow the merchant rule

A simple merchant rule is usually:

- complete the difference
- or resolve it as an exception or refund

## Handling Overpayment

### 1. Confirm the excess amount carefully

Separate the sale amount from the extra amount.

### 2. Use the refund process if needed

If the merchant will return the excess, do it through the normal BCH refund process with a verified destination address.

## Staff Rules

- do not improvise the amount rule at the counter
- do not treat an underpayment as fully complete without policy
- do not refund an overpayment casually or to an assumed address

## Escalate When

Escalate if:

- the amount mismatch is disputed
- the timing context is unclear
- the refund amount is not obvious
- staff is unsure which merchant policy applies

## Short Answer

When the BCH amount is wrong, first determine whether it is an underpayment or an overpayment. Then resolve it as an exception according to merchant policy rather than treating it as a normal completed checkout.