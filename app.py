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
import commission
import comm_fee
import salesman
import tran_tree
import q9
import testing_tools as tools

st.sidebar.title('Software Test')
option = st.sidebar.selectbox(
    'Which question do you like to test?',
    ["Types of Triangles", "Perpetual Calendar", 'Commission', 'Telecommunication charges', 'Salesmen',
     'JUnit', 'Driver & Sub', 'Testing Tools & Bug Trackers', 'Transition Tree', 'Question 9'])

st.title(option)
if option == "Types of Triangles":
    st.sidebar.markdown(triangle.description)
    s_image = Image.open('./triangle/img/triangle-1.png')
    st.sidebar.image(s_image, use_column_width=True)
    option2 = st.sidebar.selectbox(
        'How do you want to enter data?',
        ['Problem description', 'Input via .csv file', 'Input via textfield',
            'Boundary value analysis', 'Equivalence partition method']
    )
    chart_data = None

    if option2 == 'Problem description':
        st.header('Description')
        st.markdown(triangle.description)
        image = Image.open('./triangle/img/triangle.jpg')
        st.image(image, "Types of Triangles by Length of Sides", use_column_width=True)

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
        st.header('边界值法')
        st.markdown(triangle.md3)
        chart_data = pd.read_csv("./triangle/三角形-边界值.csv", encoding="gbk")
        st.table(chart_data)

    if option2 == 'Equivalence partition method':
        st.header('等价类法')
        st.markdown(triangle.md1)
        st.table(pd.read_csv("./triangle/弱一般等价类.csv"))
        st.markdown(triangle.md2)
        st.table(pd.read_csv("./triangle/额外弱健壮.csv"))
        # st.markdown(r'''所有的测试用例：''')
        chart_data = pd.read_csv("./triangle/三角形-等价类.csv", encoding="gbk")
        if st.checkbox('Show test samples'):
            st.write(chart_data)

    if option2 != 'Input via textfield' and option2 != 'Problem description':
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
                    wrong_samples.append((real_value, test_value, i, test_sample))
                latest_iteration.text(
                    f'Progress: {n_sample}/{i}. Accuracy: {round(n_right / n_sample, 2) * 100}%')
                bar.progress(i / n_sample)
                time.sleep(0.05)
            time_end = time.time()
            if n_right == n_sample:
                text = "tests" if n_sample > 1 else "test"
                st.success(
                    f"{n_sample} {text} passed in {round((time_end - time_start) * 1000 - n_sample * 50, 2)} ms.")
            else:
                if n_right == 0:
                    st.error("All tests failed.")
                else:
                    st.warning(f"{n_right} passed. {n_wrong} failed.")
                for sample in wrong_samples:
                    st.error(f"Test #{sample[2]}: {sample[3]}" +
                             f" - Output \'{sample[1]} ({triangle.type_of_triangle[sample[1]]})\'" +
                             f" is expected to be \'{int(sample[0])} ({triangle.type_of_triangle[sample[0]]})\'")

            st.header("Analysis")
            labels = 'pass', 'fail'
            sizes = [n_right, n_wrong]
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            plt.axis('equal')
            st.pyplot()

