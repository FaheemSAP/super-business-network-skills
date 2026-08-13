# Invoicing — Reference

Invoice creation, management, credit/debit memos, and Invoice Status Portal for SAP Business Network.

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

## 4. Invoice Validation
Buyers configure transaction rules that validate invoices on submission. Common rejection reasons:
- PO not found or closed
- Invoice amount exceeds PO tolerance
- Duplicate invoice number
- Missing required tax fields
- Currency mismatch
- Quantity exceeds PO (tolerance-dependent)

For buyer-side validation rules: `references/buyer-administration.md` §3.

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
- Access via: https://help.sap.com/docs/ARIBA_NETWORK_SUPPLIERS/39ee7a0f1f8547118dae8a344c54cfcb
- Features: status search by invoice number/date range, rejection reason visibility, download invoice details

## 7. Credit Memos and Debit Memos

**Credit Memo:** Reduces a previously invoiced amount. Must reference original invoice number. Navigation: Invoices → Credit Memo → select original. Uses: returns, overbilling correction, pricing adjustments.

**Debit Memo:** Increases a previously invoiced amount. References original invoice. Uses: price adjustments, additional charges.

**Line-Level Credit:** Credits a specific line item. Used when only partial correction is needed.

## 8. Multi-Tax and Multi-Currency
- Multiple tax lines supported per invoice
- APJ tax considerations: Japan consumption tax (JCT), Australia GST, India GST, Singapore GST
- Foreign currency invoices: invoice in transaction currency; SBN converts for reporting
- Tax ID requirements: configure in Supplier Tax Invoice Configuration

## 9. Routing and Transmission
Invoices route per buyer's document routing rules: cXML to buyer ERP, EDI via Managed Gateway, email PDF, or buyer portal review.

Document routing config: `references/account-management.md` §6.

## 10. Builder Playbook
- Invoice types: §1 table
- PO flip walkthrough: §2
- Generate InvoiceDetailRequest cXML: §2 + DTD reference
- Troubleshoot rejection: §4 common reasons + §5 status meanings
- Credit/debit memo: §7
- Tax guidance: §8 + region context
- EDIFACT INVOIC: edifact-d96a.md §3