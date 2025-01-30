
"""
Notes -> Obisdian

Remove extra titles that NotesExporter puts in.
"""


import os
import sys

# Check if the user provided a directory as an argument
if len(sys.argv) < 2:
    print("❌ Usage: python script.py /path/to/md_files")
    sys.exit(1)

folder = sys.argv[1]  # Get folder from command-line argument

# Validate that the provided path exists and is a directory
if not os.path.isdir(folder):
    print(f"❌ Error: '{folder}' is not a valid directory.")
    sys.exit(1)

for filename in os.listdir(folder):
    if filename.endswith(".md"):
        filepath = os.path.join(folder, filename)
        title = filename[:-3]  # Remove ".md" to get the title

        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Ensure the file has at least 3 lines before checking
        if len(lines) < 3:
            print(f"⚠️ Skipped (too short): {filename}")
            continue

        first_line = lines[0].strip()
        third_line = lines[2].strip()

        # Check if first line is "# Title" and third line is "Title"
        if 1 or first_line == f"# {title}" and third_line == title:
            cleaned_lines = lines[3:]  # Remove the first three lines
            with open(filepath, "w", encoding="utf-8") as f:
                f.writelines(cleaned_lines)
            print(f"✅ Fixed: {filename}")
        else:
            print(f"⚠️ Skipped (title mismatch): {filename}")

print("🎉 Done! Processed all .md files.")

