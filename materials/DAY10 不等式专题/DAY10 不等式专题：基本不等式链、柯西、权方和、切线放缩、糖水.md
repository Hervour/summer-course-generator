今天要用的就五个工具：基本不等式链、柯西、权方和、切线放缩、糖水。每个都先把结论写出来，再讲推导，推导看懂了就忘不了。

### 1，基本不等式链（均值不等式链）

设 $a,b>0$，四个平均数排成一串：
$$\frac{2}{\frac{1}{a}+\frac{1}{b}} \le \sqrt{ab} \le \frac{a+b}{2} \le \sqrt{\frac{a^2+b^2}{2}}$$
从左到右分别是：**调和平均、几何平均、算术平均、平方平均**。当且仅当 $a=b$ 时等号同时成立。

**推导，一步一步来**：

第一步，证 $\dfrac{a+b}{2}\ge\sqrt{ab}$。任何数的平方都 $\ge0$，所以
$$(\sqrt a-\sqrt b)^2\ge0$$
展开：
$$a+b-2\sqrt{ab}\ge0$$
移项：
$$a+b\ge2\sqrt{ab}$$
两边除以 2，就是 $\dfrac{a+b}{2}\ge\sqrt{ab}$。关键点：取 $\sqrt a$ 和 $\sqrt b$ 的差平方，正好能凑出 $\sqrt{ab}$。$a=b$ 时等号成立。

第二步，证 $\dfrac{2}{\frac1a+\frac1b}\le\sqrt{ab}$。把第一步的结论用到 $\frac1a$ 和 $\frac1b$ 上：
$$\frac{\frac1a+\frac1b}{2}\ge\sqrt{\frac1a\cdot\frac1b}=\frac{1}{\sqrt{ab}}$$
两边都是正数，取倒数（**注意：取倒数后不等号方向要反过来**）：
$$\frac{2}{\frac1a+\frac1b}\le\sqrt{ab}$$

第三步，证 $\dfrac{a+b}{2}\le\sqrt{\dfrac{a^2+b^2}{2}}$。还是从平方 $\ge0$ 出发：
$$(a-b)^2\ge0\ \Rightarrow\ a^2+b^2\ge2ab$$
两边同时加上 $a^2+b^2$：
$$2(a^2+b^2)\ge(a+b)^2$$
两边除以 4 再开方：
$$\frac{a+b}{2}\le\sqrt{\frac{a^2+b^2}{2}}$$

整条链的核心就第一步那个 $(\sqrt a-\sqrt b)^2\ge0$，把它背下来，其他两步都是代换。
![[均值不等式链几何解释.png]]

**简单例题**：$x,y>0$，$x+2y=1$，求 $\frac1x+\frac1y$ 的最小值
思路：$x+2y=1$，乘进去不改变值：
$$\frac1x+\frac1y=(x+2y)\left(\frac1x+\frac1y\right)=1+\frac{x}{y}+\frac{2y}{x}+2=3+\frac{x}{y}+\frac{2y}{x}$$
对 $\frac{x}{y}$ 和 $\frac{2y}{x}$ 用基本不等式（乘积是定值 2）：
$$\frac{x}{y}+\frac{2y}{x}\ge2\sqrt{\frac{x}{y}\cdot\frac{2y}{x}}=2\sqrt2$$
所以最小值是 $3+2\sqrt2$。取等条件 $\frac{x}{y}=\frac{2y}{x}$，即 $x=\sqrt2\,y$，代回 $x+2y=1$ 能取到。

### 2，柯西不等式

二维形式：
$$(a^2+b^2)(c^2+d^2)\ge(ac+bd)^2$$

**推导（直接展开，最直观）**：
左边减右边：
$$(a^2+b^2)(c^2+d^2)-(ac+bd)^2$$
先展开：
$$=a^2c^2+a^2d^2+b^2c^2+b^2d^2-(a^2c^2+2abcd+b^2d^2)$$
化简（$a^2c^2$ 和 $b^2d^2$ 抵消）：
$$=a^2d^2+b^2c^2-2abcd=(ad-bc)^2\ge0$$
所以左边 $\ge$ 右边。取等条件 $ad=bc$，也就是 $a:b=c:d$。

$n$ 元形式（做题直接背，证明思路一样只是展开麻烦）：
$$\left(\sum a_i^2\right)\left(\sum b_i^2\right)\ge\left(\sum a_ib_i\right)^2$$
一句话记法：**平方和 × 平方和 ≥ 乘积和的平方**。

**简单例题**：$x^2+y^2=1$，求 $2x+3y$ 的最大值
$$(2x+3y)^2\le(2^2+3^2)(x^2+y^2)=13\times1=13$$
所以 $2x+3y\le\sqrt{13}$。取等 $2:3=x:y$，即 $\frac{x}{y}=\frac23$，和 $x^2+y^2=1$ 联立能取到。

### 3，权方和不等式

$$ \frac{a^2}{x}+\frac{b^2}{y}\ge\frac{(a+b)^2}{x+y}\qquad(x,y>0)$$

