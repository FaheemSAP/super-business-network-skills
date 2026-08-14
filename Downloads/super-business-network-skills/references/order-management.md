# Order Management & Fulfillment — Reference

Receiving, confirming, and fulfilling purchase orders on SAP Business Network.

**Official SAP Source (v2605):**
- [Receiving and Fulfilling Orders](https://help.sap.com/docs/ARIBA_NETWORK_SUPPLIERS/45abc7c531754929a19c6a844bd5d6ec?locale=en-US&state=PRODUCTION&version=2605)

## 1. Order Types

| Type | Description |
|---|---|
| Standard PO | Fixed quantity and price; one-time purchase |
| Blanket PO | Framework agreement with cumulative value/quantity over a period |
| Release PO | Drawn against a blanket PO |
| Service PO | For services; requires service entry sheet confirmation |
| Scheduling Agreement | Long-term procurement with delivery schedules |
| Sub-contract PO | Includes components supplied to a manufacturing partner |
| Stock Transport | Internal transfer order (plant-to-plant) |

## 2. P2P Document Flow

```
Buyer Creates PO → SBN Routes → Supplier Receives
        ↓
Supplier Sends Order Confirmation (OC)
        ↓
Supplier Ships → Advanced Ship Notice (ASN)
        ↓
Buyer Receives Goods → Goods Receipt Notification (GRN)
        ↓
Supplier Creates Invoice → Buyer Approves → Payment
```

## 3. Order Receipt
- Suppliers receive POs in SBN Inbox or via integration (cXML/EDI)
- Notification: email alert to configured contact
- PO details: header (buyer, supplier, currency, delivery address) + line items (material, qty, UoM, price, delivery date)
- Flip actions available from PO: Create OC, Create ASN, Create Invoice

## 4. Order Confirmation (OC)

### Purpose
Supplier acknowledges receipt and intent to fulfil. May confirm, partially confirm, or propose changes.

### Partial Confirmation
At line-item level, three fields split the PO quantity:
| Field | Meaning |
|---|---|
| **Confirm** | Quantity accepted as ordered |
| **Backorder** | Quantity not yet available, to be shipped later |
| **Reject** | Quantity being declined |

The three must sum to the original PO line quantity. Supplier can confirm some lines fully, partially confirm others, and reject lines — all in a single OC.

> **Prerequisite:** Buyer must enable line-item level OC. If not enabled, only full-order accept/reject is permitted.

### cXML: ConfirmationRequest
Key elements: `<ConfirmationRequest>`, `<ConfirmationHeader>` (type: accept/accept_changes/reject/detail), `<ConfirmationItem>` with `<ConfirmationStatus>` per disposition.

**Partial accept + backorder example (10 ordered, 6 accepted, 4 backordered):**
```xml
<ConfirmationItem lineNumber="1" quantity="10">
  <UnitOfMeasure>EA</UnitOfMeasure>
  <ConfirmationStatus type="accept" quantity="6">
    <UnitOfMeasure>EA</UnitOfMeasure>
  </ConfirmationStatus>
  <ConfirmationStatus type="backordered" quantity="4">
    <UnitOfMeasure>EA</UnitOfMeasure>
  </ConfirmationStatus>
</ConfirmationItem>
```

### Confirmation Variance / Deviation Approval
If OC quantity/date/price is outside buyer-configured tolerance, buyer can enable approval routing. Reviewed in **Manage Confirmation Variances** app.

### EDIFACT: ORDRSP D96A
See `references/edifact-d96a.md` §3.

### Response Types
| Type | Meaning |
|---|---|
| accept | Supplier confirms as-is |
| accept_changes | Supplier proposes changes (qty, date, price) |
| reject | Supplier rejects PO with reason code |
| detail | Mixed — line-level dispositions |
| backordered | Item(s) on back-order with expected date |

## 5. Advanced Ship Notice (ASN)

### Purpose
Supplier notifies buyer of an imminent or in-progress shipment. Enables 3-way match preparation.

### Key ASN Fields
- ASN / shipment ID (unique per ASN)
- PO reference(s)
- Ship date and carrier
- Tracking number
- Estimated delivery date
- Ship-from address
- Line items: material, shipped quantity, batch/serial numbers (if required)
- Packaging information (if required)

### Partial ASN / Split Shipments
SBN fully supports **multiple ASNs against a single PO line** (split shipments). Use: Workbench → Items to Ship tab → select desired lines/quantities for each shipment.

| PO Status | Meaning |
|---|---|
| New / Confirmed | No ASN yet |
| Shipping | At least one ASN but not all quantities shipped |
| Shipped | All quantities covered by ASNs |

**Line splitting within one ASN:** Use the Split action to assign different delivery dates to portions of the same line.

**Quantity tracking:** SBN tracks running totals across all ASNs per PO line. Purchase Order Tracking Page shows cumulative shipped vs. ordered.

### cXML: ShipNoticeRequest
Elements: `<ShipNoticeRequest>`, `<ShipNoticeHeader>` (shipmentID, shipmentDate, carrier), `<ShipNoticePortion>` (per PO), `<ShipNoticeItem>` (per line).

### EDIFACT: DESADV D96A
See `references/edifact-d96a.md` §3.

### Portal: Create ASN (PO Flip)
Navigate to PO → Create Ship Notice → fill shipment details → submit.

## 6. Overdelivery / Underdelivery & Tolerance

### System Defaults
| Direction | Default |
|---|---|
| Underdelivery | Permitted |
| Overdelivery | Blocked (system rejects) |

### Tolerance Hierarchy (evaluated in order)
1. Supplier-specific transaction rules
2. Default transaction rules (buyer account-wide)
3. Confirmation control keys (from ERP via PO)
4. PO item-level tolerance (SAP MM purchasing value key)
5. System default

### Buyer Configuration
Path: Administration → Configuration → Default Transaction Rules → Order Confirmation and Ship Notice Rules.
- Set delivery-date tolerance (days early/late)
- Set quantity tolerance (% over/under)
- Blank = no check; 0 = zero deviation
- Route out-of-tolerance confirmations to buyer approval

## 7. 3-Way Matching (PO + ASN + GRN)

```
PO (What was ordered) → ASN (What was dispatched) → GRN (What was received) → Invoice (What was billed)
```

Invoice blocking: if variance exceeds tolerance, invoice posted but blocked for payment pending review. GR-Based IV flag on PO item is the key switch for enforcing 3-way match.

## 8. Goods Receipt (GRN)

Buyer confirms physical receipt. Enables 3-way match (PO + ASN + GRN).
- cXML: Buyer sends `<ReceiptRequest>` to SBN; supplier can view in Fulfillment section
- EDIFACT: RECADV D96A — see `references/edifact-d96a.md` §3

## 9. Service Sheets (Service POs)

For service-based POs, the service sheet replaces the ASN as the fulfillment confirmation. Supplier records services rendered; buyer approves.

**Service Sheet Fields:** Service PO reference, service period (start/end dates), line items (service description, quantity, unit, price), attachments (timesheet, sign-off documents).

**Workflow:** Service PO received → Supplier creates Service Sheet → Buyer reviews/approves → Supplier creates Service Invoice.

## 10. Change Orders and Cancellations

**Change Order:** Buyer sends revised PO (cXML `OrderRequest type="update"` or EDIFACT ORDCHG D96A). Supplier should confirm or reject via OC.

**Cancellation:** Buyer sends PO cancellation (cXML `OrderRequest type="delete"`). Supplier acknowledges.

Handling tips: Compare orderVersion to detect change vs. original; check if corresponding ASN or invoice exists before accepting cancellation.

## 11. Returns Collaboration

### Document Types
| Document | Created By | Purpose |
|---|---|---|
| Return Purchase Order | Buyer | PO with line items flagged as "Return Item" |
| Return Ship Notice | Buyer | Advance notification of inbound return shipment |
| Credit Memo for Return Items | Supplier | Reimburse buyer for returned goods |

### End-to-End Returns Flow
```
Buyer requests RMA (external to SBN)
→ Supplier authorizes
→ Buyer creates Return PO on SBN (Return Item checkbox + RMA#)
→ Buyer creates Return Ship Notice
→ Buyer ships goods to supplier
→ Supplier receives and creates Credit Memo for Return Items
→ Credit memo processed in buyer ERP
```

Line-item credit memos are **required** for returns (not header-level).

### S/4HANA Integration
- Return PO doc type: NB2
- Goods movement type: 161 (Returns for PO)
- Delivery type (EWM): RL (Return Logistics)

## 12. Scheduling Agreements / Delivery Schedules
Buyers with scheduling agreements send DELFOR/DELJIT messages. See `references/edifact-d96a.md` §4 and `references/supply-chain-collaboration.md` §2.

## 13. Builder Playbook
- P2P flow: §2 diagram
- Order types: §1 table
- Generate OC cXML: §4 (partial confirmation example)
- Generate ASN cXML: §5 ShipNoticeRequest structure
- Partial fulfillment: §4 (OC) + §5 (ASN split shipments)
- Overdelivery/tolerance: §6 hierarchy + §7 3-way match
- Service sheets: §9
- Handle change/cancel: §10
- Returns: §11 (document types + flow)
- EDIFACT messages: edifact-d96a.md
