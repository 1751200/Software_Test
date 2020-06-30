def calculate_computer_commission(test_sample):
    host, shower, affliate = test_sample
    payment = -1
    if host == -1:
        return payment # 输出-1表示结束,外部应该中断不继续计算
    else:
        costs = host * 25 + shower *30 + affliate*45
    
    if costs <= 1000:
        payment = 0.1 * costs
    elif 1000 < costs <= 1800:
        payment = 0.15 * costs
    elif costs > 1800:
        payment = 0.2 * costs
    return payment


if __name__ == "__main__":
    print(calculate_computer_commission([10,9,10]))
