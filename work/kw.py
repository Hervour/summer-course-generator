p = r"C:\Users\LHW66\AppData\Local\Temp\openai-docs-cache\codex-manual.md"
with open(p, encoding="utf-8") as f:
    lines = f.readlines()
keys = ["managed", "desktop app", "ChatGPT app", "grant", "allow list", "allowlist", "writable roots", "outside the workspace", "outside your workspace", "request access", "approve"]
hits = {}
for i, ln in enumerate(lines, 1):
    low = ln.lower()
    for k in keys:
        if k in low:
            hits.setdefault(k, []).append(i)
for k in keys:
    v = hits.get(k, [])
    print(k, "->", v[:8], ("..." if len(v)>8 else ""))
