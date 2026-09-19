# Data dictionary and reuse notes

This snapshot describes published US direct-site beauty-brand return and shipping terms. It is not a complete market sample or a fresh check of current policies. Row-level review dates are retained in `reviewed_on`.

| Field | Type | Meaning |
| --- | --- | --- |
| `brand` | string | Brand or retailer display name. |
| `return_window` | string | Recorded return timing and conditions; the start event may be purchase, shipment or delivery. |
| `return_postage` | string | Recorded payer, fees and qualifications. A prepaid label does not alone establish that returns are free. |
| `free_shipping_threshold` | string | Recorded threshold, currency, geography and membership conditions. Preserve all qualifications. |
| `opened_products` | string | Recorded rules and exceptions for opened or used items. |
| `official_sources` | object / JSON-encoded CSV cell | Four arrays keyed by the policy field names above. Each URL supports that field; an empty array means no source was recorded for that field. |
| `reviewed_on` | ISO date string | Date carried by the source row, not a promise that the policy remains current. |

## Reuse checklist

- Preserve `Unconfirmed` verbatim. It is not a negative answer, zero, or a free-service claim.
- Keep amounts with their stated currency; the snapshot includes Canadian-dollar qualifications.
- Do not rank windows by extracting the first number: eligibility dates, exceptions and store-credit windows differ.
- Do not infer that a policy applies to third-party retailers, every US address, all membership tiers or international orders.
- Keep field-level official-source links and review dates with quoted or exported records.
- Check the linked official policies before making a purchase or describing a policy as current.
- Attribute the compilation to BeautyDeals, *Beauty Brand Policy Data*, 2026-09-16 snapshot, under CC BY 4.0. Brand names and third-party policy material retain their respective rights.

## Tool behavior

`query.py` uses Python's standard library and does not contact any website. Before searching, it checks required fields, unique brand names, date syntax, source-URL structure and exact CSV/JSON record equality. These checks do not verify the truth or current availability of a policy. Exported values retain their original wording.

A search with no match prints an empty JSON array (or a CSV header) and exits with status 1. Invalid input exits with status 2. Successful validation or a matching search exits with status 0.