elif option == "Perpetual Calendar":
    st.sidebar.markdown(r'''Outputs the date of the next day of the given date.''')
    s_image = Image.open("./myCalendar/img/s_calendar.png")
    st.sidebar.image(s_image, use_column_width=True)
    option2 = st.sidebar.selectbox(
        'How do you want to enter data?',
        ['Problem description', 'Input via .csv file', 'Input via date picker',
         'Boundary value analysis', 'Equivalence partition method', 'Extended-entry decision table']
    )
    date_data = None

    if option2 == 'Problem description':
        st.header('Description')
        st.markdown(r'''Outputs the date of the next day of the given date.''')
        image = Image.open("./myCalendar/img/calendar.png")
        st.image(image, "Calendar", use_column_width=True)

    elif option2 == 'Input via .csv file':
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
        st.header('边界值法')
        st.markdown(myCalendar.md1)
        st.table(pd.read_csv("./myCalendar/基本边界值测试.csv"))
        st.markdown(myCalendar.md2)
        st.table(pd.read_csv("./myCalendar/健壮性边界值测试.csv"))
        st.markdown(myCalendar.md3)
        st.table(pd.read_csv("./myCalendar/额外测试用例.csv"))
        date_data = pd.read_csv("./myCalendar/万年历1-边界值.csv", encoding="utf-8")
        if st.checkbox('Show test samples'):
            st.write(date_data)

    elif option2 == 'Equivalence partition method':
        st.header('Equivalence partition method')
        st.markdown(myCalendar.md4)
        st.table(pd.read_csv("./myCalendar/强一般等价类.csv"))
        st.markdown(myCalendar.md5)
        st.table(pd.read_csv("./myCalendar/额外弱健壮.csv"))
        date_data = pd.read_csv("./myCalendar/万年历1-等价类.csv", encoding="utf-8")
        if st.checkbox('Show test samples'):
            st.write(date_data)

    else:
        st.header('扩展决策表')
        st.markdown(myCalendar.md6)
        table = Image.open("./myCalendar/img/table.png")
        st.image(table, "万年历扩展决策表", use_column_width=True)
        st.markdown(myCalendar.md7)
        date_data = pd.read_csv("./myCalendar/万年历9-扩展决策表.csv", encoding="utf-8")
        st.table(date_data)

    if option2 != 'Input via date picker' and option2 != 'Problem description':
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
                st.success(
                    f"{n_sample} {text} passed in {round((time_end - time_start) * 1000 - n_sample * 50, 2)} ms.")
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
    option2 = st.sidebar.selectbox(
        "How do you want to enter data?",
        ["Description", "Boundary value analysis", 'Input via .csv file']
    )
    commission_data = None

    if option2 == "Description":
        st.header("Problem restatement")
        st.markdown(commission.description)

    elif option2 == "Boundary value analysis":
        st.header("边界值法")
        st.markdown(commission.md1)
        st.table(pd.read_csv("./commission/基本边界值.csv"))
        st.markdown(commission.md2)
        st.table(pd.read_csv("./commission/设备健壮性边界.csv"))
        st.markdown(commission.md3)
        st.table(pd.read_csv("./commission/销售额基本边界值.csv"))
        st.markdown(commission.md4)
        commission_data = pd.read_csv("./commission/佣金问题-边界值.csv")

    else:
        st.header('Upload the test file')
        uploaded_file = st.file_uploader("", type="csv")
        if uploaded_file is not None:
            commission_data = pd.read_csv(uploaded_file)
        if st.checkbox('Show test samples'):
            st.write(commission_data)

    if option2 != "Description":
        if st.button("Test :)"):
            st.header("Test Result")
            latest_iteration = st.empty()
            bar = st.progress(0)
            n_sample = commission_data.shape[0]
            n_right, n_wrong = 0, 0
            wrong_samples = []
            time_start = time.time()
            for i in range(1, n_sample + 1):
                x = commission_data.loc[i - 1]['x']
                y = commission_data.loc[i - 1]['y']
                z = commission_data.loc[i - 1]['z']
                expect = commission_data.loc[i - 1]['commission']
                output = commission.calculate_computer_commission([x, y, z])
                if float(expect) == output:
                    n_right = n_right + 1
                else:
                    n_wrong = n_wrong + 1
                    wrong_samples.append((output, expect, i, f'({x}, {y}, {z})'))
                if float(expect) == -1:
                    n_right = n_sample
                    latest_iteration.text(
                        f'Progress: {n_sample}/{n_sample}. Accuracy: {round(n_right / n_sample, 2) * 100}%')
                    bar.progress(n_sample / n_sample)
                    break
                latest_iteration.text(
                    f'Progress: {n_sample}/{i}. Accuracy: {round(n_right / n_sample, 2) * 100}%')
                bar.progress(i / n_sample)
                time.sleep(0.01)
            time_end = time.time()
            if n_wrong == 0:
                text = "tests" if n_sample > 1 else "test"
                st.success(
                    f"{n_sample} {text} passed in {round((time_end - time_start) * 1000 - n_sample * 10, 2)} ms.")
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

