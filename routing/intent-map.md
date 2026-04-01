# Intent Map

## Primary Intent Categories

### 1. Support

Use this route when the user has a BCH problem to resolve.

Common sub-intents include:

- payment not received
- wrong network
- wrong address
- duplicate payment
- wrong amount
- fake payment proof
- exchange delay at checkout
- wallet restored but funds missing
- QR not scanning
- unstable internet or app interruption

### 2. Merchant

Use this route when the user mainly needs merchant setup, policy, checkout, staff, pricing, refund, or treasury guidance.

Common sub-intents include:

- onboarding a merchant
- point-of-sale flow
- staff training
- pricing BCH vs fiat
- refund handling
- merchant treasury

### 3. Objections

Use this route when the user is skeptical, dismissive, comparative, or asking why BCH matters.

Common sub-intents include:

- is BCH dead
- why not BTC
- why should merchants care
- volatility
- complexity
- nobody uses BCH

### 4. Knowledge

Use this route when the user mainly needs definitions, distinctions, or conceptual understanding.

Common sub-intents include:

- what is BCH
- what is a wallet
- what is a seed phrase
- what is self-custody
- what is zero-conf
- what is CashAddr
- BCH vs BTC at a basic level

### 5. Escalation

Use this route when the case is ambiguous, risky, or likely to produce bad guidance if handled too casually.

Common triggers include:

- unclear asset or network
- disputed payment with weak evidence
- wrong-network recovery questions
- technically ambiguous wallet restore case
- unclear refund authority or destination

## Secondary Behavior Flags

A case may carry more than one label even if one route is primary.

Examples:

- support + escalation
- merchant + objections
- knowledge + beginner
- support + exchange
