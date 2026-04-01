# Label Schema

## Purpose

This file defines a simple labeling scheme for routing BCH Defender cases.

The schema is intentionally lightweight so it can be used in datasets, runtime routing, or analysis.

## Primary Label

Each case should have one primary label:

- `support`
- `merchant`
- `objections`
- `knowledge`

## Optional Secondary Labels

A case may also include secondary labels such as:

- `escalation`
- `beginner`
- `checkout`
- `exchange`
- `self_custody`
- `wrong_network`
- `wrong_address`
- `refund`
- `duplicate_payment`
- `wrong_amount`
- `wallet_restore`
- `zero_conf`
- `volatility`
- `btc_vs_bch`
- `merchant_ops`

## Example Shapes

### Simple support case

- primary: `support`
- secondary: `checkout`, `payment_not_received`

### Support case with risk

- primary: `support`
- secondary: `wrong_network`, `escalation`

### Merchant skepticism case

- primary: `merchant`
- secondary: `objections`, `volatility`

### Beginner concept question

- primary: `knowledge`
- secondary: `beginner`, `self_custody`

## Labeling Rule

The primary label should reflect the user's main need.

Secondary labels should reflect context, risk, or useful specialization.

## Safety Rule

When in doubt between a normal route and a risky route, keep the primary route but add `escalation` as a secondary label.