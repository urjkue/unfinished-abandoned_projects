import os
import shutil
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

# Function to find the invoice number and total in the extracted text using regular expressions
def find_invoice_and_total(text):
    invoice_number = ""
    total = ""

    # Customize these regular expressions to match the invoice number and total patterns on your receipt
    invoice_number_patterns = [
        r"Invoice No:\s*(\d+)",
        r"Invoice #:\s*(\d+)",
        r"Invoice Number:\s*(\d+)"
    ]
    total_patterns = [
        r"Total\s*[$](\d+([.,]\d{2})?)",
        r"Deposit Due\s*[$](\d+([.,]\d{2})?)"
    ]

    for pattern in invoice_number_patterns:
        invoice_number_match = re.search(pattern, text, re.IGNORECASE)
        if invoice_number_match:
            invoice_number = invoice_number_match.group(1).strip()
            break

    for pattern in total_patterns:
        total_match = re.search(pattern, text, re.IGNORECASE)
        if total_match:
            total = total_match.group(1).strip().replace(',', '.')
            break

    return invoice_number, total

if __name__ == "__main__":
    try:
        # Get the current working directory
        current_directory = os.getcwd()

        # Replace 'try_folder' with the name of the folder containing the images you want to process
        source_folder = os.path.join(current_directory, "try_folder")

        # Check if the source folder exists
        if os.path.exists(source_folder):
            # Create a new Excel workbook to store the invoice information
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.title = "Invoice Info"
            sheet["A1"] = "Invoice Number"
            sheet["B1"] = "Total"

            # Get the list of all files in the source folder
            files = os.listdir(source_folder)

            for file in files:
                # Check if the file is an image (you can customize this check based on your image extensions)
                if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
                    source_path = os.path.join(source_folder, file)
                    text = extract_text_from_image(source_path)
                    invoice_number, total = find_invoice_and_total(text)
                    print(f"Processing {file}: Invoice Number: {invoice_number}, Total: {total}")

                    # Append the invoice information to the Excel sheet
                    sheet.append([invoice_number, total])

            # Save the Excel workbook
            workbook.save("check.xlsx")
            print("Invoice information saved to 'check.xlsx' successfully.")
        else:
            print("Source folder not found. Please provide a valid path to the source folder.")
    except Exception as e:
        print("Error:", str(e))