**推导**：它是柯西的变身。把 $\frac{a^2}{x}$ 看成 $\left(\frac{a}{\sqrt x}\right)^2$，$x$ 看成 $(\sqrt x)^2$，然后对这两组数用柯西：
$$\left(\frac{a^2}{x}+\frac{b^2}{y}\right)(x+y)=\left[\left(\frac{a}{\sqrt x}\right)^2+\left(\frac{b}{\sqrt y}\right)^2\right]\left[(\sqrt x)^2+(\sqrt y)^2\right]$$
$$\ge\left(\frac{a}{\sqrt x}\cdot\sqrt x+\frac{b}{\sqrt y}\cdot\sqrt y\right)^2=(a+b)^2$$
两边除以 $x+y$：
$$\frac{a^2}{x}+\frac{b^2}{y}\ge\frac{(a+b)^2}{x+y}$$
取等条件从柯西的取等条件化简出来是 $\frac{a}{x}=\frac{b}{y}$。

用途：见到**分式相加、分子是二次、分母是一次**就用它。

**简单例题**：$x,y>0$，$x+y=1$，求 $\frac1x+\frac4y$ 的最小值
$$\frac1x+\frac4y=\frac{1^2}{x}+\frac{2^2}{y}\ge\frac{(1+2)^2}{x+y}=9$$
取等 $\frac1x=\frac2y$，即 $y=2x$，$x=\frac13,y=\frac23$，最小值 9。

### 4，切线放缩不等式

思想：曲线在某点的切线，要么一直在曲线下面，要么一直在曲线上面。用切线代替曲线，不等式就出来了。

**第一个结论：$e^x\ge x+1$（取等 $x=0$）**

推导：要证 $e^x\ge x+1$，等价于证 $e^x-x-1\ge0$。设
$$f(x)=e^x-x-1$$
求导：
$$f'(x)=e^x-1$$
令 $f'(x)=0$，得 $x=0$。再看 $f'$ 的符号：
- $x<0$ 时，$e^x<1$，$f'(x)<0$，$f$ 递减；
- $x>0$ 时，$e^x>1$，$f'(x)>0$，$f$ 递增。
所以 $f$ 在 $x=0$ 取最小值，$f(0)=e^0-0-1=0$。于是 $f(x)\ge0$ 恒成立，即
$$e^x\ge x+1$$

为什么叫切线：$y=x+1$ 正好是 $y=e^x$ 在点 $(0,1)$ 处的切线（斜率 $e^0=1$）。$e^x$ 是凸函数，图像一直在切线上方，所以 $e^x\ge$ 切线。

**第二个结论：$\ln x\le x-1$（取等 $x=1$）**

推导：设
$$g(x)=\ln x-x+1$$
求导：
$$g'(x)=\frac1x-1=\frac{1-x}{x}$$
令 $g'(x)=0$，得 $x=1$：
- $0<x<1$ 时，$\frac1x>1$，$g'(x)>0$，$g$ 递增；
- $x>1$ 时，$\frac1x<1$，$g'(x)<0$，$g$ 递减。
所以 $g$ 在 $x=1$ 取最大值，$g(1)=0$。故 $g(x)\le0$，即
$$\ln x\le x-1$$
![[切线放缩.png]]

**三个常用变形（推导就是换元，考试直接背结论）**：
- $e^x\ge ex$：把 $e^x\ge x+1$ 里的 $x$ 换成 $x-1$，得 $e^{x-1}\ge x$，两边乘 $e$。
- $\ln x\le\frac{x}{e}$：把 $\ln x\le x-1$ 里的 $x$ 换成 $\frac{x}{e}$，$\ln\frac{x}{e}\le\frac{x}{e}-1$，即 $\ln x-1\le\frac{x}{e}-1$，化简。
- $\ln x\ge1-\frac1x$：把 $\ln x\le x-1$ 里的 $x$ 换成 $\frac1x$，$\ln\frac1x\le\frac1x-1$，即 $-\ln x\le\frac1x-1$，移项。

**简单例题**：求 $f(x)=e^x-x$ 的最小值
$f'(x)=e^x-1$，$x=0$ 处取最小值 $f(0)=1$。这就是 $e^x\ge x+1$ 的另一种说法。

### 5，糖水不等式

$b$ 克糖溶在 $a$ 克水里（$0<b<a$），浓度是 $\frac{b}{a}$；再加 $m$ 克糖，浓度变成 $\frac{b+m}{a+m}$。直觉上糖水变甜了，也就是
$$\frac{b}{a}<\frac{b+m}{a+m}$$

**推导（作差法，通分）**：
$$\frac{b+m}{a+m}-\frac{b}{a}=\frac{a(b+m)-b(a+m)}{a(a+m)}$$
展开分子：
$$=\frac{ab+am-ab-bm}{a(a+m)}=\frac{m(a-b)}{a(a+m)}$$
因为 $m>0$、$a>0$、$a+m>0$、$a-b>0$，所以这个差 $>0$，证完。

**简单例题**：比较 $\frac{2010}{2011}$ 和 $\frac{2011}{2012}$
$0<2010<2011$，加 $m=1$：$\frac{2010}{2011}<\frac{2010+1}{2011+1}=\frac{2011}{2012}$。

### 小结：看到结构，想到工具
- 和定求积最大 / 积定求和最小 → 基本不等式链
- 平方和 → 柯西
- 分式相加 → 权方和
- 含 $e^x$、$\ln x$ → 切线放缩
- 分数比大小 → 糖水

### 今日任务
五个不等式的推导自己各写一遍，别背结论，能推出来才算会。

