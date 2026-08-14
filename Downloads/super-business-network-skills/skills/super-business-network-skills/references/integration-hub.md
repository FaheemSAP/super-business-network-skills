# Integration Hub — Reference

7-phase lifecycle, document standards, GITP, Managed Gateway, Test Central, Timeline Planner.

## 1. 7-phase lifecycle (10–12 weeks; subsequent 4–6)

| Phase | Duration |
|---|---|
| 1. Registration | 1 week |
| 2. Discovery & Scoping | 1–2 weeks |
| 3. Managed Gateway Config | 1 week |
| 4. Development & Mapping | 3–4 weeks |
| 5. Testing & Validation | 3–4 weeks |
| 6. Go-Live | 1 week |
| 7. Ongoing Support | Ongoing |

Phase 1: Register, DUNS/Tax, Users/Roles, accept TRR, create TEST (-T).
Phase 2: Align doc scope, obtain DTD, assess ERP, designate tech lead, set timeline.
Phase 3: Gateway portal, Integration Project, Cross-References, Channel config, Routing, Test.
Phase 4: Build listener, map to ERP, response codes, outbound cXML, DTD validate, error handling.
Phase 5: Unit/Integration/Scenario/Error testing, GITP, Test Central.
Phase 6: Production creds, controlled go-live, monitor, full volume.
Phase 7: Transaction Manager, alerts, tickets, credential maintenance.

## 2. Document standards

| Document | cXML | X12 | EDIFACT/EANCOM | EDIFACT D96A | PIDX |
|---|---|---|---|---|---|
| Purchase Order | OrderRequest | 850 | ORDERS | ORDERS D96A | OrderCreate |
| PO Change | OrderRequest (update) | 860 | ORDCHG | ORDCHG D96A | OrderChange |
| Order Confirmation | ConfirmationRequest | 855 | ORDRSP | ORDRSP D96A | OrderResponse |
| Advanced Ship Notice | ShipNoticeRequest | 856 | DESADV | DESADV D96A | ShipNotice |
| Invoice | InvoiceDetailRequest | 810 | INVOIC | INVOIC D96A | Invoice |
| Goods Receipt | ReceiptRequest | 861 | RECADV | RECADV D96A | — |
| Remittance Advice | PaymentRemittanceRequest | 820 | REMADV | REMADV D96A | — |
| Delivery Forecast | ForecastRequest | 830 | DELFOR | DELFOR D96A | — |
| JIT Schedule | — | 862 | DELJIT | DELJIT D96A | — |
| Freight Order | — | — | IFTMIN | IFTMIN D96A | — |
| Transport Status | — | — | IFTSTA | IFTSTA D96A | — |

PO/Forecast/Freight: Buyer→Supplier/Carrier. OC/ASN/Invoice/Transport Status: Supplier/Carrier→Buyer.

## 3. Integration models
Portal (<100/yr), CSV (100–500/yr), cXML (>500/yr), EDI (>500/yr). Recommend full at 250–500+.

## 4. GITP (Guided Integration for Trading Partners)

### 5-Step Self-Service Process
| Step | Name | Activity |
|---|---|---|
| 1 | Enter GITP | Integration tab or Workbench → Integration Overview widget |
| 2 | Complete Integration Profile | Fill Integration Capabilities tile (transport, ERP, formats) + Document Type tiles |
| 3 | Compatibility Dashboard | View Compatibility Page → search buyers → traffic-light match results per doc type |
| 4 | Compare & Reconcile Templates | Compare SAP Golden Template vs buyer template → resolve discrepancies → save Reconciled Template |
| 5 | Map in Managed Gateway | Hand off reconciled template to integration layer for mapping/transformation |

### 11 OC Rejection Reason Codes
Standard reason codes for rejecting a PO via Order Confirmation:

| # | Rejection Reason | Use Case |
|---|---|---|
| 1 | Duplicate Order | PO already received before |
| 2 | Incorrect Delivery Date | Requested date unacceptable |
| 3 | Incorrect Description | Item description doesn't match records |
| 4 | Incorrect Price | Price wrong or doesn't match terms |
| 5 | Incorrect Quantity | Quantity not acceptable |
| 6 | Incorrect Stock / Part Number | Part/SKU doesn't match catalog |
| 7 | Incorrect Supplier Code Used | Wrong supplier account/ANID used |
| 8 | Incorrect UOM | Unit of Measure doesn't match |
| 9 | Not our Product Line | Supplier doesn't carry this item |
| 10 | Unable to Supply Item(s) | Cannot fulfill for any reason |
| 11 | Other | Catch-all; mandatory comment required |

Buyers can replace this list by uploading a custom CSV: Buyer Account → Upload → Rejected Reason Codes.

In cXML: `ConfirmationHeader type="reject"` (header-level) or `ConfirmationStatus type="rejected"` (line-level). In EDIFACT ORDRSP: rejection reason in FTX+ACD segment.

