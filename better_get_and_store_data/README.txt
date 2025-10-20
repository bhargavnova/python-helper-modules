@bhargavnova
------

BetterGetAndStoreData

Small local helper that pops open a simple form in your browser, lets you fill fields, and saves the result.
Runs on http.server, writes to a .json file by default, and then shuts itself down.

No frameworks. No cloud. Just fill → save → done.

Why you might want this
- Collect parameters for your scripts without hand-editing JSON.
- Quick “add/update an item” UI for your local tools (notes, commands, snippets, tasks).
- Build tiny utilities for teammates that don’t want to touch the terminal.
- Keep everything offline and private.

main.py
- from here all the customization can be done, it's not just limited to .json files.

#future
- can add view and delete if needed, this can be expanded with more features.