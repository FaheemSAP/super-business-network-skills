#!/usr/bin/env python3
"""
cXML Anonymizer Script
======================
Anonymizes cXML documents for safe Test Central use.

Usage:
    python anonymize_cxml.py --input <file_or_dir> --output <output_dir>

Dependencies:
    pip install lxml defusedxml
"""
import argparse
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    from lxml import etree
except ImportError:
    sys.exit("ERROR: lxml required. pip install lxml")
try:
    import defusedxml.ElementTree as defused_et
except ImportError:
    sys.exit("ERROR: defusedxml required. pip install defusedxml")

PRESERVE_EXTRINSIC_NAMES = {
    "extLineNumber", "materialStorageLocation", "warehouseStorageLocationNo",
    "incoTerm", "incoTermDesc", "incoTermLocation", "CompanyCode",
    "PurchaseGroup", "PurchaseOrganization", "Ariba.invoicingAllowed",
    "AribaNetwork.PaymentTermsExplanation", "transactionCategoryOrType",
    "invoiceSourceDocument", "invoiceType",
}

EXTRINSIC_MAP = {
    "supplierVatID": "ANON-VAT-SUP-001", "buyerVatID": "ANON-VAT-BUY-001",
    "taxID": "ANON-TAX-001", "abn": "00000000000", "gst": "ANON-GST-001",
    "supplierID": "ANON-SUP-0001", "buyerID": "ANON-BUY-0001",
    "vendorID": "ANON-VENDOR-0001", "customerId": "ANON-CUST-0001",
    "networkID": "ANON-NET-0001", "aribaNetworkID": "AN00000000000",
    "userIdentification": "anon.user@example.com",
    "mailbox": "anon.mailbox@example.com",
    "contactName": "Anonymized Contact", "Requester": "Anonymized Requester",
    "orderID": "ANON-ORDER-0001", "invoiceID": "ANON-INV-0001",
    "contractID": "ANON-CONTRACT-0001", "purchaseRequisitionNo": "ANON-PR-0001",
    "agreementID": "ANON-AGREE-0001", "blanketOrderID": "ANON-BLANKET-0001",
    "costCenter": "ANON-CC-0001", "glAccount": "ANON-GL-0001",
    "wbsElement": "ANON-WBS-0001", "profitCenter": "ANON-PC-0001",
    "companyCode": "ANON-COMP-0001", "plantCode": "ANON-PLANT-0001",
    "note": "Anonymized note.", "comment": "Anonymized comment.",
    "description": "Anonymized description.",
}

REGION_PROFILES = {
    "AU": {"City": "Anonymized City", "State": "WA", "PostalCode": "6000", "Currency": "AUD", "Phone": "0891234567", "Country": "Australia", "iso": "AU"},
    "US": {"City": "Anonymized City", "State": "CA", "PostalCode": "90210", "Currency": "USD", "Phone": "555-555-5555", "Country": "United States", "iso": "US"},
    "DE": {"City": "Anonymized City", "State": "BE", "PostalCode": "10115", "Currency": "EUR", "Phone": "03012345678", "Country": "Germany", "iso": "DE"},
    "JP": {"City": "Chiyoda", "State": "Tokyo", "PostalCode": "100-0001", "Currency": "JPY", "Phone": "0312345678", "Country": "Japan", "iso": "JP"},
    "GB": {"City": "Anonymized City", "State": "London", "PostalCode": "SW1A 1AA", "Currency": "GBP", "Phone": "02012345678", "Country": "United Kingdom", "iso": "GB"},
}

CURRENCY_TO_COUNTRY = {"AUD": "AU", "USD": "US", "EUR": "DE", "JPY": "JP", "GBP": "GB", "SGD": "AU", "INR": "AU", "NZD": "AU", "CAD": "US", "BRL": "AU"}
DEFAULT_REGION = "AU"
STATIC_TIMESTAMP = "2026-01-01T14:53:00-07:00"
CXML_VERSION = "1.2.069"
DOCTYPE = f'<!DOCTYPE cXML SYSTEM "http://xml.cxml.org/schemas/cXML/{CXML_VERSION}/cXML.dtd">'

def detect_region(root):
    countries = [el.get("isoCountryCode") for el in root.iter() if el.get("isoCountryCode")]
    if countries:
        from collections import Counter
        most_common = Counter(countries).most_common(1)[0][0]
        if most_common in REGION_PROFILES:
            return most_common
    for money in root.iter("Money"):
        curr = money.get("currency", "")
        if curr in CURRENCY_TO_COUNTRY:
            return CURRENCY_TO_COUNTRY[curr]
    return DEFAULT_REGION

