# Invoicing — Reference

Invoice creation, management, credit/debit memos, Invoice Status Portal, and APJ tax compliance for SAP Business Network.

**Official SAP Sources (v2605):**
- [SAP Business Network Guide to Invoicing](https://help.sap.com/docs/ARIBA_NETWORK_SUPPLIERS/df996b7f6947439ea45b8612e47571f5?locale=en-US&state=PRODUCTION&version=2605)
- [Creating and Managing Invoices, Credit Memos, and Debit Memos](https://help.sap.com/docs/ARIBA_NETWORK_SUPPLIERS/82a8b145b9084d9a88504b0775268576?locale=en-US&state=PRODUCTION&version=2605)
- [Invoice Status Portal for Suppliers](https://help.sap.com/docs/ARIBA_NETWORK_SUPPLIERS/39ee7a0f1f8547118dae8a344c54cfcb?locale=en-US&state=PRODUCTION&version=2605)

## 1. Invoice Types

| Type | Description | Requires PO |
|---|---|---|
| Standard Invoice | Invoice for goods/services against a PO | Yes |
| Non-PO Invoice | Invoice without a backing PO | No (buyer must allow) |
| Credit Memo | Reduces a previously submitted invoice | References original invoice |
| Debit Memo | Increases a previously submitted invoice | References original invoice |
| Line-Level Credit | Credit against a specific invoice line | References original line |
| Service Invoice | Invoice for service POs with service entry sheets | Yes (service PO) |
| Blanket PO Invoice | Invoice drawn against a framework agreement | Yes (blanket PO) |

## 2. Invoice Creation Methods

### PO Flip (Portal)
Navigate to PO in SBN → Create Invoice → fields pre-populated → adjust quantities/prices → submit. Fastest method; recommended for low-to-medium volumes.

### Manual Entry (Portal)
Invoices → Create → enter all fields manually. Used for non-PO invoices.

### cXML — InvoiceDetailRequest
Programmatic invoice submission via cXML (>500 invoices/year). DTD: `http://xml.cXML.org/schemas/cXML/1.2.069/cXML.dtd`

Key elements: `<InvoiceDetailRequest>`, `<InvoiceDetailRequestHeader>`, `<InvoiceDetailOrder>`, `<InvoiceDetailItem>`, `<InvoiceTax>`, `<InvoiceDetailPaymentTerm>`

### EDI — INVOIC D96A (Inbound)
EDIFACT INVOIC D96A via Managed Gateway. See `references/edifact-d96a.md` §3.

## 3. Key Invoice Fields

**Header (Required):** Invoice number (unique per supplier), invoice date, PO number (PO-based invoices), supplier ANID, buyer ANID, currency, total amount.

**Line Level:** Line number, item description, quantity, UoM, unit price, line total, UNSPSC (if buyer requires).

**Tax:** Tax category (VAT/GST/sales tax), tax rate (%), taxable amount, tax amount, tax registration number.

**Payment:** Payment terms, bank details (if configured), remittance email.

## 4. Invoice Validation & Rejection

Buyers configure transaction rules that validate invoices on submission. Common rejection reasons:
- PO not found or closed
- Invoice amount exceeds PO tolerance
- Duplicate invoice number
- Missing required tax fields
- Currency mismatch
- Quantity exceeds PO (tolerance-dependent)

For buyer-side validation rules: `references/buyer-administration.md` §3.

### Rejection Troubleshooting (Supplier Step-by-Step)

| Rejection Reason | Resolution Steps |
|---|---|
| **PO not found / closed** | 1. Verify PO number (leading zeros, buyer suffix) in Orders tab. 2. Check PO status — if "Closed" or "Cancelled", contact buyer to re-open or issue new PO. 3. If PO exists in buyer's ERP but not SBN, buyer must re-transmit PO. |
| **Invoice exceeds PO tolerance** | 1. Check remaining PO balance: Orders → PO → Related Documents → view invoiced totals. 2. If legitimate over-shipment, ask buyer to increase PO amount or issue change order. 3. Otherwise, issue a credit memo against the rejected invoice for the overage amount. 4. Resubmit at or below the buyer's tolerance % (common thresholds: 5–10%). |
| **Duplicate invoice number** | 1. Search Invoices → outbox for the same invoice number — confirm whether the original was already approved. 2. If originally rejected and you are resubmitting, use a new unique invoice number (e.g., append -R1). 3. If an accidental duplicate, simply cancel/discard the second submission. |
| **Missing required tax fields** | 1. Check buyer's tax requirements: Inbox → PO → scroll to header for tax instructions. 2. Add missing fields: Tax ID, Tax Rate, Tax Category, Taxable Amount, Tax Amount. 3. For APJ invoices: ensure correct country-specific tax registration (GST for AU/IN, JCT T-number for JP). 4. Resubmit with corrected tax details. |
| **Currency mismatch** | 1. Compare your invoice currency against the PO header currency. 2. SBN requires the invoice currency to match the PO currency unless buyer has enabled multi-currency. 3. Correct currency on the invoice and resubmit. |
| **Quantity exceeds PO** | 1. Review PO line quantities vs. what has already been invoiced. 2. If over-delivery was accepted (buyer confirmed GR), ask buyer to increase PO qty or submit a change order. 3. Otherwise, reduce invoice quantity to remaining open quantity and issue a partial invoice. |

### General Resolution Workflow
1. **View rejection reason:** Invoices → Outbox → click rejected invoice → view Status tab → "Rejection Reason" field
2. **Correct and resubmit:** Fix the issue in a new invoice (rejected invoices cannot be edited in place)
3. **If correction unclear:** Contact buyer's AP department referencing the PO number and original invoice number
4. **Track resubmission:** New invoice will appear in Outbox with fresh status; monitor for 24–48 hours

## 5. Invoice Status Lifecycle

```
Draft → Submitted → Sent → [Approved | Rejected | Disputed | Cancelled]
                                       ↓
                                 Paid (if buyer sends remittance)
```

| Status | Meaning |
|---|---|
| Draft | Saved but not submitted |
| Submitted | Sent to SBN |
| Sent | Delivered to buyer's system |
| Approved | Buyer approved for payment |
| Rejected | Buyer rejected — see rejection reason |
| Disputed | Buyer raised a dispute |
| Cancelled | Supplier cancelled before buyer processing |
| Paid | Payment confirmed (if buyer sends remittance) |

## 6. Invoice Status Portal
Self-service portal for suppliers to track invoice status without logging into the full SBN portal.
- Features: status search by invoice number/date range, rejection reason visibility, download invoice details

## 7. Credit Memos and Debit Memos

**Credit Memo:** Reduces a previously invoiced amount. Must reference original invoice number. Uses: returns, overbilling correction, pricing adjustments.

**Debit Memo:** Increases a previously invoiced amount. References original invoice. Uses: price adjustments, additional charges.

**Line-Level Credit:** Credits a specific line item. Used when only partial correction is needed.

## 8. Multi-Tax and Multi-Currency
- Multiple tax lines supported per invoice
- Foreign currency invoices: invoice in transaction currency; SBN converts for reporting
- Tax ID requirements: configure in Supplier Tax Invoice Configuration

## 9. APJ Tax Compliance

### India GST e-Invoicing

**Mandate:** Businesses with Aggregate Annual Turnover (AATO) exceeding ₹5 Crore must generate e-invoices with IRN (Invoice Reference Number) from the government IRP.

**Turnover Thresholds:**
| Threshold | Effective Date |
|---|---|
| Above ₹500 Crore | 1 October 2020 |
| Above ₹100 Crore | 1 January 2021 |
| Above ₹50 Crore | 1 April 2021 |
| Above ₹20 Crore | 1 April 2022 |
| Above ₹10 Crore | 1 October 2022 |
| **Above ₹5 Crore** | **1 August 2023** |

**30-Day Reporting Rule (from April 2025):** Taxpayers with AATO ≥₹10 Crore must report B2B invoices to IRP within 30 days.

**IRN Generation (SHA-256 hash of):** Supplier GSTIN + Invoice Number + Document Type (INV/CRN/DBN) + Financial Year.

**QR Code Contains (8 parameters):** Supplier GSTIN, Buyer GSTIN, Invoice Number, Invoice Date, Invoice Value, Line Item Count, HSN Code of Main Item, IRN.

**SBN Integration Path:**
1. Supplier creates invoice in ERP → JSON to IRP via GSP/ASP
2. IRP returns IRN + signed QR code
3. IRN/QR stored in SAP billing document
4. Invoice with IRN/QR submitted to buyer via SBN

**SAP Help:** [India 2019 Tax Regulation](https://help.sap.com/docs/buying-invoicing/sap-business-network-guide-to-invoicing/india-2019-tax-regulation)

### Japan Qualified Invoice System (JCT)

**Effective:** 1 October 2023. Buyers can only claim JCT input tax credit from registered qualified invoice issuers.

**Tax Registration Number:** T + 13 digits (e.g., T1234567890123). For corporations: 13 digits = Corporate Number.

**Mandatory Fields on Qualified Invoice:**
| # | Field |
|---|---|
| ① | Issuer name + Registration Number (T+13) |
| ② | Transaction date |
| ③ | Description of goods/services (mark reduced-rate items) |
| ④ | Amounts totalled separately by tax rate (10% / 8%) |
| ⑤ | Applicable tax rate(s) |
| ⑥ | Consumption tax amount by rate |
| ⑦ | Buyer name |

**JCT Tax Rates:** Standard 10%, Reduced 8% (food/beverages excl. dining out; newspaper subscriptions).

**Transitional Rules:** Non-registered supplier purchases: 80% credit (Oct 2023–Sep 2026), 50% credit (Oct 2026–Sep 2029), 0% after Oct 2029.

**SBN Support (from release 2305):**
- Suppliers configure T-number in Administration → Legal Profile
- Tax Registration Types: Registered, Non-Registered, Exempted
- SBN uses T-number to route qualified invoices
- Buyers can require Tax Registration Number on all invoices
- JP PINT Peppol format supported via SAP DRC integration

**SAP Help:** [Tax Invoicing in Japan](https://help.sap.com/docs/buying-invoicing/sap-business-network-guide-to-invoicing/tax-invoicing-in-japan)

### Australia Peppol e-Invoicing

**Standard:** PINT A-NZ Billing (Peppol International — Australia/New Zealand). Mandatory since May 2025; BIS 3.0 retired.

**Mandate Timeline:**
| Date | Obligation | Who |
|---|---|---|
| July 2022 | Must receive Peppol eInvoices | All Non-Corporate Commonwealth Entities (NCEs) |
| Nov 2024 | PINT A-NZ receivable | All Peppol participants |
| May 2025 | PINT A-NZ mandatory for sending; BIS 3.0 retired | All Peppol participants |
| July 2026 | 30% of invoices via Peppol | NCEs |
| Dec 2026 | Auto-processing AND sending | All NCEs |

**SBN Peppol Status:**
- SAP Business Network is listed as **eInvoicing Ready: Receive Only** on ATO register
- Full Peppol send/receive requires **SAP Document and Reporting Compliance (DRC)** Peppol Service
- DRC connects to a certified Peppol Access Point
- ABN (Australian Business Number) used as Peppol Participant ID
- Configuration: Administration → Configuration → Configure External Network Identifiers

**SAP Help:** [Peppol Integration for SAP Business Network](https://help.sap.com/docs/buying-invoicing/sap-business-network-guide-to-invoicing/peppol-integration-for-sap-business-network-3758806e368d4360a140b287d66b9c4f)

## 10. Routing and Transmission
Invoices route per buyer's document routing rules: cXML to buyer ERP, EDI via Managed Gateway, email PDF, or buyer portal review.

Document routing config: `references/account-management.md` §6.

## 11. Builder Playbook
- Invoice types: §1 table
- PO flip walkthrough: §2
- Generate InvoiceDetailRequest cXML: §2 + DTD reference
- Troubleshoot rejection: §4 (common reasons + step-by-step resolution table + general workflow)
- Credit/debit memo: §7
- Tax guidance: §8 + §9 (APJ-specific)
- India e-invoicing: §9 India section
- Japan JCT: §9 Japan section
- Australia Peppol: §9 Australia section
- EDIFACT INVOIC: edifact-d96a.md §3
