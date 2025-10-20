@bhargavnova
------

oncefile

what it is
----------
tiny helper that asks for a value once and stores it in .oncefile.json,
so your script doesn't keep prompting every run.

quick use
---------
python main.py get api_key --prompt "enter api key"
python main.py set default_path /tmp/data
python main.py show

in code
-------
from oncefile import OnceFile
cfg = OnceFile()
token = cfg.get("api_token", prompt="enter token")