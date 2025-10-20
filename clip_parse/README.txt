@bhargavnova
------

clip_parse

what it is
----------
reads text (clipboard by default) and extracts urls, emails, ip addresses, hex-like tokens,
code blocks, and simple curl info.

run
---
python main.py            # clipboard or stdin
python main.py --json
python main.py --text "curl -X POST https://api.example.com -H 'Accept: application/json' -d 'x=1'"