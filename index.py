# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "beautifulsoup4",
# ]
# ///
# 
# Install uv:
# https://github.com/astral-sh/uv 


import os
from bs4 import BeautifulSoup

# Define paths
base_dir = "Entries"  # Replace with the full path if needed
output_file = "index.html"

# Initialize the combined content
combined_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Journal Entries</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 2rem; color: black; }
        h2 { border-bottom: 2px solid #ccc; padding-bottom: 0.5rem; margin-top: 2rem; color: black; }
    </style>
</head>
<body>
    <h1>Journal Entries</h1>
"""

# Function to clean HTML and keep only paragraphs
def clean_html(content):
    soup = BeautifulSoup(content, "html.parser")
    
    # Extract all text and paragraphs
    clean_content = ""
    for tag in soup.find_all(["p"]):  # Keep only <p> tags
        clean_content += f"<p>{tag.get_text(strip=True)}</p>\n"

    return clean_content

# Iterate over all HTML files in the Entries folder
files = sorted([f for f in os.listdir(base_dir) if f.endswith(".html")])

for file in files:
    file_path = os.path.join(base_dir, file)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Clean the HTML content
    cleaned_content = clean_html(content)

    # Extract the file name without extension for the heading
    title = os.path.splitext(file)[0]

    # Add the content to the combined HTML with a heading
    combined_content += f"<h2>{title}</h2>\n{cleaned_content}\n"

# Close the HTML structure
combined_content += """
</body>
</html>
"""

# Write the combined content to index.html
with open(output_file, "w", encoding="utf-8") as f:
    f.write(combined_content)

print(f"Cleaned and combined journal entries have been saved to {output_file}")

