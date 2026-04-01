# Decision Tree

## Step 1: What is the user's main need?

### If the user needs a problem solved now

Route to **support**.

Examples:

- "The payment is not showing"
- "The customer paid twice"
- "The QR is not scanning"
- "I restored my wallet and the BCH is missing"

### If the user mainly wants operational business guidance

Route to **merchant**.

Examples:

- "How should a merchant accept BCH?"
- "Should I price in BCH or fiat?"
- "How should staff handle refunds?"

### If the user is mainly skeptical or comparative

Route to **objections**.

Examples:

- "Why not just use BTC?"
- "Is BCH dead?"
- "Why would any merchant care?"

### If the user mainly wants a concept explained

Route to **knowledge**.

Examples:

- "What is self-custody?"
- "What is CashAddr?"
- "What does zero-conf mean?"

## Step 2: Should escalation logic also apply?

Add **escalation** if any of these are true:

- the asset or network is unclear
- the payment is disputed and evidence is weak
- the user asks for recovery certainty in a wrong-network case
- the wallet restore case is technically ambiguous
- the refund authority or refund destination is unclear

## Step 3: Add useful secondary tags

Examples:

- `merchant`
- `beginner`
- `exchange`
- `checkout`
- `self_custody`
- `wrong_network`
- `refund`
- `volatility`
- `btc_vs_bch`

## Tie-Break Rules

### Support beats knowledge

If the user is asking about a real problem happening now, prefer support even if the question includes conceptual confusion.

### Merchant beats objections when the real need is operational

If a skeptical merchant is still asking how to operate, route to merchant and use objection-aware tone.

### Escalation beats overconfidence

If the case is risky or unclear, add escalation rather than pretending certainty.

## Short Rule

First identify whether the user needs help, operations, persuasion, or explanation. Then add escalation if ambiguity creates risk.