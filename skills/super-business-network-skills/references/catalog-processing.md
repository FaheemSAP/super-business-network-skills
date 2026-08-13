# Catalog Processing — Reference

25+1 validation rules, format conversion, cXML generation, Ariba status codes.

## 1. Workflow
Upload → Validate → Convert → Download. Extensions: .xlsx, .xls, .cif, .csv, .txt, .zip.

Outputs: CIF_TEXT (.cif), XLS_FILE (.xls), CMS_XLSX_FILE (.xlsx), CXML_FILE (.mime).

## 2. Validation rules (25+1)

### Header rules
| ruleCode | Severity | Message |
|---|---|---|
| LOADMODE_VALID | ERROR | Must be F or I |
| UNUOM_VALID | ERROR | Must be TRUE or FALSE |
| CURRENCY_VALID | ERROR | Not valid ISO 4217 |
| ITEMCOUNT_MATCH | WARNING | Doesn't match rows |

### Required fields (ERROR)
SUPPLIER_ID_REQUIRED, PART_ID_REQUIRED, DESCRIPTION_REQUIRED, UNSPSC_REQUIRED (skip CMS), PRICE_REQUIRED (skip isPartial), UOM_REQUIRED.

### Format & pricing
| ruleCode | Severity |
|---|---|
| UNSPSC_FORMAT | ERROR/WARNING |
| PRICE_POSITIVE | ERROR |
| ZERO_PRICE | WARNING |
| PRICE_MINIMUM | ERROR |
| PRICE_NUMERIC | ERROR |
| MARKET_PRICE_VALID | ERROR/WARNING |
| PRICE_UNIT_QUANTITY_VALID | ERROR |
| UNIT_CONVERSION_VALID | ERROR |

### Data quality
LEAD_TIME_POSINT (ERROR), DATE_FORMAT (ERROR), DATE_RANGE (WARNING), CURRENCY_PER_ITEM (ERROR), UOM_CODE (WARNING), URL_FORMAT (ERROR), DESCRIPTION_CHARS (WARNING), TERRITORY_LANGUAGE (WARNING).

### Length (ERROR)
SUPPLIER_ID_LENGTH (>255), PART_ID_LENGTH (>255), DESCRIPTION_LENGTH (>2000), SHORT_NAME_LENGTH (>80).

### Business
DUPLICATE_PART_ID (WARNING), RELATED_ITEM_TYPE (ERROR), PUNCHOUT_LEVEL (WARNING).

### File size
FILE_SIZE_ERROR (>10MB), FILE_SIZE_WARN (>3MB auto-zip).

### CMS-only
CMS_CLASSIFICATION_REQUIRED (ERROR), CMS_UNSPSC_RECOMMENDED (WARNING).

## 3. Size limits
10 MB hard, 3 MB auto-zip, 50,000 max items.

## 4. CIF 3.0 generation
Header order: CIF_I_V3.0, CHARSET, CODEFORMAT, LOADMODE, SUPPLIERID_DOMAIN, CURRENCY, UNUOM, ITEMCOUNT, TIMESTAMP, COMMENTS, FIELDNAMES, DATA, ENDOFDATA.

23-column CIF_FIELD_ORDER: SupplierID, SupplierPartID, SupplierPartAuxiliaryID, ItemDescription, UnitOfMeasure, ClassificationCodes, UnitPrice, Currency, MarketPrice, LeadTime, ManufacturerPartID, ManufacturerName, SupplierURL, ManufacturerURL, PriceUnitQuantity, UnitConversion, ShortName, Keywords, TerritoryAvailable, Language, StartDate, EndDate, PunchOutEnabled.

Formula-injection: prefix `= + - @ \t` cells with `'`. Auto-zip above 3 MB.

## 5. cXML CatalogUploadRequest (MIME)
Multipart/related. payloadID, boundary, UserAgent, NetworkID credential, operation="update", Part 1 text/xml, Part 2 cif/zip. DTD: `http://xml.cXML.org/schemas/cXML/1.2.069/cXML.dtd`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE cXML SYSTEM "http://xml.cXML.org/schemas/cXML/1.2.069/cXML.dtd">
<cXML payloadID="{id}" timestamp="{ISO}" xml:lang="en-US">
  <Header>
    <From><Credential domain="NetworkID"><Identity>{supplierANID}</Identity></Credential></From>
    <To><Credential domain="NetworkID"><Identity>{buyerANID}</Identity></Credential></To>
    <Sender><Credential domain="NetworkID"><Identity>{supplierANID}</Identity><SharedSecret>{secret}</SharedSecret></Credential><UserAgent>Catalog Processing Tool/2.0</UserAgent></Sender>
  </Header>
  <Request><CatalogUploadRequest operation="update"><CatalogName xml:lang="en">{name}</CatalogName></CatalogUploadRequest></Request>
</cXML>
```

## 6. Ariba status codes
| Code | Meaning | Severity |
|---|---|---|
| 200 | Success | success |
| 201 | Accepted | processing |
| 461–470, 499 | Various errors | fatal |
| 561–564 | Rate/maintenance | retryable |

Key fatals: 461 (Bad UNSPSC), 463 (Bad format), 468 (Too large), 469 (Bad extension), 470 (Has errors).

## 7. Builder playbooks
- Validate: Apply rules, report ruleCode/severity/message/fix
- Generate CIF: Header per §4, 23 columns
- Generate cXML MIME: Per §5
- Convert CIF↔Excel: Parse/write with openpyxl
- Status codes: Map per §6, advise action