# Catalog Hub — Reference

Catalog types, CIF 3.0 fields, and 12 authoring validation rules.

## 1. Three catalog types

### Static CIF
Flat file with fixed prices. Setup: Low. Live pricing: No. P2P searchable: Yes. Formats: CIF, cXML, BMEcat, Excel (CMS).

**Flow:** Create Catalog → Upload → Sync & Approval → Buyer Searches → Item Detail → Add to Cart

### PunchOut Level 1 (site-level)
Buyer punched out to supplier webstore. Setup: Medium. Live pricing: Yes. P2P searchable: No. Formats: cXML.

**Flow:** Set Up PunchOut → Upload → Sync → Buyer Finds Entry → Supplier Site → Return to P2P

### PunchOut Level 2 (item-level)
Index makes items searchable; clicking punches out for live price. Setup: High. Live pricing: Yes. P2P searchable: Yes.

**Flow:** Create Index → Upload → Sync → Buyer Searches Items → Supplier Item Page → Return to P2P

> Messages: `PunchOutSetupRequest` (Ariba→supplier) and `PunchOutOrderMessage` (supplier→Ariba).

## 2. Decision tree

- Need live pricing? No → Static CIF. Yes → Q2.
- Buyers search items in Ariba? No → L1. Yes → L2.

## 3. CIF 3.0 — 81 fields, 7 required

### Required fields
| Field | Category |
|---|---|
| SupplierID | Core-ID |
| SupplierPartID | Core-ID |
| ItemDescription | Core-ID |
| UnitOfMeasure | Core-ID |
| ClassificationCodes | Core-ID |
| UnitPrice | Pricing |
| Currency | Pricing |

### Categories
- Core Identification (6), Pricing & Commerce (12), Availability & Territory (6), Imagery & Media (8), Search & Specifications (9), Advanced & Extended (34), CMS-Only (6)

### CIF structure
```
CIF_I_V3.0
CHARSET: UTF-8
CODEFORMAT: UNSPSC_V13.5
LOADMODE: F
SUPPLIERID_DOMAIN: NetworkID
CURRENCY: USD
UNUOM: TRUE
ITEMCOUNT: {n}
TIMESTAMP: {YYYY-MM-DD}
FIELDNAMES: ...
DATA
{rows}
ENDOFDATA
```

### Pricing models
Standard, Date-Dependent, Quantity-Tiered, Lookup-Key (buyer-side CMS only).

## 4. CMS vs Non-CMS

| Feature | Non-CMS | CMS |
|---|---|---|
| Formats | CIF, cXML, BMEcat | + Excel |
| Load modes | F + I | F only |
| Fields | 75 | All 81 |
| UNSPSC | Required | Recommended |

CMS-Only fields (6): HazardousMaterials, PaymentTerms, IsInternalPartID, CMSDomain1, CMSValue1, UnspscDescription.

## 5. The 12 authoring rules (11 Error + 1 Warning)

| # | Rule | Severity |
|---|---|---|
| 1 | REQUIRED_FIELDS | Error |
| 2 | UNSPSC_FORMAT | Error |
| 3 | PRICE_POSITIVE | Error |
| 4 | MARKET_PRICE_VALID | Error |
| 5 | URL_VALID | Error |
| 6 | LANGUAGE_VALID | Error |
| 7 | DATE_VALID | Error |
| 8 | ITEMCOUNT_MATCH | Error |
| 9 | LOADMODE_VALID | Error |
| 10 | CURRENCY_VALID | Error |
| 11 | CONTROL_CHARS | Error |
| 12 | ZERO_PRICE | Warning |

## 6. Size figures
10 MB hard limit, 3 MB auto-zip, 50,000 items max, Image ZIP 300 MB.

## 7. Builder playbooks
- Recommend type: decision tree
- Field guidance: §3
- Validation: 12 rules (§5)
- Sample CIF: use structure template