import math


def calculate_comm_fee(test_sample):
    minutes, n_overdue, unpaid_fee, discount, extra_rate = test_sample

    if extra_rate == -1 or extra_rate == -1:
        return -1
    
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
