# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding="utf-8")
md = open(r"C:\obsidian知识库\暑期课程\总复习.md", encoding="utf-8").read().split("\n")
for idx, line in enumerate(md):
    if line.strip().startswith("## DAY11") or line.strip().startswith("## DAY13") or line.strip().startswith("## 答案汇总"):
        print("行号:", idx, "| repr:", repr(line))
        s = line.rstrip("\n").strip()
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        print("   s =", repr(s[:30]))
        print("   标题正则匹配:", bool(m), "| level:", len(m.group(1)) if m else None, "| 内容:", m.group(2)[:20] if m else None)
        # 检查前面 3 行和后面 1 行的上下文
        print("   上下文前:")
        for j in range(max(0, idx-3), idx):
            print("     ", j, repr(md[j][:40]))
        print("   上下文后:")
        if idx+1 < len(md):
            print("     ", idx+1, repr(md[idx+1][:40]))
