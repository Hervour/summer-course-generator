# -*- coding: utf-8 -*-
import math, os
from PIL import Image, ImageDraw, ImageFont

OUT = r"C:\Users\LHW66\Documents\Codex\2026-08-10\chrome-plugin-chrome-openai-bundled-file\outputs"
FONT = "C:/Windows/Fonts/simhei.ttf"

def f(sz):
    return ImageFont.truetype(FONT, sz)

def arrow(d, p1, p2, color, width=3, head=11):
    d.line([p1, p2], fill=color, width=width)
    dx, dy = p2[0]-p1[0], p2[1]-p1[1]
    L = math.hypot(dx, dy) or 1.0
    ux, uy = dx/L, dy/L
    px, py = -uy, ux
    base = (p2[0]-ux*head, p2[1]-uy*head)
    h1 = (base[0]+px*head*0.45, base[1]+py*head*0.45)
    h2 = (base[0]-px*head*0.45, base[1]-py*head*0.45)
    d.polygon([p2, h1, h2], fill=color)

BLACK=(20,20,20); RED=(200,40,40); BLUE=(30,80,200); GREEN=(30,150,80); GRAY=(120,120,120)

def center_text(d, cx, cy, txt, font, fill=BLACK):
    bb = d.textbbox((0,0), txt, font=font)
    w = bb[2]-bb[0]; h = bb[3]-bb[1]
    d.text((cx-w/2, cy-h/2), txt, font=font, fill=fill)

# ---------- 1. 均值不等式链几何解释 ----------
img = Image.new("RGB", (960, 580), "white"); d = ImageDraw.Draw(img)
A=(160,440); B=(800,440); R=320; O=(480,440); a=380; b=260
C=(A[0]+a, 440)
cd = math.sqrt(R*R-60*60)
D=(C[0], 440-cd)
d.arc([O[0]-R, O[1]-R, O[0]+R, O[1]+R], 180, 360, fill=BLACK, width=4)
d.line([A, B], fill=BLACK, width=3)
d.line([O, D], fill=RED, width=4)
d.line([C, D], fill=BLUE, width=4)
d.line([O, C], fill=GRAY, width=2)
for p in (A, B, C, O, D):
    d.ellipse([p[0]-5, p[1]-5, p[0]+5, p[1]+5], fill=BLACK)
d.text((A[0]-22, A[1]+6), "A", font=f(24), fill=BLACK)
d.text((C[0]-10, C[1]+6), "C", font=f(24), fill=BLACK)
d.text((B[0]+10, B[1]+6), "B", font=f(24), fill=BLACK)
d.text((O[0]-6, O[1]+6), "O", font=f(24), fill=BLACK)
d.text((D[0]-6, D[1]-30), "D", font=f(24), fill=BLACK)
d.text(((A[0]+C[0])/2-8, A[1]+12), "a", font=f(24), fill=BLACK)
d.text(((C[0]+B[0])/2-8, C[1]+12), "b", font=f(24), fill=BLACK)
d.text((O[0]+(D[0]-O[0])/2+6, (O[1]+D[1])/2-8), "(a+b)/2", font=f(22), fill=RED)
d.text((D[0]+12, (C[1]+D[1])/2-10), "√(ab)", font=f(22), fill=BLUE)
center_text(d, 480, 40, "几何解释：半圆半径 ≥ 垂直半弦，即 (a+b)/2 ≥ √(ab)", f(28))
center_text(d, 480, 76, "（图中 O 为圆心，OD 是半径，CD 是半弦；直角边 CD 不超过斜边 OD）", f(20), GRAY)
center_text(d, 480, 540, "当 a=b 时 C 与 O 重合，CD=OD，等号成立", f(20), GRAY)
img.save(os.path.join(OUT, "均值不等式链几何解释.png"))

# ---------- 2. 切线放缩 ----------
img = Image.new("RGB", (1000, 560), "white"); d = ImageDraw.Draw(img)
# 左：e^x 与切线 x+1
OL=(130,430); xu=55; yu=30
def px(x): return OL[0]+x*xu
def py(y): return OL[1]-y*yu
d.line([(30,430),(300,430)], fill=BLACK, width=2); arrow(d,(300,430),(318,430),BLACK,2)
d.line([(130,430),(130,70)], fill=BLACK, width=2); arrow(d,(130,70),(130,52),BLACK,2)
for i in range(0,3):
    d.line([(px(i),430),(px(i),436)], fill=BLACK, width=2)
    d.text((px(i)-8, 438), str(i), font=f(16), fill=BLACK)
pts=[]
x=-3.0
while x<=2.5:
    pts.append((px(x), py(math.exp(x)))); x+=0.05
d.line(pts, fill=BLUE, width=4)
d.line([(px(-3),py(-2)),(px(2.5),py(3.5))], fill=RED, width=4)
d.text((OL[0]-20, OL[1]+8), "O", font=f(20), fill=BLACK)
d.text((150, 95), "e^x ≥ x+1", font=f(26), fill=BLUE)
d.text((150, 128), "取等 x=0", font=f(20), fill=GRAY)
center_text(d, 265, 30, "凸函数 e^x：图像在切线上方", f(24))
# 右：ln x 与切线 x-1
OR=(610,430); xu2=55; yu2=48
def px2(x): return OR[0]+x*xu2
def py2(y): return OR[1]-y*yu2
d.line([(480,430),(870,430)], fill=BLACK, width=2); arrow(d,(870,430),(888,430),BLACK,2)
d.line([(610,430),(610,340)], fill=BLACK, width=2); arrow(d,(610,340),(610,322),BLACK,2)
d.line([(610,430),(610,520)], fill=BLACK, width=2)
for i in range(1,5):
    d.line([(px2(i),430),(px2(i),436)], fill=BLACK, width=2)
    d.text((px2(i)-8, 438), str(i), font=f(16), fill=BLACK)
