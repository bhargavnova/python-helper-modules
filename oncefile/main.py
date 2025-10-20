import argparse
from pathlib import Path
from oncefile import OnceFile

def main():
    p = argparse.ArgumentParser(description="remember a value once, then reuse")
    p.add_argument("--file", type=Path, default=Path.cwd() / ".oncefile.json")
    sub = p.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("get")
    g.add_argument("key")
    g.add_argument("--prompt")
    g.add_argument("--default")

    s = sub.add_parser("set")
    s.add_argument("key")
    s.add_argument("value")

    d = sub.add_parser("delete")
    d.add_argument("key")

    sh = sub.add_parser("show")

    args = p.parse_args()
    store = OnceFile(args.file)

    if args.cmd == "get":
        val = store.get(args.key, prompt=args.prompt, default=args.default)
        print(val if val is not None else "")
    elif args.cmd == "set":
        store.set(args.key, args.value)
    elif args.cmd == "delete":
        store.delete(args.key)
    elif args.cmd == "show":
        for k, v in store.as_dict().items():
            print(f"{k}={v}")

if __name__ == "__main__":
    main()