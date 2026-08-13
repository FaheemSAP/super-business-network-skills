# Catalog Hub — Reference

Catalog types, CIF 3.0 fields, and 12 authoring validation rules.

## 1. Three catalog types

### Static CIF
Flat file with fixed prices. Setup: Low. Live pricing: No. P2P searchable: Yes. Formats: CIF, cXML, BMEcat, Excel (CMS).

**Flow:** Create Catalog → Upload → Sync & Approval → Buyer Searches → Item Detail → Add to Cart

### PunchOut Level 1 (site-level)
Buyer punched out to supplier webstore. Setup: Medium. Live pricing: Yes. P2P searchable: No.

**Flow:** Set Up PunchOut → Upload → Sync → Buyer Finds Entry → Supplier Site → Return to P2P

### PunchOut Level 2 (item-level)
Index makes items searchable; clicking punches out for live price. Setup: High. Live pricing: Yes. P2P searchable: Yes.

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
Core Identification (6), Pricing & Commerce (12), Availability & Territory (6), Imagery & Media (8), Search & Specifications (9), Advanced & Extended (34), CMS-Only (6).

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
- Recommend type: decision tree (§2)
- Field guidance: §3
- Validation: 12 rules (§5)
- Sample CIF: use structure template (§3)

## 8. Official SAP Documentation Sources (v2605)

All URLs also maintained in `assets/doc-sources.json`.

| Document | SAP Help Portal URL |
|---|---|
| Customer Catalog Format Reference | https://help.sap.com/docs/ARIBA_NETWORK_SUPPLIERS/c8ad7036e6104bfaa33ec523991a6727?locale=en-US&state=PRODUCTION&version=2605 |
| Creating and Managing Customer Catalogs | https://help.sap.com/docs/ARIBA_NETWORK_SUPPLIERS/1e9220c0f83d42d097418c387d3bea9b?locale=en-US&state=PRODUCTION&version=2605 |
| Managing Network Catalog | https://help.sap.com/docs/ARIBA_NETWORK/efb9c5f471ef4c38a55cc5688a0d9509?locale=en-US&state=PRODUCTION&version=2605 |
| Content Management for SAP Ariba Spot Buy | https://help.sap.com/docs/ARIBA_NETWORK_SUPPLIERS/54bbd5c95a53450a8f923f1717e006b1?locale=en-US&state=PRODUCTION&version=2605 |

## 9. Network Catalog vs Customer Catalog

| Feature | Network Catalog | Customer Catalog |
|---|---|---|
| Visibility | All SBN buyers | Specific buyer only |
| Management | Supplier-controlled | Buyer rules apply |
| Approval | Auto or buyer | Buyer catalog admin |
| CMS | Not applicable | Buyer may enable |

Network Catalog: Catalogs → Network Catalog. Broad discoverability across SBN.
Customer Catalog: uploaded per-buyer relationship; subject to buyer validation rules and approval workflow.

Buyer-side catalog approval: `references/buyer-administration.md` §5.