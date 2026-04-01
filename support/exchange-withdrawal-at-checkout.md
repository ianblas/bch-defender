# Exchange Withdrawal at Checkout

## Summary

A customer may try to pay a merchant directly from an exchange account, or a user may send BCH to an exchange deposit address and expect it to behave like a normal BCH wallet-to-wallet payment.

This often creates confusion.

From a BCH support perspective, the key point is simple:

- BCH itself is usually fast for direct wallet-to-wallet payments
- exchange deposits and withdrawals are often slower than normal BCH payments
- the delay often comes from exchange processing, not from the BCH network

## Why It Matters

When an exchange is involved, people often misdiagnose the problem.

They may say:

- “BCH is slow”
- “the payment is stuck”
- “the merchant did not receive it”

But what often happened is one of these:

- the exchange has not broadcast the withdrawal yet
- the exchange is batching withdrawals
- the exchange has not credited the deposit yet
- the user is confused by BCH address format differences

A good support answer should defend BCH accurately and identify the real bottleneck.

## What to Verify

### 1. Ask whether the payment started from a non-custodial BCH wallet or from an exchange

A normal BCH wallet-to-wallet payment is usually much faster than an exchange withdrawal.

### 2. Ask whether there is a transaction ID

If there is no transaction ID yet, the exchange may not have broadcast the withdrawal.

### 3. Confirm that BCH is the asset being sent

Do not assume the user chose the correct asset or chain.

### 4. Confirm the destination is a BCH address

Check carefully whether the destination matches the intended BCH payment flow.

### 5. Check the BCH address format

Some exchanges still display or request a legacy BCH address instead of a CashAddr address.

That can confuse users when:

- paying from an exchange
- withdrawing to an exchange
- receiving to an exchange
- comparing one wallet screen to another

This is not the same thing as sending on the wrong blockchain, but it can still create operational mistakes.

### 6. Check whether the exchange has credited the deposit yet

Even when BCH has already arrived on-chain, the exchange may take longer to show it in the user balance.

## Step-by-Step Guidance

### 1. Explain the difference between BCH speed and exchange speed

Use plain language.

A good explanation is:

- BCH itself is normally fast for direct payments
- exchanges often add extra delay that does not come from BCH itself

### 2. Ask for the transaction ID if the exchange says the withdrawal was sent

If a valid BCH transaction exists, support can verify it.

If no transaction ID exists, the delay may still be inside the exchange.

### 3. Tell the merchant not to confuse an exchange screen with a completed BCH payment

A withdrawal request is not the same thing as a visible BCH transaction.

### 4. For live checkout, prefer a non-custodial BCH wallet

If the payment must be immediate, a normal BCH wallet is usually the better option.

### 5. Slow down when address format confusion appears

If one side shows CashAddr and the other side shows a legacy BCH address, confirm carefully before sending.

The main point is still that both must represent BCH, not another chain.

## Common Causes

- exchange withdrawal delay
- exchange deposit not yet credited
- user expects exchange speed to match BCH wallet speed
- no transaction ID yet because the exchange has not broadcast
- confusion between CashAddr and legacy BCH address formats
- customer is trying to use an exchange during a live checkout flow that expects immediate payment

## Common Mistakes

- blaming BCH for exchange-side delay
- treating an exchange withdrawal screen as proof of completed payment
- ignoring BCH address-format confusion
- assuming CashAddr and legacy BCH presentation mean different coins
- telling a merchant to release goods before the BCH transaction is actually visible

## Short Answer

If an exchange is involved, the delay may come from the exchange, not from BCH. Check whether the withdrawal was actually broadcast, verify that BCH is being used, watch for CashAddr versus legacy BCH address confusion, and prefer a non-custodial BCH wallet for live checkout.