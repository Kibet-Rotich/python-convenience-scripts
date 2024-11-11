import os
from PyPDF2 import PdfMerger

# Directory where the downloaded PDFs are stored
pdf_directory = "book"  # Modify this if your PDFs are in a different directory

# Output file name for the merged PDF
output_pdf = "merged_chapters.pdf"

# Initialize the PdfMerger object
merger = PdfMerger()

# Loop through the PDF files in the directory and merge them
for file in sorted(os.listdir(pdf_directory)):
    if file.endswith(".pdf"):
        file_path = os.path.join(pdf_directory, file)
        merger.append(file_path)
        print(f"Merging: {file}")

# Write out the merged PDF
with open(output_pdf, "wb") as output_file:
    merger.write(output_file)

# Close the merger object
merger.close()

print(f"Merged PDF saved as {output_pdf}")
