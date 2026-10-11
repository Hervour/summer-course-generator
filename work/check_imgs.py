import os
from PIL import Image
OUT = r"C:\Users\LHW66\Documents\Codex\2026-08-10\chrome-plugin-chrome-openai-bundled-file\outputs"
names = ["均值不等式链几何解释.png","切线放缩.png","闵可夫斯基距离.png","单位圆三角函数.png"]
for n in names:
    p = os.path.join(OUT, n)
    im = Image.open(p).convert("RGB")
    colors = im.getcolors(maxcolors=100000)
    nonwhite = sum(c for c, rgb in colors if rgb != (255,255,255))
    print(n, "size=", im.size, "bytes=", os.path.getsize(p), "nonwhite=", nonwhite)
