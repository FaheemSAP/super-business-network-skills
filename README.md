# Super Business Network Skills

> SAP Business Network (SBN) Catalog & Integration Enablement skill for Joule Work Desktop

## Overview

A comprehensive AI skill that provides expert-level guidance and artifact generation for SAP Business Network supplier enablement across 7 capability domains:

| Domain | Capabilities |
|--------|-------------|
| **Catalog Hub** | Catalog types (Static CIF, PunchOut L1/L2), 81-field CIF 3.0 reference, CMS vs Non-CMS, 12 authoring rules |
| **Catalog Processing** | 25+1 validation rules with exact codes, CIF/cXML/Excel generation, Ariba status codes |
| **Integration Hub** | 7-phase lifecycle, document standards (cXML/X12/EDIFACT/EANCOM/PIDX), GITP, Managed Gateway, Test Central |
| **cXML Anonymizer** | Document anonymization for Test Central, region detection, security hardening |
| **Supply Chain Collaboration** | Forecast, procurement, inventory, quality, manufacturing, shipping collaboration |
| **BN4L (Logistics)** | Freight collaboration, Global Track & Trace, dock scheduling, material traceability |
| **SAP APIs** | cXML endpoints, REST/Open APIs, authentication methods, endpoint configuration |

## Features

- **Advisory** — Authoritative answers on SBN terminology, rules, flows, and best practices
- **Builder** — Validates CIF files, generates CIF/cXML artifacts, anonymizes documents, converts formats
- **Trilingual** — Full support for English, Japanese (日本語), and Chinese-Mandarin (中文)
- **Modular** — Each domain in its own reference file for independent updates
- **12 Evaluation Tests** — Regression testing for all major workflows

## Installation

1. Open Joule Work Desktop
2. Go to Extensions → Install from file
3. Select the exported `.zip` file from this repository

Or install via the AI Skills Library tile from [github.com/FaheemSAP/super-business-network-skills](https://github.com/FaheemSAP/super-business-network-skills).

## Repository Structure

```
skills/
└── super-business-network-skills/
    ├── SKILL.md                    ← Main skill instructions
    ├── references/
    │   ├── catalog-hub.md
    │   ├── catalog-processing.md
    │   ├── integration-hub.md
    │   ├── cxml-anonymizer.md
    │   ├── supply-chain-collaboration.md
    │   ├── bn4l-logistics.md
    │   └── sap-apis.md
    ├── scripts/
    │   └── anonymize_cxml.py
    └── assets/
        └── evals.json
```

## Author

**SAP Business Network — Catalog & Integration Enablement**

Developed by a Supplier Dedicated Specialist for the APJ region, focusing on Catalog & Integration workstreams for strategic suppliers.

## Version

**2.0.0** — Merged and expanded from two prior skill packages covering catalog enablement and integration enablement.

## License

Apache License 2.0 — See [LICENSE](LICENSE) for details.

## Contributing

To extend this skill with a new domain:

1. Create a `references/<domain-name>.md` file
2. Update the Reference Map in `SKILL.md`
3. Add activation keywords and a workflow entry
4. Add evaluation test cases to `assets/evals.json`
5. Submit a pull request

## Tags

`sap` `business-network` `catalog` `integration` `cxml` `cif` `punchout` `supplier` `bn4l` `supply-chain` `api` `anonymizer` `validation`
