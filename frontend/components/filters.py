import streamlit as st
import pandas as pd
from utils.data_proccesing import *

def date_filters(df, key_prefix=""):
    
    st.subheader("Filters")
    time_unit = st.selectbox("Group by:", ["Day", "Month", "Year"], key=f"{key_prefix}time_unit_client")

    filtered_df = df.copy()
    min_date = df['date'].min().date()
    max_date = df['date'].max().date()
    date_range = st.date_input("Date range:", (min_date, max_date), key=f"{key_prefix}date_range_client")
    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = filter_by_date_range(filtered_df, start_date, end_date)

    return filtered_df, time_unit


def payment_method_filter(df, key_prefix=""):

    payment_methods = sorted(df['payment_method'].unique())
    selected_payment_method = st.selectbox("Payment Method:", ["All"] + payment_methods, key=f"{key_prefix}payment_method_filter")
    if selected_payment_method != "All":
        df = df[df['payment_method'] == selected_payment_method]
    return df, selected_payment_method

def payment_methods_multiselect_filter(df, key_prefix=""):

    payment_methods = sorted(df['payment_method'].unique())
    selected_payment_methods = st.multiselect("Payment Method(s):", payment_methods, default=payment_methods, key=f"{key_prefix}payment_method_filter")
    df = df[df['payment_method'].isin(selected_payment_methods)]
    return df, selected_payment_methods