# SAP Business Network APIs — Reference

## 1. cXML Endpoints (by Data Center)

| Data Center | Buyer Channel URL | Sourcing Channel URL |
|---|---|---|
| **US** | `https://s1.ariba.com/Buyer/cxmlchannel/{ANID}` | `https://s1.ariba.com/Sourcing/cxmlchannel/{ANID}` |
| **EU** | `https://s1-eu.ariba.com/Buyer/cxmlchannel/{ANID}` | `https://s1-eu.ariba.com/Sourcing/cxmlchannel/{ANID}` |
| **AU** | `https://s1.au.cloud.ariba.com/Buyer/cxmlchannel/{ANID}` | `https://s1.au.cloud.ariba.com/Sourcing/cxmlchannel/{ANID}` |
| **JP** | `https://s1.jp.cloud.ariba.com/Buyer/cxmlchannel/{ANID}` | `https://s1.jp.cloud.ariba.com/Sourcing/cxmlchannel/{ANID}` |
| **CN** | `https://s1.sapariba.cn/Buyer/cxmlchannel/{ANID}` | `https://s1.sapariba.cn/Sourcing/cxmlchannel/{ANID}` |

Singapore: no dedicated data center — served from AU or US depending on tenancy. Confirm by checking your Ariba site URL.

### Supplier Transaction URLs
| Data Center | Shared Secret | Certificate |
|---|---|---|
| US | `https://service.ariba.com/service/transaction/cxml.asp` | `https://certservice.ariba.com/service/transaction/cxml.asp` |
| US (Integration) | `https://service-2.ariba.com/service/transaction/cxml.asp` | `https://certservice-2.ariba.com/service/transaction/cxml.asp` |
| AU/JP/CN | Follow regional hostname pattern above | Follow regional hostname pattern above |

## 2. Authentication
| Method | Use Case |
|---|---|
| Shared Secret | cXML document exchange |
| Digital Certificates | High-security cXML |
| OAuth 2.0 | REST APIs, BN4L |
| Basic Auth | Managed Gateway |

### OAuth 2.0 — Regional Token URLs

| Data Center | OAuth Token URL | OpenAPI Base URL | Developer Portal |
|---|---|---|---|
| **US** | `https://api.ariba.com/v2/oauth/token` | `https://openapi.ariba.com/` | `https://developer.ariba.com/api/` |
| **EU** | `https://api-eu.ariba.com/v2/oauth/token` | `https://eu.openapi.ariba.com/` | `https://eu.developer.ariba.com/api/` |
| **AU** | `https://api.au.cloud.ariba.com/v2/oauth/token` | `https://openapi.au.cloud.ariba.com/` | `https://developer.au.cloud.ariba.com/api/` |
| **JP** | `https://api.jp.cloud.ariba.com/v2/oauth/token` | `https://openapi.jp.cloud.ariba.com/` | `https://developer.jp.cloud.ariba.com/api/` |
| **UAE (mn1)** | `https://api.mn1.ariba.com/v2/oauth/token` | `https://mn1.openapi.ariba.com/` | — |

### OAuth 2.0 Client Credentials Grant — Example

**Prerequisites:**
1. Register application in SAP Ariba Developer Portal (region-specific)
2. Obtain OAuthID (Client ID) and Secret
3. Configure OAuth Client ID in SBN: Settings → Integration → API Client ID Configuration

**Token Request:**
```http
POST /v2/oauth/token HTTP/1.1
Host: api.au.cloud.ariba.com
Authorization: Basic <base64(client_id:client_secret)>
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
```

**cURL Example (AU region):**
```bash
curl -X POST "https://api.au.cloud.ariba.com/v2/oauth/token" \
  -H "Authorization: Basic <base64(OAuthClientID:OAuthSecret)>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials"
```

**Using the token:**
```http
GET https://openapi.au.cloud.ariba.com/api/purchase-orders-supplier/v1/prod/orders?realm={realmName}
Authorization: Bearer <access_token>
apiKey: <your_application_key>
```

## 3. Supplier APIs
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
| Network Catalog Management API | Manage catalog products (Promote subscription) |
| Public Catalogs Shop API | Browse public catalogs |

### Supplier Information API
`GET /buyers/suppliers/{vendorID}?siteId={siteID}&collaborationType={type}`

### External Tax Document API
`POST {{runtime_URL}}/v1/taxdocument`

