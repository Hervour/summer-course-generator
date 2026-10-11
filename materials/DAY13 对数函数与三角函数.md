今天把两个大块一次性讲完：对数函数和三角函数。对数这块会把运算规则一条条推导清楚，三角函数从角的概念一直讲到图像性质，内容多，但是一步一步来，不难。

## 对数函数

### 对数的来历和定义

指数函数解决的是"知道底数和指数，求幂"；对数反过来，**知道底数和幂，求指数**。比如 $2^x=8$，x 是多少？x=3。这个"求指数"的运算就是对数。

定义：$a>0$，$a\ne1$，$N>0$，如果 $a^x=N$，就说 $x$ 是以 $a$ 为底 $N$ 的对数，记作
$$x=\log_a N$$
$a$ 叫**底数**，$N$ 叫**真数**。指数式和对数式是同一件事的两种写法：
$$a^x=N \iff x=\log_a N$$
两个特殊的对数，背下来：
$$\log_a 1=0,\qquad \log_a a=1$$
由定义还能得到两个恒等式：
$$a^{\log_a N}=N,\qquad \log_a a^x=x$$
**简单例题**：把 $5^3=125$ 写成对数式；把 $\log_2 16=4$ 写成指数式
$5^3=125 \iff \log_5 125=3$；$\log_2 16=4 \iff 2^4=16$。

### 对数的运算法则（重点，每条都会推）

先记住口诀：**乘变加、除变减、次方提前面**。下面每条都推导一遍，推导看懂了就不会忘。

法则一（积的对数）：
$$\log_a(MN)=\log_a M+\log_a N$$
推导：设 $\log_a M=p$，$\log_a N=q$，那么 $a^p=M$，$a^q=N$。于是
$$MN=a^p\cdot a^q=a^{p+q}$$
两边取以 $a$ 为底的对数：$\log_a(MN)=p+q$，也就是 $\log_a M+\log_a N$。证完。

法则二（商的对数）：
$$\log_a\frac{M}{N}=\log_a M-\log_a N$$
推导：同样设 $a^p=M$，$a^q=N$，则
$$\frac{M}{N}=\frac{a^p}{a^q}=a^{p-q}$$
取对数得 $\log_a\frac{M}{N}=p-q=\log_a M-\log_a N$。

法则三（幂的对数）：
$$\log_a M^n=n\log_a M$$
推导：$\log_a M^n=\log_a(\underbrace{M\cdot M\cdots M}_{n\text{个}})=\underbrace{\log_a M+\cdots+\log_a M}_{n\text{个}}=n\log_a M$。

注意：$\log_a(M+N)$ **不能拆**！真数里的加减法没有公式，这是最容易错的地方。

**换底公式**（也很重要）：
$$\log_a b=\frac{\log_c b}{\log_c a}$$
推导：设 $\log_a b=x$，则 $a^x=b$。两边取以 $c$ 为底的对数：
$$x\log_c a=\log_c b$$
解出 $x$ 就是换底公式。两个常用推论：
$$\log_a b\cdot\log_b a=1,\qquad \log_{a^m}b^n=\frac{n}{m}\log_a b$$

**简单例题**：
（1）$\log_2 6-\log_2 3=\log_2\frac63=\log_2 2=1$
（2）$\lg 25+\lg 4=\lg 100=2$
（3）$\log_3 27=\log_3 3^3=3$
（4）化简 $\log_2 5+\log_2 0.2$：$5\times0.2=1$，所以 $\log_2 5+\log_2 0.2=\log_2 1=0$。
（5）用换底公式算 $\log_4 8$：$\log_4 8=\frac{\log_2 8}{\log_2 4}=\frac32$。

### 对数函数的性质

$y=\log_a x$（$a>0$ 且 $a\ne1$）是对数函数，它是指数函数 $y=a^x$ 的反函数，图像关于 $y=x$ 对称。性质一条条过：

- **定义域**：$(0,+\infty)$。真数必须大于 0，这是求定义域最常见的坑；
- **值域**：$\mathbb{R}$，随便一个实数都能当对数值；
- **过定点**：$(1,0)$，因为 $\log_a 1=0$，跟底数无关；
- **单调性**：$a>1$ 在 $(0,+\infty)$ 上递增，$0<a<1$ 递减；
- **奇偶性**：非奇非偶；
- **渐近线**：$y$ 轴，图像无限接近但碰不到（$x\to0^+$ 时 $\log_a x\to-\infty$ 或 $+\infty$）；
- **底数的影响**：$a>1$ 时，底数越大，$x>1$ 的部分图像越靠近 $x$ 轴；$0<a<1$ 时，底数越小，$0<x<1$ 的部分越靠近 $x$ 轴。说白了底数大小决定图像"趴"得平不平。

