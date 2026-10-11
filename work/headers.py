p = r"C:\Users\LHW66\AppData\Local\Temp\openai-docs-cache\codex-manual.md"
with open(p, encoding="utf-8") as f:
    lines = f.readlines()
# find section headers
for i, ln in enumerate(lines, 1):
    s = ln.strip()
    if s.startswith("#") and any(k in s for k in ["Approvals, Sandboxing", "Sandboxing", "Permissions", "Windows sandbox", "Workspace", "approval_policy", "sandbox_mode"]):
        print(i, s[:120])
