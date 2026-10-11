p = r"C:\Users\LHW66\AppData\Local\Temp\openai-docs-cache\codex-manual.md"
with open(p, encoding="utf-8") as f:
    lines = f.readlines()
def show(a, b, label):
    print(f"\n===== {label} (lines {a}-{b}) =====")
    for i in range(a-1, min(b, len(lines))):
        print(f"{i+1}: {lines[i].rstrip()[:230]}")
show(8384, 8414, "writable roots context")
show(8900, 8970, "Permissions sections")
show(30901, 30930, "desktop security model")
show(31370, 31400, "outside your workspace (desktop)")
show(33480, 33510, "request access (desktop)")
