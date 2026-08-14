# Compliance, Sustainability & Supplier Risk Management — Reference

Supplier risk, ESG reporting, certification management, qualification, and compliance on SAP Business Network.

**Official SAP Sources:**
- [SAP Ariba Supplier Risk](https://www.sap.com/products/spend-management/supplier-risk.html)
- [SAP Sustainability Data Exchange](https://www.sap.com/products/business-network/sustainability-data-exchange.html)
- [Managing Certifications on Company Profiles](https://help.sap.com/docs/business-network-for-trading-partners/seller-account-settings-and-profile-configuration/managing-certifications-on-your-company-profiles)

## 1. Architecture Overview

| Layer | Product | Role |
|---|---|---|
| Collaboration & Data | SAP Business Network | Supplier profiles, certifications, document exchange |
| Risk Intelligence | SAP Ariba Supplier Risk | Risk monitoring, alerts, third-party data |
| Qualification | SAP Ariba SLP | Questionnaires, qualification status, ERP sync |
| Sustainability Data | SAP Sustainability Data Exchange (SDX) | Scope 3 / PCF data exchange |
| Compliance Screening | SAP Watch List Screening / GTS | Sanctions, denied party lists (at ERP layer) |

## 2. Supplier Risk Management

### Risk Categories (4 default; up to 25 custom)
| Category | Examples |
|---|---|
| Financial | Insolvency, credit deterioration, bankruptcy |
| Operational | Natural disasters, logistics failures, production disruptions |
| Environmental & Social | ESG violations, labor/human rights incidents |
| Regulatory & Legal | Sanctions, export control, non-compliance |

### Third-Party Data Providers
| Provider | Data Type |
|---|---|
| Moody’s Analytics | Financial + Country risk (default from 2511) |
| Dun & Bradstreet | Business intelligence |
| EcoVadis | ESG/sustainability ratings |
| RapidRatings | Financial health |
| SecurityScorecard | Cybersecurity risk |

### Key Features
- Supplier Risk Dashboard (portfolio-level view)
- Risk Alerts (configurable, proactive)
- 5-tab Supplier Profile: Risk Exposure, Risk Incidents, Corporate Info, Engagements, Custom Data
- Engagement Requests (bulk or individual, linkable to contracts)
- Residual Risk calculation: inherent risk × control effectiveness
- Supplier Segmentation: by country/commodity/exposure
- AI recommendations (Joule integration from 2511)

### SBN ↔ Supplier Risk Integration
- Business Network Certificates panel surfaces in SLP profiles (2411 release)
- Self-Assessed Questionnaires sent to SBN-registered and non-registered suppliers
- SBN profile updates sync to SLP questionnaire fields within minutes

## 3. Sustainability / ESG

### SBN Sustainability Capabilities
| Capability | Description |
|---|---|
| EcoVadis integration | Verified ratings displayed on Trading Partner Profile (May 2024) |
| Certification upload | Environmental, diversity, social certifications on profile |
| Sustainability Data Exchange (SDX) | Scope 3 product carbon footprint (PCF) data exchange |
| Discovery filtering | Buyers filter suppliers by sustainability ratings and certifications |
| ESG questionnaires | Via Engagement Requests (Human Rights Assessment, custom SAQs) |

### SAP Sustainability Data Exchange (SDX)
BTP-based SaaS running on SBN for Scope 3 / PCF data:
- Buyers request actual PCF data from suppliers (replacing estimates)
- Suppliers respond or proactively share updates
- Bulk requests supported
- Integrates with SAP Sustainability Footprint Management (SFM)
- Standards: **PACT**, **Catena-X**, **GHG Protocol**
- Audit-ready, data-sovereign exchange

### Framework Support
| Framework | SBN Integration |
|---|---|
| EcoVadis | Direct — ratings on Trading Partner Profile |
| GHG Protocol / PACT / Catena-X | Via SDX for PCF data |
| GRI | SAP SCT supports GRI; EcoVadis ratings align |
| CDP | No direct SBN integration |
| CSRD / EU Taxonomy | SAP Sustainability Control Tower (buyer-side) |

## 4. Certification Management

### Supplier Self-Service
Company Profile → Certifications tab:
- Select from predefined list or custom name
- Upload supporting document
- Provide: effective date, expiration date, certification number, certifying body, certified location

### Certification Categories (7)
| Category | Examples |
|---|---|
| Supplier Diversity | WBE, MBE, Veteran-owned, LGBTBE, HUBZone, 8(a), SBE |
| Environmental | ISO 14001, environmentally responsible operations |
| Energy | ISO 50001, Energy Star |
| Quality | ISO 9001, AS9100, industry-specific |
| Social Enterprise | B-Corp, Fair Trade, community impact |
| Security | ISO 27001, SOC 2 |
| Other | Custom certifications |

### Verification
- Certifications are **self-declared** with document upload (not independently verified by SAP)
- **EcoVadis** provides the only third-party verified credential on the profile
- 2411 release: Business Network Certificates panel in SLP supplier profiles

### Buyer Use
- Certifications filter in SBN Discovery search
- Direct profile review on Trading Partner Profile
- Qualification questionnaires can enforce certificate submission requirements

## 5. Supplier Qualification

### Process Flow
```
Supplier Identified → Invited to Register (SBN link) →
Registration Questionnaire (self-service) → Buyer Approval →
Qualification Questionnaire (commodity/region-specific) →
Decision: Qualified / Pending / Rejected / Expired
```

### Qualification Mechanics (via SAP Ariba SLP)
- Configured as Survey document, type = Qualification Request
- Dynamic/conditional questions driven by Commodity and Region
- Typical data: financial stability, certifications, regulatory compliance, ESG, H&S, insurance
- ESG included if buyer enables in SLP

### SBN ↔ SLP Relationship
| Aspect | SBN | SLP |
|---|---|---|
| Registration | Supplier creates/maintains account | Invites supplier via SBN link |
| Data sync | Pushes profile data to SLP within minutes | Receives, maps to questionnaire fields |
| Questionnaires | Supplier responds via SBN interface | Buyer configures templates |
| Qualification status | Not managed on SBN | Manages Qualified/Rejected/Expired |
| ERP sync | Not direct | Via Managed Gateway → S/4HANA/MDG |

## 6. Compliance Monitoring

### What SBN Natively Covers
| Feature | Detail |
|---|---|
| E-invoicing compliance | 40+ countries; business rules engine; audit-ready |
| Business rules engine | Configurable for regulatory policies |
| Supply chain traceability | Material Traceability module (BN4L) |
| Due diligence documents | Certificates of origin, audit records |

### Sanctions / Denied Party Screening
SBN does **NOT** include native sanctions screening. Separate SAP tools:
| Tool | Description |
|---|---|
| SAP Watch List Screening | Cloud SaaS (BTP); real-time name/address screening; REST API with S/4HANA |
| SAP Business Integrity Screening | Screen master data + transactions; Dow Jones Watchlist support |
| SAP GTS — SPL Screening | Full sanctioned party list screening for logistics/financial |

Integration pattern: These apply at the ERP/MDG layer when supplier master data is created after qualification flows through SBN → SLP → ERP.

## 7. SAP Responsible Design and Production (RDP)

BTP-based SaaS for Extended Producer Responsibility (EPR) and packaging compliance:
- Track product/packaging composition (materials, weight, recyclability)
- Calculate EPR fees and plastic taxes across global markets
- Report against packaging recyclability targets
- Regulatory filing for EPR-regulated markets (EU, UK, DE, FR)

**RDP ↔ SBN:** No direct packaged integration. Both connect to SAP ERP/S/4HANA as common backbone. Supplier packaging data could flow via qualification questionnaires but is not a documented standard scenario.

## 8. Builder Playbooks
- Supplier risk overview: §2 (categories, providers, features)
- ESG/sustainability capabilities: §3 (SDX, EcoVadis, frameworks)
- Certification management: §4 (upload, categories, verification)
- Supplier qualification: §5 (flow, SLP mechanics, ERP sync)
- Compliance approach: §6 (what’s native vs. what needs separate tools)
- Sanctions screening: §6 (explain SBN limitation + SAP alternatives)
