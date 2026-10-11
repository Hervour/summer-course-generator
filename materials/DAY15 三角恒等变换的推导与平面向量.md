今天讲三大块，顺序是：向量 → 正弦定理和余弦定理 → 三角恒等变换的推导。向量是工具，后两块全靠它推；恒等变换的公式看着多，其实只需要记住最核心的一个，其他全是它推出来的。

## 一、高中向量

### 向量的概念

**向量**：既有大小又有方向的量，用有向线段表示，记作 $\vec a$ 或 $\overrightarrow{AB}$。大小叫**模**，记 $|\vec a|$。
- **零向量**：$\vec 0$，模为 0，方向任意；
- **单位向量**：模为 1 的向量；
- **相等向量**：大小相等、方向相同；
- **平行（共线）向量**：方向相同或相反，记 $\vec a\parallel\vec b$。注意零向量和任何向量都平行。

### 向量的加减法与数乘

**加法**两个法则：
- 三角形法则：$\vec a+\vec b$，把 $\vec b$ 的起点放 $\vec a$ 的终点，和向量从 $\vec a$ 的起点指向 $\vec b$ 的终点；
- 平行四边形法则：两个向量共起点作平行四边形，对角线就是和。

**减法**：$\vec a-\vec b=\vec a+(-\vec b)$，几何上"共起点，指向被减向量"。

**数乘**：$\lambda\vec a$，模变成 $|\lambda||\vec a|$；$\lambda>0$ 同向，$\lambda<0$ 反向，$\lambda=0$ 得零向量。

**共线定理**（很重要）：$\vec a\ne\vec 0$ 时，
$$\vec a\parallel\vec b \iff \vec b=\lambda\vec a\ (\lambda\text{ 唯一})$$

### 平面向量基本定理与坐标

**基本定理**：$\vec e_1,\vec e_2$ 不共线，则任意向量 $\vec a$ 能唯一表示成
$$\vec a=x\vec e_1+y\vec e_2$$
$(x,y)$ 就是 $\vec a$ 在基底下的**坐标**。以后默认取互相垂直的单位向量做基底，就是直角坐标。

坐标运算（$\vec a=(x_1,y_1)$，$\vec b=(x_2,y_2)$）：
$$\vec a\pm\vec b=(x_1\pm x_2,\ y_1\pm y_2),\qquad \lambda\vec a=(\lambda x_1,\lambda y_1)$$
$$|\vec a|=\sqrt{x_1^2+y_1^2}$$
两点向量：$\overrightarrow{AB}=(x_B-x_A,\ y_B-y_A)$。
中点坐标：$M=\left(\frac{x_1+x_2}{2},\frac{y_1+y_2}{2}\right)$。
平行判定：$\vec a\parallel\vec b \iff x_1y_2-x_2y_1=0$。

**简单例题**：$\vec a=(1,2)$，$\vec b=(x,4)$ 平行，求 $x$
$1\times4-2x=0$，$x=2$。

### 向量的数量积（点乘）

**定义**：
$$\vec a\cdot\vec b=|\vec a||\vec b|\cos\theta$$
$\theta$ 是两向量夹角（$0\le\theta\le\pi$）。结果是个**数**，不是向量。

**坐标公式**：
$$\vec a\cdot\vec b=x_1x_2+y_1y_2$$

**几何意义**：$\vec b$ 在 $\vec a$ 方向上的投影是 $|\vec b|\cos\theta$，所以 $\vec a\cdot\vec b$ 等于"$\vec a$ 的模 × $\vec b$ 在 $\vec a$ 方向上的投影"。

**常用性质**：
- $\vec a\cdot\vec a=|\vec a|^2$，所以 $|\vec a|=\sqrt{\vec a\cdot\vec a}$；
- 垂直：$\vec a\perp\vec b \iff \vec a\cdot\vec b=0$；
- 夹角：$\cos\theta=\frac{\vec a\cdot\vec b}{|\vec a||\vec b|}$；
- 两个非零向量夹角为锐角 $\iff\vec a\cdot\vec b>0$，钝角 $\iff\vec a\cdot\vec b<0$。

**简单例题**：$\vec a=(1,2)$，$\vec b=(3,-1)$，求 $\vec a\cdot\vec b$、$|\vec a|$、两向量夹角余弦
$\vec a\cdot\vec b=1\times3+2\times(-1)=1$。
$|\vec a|=\sqrt{1+4}=\sqrt5$，$|\vec b|=\sqrt{9+1}=\sqrt{10}$。
$\cos\theta=\frac{1}{\sqrt5\cdot\sqrt{10}}=\frac{1}{\sqrt{50}}=\frac{\sqrt2}{10}$。

### 向量的应用

