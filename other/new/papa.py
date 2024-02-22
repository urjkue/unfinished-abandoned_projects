import pytesseract
from PIL import Image
import openpyxl
import re

# Function to extract text from the image using Tesseract OCR
def extract_text_from_image(image_path):
    try:
        return pytesseract.image_to_string(Image.open(image_path), config='--oem 3 --psm 6')
    except Exception as e:
        print("Error while processing the image:", str(e))
        return ""

# Function to find the name, invoice number, and total in the extracted text using regular expressions
def find_info(text):
    name = ""
    invoice_number = ""
    total = ""

    # Customize these regular expressions to match the name, invoice number, and total patterns on your receipt
    name_pattern = r"Name:\s*(.*)"
    invoice_number_pattern = r"Invoice No:\s*(\d+)"
    total_pattern = r"Total\s*[$](\d+)"

    name_match = re.search(name_pattern, text, re.IGNORECASE)
    invoice_number_match = re.search(invoice_number_pattern, text, re.IGNORECASE)
    total_match = re.search(total_pattern, text, re.IGNORECASE)

    if name_match:
        name = name_match.group(1).strip()

    if invoice_number_match:
        invoice_number = invoice_number_match.group(1).strip()

    if total_match:
        total = total_match.group(1).strip()

    return name, invoice_number, total

# Function to save the name, invoice number, and total to an Excel file
def save_to_excel(file_path, name, invoice_number, total):
    try:
        workbook = openpyxl.Workbook()
        sheet = workbook.active

        sheet["A1"] = "Name"
        sheet["B1"] = "Invoice Number"
        sheet["C1"] = "Total"

        sheet.append([name, invoice_number, total])

        workbook.save(file_path)
        print("Data saved to Excel file successfully.")
    except Exception as e:
        print("Error while saving to Excel:", str(e))

if __name__ == "__main__":
    # Replace 'receipt_image.jpg' with the path to your receipt image
    image_path = "s.jpg"
    text = extract_text_from_image(image_path)

    print("Extracted Text:")
    print(text)

    name, invoice_number, total = find_info(text)

    print("Name:", name)
    print("Invoice Number:", invoice_number)
    print("Total:", total)

    # Replace 'output.xlsx' with the desired output Excel file path
    save_to_excel("output.xlsx", name, invoice_number, total)
