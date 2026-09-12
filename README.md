# BeautyPolicies

A dated dataset of return conditions and free-shipping terms for 48 beauty brands and retailers serving US shoppers. The CSV and JSON preserve the answers published in BeautyDeals' comparison table, including 54 `Unconfirmed` cells across the four policy fields. This export adds no policy facts, coupon codes, estimates or new research.

## Files and fields

`policies.csv` is UTF-8 CSV with a header and one row per brand. `policies.json` contains the same records as a JSON array. Both contain these seven fields:

| Field | Meaning |
|---|---|
| `brand` | Brand or retailer name as displayed in the comparison. |
| `return_window` | Published return or request deadline, its starting event, and stated restrictions. It is text, not a normalized number of days. |
| `return_postage` | Who pays return postage, with a fee only where the comparison states one. Original outbound delivery charges are not a substitute for return postage. |
| `free_shipping_threshold` | Published free-shipping condition, including destination, membership or purchase restrictions. Amounts are USD unless explicitly marked C$. |
| `opened_products` | Published treatment of opened or used products and stated exceptions. |
| `official_sources` | An object mapping each policy field to official URLs already linked from its on-site evidence row. In CSV, this object is serialized as JSON. An empty array means the policy answer is `Unconfirmed`, not that an official page supports the missing answer. |
| `reviewed_on` | The original policy review date in `YYYY-MM-DD` format, preserved from the comparison. |

## Review date and updates

All records in this snapshot carry the review date **2026-09-12**. Exporting the files, republishing a dataset, or rebuilding the website does not constitute a new policy review and must not advance that date.

Updates are manual snapshots of the published comparison after its underlying evidence has been reviewed. Preserve the wording and `Unconfirmed` values, check CSV/JSON parity, and record a new version when publishing changed data. This repository has no automatic policy-refresh job.

`Unconfirmed` means the reviewed material did not establish a clear answer, or conflicting official terms remained unresolved. It does not mean that a brand never offers that benefit. Conditional windows and membership-only thresholds should not be compared as unconditional promises. Check the current official policy before buying or returning a product.

BeautyDeals summarizes official offers, shipping terms and return policies for US shoppers. Its sourced summaries distinguish confirmed terms from missing or conflicting information and do not invent coupon codes. This dataset was exported and checked with AI assistance; it is not an endorsement by any listed brand.

## Reuse

The compilation and authored summaries are shared under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). Attribution: BeautyDeals, review date 2026-09-12. Brand names, trademarks and linked official policies remain the property of their respective owners.

[View the source comparison and its on-site evidence](https://lxlex.com/beauty-returns-free-shipping-comparison.html).
