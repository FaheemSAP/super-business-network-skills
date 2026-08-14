# SAP Business Network Discovery — Reference

Supplier discoverability marketplace connecting buyers with qualified suppliers.

**Official SAP Sources (v2605):**
- [Using SBN Discovery as Buyer](https://help.sap.com/docs/business-network-for-trading-partners/selling-on-business-network-discovery/using-sap-business-network-discovery-as-buyer)
- [SAP Business Network Discovery Overview](https://community.sap.com/t5/spend-management-blog-posts-by-sap/how-buyers-discover-suppliers-on-sap-business-network/ba-p/14328306)

## 1. Overview

SAP Business Network Discovery (formerly Ariba Discovery, rebranded August 2023) is an intelligent matchmaking marketplace. Two mechanisms:
- **Buyer-posted RFI/RFX postings** — broadcasted to matched suppliers by commodity and territory
- **Direct supplier search** — buyers filter by category, certification, location, diversity

Scale: 20,000+ UNSPSC categories, 190+ countries. Embedded in Trading Partner Portal. Integrates with SAP Ariba Guided Sourcing, Classic Sourcing, Buying/Invoicing, and (from H2 2025) SAP S/4HANA Cloud directly.

## 2. Supplier Profile Optimisation

Key levers for discoverability:

### UNSPSC Category Selection
- Select broad AND specific categories (be general; use layman's terms)
- Choose next-higher level if exact code unavailable
- More categories = more posting matches
- Up to 50 commodity codes per profile

### Certifications
Seven SAP-defined certification categories:
| Category | Examples |
|---|---|
| Environmental | ISO 14001, EcoVadis |
| Energy | ISO 50001, Energy Star |
| Supplier Diversity | WBENC, NMSDC, HUBZone, LGBTBE, MBE, WBE |
| Social Enterprise | B-Corp, Fair Trade |
| Quality | ISO 9001, AS9100 |
| Security | ISO 27001, SOC 2 |
| Other | Industry-specific |

### Profile Completeness
- Company description and logo
- Banking information
- Product/service descriptions
- Location and coverage areas
- Diversity and sustainability data

### Verified Badge
Complete profile verification process for a "Verified" indicator that increases buyer trust.

### Promote Subscription (Q1 2025)
Paid add-on providing:
- Higher search ranking
- Private lead details
- AI-powered catalog generation
- Digital storefront
- Product showcase

## 3. How Buyers Use Discovery

### Creating Postings
1. Buyer navigates to Discovery → Create Posting
2. Defines commodity category, location, description
3. Posting broadcasted to all matched suppliers
4. Suppliers respond to the posting
5. Buyer reviews responses, shortlists, and initiates sourcing

Creating postings is **free** for buyers. Takes ~5 minutes.

### Direct Search
Filters available:
- Business type (manufacturer, distributor, service provider)
- Certifications (diversity, quality, environmental)
- Verification status
- Location / country
- Industry
- UNSPSC category

### Buyer Permissions
Required permission: "Create and manage posting on SAP Business Network Discovery"

## 4. Supplier Account Types and Fees

| Account | Cost | Discovery Access |
|---|---|---|
| Standard (Free) | No fee | Can respond to postings; basic profile |
| Enterprise | Tiered subscription | Full profile; analytics; enhanced visibility |
| Promote | Annual paid add-on | Highest ranking; digital storefront; AI catalog |

### Fee Thresholds
- Enterprise fees triggered at: **5 documents AND $50K USD** with one buyer in 12 months
- Responding to public sector Discovery postings is **free**
- Subscription tiers: Bronze (5–49 docs), Silver (50–99), Gold (100–499), Platinum (500+)

## 5. SBN Discovery vs Ariba Discovery

- Ariba Discovery **rebranded to SAP Business Network Discovery** on August 18, 2023
- Platform consolidated into Trading Partner Portal with new UI
- Not just a name change — also platform and feature consolidation
- Classic SAP Ariba Sourcing users: access continues as-is
- Next-gen app on SAP BTP / Fiori under development (announced Oct 2025)

## 6. Integration Points

| System | Integration |
|---|---|
| SAP Ariba Guided Sourcing | Direct posting creation from sourcing events |
| SAP Ariba Classic Sourcing | Supplier search and invitation |
| SAP Ariba Buying/Invoicing | Supplier discovery for catalog gaps |
| S/4HANA Cloud (H2 2025) | Direct supplier search integration |

## 7. Builder Playbooks
- Supplier profile optimisation: §2 (categories, certifications, completeness)
- Buyer posting creation: §3
- Account types and fees: §4
- Promote subscription benefits: §2 (Promote section)
- Compare old vs new: §5
