# Checkout Troubleshooting FAQ

## The customer scanned the QR. Does that mean the payment is complete?

No.

A QR scan only starts the flow. The customer still needs to confirm the BCH transaction.

## The payment is not visible yet. What should staff do first?

First check:

- did the customer tap Send?
- is the BCH address correct?
- is the customer using the correct network and asset?
- has the merchant wallet or POS refreshed?
- is there a transaction ID?

## What if the QR does not scan?

Improve brightness, focus, distance, and angle first.

If scanning still fails, show the BCH address and the amount separately and ask the customer to verify both before sending.

## What if the customer paid the wrong amount?

Treat that as an exception, not as a normal completed payment.

If the payment is too low, the merchant should use a simple rule such as complete the difference or resolve it as an exception.

If the payment is too high, confirm the excess and use a controlled refund flow if needed.

## What if the customer paid twice?

First verify that there are actually two real BCH transactions.

If both exist, identify the extra amount and resolve it through the refund process instead of improvising.

## What if the customer only shows a screenshot?

A screenshot is not proof of a BCH payment.

Verify the transaction in the merchant wallet or with a transaction ID before treating the payment as received.

## What if the customer paid from an exchange?

Be careful.

A normal BCH wallet-to-wallet payment is usually faster than an exchange withdrawal. The exchange may delay broadcast or crediting, so the merchant should not confuse exchange delay with BCH delay.

## What if the checkout app closed or refreshed during the sale?

Do not immediately ask the customer to pay again.

First reopen the wallet or payment history and check whether the original BCH payment already exists.

## What if internet is unstable during checkout?

The problem may be verification, not BCH itself.

Try another device, another network, or another verification path before deciding whether the payment exists.

## What if the customer used the wrong network?

Treat that as a routing problem, not as a normal pending BCH payment.

First determine what asset was sent, on which network, and whether the business controls any relevant keys.

## Can the merchant accept zero-conf?

For ordinary low-value retail payments, merchants can often accept BCH once the payment is visible.

For unusually large payments, the merchant may choose a stricter policy.
