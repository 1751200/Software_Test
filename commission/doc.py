description = r'''Given a computer sales system, main unit (25 ¥ unit price, the maximum monthly sales volume is 70),
monitor (30 ¥ unit price, the maximum monthly sales volume is 80), peripherals (45 ¥ unit price, the maximum monthly
sales volume is 90); each salesperson sells at least one complete machine every month. When the variable of the host
of the system receives a value of -1, the system automatically counts the salesperson's total sales this month. When
the sales volume is less than or equal to 1000 (including 1000), a 10% commission is charged; when the sales volume is
between 1000-1800 (including 1800), the commission is 15%, and when the sales volume is greater than 1800, the
commission is charged according to 20%. Use the boundary value method to design test cases.'''


md1 = r'''边界值法：32个测试用例

x主机的边界值（健壮性边界）：1， 2，35，69，70，71，-1

y外设的边界值（健壮性边界）：1，2，40，79，80，81，-1

z显示器的值边界（健壮性边界）：1，2，45，89，90，91，-1

佣金——设备基本边界值测试用例：12个'''


md2 = r'''健壮性边界的测试用例：9个'''


md3 = r'''直接根据设备销售数量基本边界值计算出的销售额都只在(1800,8200] 区间内，无法覆盖到其他的两个区间，所以以下对每个区间都设置了基
本边界值用例，来测试销售额在不同区间内的佣金

销售额：$25x+30y+45z$

销售额区间：[100, 1000],  (1000,1800], (1800,8200] 

三个区间的基本边界值：

- [100, 1000]：100， 125，970，1000
- (1000,1800]：1045，1775，1800
- (1800,8200] ：1830，8155，8200

佣金——销售额基本边界值测试用例:11个
'''


md4 = r'''所以总共的测试用例为：$12+9+11 = 32$ 个'''
