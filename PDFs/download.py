import requests

# Function to download a PDF from a given URL
def download_pdf(chapter, base_url, save_directory):
    url = f"{base_url}{chapter}.pdf"
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        filename = f"{save_directory}/chapter_{chapter}.pdf"
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Chapter {chapter} not found (Status: {response.status_code})")

# Define the base URL and directory to save the PDFs
base_url = "https://web.stanford.edu/~jurafsky/slp3/"
save_directory = "book"  # Make sure this folder exists or create it

# Loop over the chapter numbers (e.g., from 1 to 10)
for chapter in range(11, 29):
    download_pdf(chapter, base_url, save_directory)
