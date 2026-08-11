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
| Document | cXML | X12 | EANCOM | EDIFACT | PIDX |
|---|---|---|---|---|---|
| PO | OrderRequest | 850 | ORDERS | ORDERS | OrderCreate |
| OC | ConfirmationRequest | 855 | ORDRSP | ORDRSP | OrderResponse |
| ASN | ShipNoticeRequest | 856 | DESADV | DESADV | ShipNotice |
| Invoice | InvoiceDetailRequest | 810 | INVOIC | INVOIC | Invoice |

PO: Buyer→Supplier. OC/ASN/Invoice: Supplier→Buyer.

## 3. Integration models
Portal (<100/yr), CSV (100–500/yr), cXML (>500/yr), EDI (>500/yr). Recommend full at 250–500+.

## 4. GITP
5-step self-service + 12 OC rejection codes. Certification: Platinum/Gold.

## 5. Managed Gateway (6 steps)
Prereqs: Role + enable in Settings. Steps: Basic Info → Connection → Routing → Cross-Refs → Test → Activate.

## 6. Test Central
Core scenarios (PO→OC→ASN→Invoice), buyer-specific, doc variants (Change/Cancel PO, Credit Memo, Blanket). UAT: Name → Customers+Types → Apply → Add optional → Export CSV.

## 7. Buyer Portfolio & RACI
5 deployment phases, RACI matrices (deployment + postDeployment), roles, 14 time zones.

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

## 10. Builder playbooks
Lifecycle (§1), integration model (§3), document standard (§2), timeline (§8), UAT (§6), RACI (§7).