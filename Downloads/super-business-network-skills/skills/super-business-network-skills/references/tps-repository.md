# TPS Knowledge Repository

A growing collection of resolved issues and questions encountered during supplier and buyer enablement. Used as a supplementary knowledge base alongside domain-specific reference files.

## Privacy Rules

**The following must NEVER appear in this file:**
- Customer or supplier company names
- ANIDs or account identifiers
- Support ticket or case numbers
- Internal staff names or initials
- Any personally identifiable information

All entries are generalised to be reusable across any customer/supplier scenario.

---

## Entry Format

```
### TPS-XXX | Category: <domain>
**Problem:** <generic description of the issue>
**Resolution:** <steps to resolve>
**Prerequisites:** <if any>
**Notes:** <optional additional context>
```

---

## Entries

### TPS-001 | Category: Order Management
**Problem:** Supplier asks whether buyers can block or prevent small purchase orders below a minimum value threshold from being sent to suppliers.
**Resolution:**
1. There is no native "minimum PO amount" setting in SAP Business Network at the PO level.
2. If the buyer uses **Guided Buying**, they can configure a **validation policy** to enforce a minimum cart/requisition value before a PO is generated.
3. If the buyer uses the "Classic" procurement interface, this must be raised with the SAP Procurement Team as a **Small/Medium Customization** request.
4. The supplier cannot configure this themselves — it is entirely a buyer-side setting.
5. Once the buyer implements the rule, the supplier's Integration Specialist can assist with any integration troubleshooting caused by the change.
**Prerequisites:** Buyer-side action required. Supplier cannot self-serve.
**Notes:** This is unrelated to catalog MOQ (see TPS-002). Applies to the procurement approval workflow, not the catalog.

---

### TPS-002 | Category: Catalog
**Problem:** Supplier wants to set up Minimum Order Quantity (MOQ) on catalog items to enforce a minimum purchase quantity per line item.
**Resolution:**
1. MOQ is a supported field in the CIF catalog format (refer to Catalog Format Reference Guide).
2. **However**, the buyer must have **Content Management System (CMS) enabled** to support this catalog field.
3. If the buyer does NOT have CMS enabled, the MOQ field will not be supported on upload.
4. To check CMS status: verify with the buyer's enablement team or check buyer configuration.
5. If the buyer wants CMS enabled, they should engage their Network Liaison (NxL) to discuss CMS benefits and enablement.
6. Once CMS is active, the supplier can populate the MOQ column (Column BS in CMS template) in the catalog file.
**Prerequisites:** Buyer must have CMS enabled.
**Notes:** Standard (non-CMS) XLS catalog documentation does not include the MOQ field. CMS-specific catalog documentation is required.

---

### TPS-003 | Category: CSV Invoice
**Problem:** CSV Invoice activation option is not visible/available in the buyer's Supplier Group page within their SBN account.
**Resolution:**
1. This is a known UI limitation — the CSV Invoice activation toggle may not appear in the Supplier Group page by default.
2. Contact the **CSV team** to request activation of CSV Invoice capability for the specific supplier group.
3. Once the CSV team enables it on the backend, the option will become available in the buyer's UI.
**Prerequisites:** Internal request to CSV team required.
**Notes:** This is a backend enablement step, not a configuration error.

---

### TPS-004 | Category: CSV Invoice / Japan
**Problem:** Japanese buyer/supplier requires credit memo functionality via CSV Invoice, but it is not available.
**Resolution:**
1. Due to a historical development issue, **CSV Invoice does not support credit memos** for the Japan market.
2. When a supplier needs to create a credit memo, they must use the **SBN portal** (manual creation) instead of CSV.
3. Advise the buyer to communicate this limitation to their suppliers during enablement.
**Prerequisites:** None — this is a platform limitation.
**Notes:** This is a known, long-standing constraint. No timeline for resolution. Portal-based credit memo creation works normally.

---

### TPS-005 | Category: Catalog / PunchOut
**Problem:** Supplier uploaded a PunchOut index file but it does not synchronize to the buyer's Ariba system.
**Resolution:**
1. For **CMS-enabled buyers**, verify the CMS index file template structure.
2. The index file must contain **only 2 sheets**: one for headers and one for items.
3. **Delete all unnecessary/extra sheets** from the workbook before uploading.
4. Re-upload the corrected index file with only the required 2 sheets.
5. Verify synchronization status after re-upload.
**Prerequisites:** Buyer must have CMS enabled (which is typical for PunchOut with index files).
**Notes:** Extra sheets (even blank ones) will prevent synchronization. Always validate the file structure before upload.

