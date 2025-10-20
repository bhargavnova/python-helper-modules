@bhargavnova
------

paste_image_server #script!

What it is
----------
A tiny local server that lets you paste or drag-drop images in your browser and saves them to a folder on your machine. No internet, no accounts.

How to run
----------
python paste_image_server.py -o --dir /path/to/save

Then open the shown URL (or it opens automatically with -o), press Ctrl/Cmd+V to paste screenshots or copied images, or drag files into the drop zone. Saved files appear in the chosen folder.

Saved files
-----------
Files are named like: pasted-YYYYMMDD-HHMMSS-<hash>.ext
A JSON index is written next to them: pasted_index.json

Options
-------
-d, --dir           Output folder (default: ./pasted_images)
-p, --port          Port (default: 8090)
-o, --open          Open the browser automatically
-f, --format        original | png | jpg | webp  (requires Pillow for conversion)
-q, --quality       Quality for jpg/webp (default: 92)
--dedupe            Skip saving if identical bytes were already saved (sha256)
--max-size-mb       Max upload size in MB (default: 30)
--static            Directory for index.html (default: ./static)

Customizing the page
--------------------
Edit static/index.html. The server injects a token and the output path label at runtime.

Notes
-----
• Runs on 127.0.0.1 only.
• Works offline.
• Image conversion is optional. Install Pillow if you want -f png/jpg/webp:
  pip install pillow