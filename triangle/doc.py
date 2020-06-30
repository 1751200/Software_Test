md1 = r'''根据输出结果划分4个等价类：
$$
\begin{aligned}
&\mathrm{R} 1=\{ \langle\mathrm{a}, \mathrm{b}, \mathrm{c}\rangle: \text { 有三条边 } \mathrm{a}, \mathrm{b} \text { 和 } \mathrm{c} \text { 的等边三角形 }\}\\
&\mathrm{R} 2=\{ \langle\mathrm{a}, \mathrm{b}, \mathrm{c}\rangle: \text { 有三条边 } \mathrm{a}, \mathrm{b} \text { 和 } \mathrm{c} \text { 的等腰三角形 }\}\\
&\mathrm{R} 3=\{ \langle\mathrm{a}, \mathrm{b}, \mathrm{c}\rangle: \text { 有三条边 } \mathrm{a}, \mathrm{b} \text { 和 } \mathrm{c} \text { 的不等边三角形 }\}\\
&\mathrm{R} 4=\{ \langle\mathrm{a}, \mathrm{b}, \mathrm{c}\rangle: \text { 三条边 } \mathrm{a}, \mathrm{b}\text { 和 c 不构成三角形 }\}
\end{aligned}
$$
然后再从输入变量入手，设计出额外弱健壮测试用例

使用弱健壮等价类

其中弱一般等价类4个测试用例'''

md2 = r'''额外弱健壮测试用例为 $3\times 2=6$ 个'''

md3 = r'''健壮性边界：

假设 $1<a,b,c<200$

设abc的基本边界（最小值，略高于最小值、正常值、略低于最大值和最大值）分别为：1，2，100，199，200

设abc的健壮性边界（略超过最大值，略小于最小值）： 201， 0 '''