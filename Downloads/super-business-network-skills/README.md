# Super Business Network Skills

> SAP Business Network (SBN) enablement expert for buyers and suppliers — Joule Work Desktop AI skill

![Version](https://img.shields.io/badge/version-2.6.0-blue)
![Domains](https://img.shields.io/badge/domains-17%2B-green)
![License](https://img.shields.io/badge/license-Apache%202.0-lightgrey)
![Language](https://img.shields.io/badge/language-EN%20%7C%20JA%20%7C%20ZH-orange)

## Overview

A comprehensive AI skill providing expert-level guidance and artifact generation for SAP Business Network across **17 capability domains**, covering both buyer and supplier perspectives for the APJ region.

| Domain | Capabilities |
|--------|-------------|
| **Catalog Hub** | Catalog types (Static CIF, PunchOut L1/L2), 81-field CIF 3.0 reference, CMS vs Non-CMS, 12 authoring rules |
| **Catalog Processing** | 25+1 validation rules with exact codes, CIF/cXML/Excel generation, Ariba status codes (200–564) |
| **Integration Hub** | 7-phase lifecycle, cXML/X12/EDIFACT/EANCOM/PIDX standards, GITP, Managed Gateway, Test Central |
| **cXML Anonymizer** | Document anonymization for Test Central, region/PO-type detection, security hardening |
| **Supply Chain Collaboration** | Forecast, procurement, inventory, quality, manufacturing, shipping collaboration |
| **BN4L (Logistics)** | Freight collaboration, Global Track & Trace, dock scheduling, material traceability |
| **SAP APIs** | cXML endpoints, REST/Open APIs, OAuth & shared secret auth, data center URLs |
| **EDIFACT D96A** | DELFOR, DELJIT, DESADV, IFTMIN, IFTSTA, INVOIC, ORDCHG, ORDERS, ORDRSP, RECADV, REMADV |
| **Invoicing** | Invoice types, PO flip, credit/debit memos, validation, status lifecycle, Invoice Status Portal |
| **Order Management** | Receiving orders, OC, ASN, goods receipt, service sheets, change/cancel |
| **Account & Registration** | Sign-up, user roles, account linking, TRR, document routing, test accounts |
| **Buyer Administration** | Buyer config, transaction rules, routing rules, enabling suppliers, Spot Buy |
| **Messaging** | Inbox/Outbox, message types, automated responses, notification rules |
| **Reports** | Transaction, catalog, network activity, invoice reporting, templates |
| **Temporary Labor** | Time sheets, service sheets, approval workflow, buyer system integration |
| **SBN Discovery** | Supplier matchmaking, buyer RFI/RFX postings, profile optimisation, UNSPSC category coverage, diversity certifications |
| **Payment Programs** | Dynamic discounting (SEPTO/ad hoc/supplier-initiated), supply chain finance, virtual cards, Peppol e-invoicing, Japan JCT/IRN |
| **Compliance & Sustainability** | Supplier risk management, ESG reporting, certification management, SAP Ariba Supplier Risk, Sustainability Data Exchange |

## Features

- **Advisory** — Authoritative answers on SBN terminology, rules, flows, and best practices
- **Builder** — Validates CIF files, generates CIF/cXML artifacts, anonymizes documents, converts formats
- **Trilingual** — Full support for English, Japanese (日本語), and Chinese-Mandarin (中文)
- **Modular** — Each domain in its own reference file for independent updates
- **TPS Repository** — Growing knowledge base of resolved enablement issues (generalised, no PII)
- **17 Evaluation Tests** — Regression testing covering all major workflows

## Installation

1. Open Joule Work Desktop
2. Go to **Extensions → Install from file**
3. Select the exported `.zip` from this repository's [latest release](https://github.com/FaheemSAP/super-business-network-skills/releases/latest)

Or install via the AI Skills Library tile from [github.com/FaheemSAP/super-business-network-skills](https://github.com/FaheemSAP/super-business-network-skills).

## Repository Structure

```
├── SKILL.md                              ← Main skill instructions (v2.6.0)
├── references/
│   ├── catalog-hub.md
│   ├── catalog-processing.md
│   ├── integration-hub.md
│   ├── cxml-anonymizer.md
│   ├── supply-chain-collaboration.md
│   ├── bn4l-logistics.md
│   ├── sap-apis.md
│   ├── edifact-d96a.md
│   ├── invoicing.md
│   ├── order-management.md
│   ├── account-management.md
│   ├── buyer-administration.md
│   ├── messaging.md
│   ├── reports.md
│   ├── temp-labor.md
│   ├── sbn-discovery.md              ← NEW in v2.6.0
│   ├── payment-programs.md           ← NEW in v2.6.0
│   ├── compliance-sustainability.md  ← NEW in v2.6.0
│   └── tps-repository.md             ← Supplementary KB, v2.6.0
├── scripts/
│   ├── anonymize_cxml.py
│   └── download-edifact-d96a.js
└── assets/
    ├── evals.json
    └── doc-sources.json
```

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/anonymize_cxml.py` | Anonymize cXML documents for use in Test Central. Requires `pip install lxml defusedxml`. |
| `scripts/download-edifact-d96a.js` | Download latest EDIFACT D96A spec PDFs. Run with `node --input-type=module < scripts/download-edifact-d96a.js`. |

## Activation Triggers

The skill activates on any of these keywords:

**Catalog:** catalog, CIF, CIF 3.0, PunchOut, CMS, UNSPSC, catalog upload, catalog validation  
**Integration:** cXML, EDI, GITP, Managed Gateway, Test Central, UAT, 7-phase, go-live  
**EDIFACT D96A:** DELFOR, DELJIT, DESADV, IFTMIN, IFTSTA, INVOIC, ORDCHG, ORDERS, ORDRSP, RECADV, REMADV, D96A  
**Invoicing:** invoice, credit memo, debit memo, PO flip, InvoiceDetailRequest, Peppol, JCT, IRN  
**Order Management:** ASN, ship notice, goods receipt, service sheet, blanket order  
**Discovery:** discovery, RFI, RFX, supplier search, discoverability  
**Payment:** dynamic discounting, early payment, supply chain finance, SEPTO, virtual card  
**Japanese:** カタログ, 統合, 請求書, 注文, 登録  
**Chinese:** 目录, 集成, 发票, 订单, 注册  

## Releases

See [CHANGELOG.md](CHANGELOG.md) for the full version history, or browse [GitHub Releases](https://github.com/FaheemSAP/super-business-network-skills/releases).

### Latest — v2.6.0 (2026-08-14)

- Expanded from 15 to **17 capability domains**
- Added **SBN Discovery** reference (`references/sbn-discovery.md`) — supplier matchmaking, buyer RFI/RFX, profile optimisation, diversity certifications
- Added **Payment Programs** reference (`references/payment-programs.md`) — dynamic discounting, supply chain finance, virtual cards, Peppol e-invoicing, Japan JCT/IRN
- Added **Compliance & Sustainability** reference (`references/compliance-sustainability.md`) — supplier risk, ESG reporting, certification management, SAP Ariba Supplier Risk
- Added **TPS Repository** (`references/tps-repository.md`) — generalised enablement knowledge base (no PII)
- Updated activation triggers: `discovery`, `early payment`, `supply chain finance`, `Peppol`, `e-invoicing`, `JCT`, `IRN`, `compliance`, `sustainability`
- Updated `doc-sources.json` to v2605 for all SAP Help Portal references
- Updated EDIFACT D96A download script

## Author

**SAP Business Network — Catalog & Integration Enablement**

Developed by a Supplier Dedicated Specialist for the APJ region, focusing on Catalog & Integration workstreams for strategic suppliers.

## License

Apache 2.0 — see [LICENSE](LICENSE).
