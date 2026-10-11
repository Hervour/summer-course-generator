p = r"C:\Users\LHW66\AppData\Local\Temp\openai-docs-cache\codex-manual.md"
with open(p, encoding="utf-8") as f:
    lines = f.readlines()
def show(a, b, label):
    print(f"\n===== {label} (lines {a}-{b}) =====")
    for i in range(a-1, min(b, len(lines))):
        print(f"{i+1}: {lines[i].rstrip()[:230]}")
show(8953, 9015, "permission modes detail")
show(30880, 30925, "desktop permissions and safety")
