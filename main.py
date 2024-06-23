import os
from preprocess import preprocess_image
from ocr_extraction import extract_text_from_image
from data_extraction import extract_critical_attributes, extract_signatures, extract_line_items
from datasets import create_datasets, process_bol
import base64
import sys

def main(image_paths):
    bol_df, unprocessed_bol_df, bol_po_map_df, signatures_df, line_items_df = create_datasets()

    for image_path in image_paths:
        attributes, unprocessed, text = process_bol(
            image_path, preprocess_image,
            extract_text_from_image,
            extract_critical_attributes,
            extract_signatures,
            extract_line_items
        ) 
        if attributes:
            bol_df = bol_df.append(attributes, ignore_index=True)
            signatures = extract_signatures(text)
            for signature_type, signature in signatures:
                signature_base64 = base64.b64encode(signature.encode()).decode()
                signatures_df = signatures_df.append({'BOL#' : attributes['BOL#'], 'SignatureType': signature_type, 'SingatureBase64': signature_base64}, ignore_index=True)

            line_items = extract_line_items(text)
            for item in line_items:
                item['BOL#'] = attributes['BOL#']
                line_items_df = line_items_df.append(item, ignore_index=True)
        else:
            unprocessed_bol_df = unprocessed_bol_df.append({'UUID': str(uuid.uuid4()), 'ImagePath': unprocessed}, ignore_index=True)

    bol_df.to_csv('BillOfLandings.csv', index=False)
    unprocessed_bol_df.to_csv('BillOfLandingUnprocessed.csv', 
                              index=False)
    bol_po_map_df.to_csv('BillOfLandingPOMaps.csv', index=False)
    signatures_df.to_csv('BillOfLandingSingatures.csv', index=False)
    line_items_df.to_csv('BillOfLandingItems.csv', index=False)

if __name__ == '__main__':
    in_image_paths = sys.argv[1]

    image_paths = in_image_paths.split(" ")
    print(image_paths)
    # main(image_paths)

