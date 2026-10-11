# DAY16 简单数学测试答案

> 这是 [[DAY16 简单数学测试]] 的答案，做完题再来看。
> 说明：第 1 题是 2020 全国Ⅰ卷理科第 2 题，第 6 题是 2024 新课标Ⅱ 第 9 题，其余改编自 DAY9–DAY15 讲义的例题和练习（难度有所提升）。

### 题 1 答案（单选，B）

$A=\{x\,|\,x^2-4\le0\}=[-2,2]$，$B=\{x\,|\,2x+a\le0\}=(-\infty,-\frac a2]$。
交集 $[-2,2]\cap(-\infty,-\frac a2]$ 要等于 $[-2,1]$，说明 $-\frac a2=1$，所以 $a=-2$，选 B。

### 题 2 答案（单选，A）

$p$ 的解集：$x^2-2x-3\le0\Rightarrow -1\le x\le3$，即 $[-1,3]$。
$p$ 是 $q$ 的充分不必要条件，说明 $[-1,3]$ 是 $(-\infty,a]$ 的真子集，小范围推大范围，所以 $a\ge3$，选 A。

### 题 3 答案（单选，C）

$x<0$ 时，$-x>0$，用 $x>0$ 的式子代：
$$f(-x)=(-x)^2-2(-x)=x^2+2x$$
奇函数满足 $f(-x)=-f(x)$，所以
$$f(x)=-f(-x)=-x^2-2x$$
选 C。

### 题 4 答案（单选，A）

图象关于 $x=\frac{\pi}{12}$ 对称，说明在这条对称轴上取最值：
$$2\times\frac{\pi}{12}+\varphi=\frac{\pi}{2}+k\pi\ \Rightarrow\ \varphi=\frac{\pi}{3}+k\pi$$
再由 $|\varphi|<\frac{\pi}{2}$，取 $\varphi=\frac{\pi}{3}$，选 A。

### 题 5 答案（多选，ACD）

- A 对：$\frac{1+x}{1-x}>0$，解得 $-1<x<1$；
- B 错：$f(-x)=\ln\frac{1-x}{1+x}=-\ln\frac{1+x}{1-x}=-f(x)$，是**奇函数**，不是偶函数；
- C 对：$\frac{1+x}{1-x}=\frac{2}{1-x}-1$ 在 $(-1,1)$ 上递增，外层 $\ln$ 也递增，同增异减，整体递增；
- D 对：奇函数有 $f(\frac13)=-f(-\frac13)$，所以 $f(\frac13)+f(-\frac13)=0$。

选 ACD。

### 题 6 答案（多选，BC）

（2024 新课标Ⅱ 第 9 题）逐个比：
- 零点：$f(x)$ 的零点 $x=\frac{k\pi}{2}$，$g(x)$ 的零点 $x=\frac{\pi}{8}+\frac{k\pi}{2}$，不一样；
- 最大值都是 1，一样；
- 最小正周期都是 $\pi$，一样；
- 对称轴：$f$ 是 $x=\frac{\pi}{4}+\frac{k\pi}{2}$，$g$ 是 $x=\frac{3\pi}{8}+\frac{k\pi}{2}$，不一样。

选 BC。

### 题 7 答案

（1）$a=2$ 时，真数 $x^2-4x+3>0$，即 $(x-1)(x-3)>0$，
定义域 $(-\infty,1)\cup(3,+\infty)$。

（2）设内层 $u=x^2-2ax+3$，对称轴 $x=a$，开口向上。要在 $[4,+\infty)$ 上单调递增，三个条件：
- 内层在 $[4,+\infty)$ 上递增：对称轴在左边，$a\le4$；
- 真数恒正：$u$ 在 $[4,+\infty)$ 上递增，最小值在 $x=4$ 处，需 $u(4)=19-8a>0$，即 $a<\frac{19}{8}$；
- 复合函数同增异减：外层 $\log_a$ 必须是增函数，$a>1$。

综合：$1<a<\frac{19}{8}$。

（3）值域为 $\mathbb{R}$，等价于内层 $u=x^2-2ax+3$ 要能取遍所有正数。
开口向上的二次函数，要取遍 $(0,+\infty)$，必须和 $x$ 轴有交点，即判别式
$$\Delta=(-2a)^2-12=4a^2-12\ge0\ \Rightarrow\ a\ge\sqrt3$$
所以 $a\in[\sqrt3,+\infty)$。

### 题 8 答案

（1）先化简：
$$f(x)=(2\cos^2x-1)+2\sqrt3\sin x\cos x=\cos2x+\sqrt3\sin2x=2\sin\left(2x+\frac{\pi}{6}\right)$$
最小正周期 $T=\frac{2\pi}{2}=\pi$。
对称中心：$2x+\frac{\pi}{6}=k\pi$，解得 $x=-\frac{\pi}{12}+\frac{k\pi}{2}$，所以对称中心是 $\left(-\frac{\pi}{12}+\frac{k\pi}{2},0\right)$，$k\in\mathbb{Z}$。

（2）单调递减：
$$\frac{\pi}{2}+2k\pi\le2x+\frac{\pi}{6}\le\frac{3\pi}{2}+2k\pi\ \Rightarrow\ \frac{\pi}{6}+k\pi\le x\le\frac{2\pi}{3}+k\pi$$
在 $[0,\pi]$ 上取 $k=0$，单调递减区间是 $\left[\frac{\pi}{6},\frac{2\pi}{3}\right]$。

（3）$x\in[0,\pi]$ 时，$t=2x+\frac{\pi}{6}\in\left[\frac{\pi}{6},\frac{13\pi}{6}\right]$，方程变成 $\sin t=\frac m2$。
在这个区间上数解的个数（注意端点 $t=\frac{\pi}{6}$ 和 $t=\frac{13\pi}{6}$ 处 $\sin t=\frac12$）：
- $\frac m2=1$（$m=2$）：1 个解；
- $\frac m2=-1$（$m=-2$）：1 个解；
- $\frac m2=\frac12$（$m=1$）：$t=\frac{\pi}{6},\frac{5\pi}{6},\frac{13\pi}{6}$，3 个解；
- 其余 $-1<\frac m2<1$：都是 2 个解。

所以恰有两个不同实数解 $\Leftrightarrow m\in(-2,2)$ 且 $m\ne1$。

### 题 9 答案（附加题）

（1）由正弦定理：
$$\frac{a}{\sin A}=\frac{b}{\sin B}\ \Rightarrow\ \frac{2\sqrt3}{\sin30°}=\frac{6}{\sin B}\ \Rightarrow\ 4\sqrt3=\frac{6}{\sin B}\ \Rightarrow\ \sin B=\frac{\sqrt3}{2}$$
所以 $B=60°$ 或 $120°$。两种都能和 $A=30°$ 组成三角形（$A+B=90°$ 或 $150°$，都小于 $180°$），所以有**两组解**。

（2）$C=180°-A-B$：
- $B=60°$ 时 $C=90°$，$c=\dfrac{a\sin C}{\sin A}=\dfrac{2\sqrt3\times1}{\frac12}=4\sqrt3$；
- $B=120°$ 时 $C=30°$，$c=\dfrac{a\sin C}{\sin A}=\dfrac{2\sqrt3\times\frac12}{\frac12}=2\sqrt3$。
