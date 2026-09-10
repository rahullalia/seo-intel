#!/usr/bin/env python3
"""Deterministic prose gate for seo-intel. Exit 0 = clean. Exit 1 = findings.

Checks factors/, sources/<tier>/*.md, playbook/*.md and playbook/local/*.md, changelog.md, docs/*.md.
Skips raw HeyTony material under sources/creators/hey-tony/ (machine-generated digests, not swept).
Usage: python3 pipeline/lint-prose.py [paths...]   (no args = default set)
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT = ["factors", "sources/google", "sources/experts", "sources/creators", "sources/rsla", "playbook", "changelog.md", "docs"]
SKIP = ["sources/creators/hey-tony/"]

BANNED = [
    r"\bdelve", r"\bleverag(es|ed|ing)\b", r"\b(to|can|should|will|must) leverage\b", r"\bleverage (the|your|our|its|their|this|these|existing)\b", r"\brobust\b", r"\bseamless(ly)?\b",
    r"\bunlock(s|ing)?\b", r"\belevat(e|es|ing)\b", r"\bempower", r"\bgame[- ]chang", r"\bcutting[- ]edge\b",
    r"\bgroundbreaking\b", r"\brevolutioni[sz]", r"\btransformative\b", r"\bholistic\b", r"\bsynergy\b",
    r"\btapestry\b", r"\btestament\b", r"\bunderscor(e|es|ing)\b", r"\bpivotal\b", r"\bcrucial\b", r"\bvital\b",
    r"\bessential\b", r"\bparamount\b", r"\brealm\b", r"\bfoster(s|ing)?\b", r"\bharness(es|ing)?\b",
    r"\bstreamlin", r"\bsupercharg", r"\bskyrocket", r"\bin today'?s\b", r"\bever[- ]evolving\b", r"\bfast[- ]paced\b",
    r"\bit'?s important to note\b", r"\bit is worth noting\b", r"\bin conclusion\b", r"\bultimately\b",
    r"\bat the end of the day\b", r"\bnot only\b.*\bbut also\b", r"\bit'?s not just\b", r"\bstands as\b",
    r"\bserves as\b", r"\bboasts?\b", r"\bshowcas(e|es|ing)\b", r"\ba reminder that\b", r"\bdive into\b",
    r"\bdeep dive\b", r"\bunpack(s|ing)?\b", r"\bembark", r"\bnavigat(e|ing) the\b", r"\bcomprehensive guide\b",
    r"\bjourney\b", r"\bexperts (say|agree|believe|argue)\b", r"\bmany (believe|argue|experts)\b",
    r"\bstudies show\b", r"\bit is widely\b", r"\bindustry reports\b", r"\bobservers\b",
]
# Case sensitive: the banned abstract sense is lowercase ("the SEO landscape"). A capitalised
# Landscape is a proper noun, such as the client Select Landscape, and is not a finding.
BANNED_CASED = [r"\blandscape\b(?! photo| architect)"]
EMOJI = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000027BF]")
DASH = re.compile("[–—]")
BANNED_RE = [re.compile(p, re.I) for p in BANNED] + [re.compile(p) for p in BANNED_CASED]

def files(args):
    targets = [ROOT / a for a in args] if args else [ROOT / d for d in DEFAULT]
    out = []
    for t in targets:
        if t.is_dir():
            out += [p for p in t.rglob("*.md")]
        elif t.suffix == ".md" and t.exists():
            out.append(t)
    return [p for p in out if not any(s in str(p.relative_to(ROOT)) + "/" for s in SKIP)]

def lint(path):
    findings = []
    in_code = False
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code or line.lstrip().startswith(("- Quote:", "- Source:", "Source:")):
            continue  # quotes and source titles are verbatim and exempt
        if DASH.search(line):
            findings.append((n, "em/en dash"))
        if EMOJI.search(line):
            findings.append((n, "emoji"))
        if "!" in line and "playbook/" not in str(path) and not line.lstrip().startswith(("http", "- Source", "[")):
            if re.search(r"\w!(\s|$)", line):
                findings.append((n, "exclamation"))
        for rx in BANNED_RE:
            m = rx.search(line)
            if m:
                findings.append((n, f"banned: {m.group(0)}"))
        if re.match(r"^## \d{4}-\d{2}-\d{2} \|", line):
            pass
    return findings

def main():
    args = sys.argv[1:]
    total = 0
    for p in files(args):
        # style.md lists the banned words on purpose; lint everything else
        if p.name == "style.md" and p.parent.name == "pipeline":
            continue
        for n, why in lint(p):
            total += 1
            print(f"{p.relative_to(ROOT)}:{n}: {why}")
    if total:
        print(f"\n{total} finding(s). Fix or delete the sentence; do not decorate it.")
        sys.exit(1)
    print("clean")

if __name__ == "__main__":
    main()
