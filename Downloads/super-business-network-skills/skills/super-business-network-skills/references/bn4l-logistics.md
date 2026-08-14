# BN4L — Business Network for Logistics Reference

Collaborative logistics network for shippers, carriers, and logistics partners.

**Official SAP Sources:**
- [BN4L Freight Collaboration Help](https://help.sap.com/docs/business-network-freight-collaboration/application-help)
- [BN4L GTT FAQ](https://help.sap.com/doc/39e69a233624475580083b6ba2e803cb/LBN/en-US/SAP_LBN_GTT_FAQs.pdf)
- [BN4L Administration Guide](https://help.sap.com/doc/299aab2200034b8888212335f89bf4bf/LBN/en-US/13d98c2aedb344d9a59c6e624ace358f_EN.pdf)

## 1. Core Capabilities

### Freight Collaboration
Digital tendering (RFQ), freight order confirmation, subcontracting, settlement, invoice/dispute handling, document exchange (POD, CMR, BOL). Multi-modal: road, ocean, air, rail.

### Global Track and Trace (GTT)
Real-time milestone/event tracking, exception management, geolocation/ETA visibility, shipment monitoring, API/EDI event capture.

### Dock Appointment Scheduling (DAS)
Self-service booking, reschedule/cancel, gate/yard coordination, slot management, utilization visibility, guest user booking.

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

## 4. GTT Event Codes (Standard)

The GTT Standard Model (`gttft1`) defines the following event types:

### Planned Events
| Code | Description |
|---|---|
| `DEPARTURE` | Departure |
| `ARRIV_DEST` | Arrival at destination |
| `LOAD_BEGIN` | Loading start |
| `LOAD_END` | Loading end |
| `UNLOAD_BEGIN` | Unloading start |
| `UNLOAD_END` | Unloading end |
| `COUPLING` | Trailer attach |
| `DECOUPLING` | Trailer detach |
| `POPU` | Proof of Pick-Up |
| `POD` | Proof of Delivery |

### Unplanned Events
| Code | Description |
|---|---|
| `DELAYED` | Delay |
| `FLIGHT_BOOKED` | Flight booked |
| `MANIFEST_READY` | Manifest ready |
| `RCVD_FROM_SHIPPER` | Received from shipper |
| `CONSIGNEE_NOTIFIED` | Consignee notified |
| `GATEIN_START` | Gate-in start |
| `GATEIN_END` | Gate-in end |
| `GATEOUT_START` | Gate-out start |
| `GATEOUT_END` | Gate-out end |
| `DELIVERED` | Delivered |
| `RETURN` | Return |
| `EST_UPDATE` | Estimated time update |
| `OUT_FOR_DELIVERY` | Out for delivery |
| `EMISSION` | Emission reporting |
| `GEOLOC` | Geolocation update |
| `RECEIVE` | Received |
| `STUFF` | Container stuffing |
| `UNSTUFF` | Container unstuffing |
| `OTHER` | Other (catch-all) |
| `EXCEPTION` | Exception |
| `TRACKING_END` | Tracking end |
| `CHECK_IN` | Check-in (added 2603) |
| `SUB_VEHICLE_READY` | Subsequent vehicle ready (added 2603) |
| `GATEIN_HOLD` | Gate check-in on hold (added 2603) |

Source: [Event Code Descriptions — SAP Help Portal](https://help.sap.com/docs/business-network-freight-collaboration/code-lists/event-code-descriptions)

> Note: `CUSTOMS_CLEARED` is NOT a standard event code — implement as a custom event via Manage Models app.

### Event Reason Codes
| Code | Description |
|---|---|
| `LBN_TRAFFC` | Traffic |
| `LBN_BRKDWN` | Breakdown |
| `LBN_WTGLOC` | Waiting at location |
| `LBN_OTHERS` | Others |
| `CANCELLATION` | Cancellation |
| `CLEANING_STATION` | Cleaning station |
| `TRACKING_END` | Tracking end |

Custom reason codes can be added via Manage Model → Code List tab.

### Event Data Fields
Each event carries: `eventTypeCode`, `eventReasonCode`, `referenceEventTypeCode`, location data, actual/planned timestamps, transport mode, carrier ID, vehicle plate, attachments (PDF/image). Boolean `isFinal` marks the last milestone.

## 5. Carrier Onboarding

### Step-by-Step Flow

**Phase 1 — Invitation (Shipper Side)**
1. Shipper admin → **Discover and Invite Carriers** app
2. Search by carrier name; send invitation or connection request
3. Configure **Partner Connections** record in anticipation

**Phase 2 — Carrier Account Activation**
1. Carrier receives email → places free order in SAP Store
2. Activates SAP Store account
3. After ~2 hours, receives BN4L/LBN tenant activation email
4. Logs in with credentials to carrier tenant

**Phase 3 — Accept Connection**
1. Carrier navigates to **Manage Invitations** tile
2. Accepts pending invitation from shipper
3. Network connection established

**Phase 4 — Backend Mapping (Shipper)**
1. Carrier's **LBN ID** visible in System Connections → Manage Alternate IDs
2. Add LBN ID to carrier Business Partner in SAP TM using identification type **LBN001**
3. Assign carrier to relevant Purchasing Organization

**Phase 5 — Technical User Setup (Carrier)**
1. Create Technical User in carrier tenant
2. Assign in System Connections app
3. Configure outbound connection (endpoint URL, auth)

### Connection Types
| Type | Use Case |
|---|---|
| Web Portal (UI) | Manual operations |
| REST/API | Automated backend integration |
| EDI — ANSI X12 | US-format (204, 990, 214, 210) |
| EDI — UN/EDIFACT | International (IFTMIN, IFTSTA, INVOIC) |
| SFTP | File-based EDI transport |

### Partner ID Types
| ID Type | Description |
|---|---|
| LBN ID | Primary BN4L identifier |
| SCAC | Standard Carrier Alpha Code (US) |
| GLN | Global Location Number |
| P44_EU | project44 European partner ID |

Network visibility partners (FourKites, project44, Transporeon) onboard via **sap.dsc.network.enablement@sap.com** or the **Discover Business Partners** tile.

## 6. Dock Appointment Scheduling (DAS)

### End-to-End Process

**Step 1 — Transportation Planning (SAP TM)**
Freight Order created → carrier assigned → preferred time window and duration sent to BN4L DAS.

**Step 2 — Carrier Self-Booking**
1. Carrier → **Self-Book Dock Appointments** tile
2. FO appears in **Ready for Booking** worklist
3. Select FO → **Maintain Appointment**
4. System shows available time slots (by loading point, date, business hours, capacity)
5. Select loading point, date, and time slot(s)
6. If derived duration is set, booked slots must match exactly
7. Save → Status: **Booked**

**Step 3 — Slot Management**
- **Appointment Requests** don't consume capacity; **Booked** appointments do
- **Recurring Block Times** (2511): automatically block specific recurring slots
- Overbooking configurable per loading point

**Step 4 — Gate Check-In**
1. Truck arrives → gate personnel open **Manage Gate Operations** app
2. Click **Start Check-In** → enter Gate ID, Vehicle Plate, Registration Country, Date/Time
3. Validate documents → confirm check-in

**Step 5 — Yard Operations**
Truck moved to dock/parking/scale; yard coordinator tracks all active trucks.

**Step 6 — Gate Check-Out**
Loading/unloading complete → truck checked out → departure status created.

### Guest User (Driver) Self-Booking
1. BN4L sends email with time-limited URL
2. Driver clicks link → enters Reference Document number (FO, Sales Order, Delivery)
3. Selects available slot → books
4. No login required — token-based access

### DAS Configuration Prerequisites
1. Set up location master data (loading points, docks, gates, yards)
2. Define entity settings in **Manage Entities** app
3. Define Gate Settings (Gate ID, business hours)
4. Configure capacity (slots per loading point, duration)
5. Set integration with SAP TM or backend WMS/YMS

## 7. Freight Dispute Management

### Dispute Lifecycle

```
FO In Execution → Charges sent to BN4L
→ Carrier creates/submits invoice [Status: Submitted]
→ System detects mismatch → Dispute created [In Dispute]
→ Shipper reviews in Manage Disputes
    → Accept → Submitted for Confirmation → TM confirms → RESOLVED
    → Reject → Carrier receives reason → can re-submit
    → Counter-proposal → Carrier accepts/rejects → cycle continues
→ Invoice re-submitted after resolution [FO: Completely Invoiced]
```

### Dispute Status Values
| Status | Meaning |
|---|---|
| In Dispute | Parties have not agreed |
| Submitted for Confirmation | Shipper accepted; charges sent to TM |
| Resolved | TM confirmed; case finalized |
| No Dispute | No mismatch |

### Workflow Status
| Status | Meaning |
|---|---|
| Workflow Not Enabled | No approval workflow configured |
| Automatically Approved | Within tolerance; auto-approved |
| Awaiting Approval | In multi-step internal approval queue |
| Completed | Approval workflow finished |

### Auto-Approval (Tolerance)
If difference between TM-calculated charge and carrier invoice is within configured tolerance → auto-approved without dispute creation.

### Multi-Step Internal Approval
1. Level 1 approver reviews dispute
2. If amount exceeds Level 1 threshold → escalated to Level 2+
3. Final approver approves/rejects/edits counter-proposal
4. Mass accept/reject supported from worklist

### Freight Booking Disputes (2511)
Extended to **Freight Bookings** (ocean, air), not just FOs.

## 8. Freight Settlement Process

### Standard Carrier Invoicing Flow
| Step | Actor | Action | Status |
|---|---|---|---|
| 1 | Shipper/TM | FO in execution with charges → sends to BN4L | To Be Invoiced |
| 2 | Carrier | Opens **Invoice Freight Documents** app | — |
| 3 | Carrier | Clicks Create Invoice | Draft / Invoicing in Progress |
| 4 | Carrier | Reviews, adds unplanned charges if needed | — |
| 5 | Carrier | Submits invoice | Submitted / Awaiting Response |
| 6 | System | Checks vs FO charges; passes to TM | — |
| 7 | SAP TM | Receives via InvoiceRequest_In; creates FSD | Completely Invoiced |
| 8 | SAP MM | Verifies FSD (MIRO/MRRL) | Invoice Verified |

### Self-Billing / ERS (Evaluated Receipt Settlement)
1. FO executed and charges confirmed in TM
2. TM creates Freight Settlement Document (FSD)
3. MM runs ERS (MRRL) → creates self-billing invoice
4. FSD lifecycle: In Process → Ready for Accruals → Posted → Invoice Verified

ERS prerequisites: Carrier BP must have Automatic ERS + GR-Based Invoice Verification flags.

## 9. Platform (2025+)
Neo sunset July 18, 2025. New platform features: auto credential provisioning, SFTP schedulers, enhanced monitoring, auto-reprocessing.

## 10. APIs
| Interface | Protocol |
|---|---|
| Shipper↔BN4L | REST |
| BN4L↔Carrier | REST |
| GTT/Freight Collaboration APIs | REST on api.sap.com |
| EDI X12 | 204, 990, 214, 210 |
| EDI EDIFACT | IFTMIN, IFTSTA, INVOIC |
| Auth | OAuth 2.0 (client credentials) |

## 11. EDIFACT D96A — Logistics Messages

| Message | Direction | Purpose |
|---|---|---|
| IFTMIN D96A | Outbound (Shipper→Carrier) | Freight order / transport instructions |
| IFTSTA D96A | Inbound (Carrier→Buyer) | Transport status / GTT milestones |
| DESADV D96A | Inbound (Supplier→Buyer) | Despatch advice feeding shipment tracking |

Full message specs: `references/edifact-d96a.md` §5.
Managed Gateway config: `references/integration-hub.md` §5.

## 12. Builder Playbooks
- Explain capability: §1 detail
- Plan freight collaboration: §3 lifecycle
- Configure GTT: §4 event codes + reason codes
- Carrier onboarding: §5 step-by-step
- Dock appointment scheduling: §6 full workflow
- Freight disputes: §7 lifecycle + status values
- Settlement: §8 invoicing flow
- Plan integration: source system (§2), API type (§10), auth, migration (§9)
