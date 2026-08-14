# Changelog

All notable changes to **Super Business Network Skills** are documented here.

---

## [2.6.0] — 2026-08-14

### Added
- **SBN Discovery** domain (`references/sbn-discovery.md`) — supplier matchmaking marketplace, buyer RFI/RFX postings, direct supplier search, profile optimisation, UNSPSC category mapping (20,000+ categories, 190+ countries), diversity certifications, integration with SAP Ariba Guided Sourcing and S/4HANA Cloud (H2 2025)
- **Payment Programs** domain (`references/payment-programs.md`) — dynamic discounting (SEPTO, buyer-initiated ad hoc, supplier-initiated), supply chain finance (SAP Taulia), virtual card payments, Peppol e-invoicing, Japan JCT/IRN compliance
- **Compliance & Sustainability** domain (`references/compliance-sustainability.md`) — supplier risk management, ESG reporting, certification management, SAP Ariba Supplier Risk, Sustainability Data Exchange
- **TPS Repository** (`references/tps-repository.md`) — growing generalised knowledge base of resolved enablement issues; privacy-safe (no company names, ANIDs, ticket numbers, or PII)
- Activation triggers: `discovery`, `RFI`, `RFX`, `early payment`, `supply chain finance`, `SEPTO`, `virtual card`, `Peppol`, `e-invoicing`, `JCT`, `IRN`, `compliance`, `sustainability`, `ESG`

### Updated
- `assets/doc-sources.json` refreshed to SAP Help Portal version **v2605**
- `SKILL.md` metadata: version `2.6.0`, domain count updated to **17**, expanded tag list
- `package.json` version bumped to `2.6.0`
- README badges and domain table updated

---

## [2.1.0] — 2026-08-11

### Added
- **EDIFACT D96A** domain (`references/edifact-d96a.md`) — 12 message types: DELFOR, DELJIT, DESADV, IFTMIN, IFTSTA, INVOIC, ORDCHG, ORDERS, ORDRSP, RECADV, REMADV
- **Invoicing** domain (`references/invoicing.md`) — PO flip, credit/debit memos, InvoiceDetailRequest cXML, Invoice Status Portal
- **Order Management** domain (`references/order-management.md`) — OC, ASN/ShipNoticeRequest, goods receipt, service sheets
- **Account & Registration** domain (`references/account-management.md`) — sign-up, user roles, TRR, document routing, test accounts
- **Buyer Administration** domain (`references/buyer-administration.md`) — transaction rules, routing rules, Spot Buy
- **Messaging** domain (`references/messaging.md`) — Inbox/Outbox, automated responses, notification rules
- **Reports** domain (`references/reports.md`) — transaction, catalog, network activity, invoice reporting
- **Temporary Labor** domain (`references/temp-labor.md`) — time sheets, service sheets, approval workflow
- `scripts/download-edifact-d96a.js` — downloads latest EDIFACT D96A spec PDFs
- Workflow P (EDIFACT D96A), Q–R entries for new domains

### Changed
- Domain count expanded from 7 to 15
- `SKILL.md` version bumped to `2.1.0`
- README updated to reflect 15 domains and v2.1.0

---

## [2.0.0] — 2026-08-11

### Added
- **Supply Chain Collaboration** domain (`references/supply-chain-collaboration.md`) — forecast, procurement, inventory, quality, manufacturing, shipping
- **BN4L (Logistics)** domain (`references/bn4l-logistics.md`) — freight collaboration, Global Track & Trace, dock scheduling, material traceability
- **SAP APIs** domain (`references/sap-apis.md`) — cXML endpoints, REST/Open APIs, OAuth & shared secret, data center URLs
- Workflow G (Supply Chain Collaboration), H (BN4L & Logistics)
- BN4L retirement note: Neo platform retired July 2025

### Changed
- Domain count expanded from 4 to 7
- `package.json` initialised at `2.0.0`

---

## [1.0.0] — 2026-08-11

### Added
- Initial release with 4 core domains
- **Catalog Hub** (`references/catalog-hub.md`) — catalog types, 81-field CIF 3.0, CMS vs Non-CMS, 12 authoring rules
- **Catalog Processing** (`references/catalog-processing.md`) — 25+1 processing rules, status codes 200–564, CIF/cXML/Excel generation
- **Integration Hub** (`references/integration-hub.md`) — 7-phase lifecycle, GITP, Managed Gateway, Test Central, timeline planning
- **cXML Anonymizer** (`references/cxml-anonymizer.md`) — cXML anonymization for Test Central
- `scripts/anonymize_cxml.py` — cXML anonymization utility
- `assets/evals.json` — evaluation tests
- `assets/doc-sources.json` — SAP Help Portal source URLs
- Apache 2.0 license
