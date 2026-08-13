# cXML Anonymizer — Reference

Prepares cXML PO examples as reusable Test Central templates. Goal: show structure, not real data. Deps: lxml, defusedxml.

## 0. File Naming Convention
Save anonymized file as: **[Buyer] [Region] [PO Type]** in a central location — you will need to copy/paste the edited cXML to multiple Test Case locations.

## 1. Detection
Doc types: OrderRequest → ConfirmationRequest → ShipNoticeRequest → InvoiceDetailRequest.
PO subtypes: delete→Cancel, update→Change, orderVersion>1→Change, else→New.
Order types: regular, release, blanket, stockTransport.

## 2. Region Detection
Priority: isoCountryCode → Currency → Country text → Fallback AU/APAC.
Regions: APAC(AU), NAMAR(US), EMEA(DE), Japan(JP), LATAM(BR).
Profiles: AU(WA/6000/AUD), US(CA/90210/USD), DE(BE/10115/EUR), JP(Tokyo/100-0001/JPY), GB(London/SW1A 1AA/GBP).

## 3. Standard Header Template
Replace the full cXML header block with the following:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE cXML SYSTEM "http://xml.cxml.org/schemas/cXML/1.2.044/cXML.dtd">
<cXML payloadID="#PAYLOADID#" timestamp="2020-10-13T14:53:00-07:00" version="1.2.044" xml:lang="en-US">
<Header>
  <From><Credential domain="NetworkId"><Identity>#SENDERID#</Identity></Credential></From>
  <To><Credential domain="NetworkId"><Identity>#RECEIVERID#</Identity></Credential></To>
  <Sender><Credential domain="NetworkID"><Identity>#PROVIDERID#</Identity></Credential>
    <UserAgent>Ariba SN</UserAgent></Sender>
</Header>
<Request deploymentMode="test">
  <OrderRequest>
    <OrderRequestHeader orderDate="#DATETIME#" orderID="#DOCUMENTID#" orderType="regular" orderVersion="1" type="new">
```

## 4. Replacement Token Reference

| Element / Attribute | Replacement |
|---------------------|-------------|
| `payloadID` | `#PAYLOADID#` |
| `<From><Identity>` | `#SENDERID#` |
| `<To><Identity>` | `#RECEIVERID#` |
| `<Sender><Identity>` | `#PROVIDERID#` |
| `deploymentMode` | `"test"` |
| `orderDate` | `#DATETIME#` |
| `orderID` | `#DOCUMENTID#` |

## 5. What to Remove or Replace

**Replace with tokens:** Payload IDs, Sender/Receiver/Provider IDs, orderDate, orderID.

**Replace with standard values:**
- `<ShipFrom>` and `<RemitTo>` → `Supplier Name, Supplier Address, PA, US 15212`
- Supplier name → generic supplier name
- Supplier product details → generic name (e.g. "Argos Water Filter" → "Water Filter")
- Unit price → `1.00`; Quantity → `100`
- `deploymentMode="production"` → `"test"`

**Delete entirely:** For Change PO and Cancel PO — delete the `<DocumentReference>` line entirely.

**Key rule:** If the value identifies a real supplier or changes every PO → remove it. If it defines structure or behaviour → keep it.

## 6. What to Keep
- Buyer identifiers (buyer IDs can remain)
- XML structure: line-item hierarchy, required fields, order type logic
- `<ShipTo>` / `<BillTo>` (buyer-side addresses)
- Tax, UoM, classification, orderVersion, type
- Reusable placeholder tokens

## 7. Date Rules

| Element | Rule |
|---------|------|
| `orderDate` | `#DATETIME#` |
| `requestedDeliveryDate` | Year +100 of current year |
| `<effectiveDate>` (blanket/service POs) | Date prior to current day |
| `<expirationDate>` (blanket/service POs) | Year +100 of current year |
| `<Extrinsic name="ServicePeriod">` | Year +100 of current year |
| `<Period endDate>` | Year +100 of current year |
| `<Period startDate>` | Today's date |

## 8. Order-type Handling

- **blanket**: parentAgreementID→`#PARENT_AGREEMENTID#`, effectiveDate→yesterday, expirationDate→+100y
- **release**: agreementID→`#AGREEMENTID#`
- **Change PO**: Keep orderVersion and type; **delete** `<DocumentReference>` line entirely
- **Cancel PO**: Keep orderVersion and type; **delete** `<DocumentReference>` line entirely

## 9. Preserved Extrinsics (14)
extLineNumber, materialStorageLocation, warehouseStorageLocationNo, incoTerm, incoTermDesc, incoTermLocation, CompanyCode, PurchaseGroup, PurchaseOrganization, Ariba.invoicingAllowed, AribaNetwork.PaymentTermsExplanation, transactionCategoryOrType, invoiceSourceDocument, invoiceType.

## 10. Security
defusedxml gate, hardened lxml (resolve_entities=False, no_network=True, load_dtd=False, huge_tree=False). Limits: 50 files, 10MB/file, 50MB total.

## 11. Processing Pipeline
Security → Parse → Detect region → Profile → Pre-scan → Header → Change/Cancel → Extrinsics → Addresses → Contacts → Suppliers → Items → IDs → Serialize.

## 12. Builder Playbook
1. Detect doc/PO/order type
2. Detect region, pick profile
3. Replace header block with standard template (§3)
4. Walk extrinsics: keep 14 preserved, replace mapped keys
5. Apply order-type attributes and date rules (§7, §8)
6. Standardise unit prices → `1.00`, quantities → `100`
7. Replace all `<ShipFrom>` and `<RemitTo>` content
8. Genericise supplier product names
9. For Change/Cancel POs: delete `<DocumentReference>` line entirely
10. Verify `deploymentMode="test"`, serialize output

## 13. Extending to Other Document Types

| Document Type | Root Element | Key IDs to Tokenise |
|---|---|---|
| Order Confirmation | ConfirmationRequest | confirmationID → `#DOCUMENTID#` |
| Advanced Ship Notice | ShipNoticeRequest | shipmentID → `#SHIPMENTID#`, trackingNumber → `#TRACKINGNUMBER#` |
| Invoice | InvoiceDetailRequest | invoiceID → `#INVOICEID#`; remove financial/tax amounts; genericise line descriptions |

Apply the same header token replacements (§4) and security pipeline (§10) to all document types.