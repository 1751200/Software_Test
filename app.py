from PIL import Image
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd
import time
import re

import utils
import triangle
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

    chart_data = None

    if option2 == 'Input via .csv file':
        st.header('Upload the test file')
        uploaded_file = st.file_uploader("", type="csv")
        if uploaded_file is not None:
            chart_data = pd.read_csv(uploaded_file)
        if st.checkbox('Show test samples'):
            chart_data
    
    if option2 == 'Input via textfield':
        triangle.type_of_triangle
        sample_input = st.text_input(
            'Define your own test samples. For Example: 1,2,4:0', ' ')
        real_cols = ["side 1", "side 2", "side 3", "Ground truth"]
        if sample_input != ' ':
            real_sample_input = re.split(',|:', sample_input)
            real_sample_input = np.array([float(x) for x in real_sample_input])
            new_sample = pd.DataFrame(
                real_sample_input.reshape((1, -1)),
                columns=real_cols)
            st.table(new_sample)
            time_start = time.time()
            do_right, real_value, test_value = triangle.is_right(
                real_sample_input, triangle.decide_triangle_type)
            time_end = time.time()
            if do_right:
                st.success(f"Test passed in {round((time_end - time_start) * 1000, 2)} ms.")
            else:
                st.error(f"Test failed. Output {test_value} ({triangle.type_of_triangle[test_value]})" +
                         f" is expected to be {int(real_value)} ({triangle.type_of_triangle[real_value]})")

    if option2 == 'Boundary value analysis':
        st.header('Boundary value analysis')
        # chart_data = pd.read_csv()
        # chart_data

    if option2 == 'Equivalence partition method':
        st.header('Equivalence partition method')
        # chart_data = pd.read_csv()
        # chart_data

    if option2 != 'Input via textfield':
        if st.button("Test :)"):
            st.header("Test Result")
            latest_iteration = st.empty()
            bar = st.progress(0)
            n_sample = chart_data.shape[0]
            n_right, n_wrong = 0, 0
            time_start = time.time()
            wrong_samples = []
            for i in range(1, n_sample + 1):
                test_sample = chart_data.loc[i - 1].values
                # decide_triangle_type 是每道题的执行函数
                do_right, real_value, test_value = triangle.is_right(test_sample, triangle.decide_triangle_type)
                if do_right:
                    n_right = n_right + 1
                else:
                    n_wrong = n_wrong + 1
                    wrong_samples.append((real_value, test_value, i))
                latest_iteration.text(
                    f'Progress: {n_sample}/{i}. Accuracy: {round(n_right / n_sample, 2) * 100}%')
                bar.progress(i / n_sample)
                time.sleep(0.05)
            time_end = time.time()
            if n_right == n_sample:
                text = "tests" if n_sample > 1 else "test";
                st.success(f"{n_sample} {text} passed in {round((time_end - time_start) * 1000, 2)} ms.")
            else:
                if n_right == 0:
                    st.error("All tests failed.")
                else:
                    st.warning(f"{n_right} passed .{n_sample - n_right} failed.")
                for sample in wrong_samples:
                    st.error(f"Test #{sample[2]}: Output \'{sample[1]} ({triangle.type_of_triangle[sample[1]]})\'" +
                             f" is expected to be \'{int(sample[0])} ({triangle.type_of_triangle[sample[0]]})\'")

            st.header("Analysis")
            labels = 'pass', 'fail'
            sizes = [n_right, n_sample - n_right]
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            plt.axis('equal')
            st.pyplot()

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
    option2 = st.sidebar.selectbox(
        "Which section do you want to view?",
        ["Open Source Automation Testing Tools", "Open Source Bug Tracking Tools"]
    )
    st.header(option2)
    if option2 == "Open Source Bug Tracking Tools":
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
    else:
        pass