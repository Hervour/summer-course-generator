p = r"C:\Users\LHW66\AppData\Local\Temp\openai-docs-cache\codex-manual.md"
with open(p, encoding="utf-8") as f:
    lines = f.readlines()
def show(a, b, label):
    print(f"\n===== {label} (lines {a}-{b}) =====")
    for i in range(a-1, min(b, len(lines))):
        print(f"{i+1}: {lines[i].rstrip()[:200]}")
show(8240, 8320, "granted permissions")
show(8380, 8480, "writable roots / granular / outside workspace")
