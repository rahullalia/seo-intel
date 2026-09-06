#!/usr/bin/env python3
"""Detect NEW HeyTony Insiders call replays not yet captured.

Usage:
  1. In a Claude session with the logged-in htinsiders.com browser tab, run the
     enumeration evaluate_script from updateHeyTony.md, saving the fresh playlist
     listing to build/freshPlaylist.json (array of {hash,title,len,tr,desc}).
  2. python3 build/deltaDetect.py
     -> prints new items and writes build/newCalls.json (the work list for pulling).

Compares fresh listing against inventory.json (hashes already captured).
"""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(p, default=None):
    try:
        return json.load(open(p))
    except Exception:
        return default

def main():
    inv = load(f"{BASE}/inventory.json", {"items": []})
    have = {i["hash"] for i in inv.get("items", [])}
    fresh = load(f"{BASE}/build/freshPlaylist.json")
    if fresh is None:
        print("ERROR: build/freshPlaylist.json not found. Run the enumeration evaluate_script first (see update-hey-tony.md).", file=sys.stderr)
        sys.exit(1)
    # fresh may be {items:[...]} or a raw list
    items = fresh.get("items", fresh) if isinstance(fresh, dict) else fresh
    new = [f for f in items if f.get("hash") not in have]
    new.sort(key=lambda f: f.get("title", ""))
    json.dump({"count": len(new), "items": new}, open(f"{BASE}/build/newCalls.json", "w"), indent=1, ensure_ascii=False)
    print(f"Already captured: {len(have)} calls")
    print(f"Fresh listing:    {len(items)} calls")
    print(f"NEW to pull:      {len(new)}")
    for f in new:
        mins = (f.get("len") or 0) // 60
        print(f"   + {f.get('title')}  ({mins}m)  [{f.get('hash')}]  transcript={'yes' if f.get('tr') else 'NO'}")
    if not new:
        print("Up to date. Nothing to fold in.")

if __name__ == "__main__":
    main()
