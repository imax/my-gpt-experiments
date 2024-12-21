Read entries from Apple Journal app and combines them into a single .html file. 

It also strips all the extra formatting and images. 

To use the script export your Apple Journal entries from the phone first and unzip them-the script is looking for Entries folder with  *.html files.

Running the script is trivial:

`uv run index.py`

It will save the results into index.html.

If you don't have uv install it from here:
https://github.com/astral-sh/uv 
