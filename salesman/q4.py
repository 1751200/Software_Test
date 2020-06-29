import streamlit as st
import pandas as pd
import numpy as np

def calculate_commission(test_sample):
    commission = 0
    sales,cash_ratio,n_leave = test_sample
    if sales > 200 and n_leave <= 10:
        if cash_ratio>=0.6:
            commission = round(sales/7,2)
        else:
            commission = 0
        
    else:
        if cash_ratio<=0.85:
            commission = round(sales/6,2)
        else:
            commission = round(sales/5,2)

    return commission


if __name__ == "__main__":
    print(calculate_commission([300,0.6,9]))