pts=[]
x=0.2
while x<=4.2:
    pts.append((px2(x), py2(math.log(x)))); x+=0.03
d.line(pts, fill=BLUE, width=4)
d.line([(px2(0.2),py2(-0.8)),(px2(4.0),py2(3.0))], fill=RED, width=4)
d.text((OR[0]-20, OR[1]+8), "O", font=f(20), fill=BLACK)
d.text((700, 120), "ln x ≤ x-1", font=f(26), fill=BLUE)
d.text((700, 153), "取等 x=1", font=f(20), fill=GRAY)
center_text(d, 735, 30, "凹函数 ln x：图像在切线下方", f(24))
center_text(d, 500, 545, "放缩方向：先判断凹凸性 —— 凸函数在切线上方，凹函数在切线下方", f(20), GRAY)
img.save(os.path.join(OUT, "切线放缩.png"))

# ---------- 3. 闵可夫斯基 ----------
img = Image.new("RGB", (960, 600), "white"); d = ImageDraw.Draw(img)
O=(130,500); A=(420,300); B=(800,140)
arrow(d, O, A, RED, 4, 14)
arrow(d, A, B, BLUE, 4, 14)
arrow(d, O, B, GREEN, 3, 14)
for p in (O,A,B):
    d.ellipse([p[0]-5,p[1]-5,p[0]+5,p[1]+5], fill=BLACK)
d.text((O[0]-24,O[1]+6),"O",font=f(24),fill=BLACK)
d.text((A[0]+10,A[1]-28),"A",font=f(24),fill=BLACK)
d.text((B[0]+12,B[1]-8),"B",font=f(24),fill=BLACK)
d.text(((O[0]+A[0])/2-40,(O[1]+A[1])/2-20),"u=(a,b)",font=f(22),fill=RED)
d.text(((A[0]+B[0])/2+8,(A[1]+B[1])/2-8),"v=(c,d)",font=f(22),fill=BLUE)
d.text(((O[0]+B[0])/2-60,(O[1]+B[1])/2+6),"u+v",font=f(22),fill=GREEN)
center_text(d, 480, 40, "闵可夫斯基不等式：折线长度 ≥ 直线长度（向量三角不等式）", f(28))
d.line([(230,520),(280,520)], fill=RED, width=4); d.text((290,505),"折线 O→A→B 的一部分",font=f(20),fill=BLACK)
d.line([(560,520),(610,520)], fill=GREEN, width=3); d.text((620,505),"直线 O→B（最短）",font=f(20),fill=BLACK)
center_text(d, 480, 570, "√(a²+b²)+√(c²+d²) ≥ √((a+c)²+(b+d)²)", f(24))
img.save(os.path.join(OUT, "闵可夫斯基距离.png"))

# ---------- 4. 单位圆三角函数 ----------
img = Image.new("RGB", (900, 640), "white"); d = ImageDraw.Draw(img)
O=(330,340); r=230
d.ellipse([O[0]-r,O[1]-r,O[0]+r,O[1]+r], outline=BLACK, width=3)
arrow(d, (60,340),(640,340), BLACK, 2)
arrow(d, (330,60),(330,640), BLACK, 2)
ang=math.radians(42)
P=(O[0]+r*math.cos(ang), O[1]-r*math.sin(ang))
Q=(P[0], O[1])
d.line([O,P], fill=BLACK, width=3)
d.line([Q,P], fill=BLUE, width=3)
d.line([(O[0]+r,O[1]),(560,340)], fill=RED, width=3)  # 先画水平小段
T=(560, O[1]- (560-O[0])*math.tan(ang))
d.line([(560,340),T], fill=RED, width=3)
d.arc([O[0]-r,O[1]-r,O[0]+r,O[1]+r], 318, 360, fill=GREEN, width=4)
for p in (O,Q):
    d.ellipse([p[0]-4,p[1]-4,p[0]+4,p[1]+4], fill=BLACK)
d.ellipse([P[0]-5,P[1]-5,P[0]+5,P[1]+5], fill=BLUE)
d.text((O[0]-14,O[1]+10),"O",font=f(22),fill=BLACK)
d.text((P[0]+8,P[1]-26),"P",font=f(22),fill=BLACK)
d.text((Q[0]-6,Q[1]+12),"Q",font=f(22),fill=BLACK)
d.text((P[0]+10,(P[1]+Q[1])/2-10),"sin x",font=f(22),fill=BLUE)
d.text((T[0]+10,(T[1]+340)/2-10),"tan x",font=f(22),fill=RED)
mid=(O[0]+r*math.cos(ang/2), O[1]-r*math.sin(ang/2))
d.text((mid[0]+12, mid[1]-14),"x",font=f(22),fill=GREEN)
center_text(d, 450, 30, "单位圆里的三个长度：sin x < x < tan x", f(28))
center_text(d, 450, 66, "（扇形面积夹在两个三角形面积之间，0 < x < π/2 时成立）", f(20), GRAY)
img.save(os.path.join(OUT, "单位圆三角函数.png"))

print("done")
