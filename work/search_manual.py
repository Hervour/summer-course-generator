import re
p = r"C:\Users\LHW66\AppData\Local\Temp\openai-docs-cache\codex-manual.md"
with open(p, encoding="utf-8") as f:
    lines = f.readlines()
pats = ["sandbox_approval", "request_permissions", "workspace-write", "permission", "sandbox", "writable"]
seen = set()
count = 0
for i, ln in enumerate(lines, 1):
    low = ln.lower()
    for pat in ["sandbox_approval", "request_permissions", "workspace-write"]:
        if pat in low and pat not in seen:
            seen.add(pat)
            print(f"--- first hit for '{pat}' at line {i} ---")
            print(ln.strip()[:300])
            count += 1
print("done, hits:", count)
