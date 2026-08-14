# Supply Chain Collaboration — Reference

SAP Business Network for Supply Chain extends SBN with collaboration for suppliers and buyers.

**Official SAP Sources (v2605):**
- [SAP Business Network for Supply Chain Integration and Configuration Guide](https://help.sap.com/docs/ARIBA_NETWORK/5a679004dd4148fb8995a57e3cfcaaf2?locale=en-US&state=PRODUCTION&version=2605)
- [Supplier Guide to SAP Business Network for Supply Chain](https://help.sap.com/docs/ARIBA_NETWORK_SUPPLIERS/f0dac91c138b407c8e90c6c6a43eec83?locale=en-US&state=PRODUCTION&version=2605)

## 1. Collaboration Types

### Forecast Collaboration
Buyers share demand forecasts; suppliers view and commit to deliveries. Integrates with SAP IBP. Supports product activity and replenishment messages.

### Procurement Collaboration
Digital PO exchange (create/change/cancel). Suppliers confirm/change/reject in real-time. Scheduling agreements and delivery schedules.

### Inventory Collaboration
Shared inventory visibility. Consigned inventory, replenishment signals, VMI workflows, rolling delivery schedules.

### Quality Collaboration
Quality issues, inspection results, non-conformance reports, corrective actions, quality certificates.

### Manufacturing Collaboration
Contract manufacturing visibility, production status, component availability, WIP tracking.

### Shipping/Logistics Collaboration
ASN, packaging data, delivery confirmation, proof of delivery. Integration with BN4L.

## 2. Planning Collaboration
Full supply visibility across planning horizon. Digital forecast/demand sharing. Demand-supply mismatch resolution. Real-time via SAP IBP integration.

## 3. Business Rules
Buyer-configured rules enforce: document format, required fields, value constraints, auto-rejection, supplier notification.

## 4. Supplier Enablement
1. Supplier Enablement → Active Relationships
2. Select supplier (Classic View)
3. Enable SBN for Supply Chain
4. Configure doc types and features
5. Supplier notified, begins collaborating

## 5. Integration Points
SAP S/4HANA (direct APIs), SAP IBP (planning), SAP Ariba (procurement), SAP TM (logistics), Non-SAP (APIs/middleware).

## 6. Builder playbooks
- Explain collaboration: §1 with data flows
- Enable supplier: §4 step-by-step
- Plan forecast: §2 + IBP integration
- Configure rules: §3 enforcement
- Enablement checklist: prerequisites as actionable list

## 7. Advanced Ship Notice (ASN) — SCC Context

ASN is a critical touchpoint between supply chain collaboration and order fulfillment.

### ASN in Scheduling Agreement Scenarios
- Buyer sends DELFOR (delivery forecast) or DELJIT (JIT schedule)
- Supplier ships and sends ASN (DESADV D96A or ShipNoticeRequest) referencing the schedule line
- ASN must include: delivery schedule reference, quantities, batch/serial numbers if mandated, packaging data

### SCC ASN Key Fields
| Field | Requirement |
|---|---|
| Scheduling Agreement number | Required for schedule-based ASN |
| Delivery Schedule line reference | Required |
| Shipped quantity | Required |
| Batch number | Required if batch-managed material |
| Serial numbers | Required if serial-managed |
| Incoterms | Buyer-configured |

### ASN Validation in SCC
Common buyer-configured rules: quantity cannot exceed scheduled quantity by >X%; ASN required before invoice; packaging data required.

Full ASN field list and cXML structure: `references/order-management.md` §5.
DESADV D96A message detail: `references/edifact-d96a.md` §3.