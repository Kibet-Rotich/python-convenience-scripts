```markdown
# PDF Downloader and Merger

This repository contains two scripts: one for downloading PDF chapters from a specified URL and another for merging downloaded PDFs into a single document. These tools can be useful for compiling e-books, research papers, or any collection of PDFs from a series of URLs.

## Scripts

1. **PDF Downloader**: Downloads PDF files from a base URL for each specified chapter.
2. **PDF Merger**: Combines the downloaded PDF files into a single PDF document.

## Requirements

- **Python 3.7+**
- **Libraries**: Install required libraries using:
  ```bash
  pip install requests PyPDF2
  ```

## Usage

### PDF Downloader

The downloader script fetches PDF files for each chapter from a specified URL and saves them locally.

1. **Configure the URL and Save Directory**:
   - **Base URL**: Update `base_url` in the script to the URL where your PDFs are hosted.
   - **Save Directory**: Set `save_directory` to the folder where downloaded PDFs will be saved (e.g., `"book"`). Ensure this folder exists or create it before running the script.

2. **Run the Downloader Script**:
   ```bash
   python download_pdfs.py
   ```

   - This will download PDFs from `base_url`, naming them sequentially as `chapter_11.pdf`, `chapter_12.pdf`, etc., and save them in the `book` directory.

### PDF Merger

The merger script combines all PDFs in a specified directory into a single PDF file.

1. **Configure PDF Directory and Output Filename**:
   - **PDF Directory**: Set `pdf_directory` to the folder containing the PDFs you want to merge (e.g., `"book"`).
   - **Output PDF**: Specify the output filename for the merged document (default is `"merged_chapters.pdf"`).

2. **Run the Merger Script**:
   ```bash
   python merge_pdfs.py
   ```

   - This will merge all PDFs in `pdf_directory`, saving them as a single file named `merged_chapters.pdf`.

## Important Notes

- **Download Error Handling**: The downloader script checks for successful responses and skips missing chapters with a message indicating the chapter wasn’t found.
- **File Order in Merging**: The merger script sorts PDF files alphabetically, so ensure file naming aligns with the desired merge order.

---

These scripts are intended for personal and educational use. Adapt them as needed for your specific use cases!
``` 