elif option == 'Telecommunication charges':
    option2 = st.sidebar.selectbox(
        "How do you want to enter data?",
        ["Description", 'Input via .csv file', "Boundary value analysis",
         'Equivalence partition method', 'Decision table method', 'Conclusion']
    )
    charges_data = None

    if option2 == "Description":
        st.header("Problem restatement")
        st.markdown(comm_fee.description)

    elif option2 == 'Input via .csv file':
        st.header('Upload the test file')
        uploaded_file = st.file_uploader("", type="csv")
        if uploaded_file is not None:
            charges_data = pd.read_csv(uploaded_file)
        if st.checkbox('Show test samples'):
            st.write(charges_data)

    elif option2 == "Boundary value analysis":
        st.markdown(comm_fee.statement)
        st.header("边界值分析法")
        st.markdown(comm_fee.boundary1)
        st.table(pd.read_csv("./comm_fee/基本边界值.csv"))
        st.markdown(comm_fee.boundary2)
        st.table(pd.read_csv("./comm_fee/健壮性边界.csv"))
        charges_data = pd.read_csv("./comm_fee/电信收费问题-边界值.csv")

    elif option2 == 'Equivalence partition method':
        st.markdown(comm_fee.statement)
        st.header("等价类测试法")
        st.markdown(comm_fee.equivalence1)
        st.table(pd.read_csv("./comm_fee/强一般等价类.csv"))
        st.markdown(comm_fee.equivalence2)
        st.table(pd.read_csv("./comm_fee/额外弱健壮.csv"))
        charges_data = pd.read_csv("./comm_fee/电信收费问题-等价类.csv")

    elif option2 == 'Decision table method':
        st.markdown(comm_fee.statement)
        st.header("决策表测试法")
        st.markdown(comm_fee.dt1)
        charges_data = pd.read_csv("./comm_fee/电信收费问题-扩展决策表.csv")
        st.table(charges_data)

    else:
        st.header("总结")
        st.markdown(comm_fee.conclusion)
        charges_data = pd.read_csv("./comm_fee/电信收费问题-综合.csv")
        st.text("综合的测试用例：")
        st.table(charges_data)

    if option2 != "Description":
        if st.button("Test :)"):
            st.header("Test Result")
            latest_iteration = st.empty()
            bar = st.progress(0)
            charges_data = charges_data.fillna(-1)
            n_sample = charges_data.shape[0]
            n_right, n_wrong = 0, 0
            wrong_samples = []
            time_start = time.time()
            for i in range(1, n_sample + 1):
                minutes = charges_data.loc[i - 1]['T']
                n_overdue = charges_data.loc[i - 1]['M']
                unpaid_fee = charges_data.loc[i - 1]['L']
                discount = charges_data.loc[i - 1]['Discount']
                extra_rate = charges_data.loc[i - 1]['Extra']
                expect = charges_data.loc[i - 1]['Pay']
                output = comm_fee.calculate_comm_fee([minutes, n_overdue, unpaid_fee, discount, extra_rate])
                # if float(expect) == round(output, 2):
                #     n_right = n_right + 1
                if float(expect) - output <= 0.01:
                    n_right = n_right + 1
                else:
                    n_wrong = n_wrong + 1
                    wrong_samples.append((output, expect, i, f'{minutes, n_overdue, unpaid_fee}'))
                latest_iteration.text(
                    f'Progress: {n_sample}/{i}. Accuracy: {round(n_right / n_sample, 2) * 100}%')
                bar.progress(i / n_sample)
                time.sleep(0.01)
            time_end = time.time()
            if n_right == n_sample:
                text = "tests" if n_sample > 1 else "test"
                st.success(
                    f"{n_sample} {text} passed in {round((time_end - time_start) * 1000 - n_sample * 10, 2)} ms.")
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


elif option == 'Salesmen':
    option2 = st.sidebar.selectbox(
        "Which section do you want to view?",
        ["Problem restatement", "Flow chart", "Statement coverage", "Branch/Decision coverage",
         "Simple condition coverage", "Condition determination coverage", "Multiple condition coverage"]
    )
    salesman_data = None

    if option2 == "Problem restatement":
        st.header("Problem restatement")
        st.markdown(salesman.description)

    elif option2 == "Flow chart":
        st.header("Flow chart")
        flowchart = Image.open("./salesman/img/flowchart.png")
        st.image(flowchart, "Flow chart", use_column_width=True)

    elif option2 == "Statement coverage":
        st.header("语句覆盖")
        st.markdown(salesman.statement)
        salesman_data = pd.read_csv("./salesman/销售系统-语句覆盖.csv")

    elif option2 == "Branch/Decision coverage":
        st.header("判断覆盖")
        st.markdown(salesman.branch)
        salesman_data = pd.read_csv("./salesman/销售系统-判断覆盖.csv")

    elif option2 == "Simple condition coverage":
        st.header("条件覆盖")
        st.markdown(salesman.condition)
        salesman_data = pd.read_csv("./salesman/销售系统-条件覆盖.csv")

    elif option2 == "Condition determination coverage":
        st.header("判断——条件覆盖")
        st.markdown(salesman.condition_determination)
        salesman_data = pd.read_csv("./salesman/销售系统-判断-条件覆盖.csv")

    else:
        st.header("条件组合覆盖")
        st.markdown(salesman.multiple_condition)
        salesman_data = pd.read_csv("./salesman/销售系统-条件组合覆盖.csv")

    if "coverage" in option2:
        if st.button("Test :)"):
            st.header("Test Result")
            latest_iteration = st.empty()
            bar = st.progress(0)
            n_sample = salesman_data.shape[0]
            n_right, n_wrong = 0, 0
            wrong_samples = []
            time_start = time.time()
            for i in range(1, n_sample + 1):
                sales = salesman_data.loc[i - 1]['Sales']
                cash_ratio = salesman_data.loc[i - 1]['CashRatio']
                cash_ratio = float(cash_ratio.strip('%'))/100
                n_leave = salesman_data.loc[i - 1]['LeaveDays']
                expect = salesman_data.loc[i - 1]['commission']
                output = salesman.calculate_commission([sales, cash_ratio, n_leave])
                if float(expect) - output <= 0.01:
                    n_right = n_right + 1
                else:
                    n_wrong = n_wrong + 1
                    wrong_samples.append((output, expect, i, f'{sales, cash_ratio, n_leave}'))
                latest_iteration.text(
                    f'Progress: {n_sample}/{i}. Accuracy: {round(n_right / n_sample, 2) * 100}%')
                bar.progress(i / n_sample)
                time.sleep(0.01)
            time_end = time.time()
            if n_right == n_sample:
                text = "tests" if n_sample > 1 else "test"
                st.success(
                    f"{n_sample} {text} passed in {round((time_end - time_start) * 1000 - n_sample * 10, 2)} ms.")
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

