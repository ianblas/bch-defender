# Payment Not Received

## Summary

When a BCH payment does not appear immediately, the goal is to troubleshoot calmly and methodically.

Most payment problems are not protocol failures. They are usually caused by one of these:

- the sender did not broadcast the transaction correctly
- the merchant is checking the wrong wallet or wrong address
- the payment was sent on the wrong network
- the wallet or point-of-sale view has not refreshed yet
- the customer never actually completed the send flow

From a BCH support perspective, the right response is practical: verify what happened before assuming the payment failed.

## Why It Matters

At checkout, confusion feels like lost money even when the problem is simple.

A clear support procedure helps merchants:

- avoid panic
- avoid double-charging a customer
- identify real mistakes quickly
- preserve trust in BCH payments

## Step-by-Step Guidance

### 1. Ask the customer if they tapped Send and confirmed it

Do not assume a QR scan means payment was completed.

Many first-time users scan correctly but do not finish the transaction.

### 2. Check the receive address

Confirm the payment was sent to the correct BCH address or payment request.

If the customer sent to the wrong address, the problem is not a delayed payment. It is a wrong-destination payment.

### 3. Check the network

Confirm the customer sent BCH on the intended network and did not use another chain by mistake.

### 4. Refresh the wallet or point-of-sale tool

Sometimes the transaction was sent but the merchant app has not refreshed yet.

### 5. Ask for the transaction ID if available

If the wallet shows a transaction ID, use it to verify whether the payment exists and was broadcast.

### 6. Check whether the merchant is looking in the right wallet

Some businesses use more than one wallet, device, or address flow. Make sure staff is checking the correct one.

### 7. Decide whether this is a zero-conf checkout case or a real failure

If the transaction is visible in the merchant wallet, it may already be safe enough for an ordinary retail checkout even before confirmation.

## Common Causes

- customer scanned but did not send
- wrong BCH address used
- wrong network used
- merchant checked the wrong wallet
- stale app state or no refresh
- customer used a wallet they do not understand well

## Common Mistakes

- charging the customer twice before checking properly
- assuming no confirmation means no payment exists
- letting staff improvise without a checklist
- confusing a delayed refresh with a failed payment
- not asking for a transaction ID or on-screen proof when needed

## Short Answer

When a BCH payment seems missing, first confirm the customer actually sent it, then verify the address, network, wallet view, and transaction status before treating it as a failed payment.
