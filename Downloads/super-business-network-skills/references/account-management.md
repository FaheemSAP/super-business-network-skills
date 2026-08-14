# Account & Registration Management — Reference

Supplier and buyer registration, user management, trading relationships, and document routing.

**Official SAP Sources (v2605):**
- [Registration and Signing In](https://help.sap.com/docs/ARIBA_NETWORK_SUPPLIERS/ddd75910f67b4212b1c83f9d68cd2f01?locale=en-US&state=PRODUCTION&version=2605)
- [Managing your SAP Business Network](https://help.sap.com/docs/ARIBA_NETWORK_SUPPLIERS/c70a4dca49734ac9b09d11122a3b480f?locale=en-US&state=PRODUCTION&version=2605)
- [Collaborating with Customers](https://help.sap.com/docs/ARIBA_NETWORK_SUPPLIERS/109c7a9f53c54578bf305482e13b6cb6?locale=en-US&state=PRODUCTION&version=2605)
- [Configuring Document Routing](https://help.sap.com/docs/ARIBA_NETWORK_SUPPLIERS/76c114b292d84c379d1626cff721acec?locale=en-US&state=PRODUCTION&version=2605)
- [Using Test Accounts on SAP Business Network](https://help.sap.com/docs/ARIBA_NETWORK_SUPPLIERS/876817adf14d498799ddd906fff3e2e7?locale=en-US&state=PRODUCTION&version=2605)

## 1. Registration Process

### New Supplier Registration
1. Buyer sends TRR (Trading Relationship Request) → supplier receives email invitation
2. Supplier clicks link → SAP Business Network registration page
3. Choose account type: **Enterprise** (paid, full features) or **Standard/Free** (portal-based)
4. Enter company details: legal name, address, tax ID, DUNS (optional)
5. Create admin user: name, email, password
6. Accept terms and conditions
7. ANID assigned: `AN` + 11 digits (test: `-T` suffix)
8. Complete company profile: banking, certifications, payment preferences

### Existing Supplier with ANID
1. Buyer sends TRR
2. Supplier logs in → Customers → Pending Invitations → Accept
3. Configure customer-specific settings

## 2. Account Types

| Feature | Standard (Free) | Enterprise |
|---|---|---|
| Portal access | Yes | Yes |
| Integration (cXML/EDI) | No | Yes |
| Multiple users | Limited | Unlimited |
| Catalog upload | Limited | Yes |
| SCC / supply chain | No | Yes |
| Annual fee | No | Yes (by transaction volume) |

## 3. User Roles and Permissions

| Role | Capabilities |
|---|---|
| Administrator | Full account management, user creation, settings |
| Catalog Manager | Upload, edit, publish catalogs |
| Order Manager | View and process orders |
| Invoice Manager | Create and manage invoices |
| Integration Manager | Configure Managed Gateway, cXML channels |
| Report User | View and run reports |
| Sourcing Participant | Respond to sourcing events |

Admin creates users: Settings → Users → Create User. Assign roles per user; multiple roles allowed.

## 4. Account Linking and Consolidation

- **Multiple ANIDs:** A company may have multiple ANIDs (one per country/subsidiary)
- **Account Consolidation:** Merge subsidiaries under a parent ANID (requires SAP support)
- **Account Switch:** Users can belong to multiple ANIDs and switch context
- **Buyer-Specific Settings:** Per buyer relationship — routing preferences, notification contacts, invoice config, currency

## 5. Trading Relationship Request (TRR)

**Flow:** Buyer initiates TRR → Supplier receives email → Supplier registers or accepts → Relationship established → Buyer appears in Customers section.

| TRR Status | Meaning |
|---|---|
| Pending | Supplier has not responded |
| Active | Relationship established |
| Inactive | Relationship suspended |
| Rejected | Supplier declined |

## 6. Document Routing Configuration

Determines how SBN delivers documents to the supplier's backend.

| Method | Best For |
|---|---|
| Online (Portal) | Low-volume, manual processing |
| cXML HTTP | Medium-to-high volume, ERP integration |
| EDI via Managed Gateway | High-volume, legacy EDI systems |
| Email (PDF) | Non-integrated buyers/suppliers |

**Configuring Routing (Supplier):**
1. Settings → Electronic Order Routing
2. Choose routing method per document type (PO, PO Change, PO Cancel)
3. Enter endpoint URL (for cXML/EDI) or email address
4. Test with a sample document

**Routing Priority:** Customer-specific rule → Document-type rule → Default rule.

## 7. Test Accounts

Test accounts (`-T` suffix ANID) are used for UAT and integration testing.

**Creating a Test Account:**
1. Log in to production SBN account
2. Settings → Company Settings → Test Account → Create
3. Test ANID (e.g. AN1234567890-T) generated automatically

**Test Account Rules:**
- Can only transact with buyer test accounts
- Documents are not real transactions
- Test Central requires supplier test ANID — see `references/integration-hub.md` §6

## 8. Two-Factor Authentication (2FA)
Recommended for all administrator accounts. Options: SMS or authenticator app. Admin enables: Settings → Account Security → Two-Factor Authentication.

## 9. Profile Completeness
SBN displays a profile completeness score. Higher scores improve buyer discoverability via SBN Discovery. Complete: company profile, certifications, banking, product/service categories.

## 10. Builder Playbook
- New registration: §1 step-by-step
- Account types: §2 comparison
- User setup: §3 roles table
- TRR status: §5
- Routing config: §6 with method table
- Test account: §7 + integration-hub.md §6