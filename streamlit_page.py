import streamlit as st
import numpy as np
import pandas as pd
import time
import re


def is_right(test_sample, tfunc):
    real_value = test_sample[-1]
    test_value = tfunc(test_sample[:-1])
    if real_value == test_value:
        return True, real_value, test_value
    else:
        return False, real_value, test_value


# 每道题的input都是一个 np.array,其中最后一个值是输出值
#  0 不在范围
#  1 非三角形
#  2 啥都不等
#  3 等腰
#  4 等边
def decide_triangle_type(test_sample):
    line1, line2, line3 = test_sample
    if not (1 <= line1 <= 200 and 1 <= line2 <= 200 and 1 <= line3 <= 200):
        return 0
    elif max(test_sample) > sum(test_sample) - max(test_sample):
        return 1
    else:
        lines = list(set([line1, line2, line3]))
        n_line = len(lines)
        if n_line == 1:
            return 4
        elif n_line == 2:
            return 3
        elif n_line == 3:
            return 2


st.title('Software Test')
option = st.sidebar.selectbox(
    'Which qeustion do you like to test?',
    ["三角形类型", "万年历", '佣金问题', '销售员问题'])
st.header('Description')
if option == "三角形类型":
    st.text('输入三角形的三条边，判断它们能构成三角形的类型或者能构成三角形。')
    st.header('Upload the test file')
    uploaded_file = st.file_uploader("", type="csv")
    chart_data = None
    new_data = None
    real_cols = ["line1", "line2", "line3", "Real_Value"]
    if uploaded_file is not None:
        chart_data = pd.read_csv(uploaded_file)
    if st.checkbox('Show test samples'):
        chart_data

    st.header("Test Section")
    if st.button("Test:)"):
        latest_iteration = st.empty()
        bar = st.progress(0)
        n_sample = chart_data.shape[0]
        n_right, n_wrong = 0, 0
        for i in range(1, n_sample + 1):
            test_sample = chart_data.loc[i - 1].values
            # decide_triangle_type 是每道题的执行函数
            do_right, _, _ = is_right(test_sample, decide_triangle_type)
            if do_right:
                n_right = n_right + 1
            else:
                n_wrong = n_wrong + 1
            latest_iteration.text(
                f'Progress: {n_sample}/{i}. Accuracy: {round(n_right / n_sample, 2) * 100}%')
            bar.progress(i / n_sample)
            time.sleep(0.05)
        if n_right == n_sample:
            st.balloons()
        else:
            st.warning(f"Something wrong with your code.")

    sample_input = st.text_input('Define your own test samples. For Example:1,2,4:0', ' ')
    if sample_input != ' ':
        real_sample_input = re.split(',|:', sample_input)
        real_sample_input = np.array([float(x) for x in real_sample_input])
        new_sample = pd.DataFrame(
            real_sample_input.reshape((1, -1)),
            columns=real_cols)
        st.table(new_sample)
        do_right,real_value,test_value = is_right( real_sample_input,decide_triangle_type)
        st.text(f'Real Value: {real_value}. Test Value: {test_value}')
        if do_right:
            st.success(f"Test Passed.")
        else:
            st.warning(f"Test Failed.")
            # 测试

    st.header("Analysis")

elif option == "万年历":
    if st.checkbox('开始运行测试脚本'):
        latest_iteration = st.empty()
        bar = st.progress(0)
        for i in range(100):
            # Update the progress bar with each iteration.
            latest_iteration.text('正在测试第 {i + 1} 个用例')
            bar.progress(i + 1)
            time.sleep(0.1)
elif option == "佣金问题":
    pass

elif option == "电信收费金额":
    pass

elif option == "销售系统":
    pass

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])
#
# st.line_chart(chart_data)

# 运行测试脚本
