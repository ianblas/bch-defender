# Exchange at Checkout

## Goal

Handle BCH checkout cases involving exchanges without blaming BCH for exchange-side delay.

## Core Rule

A direct BCH wallet-to-wallet payment is usually faster and simpler than an exchange withdrawal.

If an exchange is involved, the delay may come from the exchange rather than from BCH.

## First Checks

### 1. Ask whether the customer is paying from a non-custodial BCH wallet or from an exchange

This changes the expected timing.

### 2. Ask whether there is a transaction ID yet

If there is no transaction ID, the exchange may not have broadcast the BCH withdrawal yet.

### 3. Confirm the asset and destination

Make sure the customer is actually sending BCH to the intended BCH destination.

### 4. Watch for BCH address-format confusion

Some services may still display legacy BCH address format instead of CashAddr.

That can create operational confusion even when the payment is still on BCH.

## Handling Rule

### If the merchant needs immediate checkout certainty

Prefer a non-custodial BCH wallet.

Do not assume an exchange withdrawal will behave like instant in-person BCH checkout.

### If the customer insists the exchange already sent the payment

Ask for the transaction ID and verify whether the BCH transaction actually exists.

### If there is no transaction ID yet

Do not complete the sale based on an exchange screen alone.

## Staff Rules

- do not call BCH slow when the delay may be exchange-side
- do not treat an exchange withdrawal request as proof of completed payment
- do not ignore BCH address-format confusion when exchanges are involved

## Escalate When

Escalate if:

- the asset or destination is unclear
- no one can verify whether BCH was actually broadcast
- the address-format situation is confusing
- the merchant is unsure whether to release goods before visible payment

## Short Answer

If a customer is paying from an exchange, treat it differently from a normal BCH wallet payment. Verify whether BCH was actually broadcast and do not blame BCH for delays that may come from the exchange.