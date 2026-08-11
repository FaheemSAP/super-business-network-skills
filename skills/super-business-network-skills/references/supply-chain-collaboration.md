# Supply Chain Collaboration — Reference

SAP Business Network for Supply Chain extends SBN with collaboration for suppliers and buyers.

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