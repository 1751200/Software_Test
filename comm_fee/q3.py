import pandas as pd
import numpy as np
import math

description = r'''Given a computer sales system, main unit (25 ¥ unit price, the maximum monthly sales volume is 70), 
monitor (30 ¥ unit price, the maximum monthly sales volume is 80), peripherals (45 ¥ unit price, the maximum monthly 
sales volume is 90); each salesperson sells at least one complete machine every month. When the variable of the host 
of the system receives a value of -1, the system automatically counts the salesperson's total sales this month. When 
the sales volume is less than or equal to 1000 (including 1000), a 10% commission is charged; when the sales volume is 
between 1000-1800 (including 1800), the commission is 15%, and when the sales volume is greater than 1800, the 
commission is charged according to 20%. Use the boundary value method to design test cases.'''

def calculate_comm_fee(test_sample):
    minutes,n_overdue,unpaid_fee,discount,extra_rate = test_sample
    
    max_overdue = math.ceil(minutes/60)
    max_overdue = max_overdue if 1<= max_overdue <=6 else 6

    basic_part,comm_part = 25,0 
    # 逾期次数少于限额,可以享受折扣
    if n_overdue<=max_overdue: 
        comm_part = 0.15 * (1-discount) * minutes + unpaid_fee * extra_rate
    else:
        comm_part = 0.15 * 1 * minutes + unpaid_fee * extra_rate
    
    total_part = basic_part + comm_part
    return total_part

if __name__ == "__main__":
    print(calculate_comm_fee([60,0,0,0.01,0]))
    print(calculate_comm_fee([60,6,100,0,0.05]))