## 4. Buyer/Procurement APIs
| API | Purpose |
|---|---|
| Contract Workspace Retrieval API | Retrieve/filter contract workspaces |
| Contract Workspace Modification API | Create/update contract workspaces |
| Supplier Invite API | Programmatically create vendor records |
| Document Approval API v2 | External approval routing |
| SCIM API | User and group master data |
| Supplier Data with Pagination API v2-v4 | Paginated bulk supplier retrieval |
| Supplier Risk Data Retrieval API | Transfer finding data |
| Supplier Qualification APIs | Manage qualification questionnaires |

## 5. Analytical/Reporting APIs
| API | Purpose |
|---|---|
| Analytical Reporting — Synchronous | Direct synchronous query |
| Analytical Reporting — Job Submission | Async job for large data |
| Analytical Reporting — Job Results | Retrieve async results |
| Operational Reporting for Procurement | Async procurement reporting |
| Operational Reporting for Sourcing | Async sourcing reporting |

## 6. BN4L APIs
| Interface | Protocol |
|---|---|
| Shipper↔BN4L | REST |
| BN4L↔Carrier | REST |
| GTT/FC APIs | REST on api.sap.com |
| Provider API for Freight Booking | Carrier booking confirmations |
| Provider API for Freight Tendering | Freight order tendering |
| Provider API for Freight Subcontracting | Subcontracting events |
| Provider API for Invoicing (LBN) | Freight invoice submission |
| Global Track and Trace API | Shipment tracking events |
| Provider API for Dock Appointments | Create/manage dock appointments |

OAuth 2.0 (client credentials) for all BN4L APIs.

## 7. Rate Limiting

SBN applies **endpoint-specific rate limits**. HTTP 429 returned when exceeded.

### Rate Limit Response Headers
- `X-RateLimit-Limit-minute`
- `X-RateLimit-Remaining-minute`
- `X-RateLimit-Limit-hour` / `X-RateLimit-Remaining-hour`
- `X-RateLimit-Limit-day` / `X-RateLimit-Remaining-day`

### Example Limits
| API | Per Minute | Per Hour | Per Day |
|---|---|---|---|
| Analytical Reporting (Job Submit) | 2 | 8 | 40 |
| Document Approval API | 800 | 35,000 | — |
| Operational Reporting (Procurement) | 3 | 50 | 300 |
| External Approval API (Sourcing) | 400 | 12,000 | 40,000 |

Some SBN supplier APIs use **dynamic runtime throttling** without published limits. SAP Support cannot increase limits.

## 8. API Versioning & Deprecation

| State | Meaning |
|---|---|
| Active | Current, supported |
| Deprecated | Existing apps supported 12 months; new apps cannot request access |
| Decommissioned | No longer supported |

**Rules:**
- API must be Active or Deprecated for ≥24 months before decommission
- Deprecated state must last ≥12 months
- Deprecated responses include `X-API-Warn` header
- Versions in path: `/api/{api-name}/v1/prod/...`

## 9. Endpoint Configuration
Buyer: Settings → Integration → Business Application IDs and End Points.
Supplier: Managed Gateway Step 2 or Cloud Integration Gateway.
S/4HANA Cloud: scope item 7VL (Supplier Integration) must be active.

## 10. cXML Validation
DTD: `http://xml.cXML.org/schemas/cXML/1.2.069/cXML.dtd` (current). Fallback: 1.2.045. All docs need DOCTYPE declaration.

## 11. SAP Business Accelerator Hub
`https://api.sap.com` — browse 106+ REST APIs (SAPAribaOpenAPIs package), download OpenAPI specs, sandbox testing.

## 12. Official API Documentation Sources (v2605)

All source URLs maintained in `assets/doc-sources.json`.

| Portal | URL |
|---|---|
| SAP Ariba Network Suppliers | https://help.sap.com/docs/ARIBA_NETWORK_SUPPLIERS?version=2605 |
| Business Network for Trading Partners | https://help.sap.com/docs/business-network-for-trading-partners?version=2605 |
| Business Network for Procurement | https://help.sap.com/docs/business-network-for-procurement?version=2605 |
| SAP Business Accelerator Hub | https://api.sap.com |

Use `web_search` to verify latest API versions. Never fabricate endpoint URLs.

## 13. Builder Playbooks
- Configure endpoint: §1 URL + §2 auth + ANID
- List APIs: §3–§6 filtered by use case
- Set up OAuth: §2 regional token URLs + example
- Rate limits: §7 headers + examples
- API lifecycle: §8 versioning/deprecation
- Validate cXML: §10 DTD URL
- API call template: REST/cXML with auth headers
