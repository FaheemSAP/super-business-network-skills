# SAP Business Network APIs — Reference

## 1. cXML Endpoints
| Data Center | URL |
|---|---|
| US | `https://s1.ariba.com/Buyer/cxmlchannel/{ANID}` |
| EU | `https://s1-eu.ariba.com/Buyer/cxmlchannel/{ANID}` |
| General | `https://service.ariba.com` |

## 2. Authentication
| Method | Use Case |
|---|---|
| Shared Secret | cXML document exchange |
| Digital Certificates | High-security |
| OAuth 2.0 | REST APIs, BN4L |
| Basic Auth | Managed Gateway |

OAuth: Provision OAuthID → client credentials grant → bearer token.

## 3. Supplier APIs (2024)
| API | Purpose |
|---|---|
| Purchase Orders Supplier API | Retrieve POs |
| SCC Ship Notices API | Submit ASNs |
| Order Change Requests API | Submit changes |
| Planning Collaboration API | Forecasts/commitments |
| Proof of Service API | Submit PoS |
| Invoice Data Extraction API | Extract invoices |
| Audit Search API | Audit records |
| Integration Events API | Track events |
| Supplier Information API | Check relationships |
| External Tax Document API | Post tax docs |

### Supplier Information API
`GET /buyers/suppliers/{vendorID}?siteId={siteID}&collaborationType={type}`

### External Tax Document API
`POST {{runtime_URL}}/v1/taxdocument`

## 4. BN4L APIs
Shipper→BN4L: SOAP. BN4L→Carrier: REST. GTT: REST. All on api.sap.com.

## 5. Endpoint Configuration
Buyer: Settings → Integration → Business Application IDs and End Points.
Supplier: Managed Gateway Step 2 or Cloud Integration Gateway.
S/4HANA Cloud: scope item 7VL (Supplier Integration) must be active.

## 6. cXML Validation
DTD: `http://xml.cXML.org/schemas/cXML/1.2.069/cXML.dtd` (current). Fallback: 1.2.045. All docs need DOCTYPE declaration.

## 7. SAP Business Accelerator Hub
`https://api.sap.com` — browse APIs, download OpenAPI specs, sandbox testing.

## 8. Builder playbooks
- Configure endpoint: §1 URL + §2 auth + ANID
- List APIs: §3 filtered by use case
- Set up OAuth: §2 provisioning
- Validate cXML: §6 DTD URL + validation
- API call template: REST/cXML with auth headers