description = r'''Given a sales system, if a salesperson’s annual sales is greater than 2 million RMB and the number of 
days of leave is not more than 10 days, the cash receipt is greater than or equal to 60%, then the commission 
coefficient is 7, that is, the commission value is sales The amount is divided by the commission factor; the cash 
receipt is less than 60%, and the commission is not calculated. In all other cases and the cash arrival is less than or 
equal to 85%, the commission is calculated based on the commission factor of 6; the cash arrival is greater than 85% and 
the commission factor is treated as 5. Design a flow chart and design test cases according to the topic to achieve 

1. sentence coverage
2. judgment coverage 
3. condition coverage 
4. judgment-condition coverage 
5. conditional combination coverage 

(test cases of White Box Test And coverage should be clear).'''


def calculate_commission(test_sample):
    sales, cash_ratio, n_leave = test_sample
    if sales > 200 and n_leave <= 10:
        if cash_ratio >= 0.6:
            commission = round(sales/7, 2)
        else:
            commission = 0

    else:
        if cash_ratio <= 0.85:
            commission = round(sales/6, 2)
        else:
            commission = round(sales/5, 2)

    return commission


if __name__ == "__main__":
    print(calculate_commission([300, 0.6, 9]))