- **证明垂直**：算点乘等于 0；
- **证明平行/三点共线**：$\overrightarrow{AB}\parallel\overrightarrow{AC}$，说明 A、B、C 共线；
- **求夹角、求模**：套公式；
- **几何题**：把线段看成向量，中点、重心都能用向量表示，比如 $\overrightarrow{OA}+\overrightarrow{OB}=2\overrightarrow{OM}$（M 是 AB 中点）；
- **预告第三部分**：$A=(\cos\alpha,\sin\alpha)$、$B=(\cos\beta,\sin\beta)$ 看成单位圆上的向量，点乘一步就推出 $\cos(\alpha-\beta)$，恒等变换和向量是打通的。

**想一想**：$|\vec a+\vec b|=|\vec a-\vec b|$ 能推出 $\vec a\perp\vec b$ 吗？提示：两边平方。

## 二、正弦定理和余弦定理（解三角形）

这块严格说是高一**下学期**（必修第二册）的内容，但它和向量是同一章，两个定理都能用向量推，正好放今天讲。

### 正弦定理

$$\frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C}=2R$$

$a,b,c$ 分别是角 $A,B,C$ 的对边，$R$ 是外接圆半径。

**推导（面积法，最直观）**：同一个三角形的面积有三种写法：
$$S=\frac12 bc\sin A=\frac12 ac\sin B=\frac12 ab\sin C$$
三个式子相等，同除以 $\frac12abc$：
$$\frac{\sin A}{a}=\frac{\sin B}{b}=\frac{\sin C}{c}$$
倒过来就是正弦定理。所以正弦定理的本质是"面积怎么算都一样"。
（外接圆版本 $a=2R\sin A$ 由"直径所对圆周角是直角"得到。）

**什么时候用**：
- 已知两角一边，求其他边角；
- 已知两边和其中一边的对角，这时可能有两解，要讨论。

### 余弦定理

$$a^2=b^2+c^2-2bc\cos A$$

其余两条轮换字母：$b^2=a^2+c^2-2ac\cos B$，$c^2=a^2+b^2-2ab\cos C$。

**推导（向量法，呼应今天的向量）**：把 $BC$ 看成两个向量的差：
$$\overrightarrow{BC}=\overrightarrow{AC}-\overrightarrow{AB}$$
两边自己点乘自己（平方）：
$$a^2=|\overrightarrow{BC}|^2=|\overrightarrow{AC}-\overrightarrow{AB}|^2=|\overrightarrow{AC}|^2+|\overrightarrow{AB}|^2-2\overrightarrow{AC}\cdot\overrightarrow{AB}$$
其中 $|\overrightarrow{AC}|=b$，$|\overrightarrow{AB}|=c$，$\overrightarrow{AC}\cdot\overrightarrow{AB}=bc\cos A$，于是
$$a^2=b^2+c^2-2bc\cos A$$

**推论（求角）**：
$$\cos A=\frac{b^2+c^2-a^2}{2bc}$$

**什么时候用**：
- 已知三边求角；
- 已知两边和夹角，求第三边；
- 判断三角形形状：最大边 $a$ 满足 $a^2=b^2+c^2$ 是直角，$a^2>b^2+c^2$ 是钝角，$a^2<b^2+c^2$ 是锐角。

**简单例题**：
（1）$A=60°$，$B=45°$，$a=2$，求 $b$
由正弦定理 $\dfrac{a}{\sin A}=\dfrac{b}{\sin B}$：
$$b=\frac{a\sin B}{\sin A}=\frac{2\times\frac{\sqrt2}{2}}{\frac{\sqrt3}{2}}=\frac{2\sqrt6}{3}$$

（2）$a=5$，$b=7$，$C=60°$，求 $c$
由余弦定理：
$$c^2=5^2+7^2-2\times5\times7\times\cos60°=25+49-35=39,\qquad c=\sqrt{39}$$

（3）三边是 3、4、5，判断三角形形状
$5^2=3^2+4^2$，是直角三角形。

**想一想**：已知三边求角用哪个定理？已知两边和夹角求第三边用哪个？
## 三、三角恒等变换是怎么推导出来的

### 一切的起点：cos(α−β)

所有公式都从它出发。推导方法用单位圆，过程如下。

在单位圆上取两个点：
$$A=(\cos\alpha,\ \sin\alpha),\qquad B=(\cos\beta,\ \sin\beta)$$
半径 $OA=OB=1$，两半径的夹角是 $\alpha-\beta$。

先按"坐标距离"算 AB 的长度平方：
$$AB^2=(\cos\alpha-\cos\beta)^2+(\sin\alpha-\sin\beta)^2$$
展开：
$$=\cos^2\alpha-2\cos\alpha\cos\beta+\cos^2\beta+\sin^2\alpha-2\sin\alpha\sin\beta+\sin^2\beta$$
用 $\sin^2+\cos^2=1$ 合并：
$$=2-2(\cos\alpha\cos\beta+\sin\alpha\sin\beta)$$

