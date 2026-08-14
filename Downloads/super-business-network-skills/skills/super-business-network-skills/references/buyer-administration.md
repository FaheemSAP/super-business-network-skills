# Buyer Administration — Reference

Buyer account configuration, supplier enablement, transaction rules, and Spot Buy management.

**Official SAP Sources (v2605):**
- [SAP Business Network Buyer Administration Guide](https://help.sap.com/docs/ARIBA_NETWORK/5c0bdb0caa3042a288b3a1fb83b2fb1e?locale=en-US&state=PRODUCTION&version=2605)
- [Enabling Suppliers on SAP Business Network](https://help.sap.com/docs/ARIBA_NETWORK/94006af654b1475da6fcf0072628f3af?locale=en-US&state=PRODUCTION&version=2605)
- [Content Management for SAP Ariba Spot Buy](https://help.sap.com/docs/ARIBA_NETWORK_SUPPLIERS/54bbd5c95a53450a8f923f1717e006b1?locale=en-US&state=PRODUCTION&version=2605)

## 1. Buyer Account Overview

Key buyer administration areas: supplier enablement and relationship management, transaction rules (invoice and order validation), document routing to ERP, catalog management (approving supplier catalogs), reporting, and integration configuration.

## 2. Supplier Enablement from the Buyer Side

| Enablement Type | Description |
|---|---|
| TRR (Trading Relationship Request) | Invite a supplier to join SBN |
| Bulk Enablement | Invite multiple suppliers via CSV upload |
| Self-Registration | Supplier registers independently; buyer approves |
| Migration | Move existing supplier from legacy Ariba to SBN |

**Enablement Workflow:**
1. Supplier Management → Suppliers → Enable Supplier
2. Enter supplier details (name, contact email, country, DUNS)
3. Send TRR → supplier receives email
4. Supplier registers or accepts (if existing ANID)
5. Buyer validates Active relationship status
6. Configure supplier-specific rules and routing

| Supplier Status | Meaning |
|---|---|
| Invited | TRR sent, not yet responded |
| Registered | Supplier has created/linked an ANID |
| Active | Full trading relationship established |
| Inactive | Relationship paused |

### Bulk Supplier Enablement (Vendor CSV Upload)

Buyers upload a **Vendor CSV file** (VUF) to bulk-register/enable suppliers.

**Path:** Supplier Enablement → Manage Vendors → Upload

**Required CSV Fields:**
| Column | Required | Notes |
|---|---|---|
| Vendor Name | Yes | Buying org’s name for vendor |
| Vendor ID | Yes (or Tax ID) | Buyer-specific vendor identifier |
| Tax ID | Yes (or Vendor ID) | Alternative identifier |
| Vendor City | Yes (or Postal Code) | At least one of City/Postal required |
| Vendor Postal Code | Yes (or City) | At least one of City/Postal required |
| Vendor Country Code | Yes | ISO country code (e.g., US, DE, AU) |
| Vendor Province/State | Conditional | Required for US states |
| System ID | Conditional | Required for multi-ERP buyers |

**Optional CSV Fields:**
| Column | Notes |
|---|---|
| ERP Purchase Order Count | Integer |
| ERP Invoice Count | Integer |
| ERP Spend Per Year | Decimal |
| ERP Spend Currency | ISO 3-letter (e.g., USD) |
| Wave | Wave01 through Wave20 (phased rollouts) |
| Proposed Enablement Mode | Segmentation field |
| D-U-N-S Number | 9-digit DUNS |
| AN Supplier Group | SBN supplier group name |

**CSV Rules:** UTF-8 encoding, commas in values must be double-quoted, column headers are case-sensitive (use Download Template).

**Upload Process:**
1. Navigate to Supplier Enablement → Manage Vendors
2. Click Download Template (if first time)
3. Populate CSV
4. Click Upload → select file
5. SBN validates; errors reported with row-level detail
6. Successful entries appear in Manage Vendors list
7. Segment into waves for enablement outreach

**Supplier ID File (4-column format)** — for mapping already-registered suppliers to vendor records:
| Column | Purpose |
|---|---|
| Vendor ID | Buyer-side ID |
| System ID | ERP system identifier |
| ANID | Supplier’s SBN ID |
| Preferred | Yes/No |

## 3. Transaction Rules

Buyer-configured rules validate transactions. Location: Administration → Transaction Rules.

**Invoice Rules:**
- Tolerance rules: accept invoices within X% of PO amount
- Duplicate invoice check: block resubmission of same invoice number
- Required tax fields: mandate tax ID, rate, amount
- Date rules: reject invoices older than N days from PO date
- Line-level matching: require PO reference on each invoice line

**Order Rules:**
- PO acknowledgement required before ASN/invoice
- ASN required before invoice
- Tolerance on ASN quantities (% over/under)
- Delivery date tolerance (days early/late)
- Line-item OC enabled/disabled
- Route out-of-tolerance confirmations to buyer approval

## 4. Document Routing (Buyer Side)

**Routing Setup:** Administration → Document Routing → configure inbound routing (ASN, Invoice, OC → destination) and outbound routing (PO → source system).

**Integration with SAP S/4HANA:**
- S/4HANA Cloud: Scope item **7VL** (Supplier Integration) + **BD9** (SBN Integration)
- On-premise: configure cXML channel in SAP PI/PO or Integration Suite
- ANIDs must be maintained in S/4HANA vendor master (partner profile)

## 5. Catalog Management (Buyer Side)

**Catalog Approval Workflow:** Supplier uploads catalog → SBN validates → Buyer catalog admin reviews → Approve / Reject / Request changes → Approved catalog published.

**Buyer Catalog Settings:** Set UNSPSC required/recommended; configure allowed catalog types (CIF, PunchOut L1/L2); enable/disable CMS per supplier; set size limits; configure auto-approval for trusted suppliers.

Cross-reference: `references/catalog-hub.md` for CMS vs Non-CMS and catalog types.

## 6. SAP Ariba Spot Buy

Spot Buy is an embedded marketplace within SAP Ariba Buying for unplanned, maverick, or tail-spend purchases.

**Content Sources:** Supplier-uploaded Spot Buy catalogs, external marketplace content (e.g. Amazon Business), PunchOut connections.

**Spot Buy Catalog Requirements:**
- Format: CIF 3.0 or cXML
- Additional required fields vs. standard CIF: ManufacturerName, LeadTime, ImageURL
- UNSPSC codes mandatory for Spot Buy
- Content visibility controlled by buyer’s Spot Buy configuration

**Supplier Setup for Spot Buy:**
1. Enable Spot Buy in supplier’s catalog settings
2. Upload Spot Buy-specific catalog (may differ from standard P2P catalog)
3. Buyer content admin approves Spot Buy catalog separately

## 7. Buyer Reporting and Analytics
Administration → Reports → Transaction Summary. Key reports: Invoice Approval Rate, PO Cycle Time, Catalog Coverage, Supplier Compliance.

Full report types: `references/reports.md`.

## 8. Builder Playbook
- Supplier enablement: §2 workflow + status table
- Bulk enablement CSV: §2 (Bulk section) — fields, upload process, template
- Invoice rules config: §3 rules list
- Order/ASN tolerance: §3 order rules
- Routing setup: §4 buyer-side routing
- Catalog approval: §5 + catalog-hub.md
- Spot Buy: §6 catalog requirements
- S/4HANA integration: §4 scope items
