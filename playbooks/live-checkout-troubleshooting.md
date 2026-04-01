# Live Checkout Troubleshooting

## Goal

Resolve BCH checkout confusion quickly without blaming BCH too early or improvising under pressure.

## Standard Triage Order

### 1. Confirm the customer completed the send flow

A QR scan is not enough.

Ask whether the customer tapped Send and confirmed the BCH transaction.

### 2. Check the destination and network

Verify:

- the intended BCH address or payment request
- the correct asset
- the correct network

### 3. Refresh the merchant view

Sometimes the BCH transaction exists but the wallet or POS view is stale.

### 4. Ask for the transaction ID if needed

If the customer wallet shows a transaction ID, use it to verify whether the BCH payment exists.

### 5. Decide whether the case is operational or exceptional

Normal operational cases include:

- payment visible after refresh
- QR scan failure solved with fallback address
- small zero-conf payment visible and acceptable

Exceptional cases include:

- wrong network
- wrong amount
- duplicate payment
- exchange delay
- no transaction record

## Decision Rules

### If the BCH payment is visible and the amount is correct

Complete the sale according to the merchant confirmation policy.

### If the QR does not scan

Improve scan conditions first.

If needed, switch to showing the BCH address and amount separately.

### If the transaction is not visible but the customer claims it was sent

Do not complete the sale yet.

Verify the address, network, and transaction record.

### If the amount is wrong

Treat it as an exception, not a normal completed payment.

### If the customer used the wrong network

Escalate or move to wrong-network triage.

## Staff Rules

- do not improvise under pressure
- do not rely on screenshots alone
- do not ask for a second payment before checking whether the first one arrived
- do not blame BCH before verifying the real cause

## Escalate When

Escalate if:

- the asset or network is unclear
- the customer used the wrong network
- the amount mismatch cannot be resolved quickly
- the customer paid from an exchange and no transaction is visible yet
- staff is unsure whether the payment should be accepted

## Short Answer

At live checkout, the right BCH troubleshooting order is: confirm Send, verify address and network, refresh the merchant view, check for a transaction ID, and only then decide whether the case is normal or exceptional.