再用"余弦定理"（$OA=OB=1$，夹角 $\alpha-\beta$）算一遍：
$$AB^2=1^2+1^2-2\cdot1\cdot1\cos(\alpha-\beta)=2-2\cos(\alpha-\beta)$$

两个式子说的是同一个 AB²，相等：
$$2-2(\cos\alpha\cos\beta+\sin\alpha\sin\beta)=2-2\cos(\alpha-\beta)$$
所以
$$\boxed{\cos(\alpha-\beta)=\cos\alpha\cos\beta+\sin\alpha\sin\beta}$$

这就是所有恒等变换的老祖宗。

hint：其实还有更快的推法——把 $A$、$B$ 看成向量，用点乘：
$$\vec{OA}\cdot\vec{OB}=\cos\alpha\cos\beta+\sin\alpha\sin\beta=|\vec{OA}||\vec{OB}|\cos(\alpha-\beta)=\cos(\alpha-\beta)$$
一步到位。上面向量部分讲过点乘，这条你应该能直接看懂。

### 从它推出所有公式

**1，cos(α+β)**：把上面公式里的 $\beta$ 换成 $-\beta$：
$$\cos(\alpha+\beta)=\cos\alpha\cos(-\beta)+\sin\alpha\sin(-\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$$

**2，sin(α+β)**：用"余角"公式 $\sin\theta=\cos(\frac{\pi}{2}-\theta)$：
$$\sin(\alpha+\beta)=\cos\left(\frac{\pi}{2}-\alpha-\beta\right)=\cos\left((\frac{\pi}{2}-\alpha)-\beta\right)$$
套 cos 的差公式：
$$=\cos(\frac{\pi}{2}-\alpha)\cos\beta+\sin(\frac{\pi}{2}-\alpha)\sin\beta=\sin\alpha\cos\beta+\cos\alpha\sin\beta$$

**3，sin(α−β)**：把 $\beta$ 换成 $-\beta$：
$$\sin(\alpha-\beta)=\sin\alpha\cos\beta-\cos\alpha\sin\beta$$

**4，tan(α+β)**：用 $\tan=\frac{\sin}{\cos}$，分子分母同除以 $\cos\alpha\cos\beta$：
$$\tan(\alpha+\beta)=\frac{\sin\alpha\cos\beta+\cos\alpha\sin\beta}{\cos\alpha\cos\beta-\sin\alpha\sin\beta}=\frac{\tan\alpha+\tan\beta}{1-\tan\alpha\tan\beta}$$

**5，二倍角**：令 $\beta=\alpha$ 直接得到：
$$\sin2\alpha=2\sin\alpha\cos\alpha$$
$$\cos2\alpha=\cos^2\alpha-\sin^2\alpha=2\cos^2\alpha-1=1-2\sin^2\alpha$$
$$\tan2\alpha=\frac{2\tan\alpha}{1-\tan^2\alpha}$$

**6，降幂公式**：把 $\cos2\alpha$ 的两个形式倒过来：
$$\cos^2\alpha=\frac{1+\cos2\alpha}{2},\qquad \sin^2\alpha=\frac{1-\cos2\alpha}{2}$$
见到平方就降幂，做题很有用。

**7，辅助角公式**：
$$a\sin x+b\cos x=\sqrt{a^2+b^2}\sin(x+\varphi),\qquad \tan\varphi=\frac{b}{a}$$
推导：提 $\sqrt{a^2+b^2}$ 出来，
$$a\sin x+b\cos x=\sqrt{a^2+b^2}\left(\frac{a}{\sqrt{a^2+b^2}}\sin x+\frac{b}{\sqrt{a^2+b^2}}\cos x\right)$$
令 $\cos\varphi=\frac{a}{\sqrt{a^2+b^2}}$、$\sin\varphi=\frac{b}{\sqrt{a^2+b^2}}$，括号里就是 $\cos\varphi\sin x+\sin\varphi\cos x=\sin(x+\varphi)$。

**8，和差化积**（了解即可）：令 $\alpha=\frac{A+B}{2}$、$\beta=\frac{A-B}{2}$，把 $\sin(A+B)+\sin(A-B)$ 用和角公式展开合并：
$$\sin A+\sin B=2\sin\frac{A+B}{2}\cos\frac{A-B}{2}$$

**小结**：真正要背的其实就一个 $\cos(\alpha-\beta)$，其他全部从它推。推导走一遍，公式再也忘不了。

**简单例题**：用两角和的公式化简 $\sin x\cos 30°+\cos x\sin 30°$
就是 $\sin(x+30°)=\sin(x+\frac{\pi}{6})$，直接倒过来用。

### 今日任务
把 cos(α−β) 的推导自己写一遍，再从它推出 sin 和 cos 的和差公式；用向量点乘再证一遍 cos(α−β)；做三道向量题：已知坐标求点乘、判断垂直、证明三点共线；再用面积法推一遍正弦定理、用向量推一遍余弦定理。


