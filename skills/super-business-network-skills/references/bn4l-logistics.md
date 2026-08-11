# BN4L — Business Network for Logistics Reference

Collaborative logistics network for shippers, carriers, and logistics partners.

## 1. Core Capabilities

### Freight Collaboration
Digital tendering (RFQ), freight order confirmation, subcontracting, settlement, invoice/dispute handling, document exchange (POD, CMR, BOL). Multi-modal: road, ocean, air, rail.

### Global Track and Trace (GTT)
Real-time milestone/event tracking, exception management, geolocation/ETA visibility, shipment monitoring, API/EDI event capture.

### Dock Appointment Scheduling
Self-service booking, reschedule/cancel, gate/yard coordination, slot management, utilization visibility.

### Material Traceability
Batch/product lineage, end-to-end traceability, compliance/recall support.

### Intelligent Insights
Custom reporting, shipment dashboards, carrier performance analytics, risk monitoring, real-time alerts.

## 2. SAP Integration
| System | Integration |
|---|---|
| SAP TM | Freight orders, bookings, settlement |
| S/4HANA (embedded TM) | Direct freight collaboration |
| SAP EWM | Dock scheduling |
| Non-SAP | REST APIs |

## 3. Freight Order Lifecycle
1. Planned in SAP TM/S4 → 2. Tendered via BN4L → 3. Carrier confirms → 4. Executed → 5. GTT milestones → 6. Settlement → 7. Invoice/dispute

## 4. Platform (2025)
Neo sunset July 18, 2025. New platform: auto credential provisioning, SFTP schedulers, enhanced monitoring, auto-reprocessing.

## 5. APIs
Shipper↔BN4L: SOAP. BN4L↔Carrier: REST. GTT/FC APIs on api.sap.com. OAuth 2.0 (client credentials).

## 6. Builder playbooks
- Explain capability: §1 detail
- Plan freight collaboration: §3 lifecycle
- Configure GTT: milestone types, event sources, APIs
- Plan integration: source system (§2), API type (§5), auth, migration (§4)
- Freight order template: key fields for carrier collaboration