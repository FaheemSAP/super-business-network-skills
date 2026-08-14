# Messaging on SAP Business Network — Reference

Inbox, outbox, message types, automated responses, and notification management.

**Official SAP Source (v2605):**
- [Messaging on SAP Business Network](https://help.sap.com/docs/ARIBA_NETWORK_SUPPLIERS/3bb5a70f1418416db4ebbecf9c55c6ec?locale=en-US&state=PRODUCTION&version=2605)

## 1. Inbox and Outbox Overview

| Area | Contents |
|---|---|
| Inbox | Incoming: POs, PO Changes, Cancellations, GRN/RECADV, Remittance Advice, buyer messages |
| Outbox | Outgoing: Order Confirmations, ASNs, Invoices, Credit Memos, supplier messages |
| Pending | Documents requiring action (e.g. awaiting OC submission) |
| Archive | Processed documents; searchable |

## 2. Message Types

### Transactional Messages
Automatically generated as part of document exchange:
- Purchase Order receipt notification
- Invoice status change (approved, rejected, disputed)
- PO change or cancellation alert
- Goods receipt confirmation
- Payment remittance notification

### Manual Messages (Buyer-Supplier Chat)
- Direct messaging between buyer and supplier within SBN
- Attached to a specific document (PO, Invoice) or standalone
- Supports file attachments
- Triggered from: document detail view → "Send Message"

### System Notifications
- Account security alerts (login from new device, password change)
- Account expiry warnings
- Integration errors (cXML delivery failures)
- Catalog processing results

## 3. Notification Rules

Configure which events trigger email notifications and to which recipients.

**Configuring Notifications (Supplier):** Settings → Notifications → configure per event type:
- New PO received
- PO change received
- PO cancellation received
- Invoice approved / rejected / disputed
- GRN received
- Catalog processing result
- Message received from customer

**Notification Recipients:** Primary admin email (always notified) + additional contacts per event type and per customer relationship. Useful for routing: POs → procurement team; Invoices → accounts receivable.

## 4. Automated Responses

**Auto-Accept Order Confirmations:** Buyers can configure rules to automatically send an OC (accept) without supplier action. Supplier should check if this is active for a buyer relationship.

**Auto-Routing Rules:** Suppliers can configure rules to automatically forward incoming documents to backend system (cXML endpoint), email, or EDI channel. See `references/account-management.md` §6.

## 5. Document Status Visibility
From Inbox/Outbox: current document status, processing history, rejection/error reasons, related documents (PO → OC → ASN → Invoice chain).

## 6. Search and Filtering
- Search by: document number, buyer name, date range, document type, status
- Advanced filters: amount range, currency, country
- Export search results to CSV

## 7. Message Retention and Archive
- Active documents: last 2 years visible in Inbox/Outbox
- Archived documents: searchable; download available
- For full audit: use Reports (→ `references/reports.md`)

## 8. Builder Playbook
- Inbox/Outbox orientation: §1 table
- Notification setup: §3 configuration steps
- Troubleshoot missing PO notification: §3 + check routing rules in account-management.md
- Message a buyer: §2 Manual Messages
- Document status: §5