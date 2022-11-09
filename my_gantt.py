#!/usr/bin/python3
# -*- coding:UTF-8 -*-

"""
@author:liulipeng
@file:my_gantt.py
@time:2022/11/02
"""
import datetime

import altair as alt
import pandas as pd
import streamlit as st

import os

if not os.path.exists("my_jobs.csv"):
    init_data = pd.DataFrame(columns=["我的项目", "开始时间", "结束时间", "备注","需求方"])
    init_data.to_csv("my_jobs.csv", index=False)

data = pd.read_csv("my_jobs.csv")

st.title("给点活路吧！排不下去了")
form = st.form(key="annotation")
with form:
    task = st.text_input("工作名称:")
    start_time = st.date_input(
        "开始时间",
        datetime.date.today())
    end_time = st.date_input(
        "结束时间",
        datetime.date.today())
    comment = st.text_area("备注:")
    commander = st.text_area("需求方:")
    submitted = st.form_submit_button(label="添加需求")

if submitted:
    data.loc[len(data)] = {"我的项目": task, "开始时间": start_time, "结束时间": end_time, "备注": comment,"需求方":commander}
    df = data.copy()
    df.to_csv("my_jobs.csv", index=False)
    st.success("加钱！加钱！加钱！")
    st.balloons()

if not data.empty:
    c = alt.Chart(pd.read_csv("my_jobs.csv")).mark_bar().encode(
        x='开始时间',
        x2='结束时间',
        y='我的项目'
    )

    st.altair_chart(c, use_container_width=True)

expander = st.expander("点击查看丽鹏无趣的一生时光")
with expander:
    st.table(pd.read_csv("my_jobs.csv"))


if not data.empty:
    form2 = st.form(key="delete")
    with form2:
        number = st.number_input('请输入需要删除的需求序号',min_value=0,max_value=len(data)-1,value=len(data)-1,step=1)
        button = st.form_submit_button("点击删除")
    if button:
        df = data.drop(labels=number)
        df.to_csv("my_jobs.csv",index=False)
        st.experimental_rerun()
