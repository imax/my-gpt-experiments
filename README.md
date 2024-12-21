Read entries from Apple Journal app and combines them into a single .html file. 

To use the script export your Apple Journal entries from the phone first and unzip them-the script is looking for Entries folder with  *.html files. The script will save the results into index.html, it will also strip all extra formatting and img tags.

You can run it with uv:  
`uv run https://raw.githubusercontent.com/imax/apple-journal-cleaner/refs/heads/main/index.py`

If you don't have uv install it from here:  
https://github.com/astral-sh/uv 
