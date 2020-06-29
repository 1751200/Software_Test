from PIL import Image
import streamlit as st
import numpy as np
import pandas as pd
import time
import re

from triangle.triangle import decide_triangle_type, is_right
import testing_tools as tools

st.sidebar.title('Software Test')
option = st.sidebar.selectbox(
    'Which qeustion do you like to test?',
    ["Types of Triangles", "Perpetual Calendar", 'Commission', 'Salesmen', 'Testing Tools & Bug Trackers'])

st.title(option)
if option == "Types of Triangles":
    st.header('Description')
    st.markdown(r'''Enter the three sides of the triangle and determine whether they can form a triangle.
                If so, judge the type of the triangle by the length of its sides.''' )
    image = Image.open('./triangle/img/triangle.jpg')
    st.image(image, "Types of Triangles by Length of Sides", use_column_width=True)

    option2 = st.sidebar.selectbox(
        'How do you want to enter data?',
        ['Input via .csv file', 'Input via textfield',
            'Boundary value analysis', 'Equivalence partition method']
    )

    if option2 == 'Input via .csv file':
        st.header('Upload the test file')
        uploaded_file = st.file_uploader("", type="csv")
        chart_data = None
        new_data = None
        real_cols = ["line1", "line2", "line3", "Real_Value"]
        if uploaded_file is not None:
            chart_data = pd.read_csv(uploaded_file)
        if st.checkbox('Show test samples'):
            chart_data
    
    if option2 == 'Input via textfield':
        sample_input = st.text_input(
            'Define your own test samples. For Example:1,2,4:0', ' ')
        if sample_input != ' ':
            real_sample_input = re.split(',|:', sample_input)
            real_sample_input = np.array([float(x) for x in real_sample_input])
            new_sample = pd.DataFrame(
                real_sample_input.reshape((1, -1)),
                columns=real_cols)
            st.table(new_sample)
            do_right, real_value, test_value = is_right(
                real_sample_input, decide_triangle_type)
            st.text(f'Real Value: {real_value}. Test Value: {test_value}')
            if do_right:
                st.success(f"Test Passed.")
            else:
                st.warning(f"Test Failed.")
                # 测试

    if st.button("Test:)"):
        st.header("Test Result")
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

    st.header("Analysis")

elif option == "Perpetual Calendar":
    if st.checkbox('开始运行测试脚本'):
        latest_iteration = st.empty()
        bar = st.progress(0)
        for i in range(100):
            # Update the progress bar with each iteration.
            latest_iteration.text('正在测试第 {i + 1} 个用例')
            bar.progress(i + 1)
            time.sleep(0.1)
elif option == 'Commission':
    pass

elif option == 'Testing Tools & Bug Trackers':
    st.header("Open Source Automation Testing Tools")
    st.header("Open Source Bug Tracking Tools")
    st.markdown(tools.bug_tracker_md1)
    redmine_img = Image.open("./testing_tools/img/redmine.png")
    st.image(redmine_img, "Redmine", use_column_width=True)
    st.markdown(tools.bug_tracker_md2)
    bugzilla_img = Image.open("./testing_tools/img/bugzilla.png")
    st.image(bugzilla_img, "BugZilla", use_column_width=True)
    st.markdown(tools.bug_tracker_md3)
    mantisbt_img = Image.open("./testing_tools/img/mantisBT.png")
    st.image(mantisbt_img, "MantisBT", use_column_width=True)
    st.markdown(tools.bug_tracker_md4)
