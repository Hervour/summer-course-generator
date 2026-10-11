# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
from docx import Document
d = Document(r"C:\Users\LHW66\Documents\Codex\2026-08-10\chrome-plugin-chrome-openai-bundled-file\outputs\总复习.docx")
ps = d.paragraphs
# 找到答案汇总的起始，检查其后内容
start = None
for idx, p in enumerate(ps):
    if p.text.strip() == "答案汇总" and p.style.name == "Heading 1":
        start = idx
        break
print("答案汇总位置:", start)
h2_in_ans = [p.text for p in ps[start:start+120] if p.style.name == "Heading 2" and p.text.strip()]
print("答案汇总下 Heading 2（前 20）:")
for h in h2_in_ans[:20]:
    print("  -", h[:45])
# 检查 DAY8 答案里的关键内容
found = 0
for p in ps[start:start+40]:
    if "0.50 m/s²" in p.text or "44 m" in p.text or "19/4" in p.text or "4.75 s" in p.text or "40 g" in p.text:
        print("DAY8 答案关键内容:", p.text[:50])
        found += 1
print("DAY8 答案关键点命中:", found)
