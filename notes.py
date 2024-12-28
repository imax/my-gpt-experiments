# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "appscript",
# ]
# ///
# 
# Install uv:
# https://github.com/astral-sh/uv 

from appscript import app

# Path to save the output file
output_file = "notes.html"

# Access Apple Notes
notes_app = app("Notes")

# Fetch the folder directly by name
folder_name = "Плани"
target_folder = None

for f in notes_app.folders():
    print(f"Folder: {f.name()}")
    if f.name() == folder_name:
        target_folder = f
        print("Found!")
        break

if not target_folder:
    raise ValueError(f"Folder '{folder_name}' not found!")


# Get the folder named 'Плани'
# folder = [f for f in notes_app.folders() if f.name() == "Плани"][0]

# Start building the HTML content
html_content = """<html><head><title>Exported Notes</title></head><body>"""

# Iterate through notes in the folder
for note in target_folder.notes():
    title = note.name()
    body = note.body()
    print(f"Reading: {title}")
    
    # Check if "2024" is in the title
    if "2024" in title:
        html_content += f"<h1>{title}</h1>\n"
        html_content += f"<p>{body}</p>\n"

# Close the HTML structure
html_content += "</body></html>"

# Write to the output file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Notes exported to {output_file}")

