# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
from docx import Document

md = open(r"C:\obsidian知识库\暑期课程\总复习.md", encoding="utf-8").read().split("\n")
print("===== md 中目标标题行的 repr =====")
for l in md:
    if l.startswith("## ") and any(k in l for k in ["DAY11", "DAY13", "DAY15", "DAY16", "答案汇总", "对数函数", "一、高中向量", "一、单选题"]):
        print(repr(l[:40]))

print()
d = Document(r"C:\Users\LHW66\Documents\Codex\2026-08-10\chrome-plugin-chrome-openai-bundled-file\outputs\总复习.docx")
print("===== docx 中包含关键字的段落（含样式）=====")
for p in d.paragraphs:
    t = p.text
    if any(k in t for k in ["DAY11", "DAY13", "DAY15 三角", "DAY16 简单", "答案汇总", "对数函数", "一、高中向量", "一、单选题"]):
        print(f"[{p.style.name}] {t[:45]!r}")
