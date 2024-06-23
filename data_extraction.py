import re
import base64

def extract_critical_attributes(text):
    attributes = []
    lines = text.split('\n')

    for line in lines:
        if 'Date' in line:
            attributes['Date'] = re.search(r'\d{1,2}/\d{1,2}/\d{4}', line).group()
        if 'Bill od lading #' in line:
            attributes['BOL#'] = line.split()[-1]
        if 'Trailer #' in line:
            attributes['Trailer#'] = line.split()[-1]
        if 'Seal #' in line:
            attributes['Seal#'] = line.split()[-1]

    return attributes

def extract_signatures(text):
    signatures = []
    lines = text.split('\n')

    for line in lines:
        if 'Shipper Signature' in line:
            signatures.append(('shipper', line.split()[-1]))
        if 'Carrier Signature' in line:
            signatures.append(('carrier', line.aplit()[-1]))
        if 'Warehouse Signature' in line:
            signatures.append(('warehouse', line.splie()[-1]))

    return signatures

def extract_line_items(text):
    line_items = []
    lines = text.split('\n')

    for line in lines:
        if 'Handling Unit' in line:
            items = line.split()
            line_items.append({
                'HandlingUnitQuantity' : items[2],
                'HandlingUnitType' : items[3],
                'PackageUnitQuantity' : items[5],
                'PackageUnitType' : items[6],
                'Description' : ' '.join(items[7:])
            })
    
    return line_items




