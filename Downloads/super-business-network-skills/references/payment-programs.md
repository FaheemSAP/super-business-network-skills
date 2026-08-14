# Payment & Early Payment Programs — Reference

Dynamic discounting, supply chain finance, virtual cards, and payment methods on SAP Business Network.

**Official SAP Sources:**
- [Discount Offers Defined](https://help.sap.com/docs/business-network-for-procurement/payments-and-discounting-buyer/discount-offers-defined)
- [SAP Taulia Dynamic Discounting](https://taulia.com/platform/payables/dynamic-discounting/)
- [SBN Procurement — DD + SCF + Virtual Cards](https://www.sap.com/products/business-network/procurement.html)

## 1. Dynamic Discounting

**Definition:** Buyer-funded early payment model (no third party). Buyer uses surplus cash to pay early; supplier grants a sliding-scale discount in return.

### Program Types
| Type | Description |
|---|---|
| **SEPTO** (Standing Early Payment Term Offer) | Auto-applied to all qualifying invoices; supplier accepts once |
| **Buyer-Initiated Ad Hoc** | Buyer selects specific invoices; sends offer to supplier |
| **Supplier-Initiated** | Supplier requests early payment on specific invoices (where buyer enables) |

### Discount Calculation Models
| Model | Formula |
|---|---|
| **APR Sliding Scale** | `Discount = Amount × (APR/365) × Days Early` — most common |
| **Face Value Sliding Scale** | Fixed rate if within discount term; prorated between discount term and net term |
| **Net Term** | No discount |

### Auto-Acceptance Rules
Buyers/suppliers can configure auto-acceptance rules by:
- Amount range (min/max invoice value)
- APR range (acceptable discount rate)
- Status becomes "Supplier Accepted" when auto-accepted

### VAT/GST Considerations (APJ)
In VAT/GST regions (AU, NZ, SG, JP, IN): a dynamic discounting **credit memo** is auto-generated to adjust the tax on the discount amount.

## 2. Supply Chain Finance (SCF)

**Definition:** Third-party-funded model. A funder (bank) pays the supplier early against approved invoices; buyer repays the funder on the original due date.

**Benefits:**
- Supplier gets early payment without buyer cash outlay
- Buyer preserves or extends DPO (Days Payable Outstanding)
- Funder earns a return on advance

**Delivered via:** SAP Taulia integrated with SAP Business Network.

### SCF Flow
1. Supplier submits invoice → buyer approves
2. Approved invoice eligible for early payment
3. Funder (bank) advances payment to supplier minus a small discount
4. Buyer repays funder on original maturity date

### Supplier Enrollment
- Buyer or SAP sends email invitation to supplier
- Supplier completes Taulia onboarding (~90 seconds)
- Supplier selects invoices for early payment or sets auto-acceptance

### Key Point
Same approved invoices can serve DD, SCF, or Virtual Cards simultaneously — the programs are complementary.

## 3. Early Payment — Supplier Request Paths

| Path | Flow |
|---|---|
| A — Accept SEPTO | Supplier accepts standing offer once; all qualifying invoices auto-enrolled |
| B — Respond to ad hoc | Inbox → Early Payments → review offer → accept/reject |
| C — Supplier-initiate | Where buyer enables: supplier selects invoices and requests early payment |
| D — Taulia SCF self-service | Supplier logs into Taulia → selects invoices → confirms early payment |

## 4. Virtual Card Payments

**Definition:** Buyer pays supplier using a single-use virtual card number instead of traditional bank transfer.

### 8-Step Process
1. Buyer registers funding card (corporate credit card)
2. Supplier activates virtual card acceptance in SBN
3. Supplier submits invoice → buyer approves
4. Taulia auto-issues single-use virtual card number
5. Supplier charges card for approved amount
6. Card network processes payment
7. Bank settles to supplier
8. GL auto-reconciled

### APJ Virtual Card Partners (2026)
- **Paymate** and **ipaymy** — APAC-specific providers for automated settlement
- Added March 2026 for supplier-side card acceptance

## 5. Payment Methods on SBN

### Supplier Receives Payment Via
| Method | Notes |
|---|---|
| ACH (CTX/CCD+/CCD) | US standard |
| Wire Transfer | International |
| Check | Legacy |
| Credit Card / P-Card | Buyer pays directly |
| Virtual Card (Taulia) | Single-use number |
| AribaPay | SBN-native payment rail |

### Supplier Pays SBN Fees Via
| Method | Notes |
|---|---|
| Credit Card (Visa/MC/Amex) | Most common |
| Direct Debit | Regional |
| EFT/Wire | Bank transfer |
| Check | Legacy |

JPY credit card threshold: ¥1,540 minimum.

## 6. APJ-Specific Considerations

### Japan
- **Subcontract Act** caps payment terms at 60 days for qualifying SME transactions (14.6% p.a. late penalty)
- Japan uses **fixed billing cycle dates** (not invoice-date net), affecting early payment scheduling
- Revised in 2024 with stricter enforcement

### Australia / New Zealand / Singapore
- VAT/GST credit memo required if early payment discount applied post-invoice
- Peppol e-invoicing compatibility for payment references

### General APJ
- Taulia SCF funder availability varies by country (not publicly documented per-country)
- Virtual card acceptance growing via Paymate/ipaymy partnerships

## 7. SAP Early Payment Program (for SAP's own suppliers)
SAP runs its own early payment program via Taulia at a "favorable discount rate" for SAP suppliers.
- Access: https://www.sap.com/about/agreements/sap-supplier-portal/taulia-early-payments.html

## 8. Builder Playbooks
- Dynamic discounting overview: §1
- SCF explanation: §2
- Supplier early payment paths: §3
- Virtual card setup: §4
- Payment methods: §5
- APJ regulatory considerations: §6
- Discount calculation: §1 (models table)
