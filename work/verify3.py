# -*- coding: utf-8 -*-
from docx import Document
d = Document(r"C:\Users\LHW66\Documents\Codex\2026-08-10\chrome-plugin-chrome-openai-bundled-file\outputs\总复习.docx")
targets = ["DAY11", "DAY13", "DAY15", "DAY16 简单", "答案汇总", "对数函数", "一、高中向量", "一、单选题"]
print("===== 在 docx 里搜索目标标题 =====")
for p in d.paragraphs:
    t = p.text.strip()
    for kw in targets:
        if t.startswith(kw) or (kw == "对数函数" and t == "对数函数"):
            print(f"[{p.style.name}] {t[:50]}")
            break
print()
print("===== 检查原始 md 的标题行（Python 统计）=====")
md = open(r"C:\obsidian知识库\暑期课程\总复习.md", encoding="utf-8").read().split("\n")
hd = [l for l in md if l.startswith("## ") or l.startswith("### ")]
print("## 或 ### 标题行数:", len(hd))
for l in hd:
    if any(k in l for k in ["DAY11", "DAY13", "DAY15", "DAY16", "答案汇总", "对数函数", "一、高中向量", "一、单选题"]):
        print("  MD:", l[:50])