elif option == 'Transition Tree':
    option2 = st.sidebar.selectbox(
        "Which section do you want to view?",
        ["ATM", "APP Login"]
    )
    st.header(option2)
    if option2 == "ATM":
        st.subheader("状态图")
        atm1 = Image.open("./tran_tree/img/ATM1.png")
        st.image(atm1, "ATM 状态图", use_column_width=True)
        st.write(tran_tree.state_diagram)
        st.subheader("Transition Tree")
        st.code(tran_tree.code, language='python')
        if st.button("run"):
            st.write(tran_tree.tran_tree(tran_tree.state_diagram))
            atm2 = Image.open("./tran_tree/img/ATM2.png")
            st.image(atm2, "ATM Transition Tree", use_column_width=True)
        st.subheader("状态表")
        st.markdown(tran_tree.md)
    else:
        st.subheader("状态图")
        login1 = Image.open("./tran_tree/img/login.png")
        st.image(login1, "APP Login 状态图", use_column_width=True)
        st.subheader("用例")
        login2 = Image.open("./tran_tree/img/login2.png")
        st.image(login2, "APP Login 用例", use_column_width=True)

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

elif option == 'Question 9':
    st.header("Code")
    st.code(q9.code, language="C")
    st.header("控制流图")
    dia = Image.open("./q9/img/diagram.png")
    st.image(dia, "控制流图", use_column_width=True)
    st.header("基路径")
    st.markdown(q9.md)

elif option == 'JUnit':
    st.markdown(r'''`JUnit` 是一个 Java 编程语言的单元测试框架，其主要利用断言的机制来进行测试预期结果。 
`Junit4` 中的测试代码可被执行，是因为其真正的入口是名为 `JUnitCore` 。它作为 `Junit` 的 `Facade` 模式，来对外进行交互。

它主要有以下特性：

- `JUnit` 提供了注释 `@Test` 等以及确定的测试方法；
- `JUnit` 提供了断言用于测试预期的结果；
- `Junit` 显示测试进度，如果测试是没有问题条形是绿色的，测试失败则会变成红色；

JUnit 很重要的是一个提供注解的功能，常见的有以下注解：

- `@Test` ：用其附着的公共无效方法（即用public修饰的void类型的方法 ）可以作为一个测试用例;
- `@Before` ：用其附着的方法必须在类中的每个测试之前执行，以便执行测试某些必要的先决条件。比如说一些操作可能存在副作用，在进行测试前需要对其进行状态复位，以消除上次测试产生的影响。
- `@After` ：用其附着的方法在执行每项测试后执行，如执行每一个测试后重置某些变量，删除临时变量等。''')

elif option == 'Driver & Stub':
    st.markdown('以类作为单位如何定义 `Driver` 和 `Stub`？')
    st.header('Driver')
    st.markdown(r'''
- `Driver` 即相当于被测模块(类)的调用类，作为被测类的输入，以及对被测类的返回进行检验。作为测试用例的入口，可以模拟用户的数据操作行为。 
- 举例说明: 类A为待测试模块，类B为主函数/其他类，在运行过程中调用了A，通过编写类/主函数Da模块来代替B，调用A模块进行测试。这个过程中Da就是驱动模块。''')
    st.header('Stub')
    st.markdown(r'''
- `Stub` 即为被测模块需要调用的外部函数或类，通过对这些函数或类进行模拟，输出相应的预设结果，从而确保该被测模块只与自己的内部相关，而不受外部影响。 
- 举例说明:类A为待测试模块，类C、D为其他类，A模块在运行中需要调用C、D来实现，通过编写Db、Dc来代替C、D，提供A运行过程中需要的参数，来对A进行测试。这个过程中Db、Dc就是桩模块''')
    img = Image.open("./utils/img/DB.png")
    st.image(img, option, use_column_width=True)
