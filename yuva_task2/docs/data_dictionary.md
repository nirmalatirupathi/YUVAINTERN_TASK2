# Proposed Data Dictionary — Hypothetical Customer Churn Dataset

The following fields are proposed examples for a customer churn analysis. They are planning definitions, not a claim that these columns exist in a supplied dataset.

| Field | Type | Example meaning |
|---|---|---|
| customer_id | identifier | Unique customer identifier; exclude from predictive analysis |
| tenure_months | numeric | Months since customer started service |
| monthly_charges | numeric | Monthly amount charged |
| total_charges | numeric | Total amount charged over the relationship |
| contract_type | categorical | Month-to-month, annual, or other contract grouping |
| payment_method | categorical | Payment method category |
| support_tickets | numeric | Number of support contacts in a defined period |
| service_usage | numeric | Usage measure appropriate to the service |
| satisfaction_score | numeric | Customer satisfaction measure |
| churn | binary target | Whether the customer left during the defined observation window |

Before analysis, definitions, units, observation windows and category values must be verified against the actual approved dataset.
