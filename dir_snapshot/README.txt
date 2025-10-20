@bhargavnova
------

dir_snapshot

what it is
----------
creates a simple json snapshot of a folder (paths, sizes, hashes) and can compare two snapshots.

examples
--------
python main.py create ./mydir -o snap1.json
python main.py create ./mydir -o snap2.json
python main.py diff snap1.json snap2.json