**比较大小的套路**（对数版）：
- 同底：直接用单调性；
- 同真数不同底：用换底公式或者画图，比如 $\log_2 3$ 和 $\log_3 3=1$……不对，同真数比的是 $\log_2 3$ 和 $\log_4 3$，底数越大（都大于 1）值越小，因为 $2^x=3$ 比 $4^x=3$ 需要的指数大；
- 不同底不同真：找中间值 0 和 1，比如 $\log_2 0.3<0<1<\log_2 3$。

**简单例题**：求 $y=\log_2(x^2-3x+2)$ 的定义域
真数 $x^2-3x+2>0$，即 $(x-1)(x-2)>0$，解得 $x<1$ 或 $x>2$。定义域 $(-\infty,1)\cup(2,+\infty)$。

**想一想**：$y=\log_{\frac12} x$ 是增函数还是减函数？它和 $y=\log_2 x$ 的图像有什么关系？

## 三角函数

### 任意角与弧度制

初中学的角都是 $0°$ 到 $360°$，不够用。把角的概念推广：按逆时针转出来的角叫**正角**，顺时针转的叫**负角**，不转的叫**零角**。这样角可以任意大，也可以为负。

终边相同的角：和角 $\alpha$ 终边相同的角可以写成
$$\beta=\alpha+2k\pi,\quad k\in\mathbb{Z}$$
（用角度制就是 $\alpha+k\cdot360°$）。

**弧度制**：把弧长等于半径的弧所对的圆心角规定为 1 弧度。于是
$$180°=\pi\ \text{弧度}$$
换算公式：$1°=\frac{\pi}{180}$ 弧度，$1$ 弧度 $=\frac{180°}{\pi}$。

弧长公式和扇形面积公式（注意这里的角必须用弧度制）：
$$l=|\alpha|r,\qquad S=\frac12 lr=\frac12|\alpha|r^2$$

**简单例题**：$60°$ 化成弧度是多少？半径 $r=3$、圆心角 $\frac{\pi}{3}$ 的扇形面积？
$60°=\frac{\pi}{3}$。$S=\frac12|\alpha|r^2=\frac12\cdot\frac{\pi}{3}\cdot9=\frac{3\pi}{2}$。

### 任意角的三角函数（单位圆定义）

在单位圆上，角 $\alpha$ 的终边与圆交于点 $P(x,y)$，规定：
$$\sin\alpha=y,\qquad \cos\alpha=x,\qquad \tan\alpha=\frac{y}{x}\ (x\ne0)$$
这样定义的好处是角可以任意大，三角函数值由终边位置决定。

**各象限的符号**，口诀「一全正、二正弦、三正切、四余弦」：
- 第一象限：$\sin$、$\cos$、$\tan$ 全正；
- 第二象限：只有 $\sin$ 正；
- 第三象限：只有 $\tan$ 正；
- 第四象限：只有 $\cos$ 正。

**同角三角函数关系**（两条，做题随时用）：
$$\sin^2\alpha+\cos^2\alpha=1,\qquad \tan\alpha=\frac{\sin\alpha}{\cos\alpha}$$

**简单例题**：已知 $\sin\alpha=\frac35$，$\alpha$ 在第二象限，求 $\cos\alpha$ 和 $\tan\alpha$
$\cos^2\alpha=1-\frac{9}{25}=\frac{16}{25}$，第二象限 $\cos<0$，所以 $\cos\alpha=-\frac45$。$\tan\alpha=\frac{\sin\alpha}{\cos\alpha}=-\frac34$。

### 诱导公式

诱导公式就是把大角化成锐角来算。口诀只有两句：**奇变偶不变，符号看象限**。
意思是：$\frac{\pi}{2}$ 的奇数倍变名（$\sin$ 变 $\cos$，$\cos$ 变 $\sin$，$\tan$ 变 $\cot$ 之类），偶数倍不变名；然后把 $\alpha$ 当成锐角，看原函数在对应象限的符号。

常用的几条（都要熟）：
- $\sin(-\alpha)=-\sin\alpha$，$\cos(-\alpha)=\cos\alpha$（负角）
- $\sin(\pi-\alpha)=\sin\alpha$，$\cos(\pi-\alpha)=-\cos\alpha$
- $\sin(\pi+\alpha)=-\sin\alpha$，$\cos(\pi+\alpha)=-\cos\alpha$
- $\sin(\frac{\pi}{2}-\alpha)=\cos\alpha$，$\cos(\frac{\pi}{2}-\alpha)=\sin\alpha$
- $\sin(\frac{\pi}{2}+\alpha)=\cos\alpha$，$\cos(\frac{\pi}{2}+\alpha)=-\sin\alpha$

**简单例题**：化简 $\sin(\pi+\alpha)$
$\pi$ 是 $\frac{\pi}{2}$ 的 2 倍（偶数），不变名，还是 $\sin$；把 $\alpha$ 当锐角，$\pi+\alpha$ 在第三象限，$\sin$ 为负。所以 $\sin(\pi+\alpha)=-\sin\alpha$。

### 两角和差、二倍角、辅助角

和差公式：
$$\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$$
$$\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$$
$$\tan(\alpha\pm\beta)=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$$

