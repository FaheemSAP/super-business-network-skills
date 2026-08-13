# EDIFACT D96A — Reference

SAP Business Network EDIFACT D96A message specifications for procurement, supply chain, and logistics.

**Download latest spec PDFs:** `node --input-type=module < scripts/download-edifact-d96a.js` → saves to `~/Downloads/SBN/`

## 1. Overview

EDIFACT D96A is the revision used by SAP Business Network for structured EDI document exchange. SBN supports 12 D96A message types across three domains. All are configured via Managed Gateway (SAP Integration Suite).

## 2. Message Directory

| Message | Direction | Domain | Purpose | cXML Equivalent |
|---|---|---|---|---|
| ORDERS D96A | Outbound (Buyer→Supplier) | Procurement | Purchase Order | OrderRequest |
| ORDCHG D96A | Outbound (Buyer→Supplier) | Procurement | PO Change | OrderRequest (update) |
| ORDRSP D96A | Inbound (Supplier→Buyer) | Procurement | Order Response / OC | ConfirmationRequest |
| DESADV D96A | Inbound (Supplier→Buyer) | Procurement/SCC | Despatch Advice / ASN | ShipNoticeRequest |
| RECADV D96A | Outbound (Buyer→Supplier) | Procurement | Receiving Advice / GRN | ReceiptRequest |
| INVOIC D96A | Inbound (Supplier→Buyer) | Procurement | Invoice | InvoiceDetailRequest |
| REMADV D96A | Outbound (Buyer→Supplier) | Procurement | Remittance Advice | PaymentRemittanceRequest |
| DELFOR D96A (Order) | Outbound (Buyer→Supplier) | Supply Chain | Delivery Forecast (order-based) | ForecastRequest |
| DELFOR D96A (ProductActivity) | Outbound (Buyer→Supplier) | Supply Chain | Delivery Forecast (VMI/replenishment) | ForecastRequest |
| DELJIT D96A | Outbound (Buyer→Supplier) | Supply Chain | JIT Delivery Schedule | ForecastRequest (JIT) |
| IFTMIN D96A | Outbound (Buyer→Carrier) | Logistics | Freight Order / Transport Instructions | TransportRequest |
| IFTSTA D96A | Inbound (Carrier→Buyer) | Logistics | Transport Status / GTT Milestones | TransportStatusNotification |

**Direction:** Outbound = SBN sends to trading partner. Inbound = SBN receives from trading partner.

## 3. Procurement Messages

### ORDERS D96A — Purchase Order (Outbound)
New PO from buyer to supplier. Contains: PO number, date, buyer/supplier IDs, line items (material, quantity, UoM, price, delivery date, ship-to, tax), payment terms.
- SBN equivalent: OrderRequest
- Spec: https://help.sap.com/doc/sap-business-network-edifact-orders-d96a-outbound/cloud/en-US/SAP_EDIFACT%20ORDERS_D96A%20Out.pdf

### ORDCHG D96A — Purchase Order Change (Outbound)
Changes to an existing PO (quantity, date, price, line additions/deletions). References original ORDERS.
- SBN equivalent: OrderRequest with `type="update"`
- Spec: https://help.sap.com/doc/sap-business-network-edifact-ordchg-d96a-outbound/cloud/en-US/SAP_EDIFACT%20ORDCHG_D96A%20Out.pdf

### ORDRSP D96A — Order Response (Inbound)
Supplier acknowledgement: accept, accept with changes, or reject at header or line level.
- SBN equivalent: ConfirmationRequest
- Spec: https://help.sap.com/doc/sap-business-network-edifact-ordrsp-d96a-inbound/cloud/en-US/SAP%20Business%20Network%20EDIFACT%20ORDRSP%20D96A%20Inbound.pdf

### DESADV D96A — Despatch Advice / ASN (Inbound)
Supplier notifies buyer of shipment. Contains: shipment ID, carrier, tracking, line items, quantities, packaging. Key for SCC scheduling agreement fulfillment.
- SBN equivalent: ShipNoticeRequest
- Spec: https://help.sap.com/doc/sap-business-network-edifact-desadv-d96a-inbound/cloud/en-US/SAP%20Business%20Network%20EDIFACT%20DESADV%20D96A%20Inbound.pdf

### RECADV D96A — Receiving Advice / GRN (Outbound)
Buyer confirms goods receipt. Triggers 3-way match (PO + ASN + GRN).
- SBN equivalent: ReceiptRequest
- Spec: https://help.sap.com/doc/sap-business-network-edifact-recadv-d96a-outbound/cloud/en-US/SAP%20Business%20Network%20EDIFACT%20RECADV%20D96A%20Outbound.pdf