### Certification Tiers (Supplier Account)
| Tier | Annual Documents | Integration Level |
|---|---|---|
| Platinum | 500+ | High-volume |
| Gold | 100–499 | Medium |
| Silver | 50–99 | Basic |
| Bronze | 5–49 | Entry |

## 5. Managed Gateway

### 6 Configuration Steps
Prereqs: Role + enable in Settings. Steps: Basic Info → Connection → Routing → Cross-Refs → Test → Activate.

### Connection Types
| Type | Protocol | Certificate | Best For |
|---|---|---|---|
| **HTTPS** | HTTPS/TLS 1.2+ | CA-signed for auth; import SSL from acig.ariba.com (STRUST) | SAP ERP with Add-On |
| **AS2** | AS2 over HTTPS | Self-signed OK for signing/encryption; CA required for client auth only | High-volume direct EDI |
| **VAN** | Via third-party VAN | VAN-managed (no manual upload) | Existing VAN relationships |

### AS2 Certificate Details
- Signing: Supplier's private key signs outbound messages; self-signed supported
- Encryption: Partner's public certificate encrypts payload
- MDN: Supports synchronous and asynchronous acknowledgements
- Update: Self-service via Managed Gateway portal (direct AS2); SAP Support case required for VAN

### Deployment Models
| Model | Description | Middleware? |
|---|---|---|
| Direct Connectivity | Documents flow directly via SAP Cloud Connector | No |
| Mediated Connectivity | Documents flow through SAP PI/PO or Integration Suite | Yes |

## 6. Test Central
Core scenarios (PO→OC→ASN→Invoice), buyer-specific, doc variants (Change/Cancel PO, Credit Memo, Blanket). UAT: Name → Customers+Types → Apply → Add optional → Export CSV.

## 7. RACI Matrix — SBN Integration Project

**Roles:** CBL=Customer Business Lead, CSA=Customer SBN Admin, CTL=Customer Technical Lead, SUP=Supplier, SAP=SAP/BN Integrator

| Phase | Activity | CBL | CSA | CTL | SUP | SAP |
|---|---|:---:|:---:|:---:|:---:|:---:|
| 1. Registration | Create/verify buyer account | A | R | I | I | C |
| | Enable Managed Gateway | I | R | C | I | C |
| | Establish trading relationships | A | R | I | C | I |
| 2. Discovery | Scope requirements & doc types | A | C | R | C | C |
| | Define transaction rules | A | R | C | I | C |
| | Supplier segmentation | A | R | C | I | C |
| 3. Gateway Config | Configure Managed Gateway | I | C | R | I | A |
| | Set up ERP connection | I | I | R | I | A |
| | Configure authentication | I | I | R | C | A |
| 4. Development | Build mappings & transforms | I | I | A/R | C | C |
| | Create test scripts | I | C | R | C | A |
| 5. Testing | Execute integration tests | C | C | R | R | C |
| | Business sign-off | A | R | C | C | I |
| 6. Go-Live | Cutover + production switch | A | R | R | I | C |
| | Confirm first production txn | A | R | R | R | C |
| 7. Support | Monitor + error resolution | I | R | R | C | C |
| | Certificate renewal | I | C | R | I | C |
| | Onboard additional partners | A | R | C | I | C |

R=Responsible, A=Accountable, C=Consulted, I=Informed

## 8. Timeline Planner
| Phase | Days |
|---|---|
| Discovery | 10 |
| Development | 15 |
| Testing | 15 |
| Go-Live | 5 |
| Post Go-Live | 10 |
| **Total** | **55 (~11 weeks)** |

14 regions: AU, US, GB, CA, DE, FR, IN, JP, SG, KR, CN, BR, ZA, AE. Skips weekends + holidays.

## 9. FAQ
ANID: AN + 11 digits (-T for test). Auth: Shared Secret or Certificates. HTTP: 400, 401, 406, 500.

## 10. Builder Playbooks
Lifecycle (§1), integration model (§3), GITP process (§4), Managed Gateway connection types (§5), document standard (§2), timeline (§8), UAT (§6), RACI (§7).

## 11. EDIFACT D96A — Cross-Reference
For full message-by-message detail, read `references/edifact-d96a.md`.

D96A messages on SBN: ORDERS, ORDCHG, ORDRSP, DESADV, RECADV, INVOIC, REMADV (procurement); DELFOR ×2, DELJIT (supply chain); IFTMIN, IFTSTA (logistics/BN4L).

All D96A messages configured via Managed Gateway (§5). Download latest spec PDFs: `node --input-type=module < scripts/download-edifact-d96a.js`

## 12. Document Routing Configuration
- Portal (online): default for Standard accounts
- cXML HTTP: Settings → Electronic Order Routing → enter endpoint URL
- EDI via Managed Gateway: channel configuration required (§5)
- Email PDF: for low-volume or non-integrated suppliers

Full routing setup: `references/account-management.md` §6.
