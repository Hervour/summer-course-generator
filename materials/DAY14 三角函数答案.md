# DAY14 三角函数答案

> 这是 [[DAY14 三角函数进阶与高考题]] 的答案，做完题再来看。

### 题 1 答案

先化简：
$$f(x)=2\sin x\cos x+2\sqrt3\cos^2x-\sqrt3=\sin2x+\sqrt3(1+\cos2x)-\sqrt3=\sin2x+\sqrt3\cos2x=2\sin\left(2x+\frac{\pi}{3}\right)$$

（1）单调递增区间：
$$-\frac{\pi}{2}+2k\pi\le2x+\frac{\pi}{3}\le\frac{\pi}{2}+2k\pi$$
解得
$$-\frac{5\pi}{12}+k\pi\le x\le\frac{\pi}{12}+k\pi,\quad k\in\mathbb{Z}$$

（2）$x\in[0,\frac{\pi}{2}]$ 时，$2x+\frac{\pi}{3}\in[\frac{\pi}{3},\frac{4\pi}{3}]$。
- 当 $2x+\frac{\pi}{3}=\frac{\pi}{2}$（$x=\frac{\pi}{12}$）时取最大值 $2$；
- 当 $2x+\frac{\pi}{3}=\frac{4\pi}{3}$（$x=\frac{\pi}{2}$）时取最小值 $2\sin\frac{4\pi}{3}=-\sqrt3$。
所以值域 $[-\sqrt3,2]$。

### 题 2 答案

设 $\theta=\frac{\pi}{4}+x$。由 $x\in(\frac{17\pi}{12},\frac{7\pi}{4})$ 得 $\theta\in(\frac{5\pi}{3},2\pi)$，是第四象限角，所以 $\cos\theta=\frac35$，$\sin\theta=-\frac45$。

$$
\sin2x=\sin\left(2\theta-\frac{\pi}{2}\right)=-\cos2\theta=-(2\cos^2\theta-1)=-\left(\frac{18}{25}-1\right)=\frac{7}{25}
$$

$$
\cos2x=\cos\left(2\theta-\frac{\pi}{2}\right)=\sin2\theta=2\sin\theta\cos\theta=-\frac{24}{25}
$$

$$
\sin^2x=\frac{1-\cos2x}{2}=\frac{1+\frac{24}{25}}{2}=\frac{49}{50}
$$

$$
\tan\theta=\frac{\sin\theta}{\cos\theta}=-\frac43,\qquad \tan x=\tan\left(\theta-\frac{\pi}{4}\right)=\frac{\tan\theta-1}{1+\tan\theta}=\frac{-\frac43-1}{1-\frac43}=7
$$

原式：
$$
\frac{\sin2x+2\sin^2x}{1-\tan x}=\frac{\frac{7}{25}+2\times\frac{49}{50}}{1-7}=\frac{\frac{56}{25}}{-6}=-\frac{28}{75}
$$

答案：$-\dfrac{28}{75}$。

### 题 3 答案

先伸缩：横坐标变为原来的 $\frac12$，$y=\sin2x\to y=\sin4x$。
再平移：向右平移 $\frac{\pi}{4}$，$y=\sin4\left(x-\frac{\pi}{4}\right)=\sin(4x-\pi)$。

如果顺序反过来：先右移 $\frac{\pi}{4}$，$y=\sin2\left(x-\frac{\pi}{4}\right)=\sin\left(2x-\frac{\pi}{2}\right)$；再横坐标变 $\frac12$，$y=\sin\left(4x-\frac{\pi}{2}\right)$。

结果不同，说明变换的次序不能乱：**先伸缩后平移，平移量要跟着 $\omega$ 变**。

### 题 4 答案

（1）相邻最高点、最低点横坐标差
$$\frac{2\pi}{3}-\frac{\pi}{6}=\frac{\pi}{2}=\frac{T}{2}$$
所以 $T=\pi$，$\omega=\frac{2\pi}{T}=2$。最高点纵坐标为 3，所以 $A=3$。

代入最高点 $\left(\frac{\pi}{6},3\right)$：
$$3\sin\left(2\times\frac{\pi}{6}+\varphi\right)=3\ \Rightarrow\ \frac{\pi}{3}+\varphi=\frac{\pi}{2}+2k\pi\ \Rightarrow\ \varphi=\frac{\pi}{6}$$
所以 $f(x)=3\sin\left(2x+\frac{\pi}{6}\right)$。

（2）零点：$\sin\left(2x+\frac{\pi}{6}\right)=0$，即
$$2x+\frac{\pi}{6}=k\pi\ \Rightarrow\ x=\frac{k\pi}{2}-\frac{\pi}{12}$$
在 $[0,2\pi]$ 内取 $k=1,2,3,4$：
$$x=\frac{5\pi}{12},\ \frac{11\pi}{12},\ \frac{17\pi}{12},\ \frac{23\pi}{12}$$
共 **4 个零点**。

### 题 5 答案

先化简左边：
$$2\sin^2x-\sqrt3\sin2x=(1-\cos2x)-\sqrt3\sin2x=1-(\cos2x+\sqrt3\sin2x)=1-2\sin\left(2x+\frac{\pi}{6}\right)$$
原方程变为
$$\sin\left(2x+\frac{\pi}{6}\right)=\frac{1-m}{2}$$

$x\in[0,\pi]$ 时，令 $t=2x+\frac{\pi}{6}$，则 $t\in[\frac{\pi}{6},\frac{13\pi}{6}]$。记 $c=\frac{1-m}{2}$，数 $\sin t=c$ 在 $t\in[\frac{\pi}{6},\frac{13\pi}{6}]$ 上的解：
- $c=1$（$m=-1$）：$t=\frac{\pi}{2}$，1 个解；
- $c=-1$（$m=3$）：$t=\frac{3\pi}{2}$，1 个解；
- $c=\frac12$（$m=0$）：$t=\frac{\pi}{6},\frac{5\pi}{6},\frac{13\pi}{6}$，3 个解；
- 其余 $c\in(-1,1)$：2 个解。

所以恰有两个不同实数解 $\Leftrightarrow m\in(-1,3)$ 且 $m\ne0$。

答案：$m\in(-1,3)$ 且 $m\ne0$。