### INVOIC D96A — Invoice (Inbound)
Supplier invoice for goods/services. References PO and ASN for 3-way match.
- SBN equivalent: InvoiceDetailRequest
- Spec: https://help.sap.com/doc/sap-business-network-edifact-invoic-d96a-inbound/cloud/en-US/SAP%20Business%20Network%20EDIFACT%20INVOIC%20D96A%20Inbound.pdf

### REMADV D96A — Remittance Advice (Outbound)
Buyer notifies supplier of payment details. Closes the P2P cycle.
- SBN equivalent: PaymentRemittanceRequest
- Spec: https://help.sap.com/doc/sap-business-network-edifact-remadv-d96a-outbound/cloud/en-US/SAP%20Business%20Network%20EDIFACT%20REMADV%20D96A%20Outbound.pdf

## 4. Supply Chain Messages

### DELFOR D96A — Delivery Forecast, Order-based (Outbound)
Forward delivery schedule based on POs. Supplier uses for production and shipping planning.
- Use case: Standard procurement with scheduling agreements
- Spec: https://help.sap.com/doc/sap-business-network-edifact-delfor-order-based-d96a-outbound/cloud/en-US/SAP%20Business%20Network%20EDIFACT%20DELFOR%20Order%20based%20D96A%20Outbound.pdf

### DELFOR D96A — Delivery Forecast, ProductActivity-based (Outbound)
Delivery schedule based on product consumption/activity (not PO lines). Used in VMI and replenishment.
- Use case: VMI, consignment, replenishment collaboration
- Spec: https://help.sap.com/doc/sap-business-network-edifact-delfor-productactivity-based-d96a-outbound/cloud/en-US/SAP%20Business%20Network%20EDIFACT%20DELFOR%20ProductActivity%20based%20D96A%20Outbound.pdf

### DELJIT D96A — Delivery Just-In-Time Schedule (Outbound)
Short-horizon, high-frequency delivery schedule for JIT manufacturing. More granular than DELFOR.
- Use case: JIT/JIS manufacturing (automotive, high-velocity)
- Spec: https://help.sap.com/doc/sap-business-network-edifact-deljit-d96a-order-based-outbound/cloud/en-US/SAP%20Business%20Network%20EDIFACT%20DELJIT%20D96A%20Order%20based%20Outbound.pdf

## 5. Logistics Messages (BN4L)

### IFTMIN D96A — Freight Order / Transport Instructions (Outbound)
Buyer/shipper sends transport instructions to carrier. Triggers freight collaboration in BN4L.
- Use case: BN4L freight tendering and execution
- Spec: https://help.sap.com/doc/sap-business-network-edifact-iftmin-d96a-outbound/cloud/en-US/SAP%20Business%20Network%20EDIFACT%20IFTMIN%20D96A%20Outbound.pdf

### IFTSTA D96A — International Transport Status (Inbound)
Carrier sends shipment status milestones. Feeds into BN4L GTT for real-time tracking.
- Use case: GTT milestone updates, track & trace
- Spec: https://help.sap.com/doc/sap-business-network-edifact-iftsta-d96a-inbound/cloud/en-US/SAP%20Business%20Network%20EDIFACT%20IFTSTA%20D96A%20Inbound.pdf

## 6. End-to-End Document Flow

```
Procurement:
Buyer → ORDERS → Supplier
Buyer → ORDCHG → Supplier  (if PO changes)
Supplier → ORDRSP → Buyer
Supplier → DESADV → Buyer  (at shipment)
Buyer → RECADV → Supplier  (on goods receipt)
Supplier → INVOIC → Buyer
Buyer → REMADV → Supplier  (on payment)

Supply Chain:
Buyer → DELFOR (order-based) → Supplier
Buyer → DELFOR (product-activity) → Supplier  (VMI)
Buyer → DELJIT → Supplier  (JIT)

Logistics (BN4L):
Buyer/Shipper → IFTMIN → Carrier
Carrier → IFTSTA → Buyer
```

## 7. Integration Setup
All D96A messages via Managed Gateway (SAP Integration Suite):
1. Enable EDIFACT channel in Integration Project
2. Set D96A version in channel parameters
3. Map SBN document fields ↔ EDIFACT segments
4. Test with Test Central using corresponding document type

Cross-reference: `references/integration-hub.md` §5 (Managed Gateway), §6 (Test Central).

## 8. Refreshing Specs
```bash
node --input-type=module < scripts/download-edifact-d96a.js
```
Downloads latest PDFs to `~/Downloads/SBN/`. Skips files that already exist.

## 9. Builder Playbook
- Identify message: §2 table (direction, domain, cXML equivalent)
- Explain message detail: §3 (procurement), §4 (supply chain), §5 (logistics)
- Document flow: §6
- Integration config: §7 + integration-hub.md §5
- Download latest specs: §8