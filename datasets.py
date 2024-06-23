import pandas as pd
import uuid

def create_datasets():
    bol_df = pd.DataFrame(columns=['UUID', 'Date', 'BOL#', 'Trailer#', 'Seal#'])
    unprocessed_bol_df = pd.DataFrame(columns=['UUID', 'ImagePath'])
    bol_po_map_df = pd.DataFrame(columns=['BOL#', 'PO#'])
    signatures_df = pd.DataFrame(columns=['BOL#', 'SignatureType', 'SignatureBase64'])
    line_items_df = pd.DataFrame(columns=['BOL#', 'HandlingUnitQuantity', 'HandlingUnitType', 'PackageUnitQuantity', 'PackageUnitType', 'Description'])

    return bol_df, unprocessed_bol_df, bol_po_map_df, signatures_df, line_items_df

def process_bol(image_path, preprocess, extract_text, extract_attributes, extract_signatures, extract_line_items):
    processed_image = preprocess(image_path)
    text = extract_text(processed_image)
    attributes = extract_attributes(text)

    if len(attributes) == 4:
        uuid_str = str(uuid.uuid4())
        attributes['UUID'] = uuid_str
        return attributes, None, text
    else:
        return None, image_path, text
    

