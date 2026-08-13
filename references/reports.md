# Reports and Report Templates — Reference

Transaction reporting, catalog reporting, and analytics on SAP Business Network.

**Official SAP Source (v2605):**
- [Reports and Report Templates](https://help.sap.com/docs/ARIBA_NETWORK_SUPPLIERS/d4d8f20708534c808faf6a905c4615e4?locale=en-US&state=PRODUCTION&version=2605)

## 1. Report Types

### Transaction Reports (Suppliers)
| Report | Description |
|---|---|
| Transaction Activity | All documents (PO, OC, ASN, Invoice) in a period |
| Invoice Summary | Invoice status breakdown: approved, rejected, pending, disputed |
| Order Summary | PO volume, value, confirmation rate |
| ASN Summary | Shipment activity and on-time delivery |
| Payment Status | Payment dates and remittance details (requires buyer payment data) |
| Failed Transaction | Integration errors: cXML failures, EDI processing errors |

### Catalog Reports (Suppliers)
| Report | Description |
|---|---|
| Catalog Upload History | All catalog submissions, validation results, approval status |
| Catalog Item Activity | Which catalog items were viewed/purchased by buyers |
| Catalog Error Report | Processing errors per upload, with rule codes |

### Network Activity Reports
| Report | Description |
|---|---|
| Relationship Summary | Active/inactive buyer relationships, TRR status |
| Network Usage | Portal logins, API calls, message volumes |
| Compliance Report | Supplier compliance score per buyer's enablement requirements |

### Buyer-Side Reports (Buyer Admins)
| Report | Description |
|---|---|
| Supplier Enablement Status | Progress of supplier enablement campaigns |
| Invoice Approval Rate | % of invoices auto-approved vs. manually reviewed |
| PO Cycle Time | Time from PO creation to fulfilment |
| Catalog Coverage | % of spend covered by catalogs vs. free-text |
| Spend by Category | UNSPSC-based spend analytics |

## 2. Creating a Report

**Standard Report:**
1. Reports → Reporting → Create Report
2. Select report type
3. Set parameters: date range, document type, buyer/supplier filter
4. Run → view inline or download as CSV/Excel

**Report Templates:**
1. Reports → Report Templates → Create Template
2. Configure: type, filters, columns, sort order
3. Save as named template for reuse

## 3. Scheduled Reports
- Frequency: daily, weekly, monthly
- Delivery: email to configured recipients or download from Reports section
- Format: CSV, Excel, PDF (varies by report type)

## 4. Key Metrics Available

| Metric | Description |
|---|---|
| Invoice Approval Rate | % of invoices approved on first submission |
| Invoice Rejection Rate | % rejected + top rejection reasons |
| PO Confirmation Time | Hours/days from PO receipt to OC |
| ASN Lead Time | Days from ship notice to goods receipt |
| Catalog Hit Rate | Buyer searches resulting in catalog items vs. free text |
| Integration Error Rate | Failed cXML/EDI transmissions as % of total |

## 5. Historical Data
- Reports cover up to 24 months of transaction history
- For longer retention, export and store externally
- SBN can push report data to buyer's analytics system via API — see `references/sap-apis.md`

## 6. Builder Playbook
- Identify report type: §1 tables by audience (supplier/buyer)
- Create report: §2
- Schedule: §3
- Metric explanation: §4
- Historical data: §5