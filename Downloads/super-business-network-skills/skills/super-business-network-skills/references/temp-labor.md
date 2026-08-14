# Temporary Labor Tracking — Reference

Time sheets, service sheets, and labor tracking for temporary staffing on SAP Business Network.

**Official SAP Source (v2605):**
- [Tracking Temporary Labor Time](https://help.sap.com/docs/ARIBA_NETWORK_SUPPLIERS/b62ba04e48ff49df99e4e78a720f0c72?locale=en-US&state=PRODUCTION&version=2605)

## 1. Overview

SAP Business Network supports temporary labor tracking for service-based procurement, particularly staffing and contingent workforce scenarios. Suppliers (staffing agencies) submit time sheets or service sheets that buyers review and approve before invoicing.

## 2. Service Types for Temporary Labor

| Type | Description |
|---|---|
| Time & Material (T&M) | Contingent workers billed by time units (hourly/daily) against a service PO |
| Fixed Price Service | Billed on milestone completion; service sheet confirms delivery |
| Blanket Service PO | Framework for ongoing staffing; drawn down over time |

## 3. Time Sheet Workflow

```
Buyer creates Service PO → Supplier receives PO
        ↓
Worker performs services → Supplier creates Time Sheet
        ↓
Submit Time Sheet → Buyer reviews and approves
        ↓
Supplier creates Service Invoice
```

### Creating a Time Sheet (Portal)
1. Fulfillment → Time Sheets → Create Time Sheet
2. Reference the Service PO
3. Enter: worker reference, service period (start/end date), hours per day/week
4. Attach supporting documents (sign-off forms) if required
5. Submit → buyer receives notification

### Time Sheet Fields
- Service PO number
- Worker reference (name or ID — per buyer configuration)
- Service period (start and end date)
- Work location
- Hours/days worked per time unit
- Overtime hours (if applicable)
- Comments / notes

## 4. Service Sheet Workflow

Service sheets are used for fixed-price or milestone-based service confirmation.

**Creating a Service Sheet:**
1. Fulfillment → Service Sheets → Create Service Sheet
2. Reference the Service PO line item
3. Enter: service description, quantity performed, unit price
4. Attach completion evidence
5. Submit for buyer approval

## 5. Approval Workflow

| Step | Actor | Action |
|---|---|---|
| Submit | Supplier | Submit time sheet / service sheet |
| Review | Buyer (AP / manager) | Review time entries |
| Approve | Buyer approver | Approve → releases for invoicing |
| Reject | Buyer approver | Reject with reason → supplier corrects and resubmits |

Approval notifications sent to buyer's configured contacts via SBN messaging.

## 6. Invoicing After Approval

Once approved, supplier creates a Service Invoice referencing the approved time sheet or service sheet.
- Invoice amount = approved hours × rate (T&M) or fixed milestone value
- Reference: `references/invoicing.md` §2 for invoice creation methods

## 7. Integration with Buyer Systems
- Time sheet data can integrate with buyer's HR/workforce management system via cXML
- For SAP buyers: integration with SAP Fieldglass or SAP S/4HANA HR modules
- Portal-based submission preferred for low complexity; cXML for high-volume staffing agencies

## 8. Builder Playbook
- T&M vs. fixed price: §2
- Time sheet creation: §3
- Service sheet: §4
- Approval flow: §5
- Invoice after approval: §6 + invoicing.md