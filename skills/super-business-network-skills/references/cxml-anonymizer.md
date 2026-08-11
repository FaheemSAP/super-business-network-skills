# cXML Anonymizer — Reference

Anonymizes cXML for Test Central. Deps: lxml, defusedxml.

## 1. Detection
Doc types: OrderRequest → ConfirmationRequest → ShipNoticeRequest → InvoiceDetailRequest.
PO subtypes: delete→Cancel, update→Change, orderVersion>1→Change, else→New.
Order types: regular, release, blanket, stockTransport.

## 2. Region detection
Priority: isoCountryCode → Currency → Country text → Fallback AU/APAC.
Regions: APAC(AU), NAMAR(US), EMEA(DE), Japan(JP), LATAM(BR).
Profiles: AU(WA/6000/AUD), US(CA/90210/USD), DE(BE/10115/EUR), JP(Tokyo/100-0001/JPY), GB(London/SW1A 1AA/GBP).

## 3. Tokens
#PAYLOADID#, #SENDERID#, #RECEIVERID#, #PROVIDERID#, #DATETIME#, #DOCUMENTID#, #PREV_PAYLOADID#

## 4. Preserve vs anonymize
**14 preserved extrinsics:** extLineNumber, materialStorageLocation, warehouseStorageLocationNo, incoTerm, incoTermDesc, incoTermLocation, CompanyCode, PurchaseGroup, PurchaseOrganization, Ariba.invoicingAllowed, AribaNetwork.PaymentTermsExplanation, transactionCategoryOrType, invoiceSourceDocument, invoiceType.

**Also preserved:** XML structure, Money, ShipTo/BillTo, tax, UoM, classification, orderVersion, type.

**Anonymized:** PII, tax IDs, business IDs, procurement refs, addresses, financial codes, system IDs, free text, headers.

**Key map:** supplierVatID→ANON-VAT-SUP-001, abn→00000000000, supplierID→ANON-SUP-0001, orderID→ANON-ORDER-0001, costCenter→ANON-CC-0001, userIdentification→anon.user@example.com.

## 5. Order-type handling
- blanket: parentAgreementID→#PARENT_AGREEMENTID#, effectiveDate→yesterday, expirationDate→+100y
- release: agreementID→#AGREEMENTID#
- Change/Cancel: orderVersion kept, type kept, DocumentReference→#PREV_PAYLOADID#

## 6. Dates
Blanket effective→yesterday, expiration→+100y. requestedDeliveryDate→+100y. ServicePeriod start→today, end→+100y.

## 7. Security
defusedxml gate, hardened lxml (resolve_entities=False, no_network=True, load_dtd=False, huge_tree=False). Content sniff. Limits: 50 files, 10MB/file, 50MB total.

## 8. Pipeline
Security → Parse → Detect region → Profile → Pre-scan → Header → Change/Cancel → Extrinsics → Addresses → Contacts → Suppliers → Items → IDs → Serialize.

## 9. Builder playbook
1. Detect doc/PO/order type
2. Detect region, pick profile
3. Replace header with tokens
4. Walk extrinsics (keep 14, replace mapped)
5. Apply order-type attrs + dates
6. Stamp static timestamp/version