二倍角（由和差公式令 $\beta=\alpha$ 得到）：
$$\sin2\alpha=2\sin\alpha\cos\alpha$$
$$\cos2\alpha=\cos^2\alpha-\sin^2\alpha=2\cos^2\alpha-1=1-2\sin^2\alpha$$
$$\tan2\alpha=\frac{2\tan\alpha}{1-\tan^2\alpha}$$
$\cos2\alpha$ 的三个形式里，后两个常用于降幂：$\cos^2\alpha=\frac{1+\cos2\alpha}{2}$，$\sin^2\alpha=\frac{1-\cos2\alpha}{2}$。

辅助角公式（把两个三角函数的和压成一个）：
$$a\sin x+b\cos x=\sqrt{a^2+b^2}\sin(x+\varphi),\qquad \tan\varphi=\frac{b}{a}$$
由此立刻得到最值：
$$-\sqrt{a^2+b^2}\le a\sin x+b\cos x\le\sqrt{a^2+b^2}$$

**简单例题**：化简 $y=\sin x+\sqrt3\cos x$ 并求最大值
$y=2\sin(x+\frac{\pi}{3})$，最大值 2，取等 $x+\frac{\pi}{3}=\frac{\pi}{2}+2k\pi$。

### 三角函数的图像与性质（重点，逐条背）

**正弦函数 $y=\sin x$**：
- 定义域 $\mathbb{R}$，值域 $[-1,1]$；
- 周期 $2\pi$，奇函数（图像关于原点对称）；
- 单调递增区间 $[-\frac{\pi}{2}+2k\pi,\ \frac{\pi}{2}+2k\pi]$；
- 单调递减区间 $[\frac{\pi}{2}+2k\pi,\ \frac{3\pi}{2}+2k\pi]$；
- 最大值 1：$x=\frac{\pi}{2}+2k\pi$；最小值 −1：$x=-\frac{\pi}{2}+2k\pi$；
- 对称轴 $x=\frac{\pi}{2}+k\pi$（过最高点或最低点）；
- 对称中心 $(k\pi,0)$。

**余弦函数 $y=\cos x$**：
- 定义域 $\mathbb{R}$，值域 $[-1,1]$；
- 周期 $2\pi$，偶函数（关于 $y$ 轴对称）；
- 单调递增区间 $[-\pi+2k\pi,\ 2k\pi]$；单调递减区间 $[2k\pi,\ \pi+2k\pi]$；
- 对称轴 $x=k\pi$；对称中心 $(\frac{\pi}{2}+k\pi,0)$。

**正切函数 $y=\tan x$**：
- 定义域 $x\ne\frac{\pi}{2}+k\pi$，值域 $\mathbb{R}$；
- 周期 $\pi$，奇函数；
- 在 $(-\frac{\pi}{2}+k\pi,\ \frac{\pi}{2}+k\pi)$ 上单调递增（没有单调递减区间）；
- 对称中心 $(\frac{k\pi}{2},0)$；
- 渐近线 $x=\frac{\pi}{2}+k\pi$。

**五点作图法**：画 $y=\sin x$ 一个周期，取五个关键点：$(0,0)$、$(\frac{\pi}{2},1)$、$(\pi,0)$、$(\frac{3\pi}{2},-1)$、$(2\pi,0)$，描点连线就是正弦曲线。

**$y=A\sin(\omega x+\varphi)$ 的图像**：
- $A$ 管振幅（最高点离平衡位置的距离），$\omega$ 管周期 $T=\frac{2\pi}{|\omega|}$，$\varphi$ 管左右平移；
- 平移伸缩的次序要注意：先平移后伸缩，和先伸缩后平移，平移的量不一样，做题时画图验证最稳；
- 由图像求解析式：从最高点最低点读 $A$，从相邻关键点读周期再算 $\omega$，代入一个点解 $\varphi$。

**简单例题**：$y=2\sin(2x+\frac{\pi}{3})$，求周期、最大值、单调递增区间
周期 $T=\frac{2\pi}{2}=\pi$。最大值 2，此时 $2x+\frac{\pi}{3}=\frac{\pi}{2}+2k\pi$，即 $x=\frac{\pi}{12}+k\pi$。单调递增：$-\frac{\pi}{2}+2k\pi\le2x+\frac{\pi}{3}\le\frac{\pi}{2}+2k\pi$，解得 $-\frac{5\pi}{12}+k\pi\le x\le\frac{\pi}{12}+k\pi$。

**想一想**：$y=\cos x$ 的图像可以由 $y=\sin x$ 的图像怎么平移得到？提示：$\cos x=\sin(x+\frac{\pi}{2})$。

### 今日任务
把对数的三个运算法则和换底公式各推导一遍；诱导公式按"奇变偶不变，符号看象限"自己推一遍；把 $\sin$、$\cos$、$\tan$ 的图像各画一个周期，旁边标全定义域、值域、周期、单调区间、对称轴、对称中心；做三道化简求值的题。
