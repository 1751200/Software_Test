description = r'''Study a telecommunications charging system that is closely related to our lives. The requirements are 
described as follows:

$$\text{The total monthly fee = basic monthly fee + actual call fee after discount.}$$

If there is no discount, the actual call fee is calculated. The basic monthly fee is 25 yuan and the call fee per minute
is 0.15 yuan.

Whether there is a discount on the actual call charge is related to the call time (minutes) of the month and the 
cumulative number of non-time payment from this year to this month. Cross-year unpaid fees have nothing to do with 
discounts, but the unpaid part of the cross-year needs to pay a 5% late fee per month.

There is a direct correspondence between the call minutes of the month and the discount rate and the number of non-time 
payments in this year. If the number of non-time payments in this year exceeds the allowable value corresponding to the 
call time of this month, the discount will be exempted and the actual call Fee calculation.

The telephone fee is collected by online payment. The payment method is: Alipay or bank card (developing a simple analog 
subsystem). After payment, a list of successful or unsuccessful payments is printed.

The relationship between call time and discount rate and the number of non-payment on time is:

| Minutes of calls this month | The maximum allowable non-time payment times during the talk time | Discount rate for talk time |
| :-------------------------: | :----------------------------------------------------------: | :-------------------------: |
|          $(0, 60]$          |                              1                               |           $1.0\%$           |
|         $(60, 120]$         |                              2                               |           $1.5\%$           |
|        $(120, 180]$         |                              3                               |           $2.0\%$           |
|        $(180, 300]$         |                              3                               |           $2.5\%$           |
|       $(300, \infty)$       |                              6                               |           $3.0\%$           |


Test cases are designed with boundary values, equivalence classes and decision tables respectively, and a comprehensive 
set of test cases is obtained through comprehensive analysis.'''


statement = "假设每年欠费不能累积，一年欠费的上限为79356元"

boundary1 = r'''由于本月通话分钟数是按区间划分的，所以针对每个区间，都进行了边界值的设定；同理不按时缴费次数M也按区间设定边界值

基本边界+健壮性边界：

本月通话分钟数T: -1,   0, 1, 59, 60,   61, 119, 120,   121,179, 180,   181, 299, 300,   301, 2000, 44639, 44640,   44641

不按时缴费次数M: -1, 0, 1, 2, 3, 6, 11,  12

跨年未交部分L:-1,  0, 10, 100, 1000, 79356, 80000

基本边界值测试用例27个：'''


boundary2 = "健壮性边界值测试用例7个："


equivalence1 = r'''有效等价类

T本月通话分钟数:{0< T<= 60}, {60 < T<= 120}, {120< T<= 180}, {180 < T<= 300}, {300< T<=44640}

不按时缴费次数M: {0,1}, {2}, {3}, {4,5,6}, {7,8,9,10,11}

跨年未交部分L: {0}, { 0< L<=79356}

无效等价类：

本月通话分钟数T:	{0,-1}, {T>44640}

不按时缴费次数M: {M < 0},{M>11}

跨年未交部分L: {L < 0}, {L > 79356}

强一般等价类测试用例：5x5x2 = 50'''


equivalence2 = r'''额外弱健壮等价类测试用例：3*2 = 6'''


dt1 = r'''条件：T本月通话分钟数、不按时缴费次数M、跨年未交部分L

T1 ={0< T<= 60}

T2 ={60 < T<= 120}

T3 ={120< T<= 180}

T4 ={180 < T<= 300}

T5 ={300< T<=44640}

M1={0,1}

M2={2}

M3={3}

M4={4,5,6}

M5={7,8,9,10,11}

L1 ={0}

L2 ={  0< L<=79356}

行动：

A1：有通话时间段的折扣

A2：无通话时间段的折扣

Discount的扩展决策表：

|          | 1    | 2     | 3     | 4     | 5     | 6     | 7     | 8     | 9     | 10   |
| -------- | ---- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ---- |
| C1:T     | T1   | T1    | T2    | T2    | T3    | T3    | T4    | T4    | T5    | T5   |
| C2:M     | M1   | M2-M5 | M1-M2 | M3-M5 | M1-M3 | M4-M5 | M1-M3 | M4-M5 | M1-M4 | M5   |
| A1       | X    |       | X     |       | X     |       | X     |       | X     |      |
| A2       |      | X     |       | X     |       | X     |       | X     |       | X    |
| discount | 1.0% | 0     | 1.5%  | 0     | 2.0%  | 0     | 2.5%  | 0     | 3.0%  | 0    |

再根据条件L可得以上每个测试用例都可再划分为两个测试用例

测试用例集10*2 = 20 个测试用例：'''


conclusion = r'''从以上三种黑盒测试的方法可以看出：

- 边界值法测试虽然考虑了大量边界，但是由于该问题是在不同条件集合下采取不同行动，会导致边界测试的测试用例并不能覆盖所有条件区间，比如通话时间折扣率为1.0%和1.5%的情况在测试用例中根本没有。
- 等价类法，通过强一般等价类测试用例覆盖了全部的业务条件和情况，通过额外弱健壮等价类测试用例覆盖了边界情况。但是其测试用例的数量很多，有一些冗余。
- 决策表测试法：该方法很适合描述不同条件集合下采取行动的各种组合的情况，所以很契合这题。在使用较少的用例的情况下覆盖了全部的正常业务条件和活动。但是其有一个缺点就是没有考虑到一些边界情况，尤其是健壮性边界。
- 综上所述：最后的测试用例集为：决策表测试法20个测试用例+额外弱健壮等价类测试用例6个
'''
