from docling.document_converter import DocumentConverter
import re
print("Working!")

def extract_transaction_from_pdf(pdf_path):
    converter = DocumentConverter()
    result = converter.convert(pdf_path)
    full_text = result.document.export_to_markdown()

    table_text = ""
    # if hasattr(result.document, 'tables'):
    #     for table in result.document.tables:
    #         table_text += str(table) + "\n"

    final_text = full_text + "\n" + table_text
    print(final_text)
    return final_text