# Merchant FAQ

## How does BCH checkout work for a merchant?

A typical BCH checkout is simple:

1. enter the sale amount
2. show the BCH QR or payment request
3. customer scans with a BCH wallet
4. customer taps Send
5. staff confirms the payment is visible
6. complete the sale

For most merchants, the goal is a repeatable payment flow, not a complicated crypto stack.

## Do I need a full POS integration to start?

No.

Many merchants start with a basic BCH wallet and QR flow. A more advanced point-of-sale setup can come later if volume or workflow complexity increases.

## Should I price in BCH or in local fiat?

Most merchants should start by keeping prices in local fiat and converting to BCH at checkout.

That keeps business logic simple while still using BCH as the payment method.

## Can I accept zero-conf payments?

For ordinary low-value retail payments, merchants can often accept BCH once the payment is visible.

For unusually large payments, the business may choose a stricter process.

## What should staff know?

Staff should know:

- how to open the BCH checkout screen
- how to show the QR
- how to recognize a visible payment
- when to call a manager

They do not need to become protocol experts.

## What if the customer says they paid but I do not see it?

Do not panic.

Check whether the customer actually tapped Send, verify the correct BCH address and network, refresh the wallet or POS view, and ask for the transaction ID if needed.

## What if the customer paid from the wrong network?

Treat that as a routing mistake, not as a delayed BCH payment.

First identify what asset was sent, on which network, and whether the business controls any relevant keys before saying anything about recovery.

## What if the QR does not scan?

First improve the scan conditions.

If that still fails, show the BCH address and amount separately and ask the customer to confirm both before sending.

## What if the customer paid twice?

First verify that there are actually two real BCH transactions.

If there was a duplicate payment, handle the extra amount through a controlled refund process instead of improvising at the counter.

## How should refunds work?

A BCH refund should be treated as a new outgoing payment from the business.

The merchant should define in advance:

- who approves refunds
- whether refunds are based on BCH amount or local fiat value
- which wallet sends the refund
- how the destination BCH address is verified

## Can BCH payments be reversed automatically?

No.

A BCH refund is a new transaction. It is not an automatic reversal of the original payment.

## What if internet is unstable during checkout?

If the merchant cannot verify the payment, staff should avoid making strong claims too quickly.

Try another device, network, or verification path before deciding whether the payment was received.

## Why accept BCH at all?

For many merchants, BCH is attractive because it offers:

- low fees
- direct payment
- no mandatory chargebacks when accepted directly
- a practical peer-to-peer payment flow
