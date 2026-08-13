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

### cXML: ConfirmationRequest
Key elements: `<ConfirmationRequest>`, `<ConfirmationHeader>` (type: accept/accept_changes/reject), `<ConfirmationItem>` with confirmQuantity.

### EDIFACT: ORDRSP D96A
See `references/edifact-d96a.md` §3.

### Response Types
| Type | Meaning |
|---|---|
| accept | Supplier confirms as-is |
| accept_changes | Supplier proposes changes (qty, date, price) |
| reject | Supplier rejects PO with reason code |

## 5. Advanced Ship Notice (ASN)

### Purpose
Supplier notifies buyer of an imminent or in-progress shipment. Enables 3-way match preparation.

### Key ASN Fields
- ASN / shipment ID
- PO reference(s)
- Ship date and carrier
- Tracking number
- Estimated delivery date
- Ship-from address
- Line items: material, shipped quantity, batch/serial numbers (if required)
- Packaging information (if required)

### cXML: ShipNoticeRequest
Elements: `<ShipNoticeRequest>`, `<ShipNoticeHeader>` (shipmentID, shipmentDate, carrier), `<ShipNoticePortion>` (per PO), `<ShipNoticeItem>` (per line).

### EDIFACT: DESADV D96A
See `references/edifact-d96a.md` §3.

### Portal: Create ASN (PO Flip)
Navigate to PO → Create Ship Notice → fill shipment details → submit.

## 6. Goods Receipt (GRN)

Buyer confirms physical receipt. Enables 3-way match (PO + ASN + GRN).
- cXML: Buyer sends `<ReceiptRequest>` to SBN; supplier can view in Fulfillment section
- EDIFACT: RECADV D96A — see `references/edifact-d96a.md` §3

## 7. Service Sheets (Service POs)

For service-based POs, the service sheet replaces the ASN as the fulfillment confirmation. Supplier records services rendered; buyer approves.

**Service Sheet Fields:** Service PO reference, service period (start/end dates), line items (service description, quantity, unit, price), attachments (timesheet, sign-off documents).

**Workflow:** Service PO received → Supplier creates Service Sheet → Buyer reviews/approves → Supplier creates Service Invoice.

## 8. Change Orders and Cancellations

**Change Order:** Buyer sends revised PO (cXML `OrderRequest type="update"` or EDIFACT ORDCHG D96A). Supplier should confirm or reject via OC.

**Cancellation:** Buyer sends PO cancellation (cXML `OrderRequest type="delete"`). Supplier acknowledges.

Handling tips: Compare orderVersion to detect change vs. original; check if corresponding ASN or invoice exists before accepting cancellation.

## 9. Scheduling Agreements / Delivery Schedules
Buyers with scheduling agreements send DELFOR/DELJIT messages. See `references/edifact-d96a.md` §4 and `references/supply-chain-collaboration.md` §2.

## 10. Builder Playbook
- P2P flow: §2 diagram
- Order types: §1 table
- Generate OC cXML: §4 ConfirmationRequest structure
- Generate ASN cXML: §5 ShipNoticeRequest structure
- Service sheets: §7
- Handle change/cancel: §8
- EDIFACT messages: edifact-d96a.md