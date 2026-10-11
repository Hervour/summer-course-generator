昨天把三角函数的基础过完了，今天讲进阶：恒等变换的技巧、图像变换的坑、由图像求解析式、最值问题，最后上几道高考级别的题。题目和答案分开，答案放在数学课堂展示文件夹里，点链接就能跳过去。

### 先看这个：单位圆是怎么推出三角函数的

![[数学课堂展示/单位圆推导三角函数.html]]
拖动滑块让角转一圈，看 $\sin$、$\cos$、$\tan$ 分别是哪条线段，勾股关系就是 $\sin^2\alpha+\cos^2\alpha=1$。

### 三角恒等变换的四个核心技巧

**1，拆角凑角**。把要求的角拆成已知角的和差。比如
$$\alpha=(\alpha+\beta)-\beta,\qquad 2\alpha=(\alpha+\beta)+(\alpha-\beta)$$
做题先看已知角是什么，再想办法把未知角凑成已知角的和差。

**2，降幂公式**（二倍角公式倒过来用）：
$$\sin^2\alpha=\frac{1-\cos2\alpha}{2},\qquad \cos^2\alpha=\frac{1+\cos2\alpha}{2}$$
见到平方就想降幂，这是把二次变成一次的关键。

**3，齐次式化切**。形如 $a\sin^2x+b\sin x\cos x+c\cos^2x$ 的式子，整体除以 $\cos^2x$，就变成只含 $\tan x$ 的式子。配合 $\sin^2x+\cos^2x=1$ 用，能把"弦"全部换成"切"。

**4，$\sin x\pm\cos x$ 与 $\sin x\cos x$ 互化**：
$$(\sin x+\cos x)^2=1+2\sin x\cos x,\qquad (\sin x-\cos x)^2=1-2\sin x\cos x$$
遇到 $\sin x+\cos x$ 和 $\sin x\cos x$ 一起出现，就设 $t=\sin x\pm\cos x$ 换元，注意 $|t|\le\sqrt2$。

**简单例题**：已知 $\sin x+\cos x=\frac15$，$x\in(0,\pi)$，求 $\sin x\cos x$ 和 $\tan x$
$(\sin x+\cos x)^2=1+2\sin x\cos x=\frac1{25}$，所以 $\sin x\cos x=-\frac{12}{25}<0$，说明 $x$ 在第二象限。又 $(\sin x-\cos x)^2=1-2\sin x\cos x=\frac{49}{25}$，第二象限 $\sin>\cos$，所以 $\sin x-\cos x=\frac75$。联立解得 $\sin x=\frac45$、$\cos x=-\frac35$，$\tan x=-\frac43$。

### 图像变换的次序陷阱

$y=\sin x$ 变到 $y=A\sin(\omega x+\varphi)$ 有两条路，**结果不一样，必须按题目的顺序一步步来**：
- 先平移后伸缩：$y=\sin x$ 平移得 $\sin(x+\varphi)$，再横坐标变 $\frac1\omega$ 得 $\sin(\omega x+\varphi)$；
- 先伸缩后平移：$y=\sin x$ 横坐标变 $\frac1\omega$ 得 $\sin\omega x$，再平移是 $\sin\omega(x+\frac{\varphi}{\omega})$，平移量是 $\frac{\varphi}{\omega}$，不是 $\varphi$。

**简单例题**：把 $y=\sin2x$ 的横坐标变为原来的 $\frac12$，再向右平移 $\frac{\pi}{4}$，求解析式
先伸缩：$y=\sin2x\to y=\sin4x$；再平移：$y=\sin4(x-\frac{\pi}{4})=\sin(4x-\pi)$。顺序反过来结果会变成 $\sin(4x-\frac{\pi}{2})$，不一样。

### 由图像求解析式 $y=A\sin(\omega x+\varphi)$

三个量各看各的：
- $A$：看最高点（或最低点）离平衡位置的距离；
- $\omega$：看周期，$T=\frac{2\pi}{\omega}$，相邻最高点和最低点的横坐标差是 $\frac T2$；
- $\varphi$：代入一个特殊点（最高点、零点）解出来，注意题目给的 $\varphi$ 范围。

（下面高考题里的题 4 就是这个类型。）

### 三角函数的最值问题

三类常考：
- **辅助角型**：$a\sin x+b\cos x$ 用辅助角压成一个，最值 $\pm\sqrt{a^2+b^2}$；
- **二次型**：比如 $y=\sin^2x+\sin x+1$，换元 $t=\sin x$（$t\in[-1,1]$），变成二次函数在闭区间上求最值；混合 $\cos2x$、$\sin x$ 的先降幂统一成同名；
- **换元型**：$\sin x+\cos x$ 和 $\sin x\cos x$ 同时出现，设 $t=\sin x+\cos x$，则 $\sin x\cos x=\frac{t^2-1}{2}$。

### 高考真题练手（题目在下，答案在文末反向链接）

**题 1**（恒等变换 + 单调区间 + 值域）
已知函数 $f(x)=2\sin x\cos x+2\sqrt3\cos^2x-\sqrt3$。
（1）求 $f(x)$ 的单调递增区间；
（2）求 $f(x)$ 在 $[0,\frac{\pi}{2}]$ 上的值域。

**题 2**（给值求值，高考经典）
已知 $\cos(\frac{\pi}{4}+x)=\frac35$，$\frac{17\pi}{12}<x<\frac{7\pi}{4}$，求 $\dfrac{\sin2x+2\sin^2x}{1-\tan x}$ 的值。

**题 3**（图像变换）
把函数 $y=\sin2x$ 的图像上各点的横坐标变为原来的 $\frac12$（纵坐标不变），再把所得图像向右平移 $\frac{\pi}{4}$，求所得函数的解析式；并判断：如果先平移后伸缩，结果是否相同？

**题 4**（由图像求解析式 + 零点个数）
函数 $f(x)=A\sin(\omega x+\varphi)$（$A>0,\ \omega>0,\ |\varphi|<\frac{\pi}{2}$）的图像上，相邻的最高点为 $(\frac{\pi}{6},3)$、最低点为 $(\frac{2\pi}{3},-3)$。
（1）求 $f(x)$ 的解析式；
（2）求 $f(x)$ 在 $[0,2\pi]$ 上的零点个数。

**题 5**（含参方程，压轴风格）
已知关于 $x$ 的方程 $2\sin^2x-\sqrt3\sin2x=m$ 在 $[0,\pi]$ 上恰有两个不同的实数解，求 $m$ 的取值范围。

> 答案都放在 [[数学课堂展示/DAY14 三角函数答案]]，做完再对。单位圆演示在开头，转一圈就明白三角函数从哪来了。
