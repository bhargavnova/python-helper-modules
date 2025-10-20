import argparse
from pathlib import Path
from dir_snapshot import snapshot, save_snapshot, load_snapshot, diff

def main():
    p = argparse.ArgumentParser(description="make and compare simple directory snapshots")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("create")
    s.add_argument("root", type=Path)
    s.add_argument("-o", "--out", type=Path, required=True)
    s.add_argument("--hash", choices=["hash", "fast", "none"], default="hash")

    d = sub.add_parser("diff")
    d.add_argument("old", type=Path)
    d.add_argument("new", type=Path)

    args = p.parse_args()

    if args.cmd == "create":
        snap = snapshot(args.root, hash_mode=args.hash)
        save_snapshot(snap, args.out)
        print(f"saved {args.out}")
    elif args.cmd == "diff":
        a = load_snapshot(args.old)
        b = load_snapshot(args.new)
        out = diff(a, b)
        print("added:")
        for x in out["added"]: print(f"  + {x}")
        print("removed:")
        for x in out["removed"]: print(f"  - {x}")
        print("changed:")
        for x in out["changed"]: print(f"  * {x}")

if __name__ == "__main__":
    main()