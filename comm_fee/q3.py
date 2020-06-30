import math


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


def calculate_comm_fee(test_sample):
    minutes, n_overdue, unpaid_fee, discount, extra_rate = test_sample
    
    max_overdue = math.ceil(minutes/60)
    max_overdue = max_overdue if 1 <= max_overdue <= 6 else 6

    basic_part, comm_part = 25, 0
    # 逾期次数少于限额,可以享受折扣
    if n_overdue <= max_overdue:
        comm_part = 0.15 * (1 - discount) * minutes + unpaid_fee * extra_rate
    else:
        comm_part = 0.15 * 1 * minutes + unpaid_fee * extra_rate
    
    total_part = basic_part + comm_part
    return total_part


if __name__ == "__main__":
    print(calculate_comm_fee([60, 0, 0, 0.01, 0]))
    print(calculate_comm_fee([60, 6, 100, 0, 0.05]))
