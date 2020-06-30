from PIL import Image
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd
import datetime
import time
import re

# import utils
import triangle
import myCalendar
import comm_fee
import salesman
import testing_tools as tools

st.sidebar.title('Software Test')
option = st.sidebar.selectbox(
    'Which question do you like to test?',
    ["Types of Triangles", "Perpetual Calendar", 'Commission', 'Telecommunication charges', 'Salesmen',
     'Testing Tools & Bug Trackers'])

st.title(option)
if option == "Types of Triangles":
    st.header('Description')
    st.markdown(triangle.description)
    image = Image.open('./triangle/img/triangle.jpg')
    st.image(image, "Types of Triangles by Length of Sides", use_column_width=True)

    st.sidebar.markdown(triangle.description)
    s_image = Image.open('./triangle/img/triangle-1.png')
    st.sidebar.image(s_image, use_column_width=True)
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
            st.write(chart_data)
    
    if option2 == 'Input via textfield':
        st.write(triangle.type_of_triangle)
        sample_input = st.text_input(
            'Define your own test samples. For Example: 1,2,4:0', ' ')
        real_cols = ["side 1", "side 2", "side 3", "Ground truth"]
        if sample_input != " ":
            real_sample_input = re.split('[,:]', sample_input)
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
        chart_data = pd.read_csv("./triangle/三角形-边界值.csv", encoding="gbk")
        st.write(chart_data)

    if option2 == 'Equivalence partition method':
        st.header('Equivalence partition method')
        chart_data = pd.read_csv("./triangle/三角形-等价类.csv", encoding="gbk")
        st.write(chart_data)

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
                text = "tests" if n_sample > 1 else "test"
                st.success(f"{n_right} {text} passed in {round((time_end - time_start) * 1000, 2)} ms.")
            else:
                if n_right == 0:
                    st.error("All tests failed.")
                else:
                    st.warning(f"{n_right} passed. {n_wrong} failed.")
                for sample in wrong_samples:
                    st.error(f"Test #{sample[2]}: Output \'{sample[1]} ({triangle.type_of_triangle[sample[1]]})\'" +
                             f" is expected to be \'{int(sample[0])} ({triangle.type_of_triangle[sample[0]]})\'")

            st.header("Analysis")
            labels = 'pass', 'fail'
            sizes = [n_right, n_wrong]
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            plt.axis('equal')
            st.pyplot()

elif option == "Perpetual Calendar":
    st.header('Description')
    st.markdown(r'''Outputs the date of the next day of the given date.''')
    image = Image.open("./myCalendar/img/calendar.png")
    st.image(image, "Calendar", use_column_width=True)

    st.sidebar.markdown(r'''Outputs the date of the next day of the given date.''')
    s_image = Image.open("./myCalendar/img/s_calendar.png")
    st.sidebar.image(s_image, use_column_width=True)
    option2 = st.sidebar.selectbox(
        'How do you want to enter data?',
        ['Input via .csv file', 'Input via date picker',
         'Boundary value analysis', 'Equivalence partition method', 'Extended-entry decision table']
    )
    date_data = None

    if option2 == 'Input via .csv file':
        st.header('Upload the test file')
        uploaded_file = st.file_uploader("", type="csv")
        if uploaded_file is not None:
            date_data = pd.read_csv(uploaded_file)
        if st.checkbox('Show test samples'):
            st.write(date_data)

    elif option2 == 'Input via date picker':
        st.header('Input date via date picker')
        date1 = st.date_input("Select any one day", datetime.date(2020, 7, 1))
        date2 = st.date_input("Select the day after " + date1.strftime("%Y/%m/%d"), datetime.date(2020, 7, 2))
        if date1 and date2:
            time_start = time.time()
            present_date = myCalendar.PresentDate(date1.year, date1.month, date1.day)
            output = present_date.add_day(1)
            time_end = time.time()
            st.header('Test Result')
            st.write('Output: ' + output)
            expected_output = date2.strftime("%Y/%-m/%-d")
            if expected_output == output:
                st.success(f"Test passed in {round((time_end - time_start) * 1000, 2)} ms.")
            else:
                st.error(f"Test failed. Output {output} is expected to be {expected_output}")

    elif option2 == 'Boundary value analysis':
        st.header('Boundary value analysis')
        date_data = pd.read_csv("./myCalendar/万年历1-边界值.csv", encoding="utf-8")
        st.write(date_data)

    elif option2 == 'Equivalence partition method':
        st.header('Equivalence partition method')
        date_data = pd.read_csv("./myCalendar/万年历1-等价类.csv", encoding="utf-8")
        st.write(date_data)

    else:
        st.header('Extended-entry decision table')
        date_data = pd.read_csv("./myCalendar/万年历9-扩展决策表.csv", encoding="utf-8")
        st.write(date_data)

    if option2 != 'Input via date picker':
        if st.button("Test :)"):
            st.header("Test Result")
            latest_iteration = st.empty()
            bar = st.progress(0)
            n_sample = date_data.shape[0]
            n_right, n_wrong = 0, 0
            wrong_samples = []
            time_start = time.time()
            for i in range(1, n_sample + 1):
                year = date_data.loc[i - 1]['year']
                month = date_data.loc[i - 1]['month']
                day = date_data.loc[i - 1]['day']
                expect = date_data.loc[i - 1]['NextDay']
                test_data = myCalendar.PresentDate(year, month, day)
                output = test_data.add_day(1)
                if expect == output:
                    n_right = n_right + 1
                else:
                    n_wrong = n_wrong + 1
                    wrong_samples.append((output, expect, i, f'{year}/{month}/{day}'))
                latest_iteration.text(
                    f'Progress: {n_sample}/{i}. Accuracy: {round(n_right / n_sample, 2) * 100}%')
                bar.progress(i / n_sample)
                time.sleep(0.05)
            time_end = time.time()
            if n_right == n_sample:
                text = "tests" if n_sample > 1 else "test"
                st.success(f"{n_sample} {text} passed in {round((time_end - time_start) * 1000, 2)} ms.")
            else:
                if n_right == 0:
                    st.error("All tests failed.")
                else:
                    st.warning(f"{n_right} passed. {n_wrong} failed.")
                for sample in wrong_samples:
                    st.error(f"Test #{sample[2]}: {sample[3]} - Output {sample[0]} is expected to be {sample[1]}")

            st.header("Analysis")
            labels = 'pass', 'fail'
            sizes = [n_right, n_wrong]
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            plt.axis('equal')
            st.pyplot()

elif option == 'Commission':
    st.header("Problem restatement")
    # st.markdown(comm_fee.description)

elif option == 'Telecommunication charges':
    st.header("Problem restatement")
    st.markdown(comm_fee.description)

elif option == 'Salesmen':
    st.header("Problem restatement")
    st.markdown(salesman.description)

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
        st.markdown(tools.testing_tool_md1)
        selenium_img = Image.open("./testing_tools/img/Selenium.png")
        st.image(selenium_img, "Selenium", use_column_width=True)
        st.markdown(tools.testing_tool_md2)
        appium_img = Image.open("./testing_tools/img/Appium.png")
        st.image(appium_img, "Appium", use_column_width=True)
        st.markdown(tools.testing_tool_md3)
        jmeter_img = Image.open("./testing_tools/img/jmeter.png")
        st.image(jmeter_img, "JMeter", use_column_width=True)
        st.markdown(tools.testing_tool_md4)