---

### TPS-006 | Category: CSV / Service Entry Sheet
**Problem:** Integration Specialist needs to check CSV Service Entry Sheet (SES) specification/field details for a buyer, but cannot download the specification from SBN directly.
**Resolution:**
1. The CSV SES specification file can be downloaded via the **Customization Admin** site.
2. **Prerequisites:** VPN must be connected.
3. Steps:
   - Login to `https://service.ariba.com/CustomizationAdmin.aw/ad/login/SSOActions` with admin credentials
   - Enter the Buyer's ANID and click "Search"
   - Find the required resource and click "Edit"
   - Scroll down to the **"Localization"** section
   - Click **"Download"** to retrieve the specification file
**Prerequisites:** VPN connection required. Admin access to Customization Admin site required.
**Notes:** This is not available through the standard SBN portal interface. Only accessible via the internal admin tool.

---

### TPS-007 | Category: Supplier Account
**Problem:** Supplier user cannot access the "Remittances" tab within the SAP Business Network portal.
**Resolution:**
1. The issue is a **role/permission configuration** problem on the supplier's account.
2. Check which role the user is assigned to (e.g., "Credit" role).
3. The assigned role may not have **payment activities** enabled.
4. Fix options:
   - **Option A:** Supplier AN Admin updates the role to include payment/remittance permissions.
   - **Option B:** Reassign the user to a different role that already has the correct permissions (e.g., a role with Payments activities enabled).
5. The Supplier AN Admin performs this change in: Administration → Users → select user → modify role assignments.
**Prerequisites:** Supplier AN Admin access required to modify roles.
**Notes:** The "Credit" role by default does not include payment activities. This is a common oversight during initial account setup.

---

### TPS-008 | Category: Integration / Routing
**Problem:** Buyer sends orders from multiple ERP systems to the same supplier. Some ERPs are not in the integration scope, causing non-integrated POs to flow through the integrated channel incorrectly.
**Resolution:**
1. The supplier needs to set up **multiple exception routings** in their SBN account.
2. Use the **ERP System ID** (sent in the PO header) to identify which system the PO originated from.
3. Configure exception routing rules that match the non-integrated ERP identifiers and route those POs to **manual/portal processing** instead of the integration channel.
4. Steps:
   - Identify the System IDs for non-integrated ERPs (obtain from buyer)
   - Go to Administration → Configuration → Routing Rules → Exception Routing
   - Create a rule per non-integrated ERP System ID
   - Set the routing destination to "Online" (portal) for those rules
5. Test by having the buyer send a PO from a non-integrated ERP and verify it arrives in the portal inbox (not the integration queue).
**Prerequisites:** Buyer must provide the ERP System IDs for non-integrated systems.
**Notes:** This is common for large buyers with multiple ERP landscapes (e.g., regional ERPs, acquired company systems). The System ID is visible in the PO header details.

---

## Quick Links

Useful internal and external resources for day-to-day enablement work.

| Resource | URL | Description |
|---|---|---|
| CIG Translation Documentation | https://workzone.one.int.sap/site#workzone-home&/groups/Y2NzP6jFYTpx4XWWRLG4g6/content?view_mode=list | How cXML is converted to/from various languages on the CIG |
| EDI Sandbox (SmartPost) | https://edisandbox.com/smartpost/ | For CIG/non-cXML posting and testing |
| SAP Cloud Service Status | https://www.sap.com/about/cloud-trust-center/cloud-service-status.html | Current availability and performance of SAP cloud services |
| CIG Config (Help Portal) | https://help.sap.com/docs/business-network-for-trading-partners/configuring-document-routing/configuring-your-sap-business-network-account-to-access-sap-integration-suite-managed-gateway-for-spend-management-and-sap-business-network | Managed Gateway configuration documentation |
| GITP (Help Portal) | https://help.sap.com/docs/business-network-for-trading-partners/guided-integration-for-trading-partners-59ee04ae427245dfbb7d2766c14270b4/guided-integration-for-trading-partners | Guided Integration for Trading Partners |
| PIDX Note | N/A | PIDX requires DUNS Number to be sent back for translation |

---

## Adding New Entries

When a user says "add this to the repository", the assistant will:
1. Extract the problem and solution from the conversation
2. **Sanitize:** Remove all customer/supplier names, ANIDs, ticket numbers, and staff names
3. **Categorize:** Assign to an existing domain category (Catalog, Integration, Invoicing, Order Management, CSV Invoice, Supplier Account, etc.)
4. **Assign ID:** Next sequential TPS-XXX number
5. **Append:** Add the new entry to this file via skill update