def detect_doc_type(root):
    if root.find(".//OrderRequest") is not None:
        order = root.find(".//OrderRequestHeader")
        if order is not None:
            t = order.get("type", "new")
            if t == "delete": return "Cancel PO"
            if t == "update" or int(order.get("orderVersion", "1")) > 1: return "Change PO"
        return "New PO"
    if root.find(".//ConfirmationRequest") is not None: return "Order Confirmation"
    if root.find(".//ShipNoticeRequest") is not None: return "Ship Notice"
    if root.find(".//InvoiceDetailRequest") is not None: return "Invoice"
    return "Unknown"

def anonymize_extrinsics(root):
    count = 0
    for ext in root.iter("Extrinsic"):
        name = ext.get("name", "")
        if name in PRESERVE_EXTRINSIC_NAMES:
            continue
        if name in EXTRINSIC_MAP:
            ext.text = EXTRINSIC_MAP[name]
            count += 1
    return count

def anonymize_header(root):
    cxml = root if root.tag == "cXML" else root.find(".//cXML")
    if cxml is not None:
        cxml.set("payloadID", "#PAYLOADID#")
        cxml.set("timestamp", STATIC_TIMESTAMP)
    for cred in root.iter("Credential"):
        identity = cred.find("Identity")
        if identity is not None:
            if cred.getparent().tag == "From": identity.text = "#SENDERID#"
            elif cred.getparent().tag == "To": identity.text = "#RECEIVERID#"
        secret = cred.find("SharedSecret")
        if secret is not None: secret.text = "ANONYMIZED"

def anonymize_addresses(root, profile):
    for addr in root.iter("Address"):
        for el in addr.iter():
            tag = el.tag if isinstance(el.tag, str) else ""
            if tag == "Street": el.text = "123 Anonymized Street"
            elif tag == "City": el.text = profile["City"]
            elif tag == "State": el.text = profile["State"]
            elif tag == "PostalCode": el.text = profile["PostalCode"]
            elif tag == "Country":
                el.text = profile["Country"]
                el.set("isoCountryCode", profile["iso"])

def anonymize_contacts(root):
    for contact in root.iter("Contact"):
        name = contact.find("Name")
        if name is not None: name.text = "Anonymized Contact"
        for email in contact.iter("Email"): email.text = "anon@example.com"
        for phone in contact.iter("Phone"):
            num = phone.find(".//TelephoneNumber/number")
            if num is not None: num.text = "0000000000"

def process_file(input_path, output_dir):
    content = input_path.read_bytes()
    if not (content.lstrip()[:5] in (b"<?xml", b"<cXML")):
        print(f"SKIP (not cXML): {input_path.name}")
        return
    try:
        defused_et.fromstring(content)
    except Exception as e:
        print(f"SECURITY REJECT: {input_path.name}: {e}")
        return
    parser = etree.XMLParser(resolve_entities=False, no_network=True, load_dtd=False, huge_tree=False)
    root = etree.fromstring(content, parser=parser)
    region = detect_region(root)
    doc_type = detect_doc_type(root)
    profile = REGION_PROFILES.get(region, REGION_PROFILES[DEFAULT_REGION])
    anonymize_header(root)
    count = anonymize_extrinsics(root)
    anonymize_addresses(root, profile)
    anonymize_contacts(root)
    output = etree.tostring(root, xml_declaration=True, encoding="UTF-8", pretty_print=True).decode()
    output = f'{DOCTYPE}\n{output}'
    out_path = Path(output_dir) / f"anon_{input_path.name}"
    out_path.write_text(output, encoding="utf-8")
    print(f"OK: {input_path.name} → {out_path.name} | Region: {region} | Type: {doc_type} | Substitutions: {count}")

def main():
    ap = argparse.ArgumentParser(description="Anonymize cXML documents")
    ap.add_argument("--input", required=True, help="Input file or directory")
    ap.add_argument("--output", required=True, help="Output directory")
    args = ap.parse_args()
    os.makedirs(args.output, exist_ok=True)
    inp = Path(args.input)
    if inp.is_file():
        process_file(inp, args.output)
    elif inp.is_dir():
        files = list(inp.glob("*.xml")) + list(inp.glob("*.cxml"))
        if len(files) > 50:
            sys.exit(f"ERROR: Max 50 files, found {len(files)}")
        for f in files:
            if f.stat().st_size > 10 * 1024 * 1024:
                print(f"SKIP (>10MB): {f.name}")
                continue
            process_file(f, args.output)
    else:
        sys.exit(f"ERROR: {args.input} not found")

if __name__ == "__main__":
    main()
