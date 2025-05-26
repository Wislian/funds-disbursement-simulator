import streamlit as st
from app.api import fetch_all_transactions
from utils.data_proccesing import (
    load_and_preprocess_data,
    calculate_metrics,
)
from components.filters import date_filters, payment_methods_multiselect_filter
from components.charts import display_transaction_history_charts, display_metrics_sidebar


def transactions_page():
    st.header("Transaction Analysis")

    df = load_and_preprocess_data(fetch_all_transactions())

    with st.container():
        col_charts, col_filters = st.columns([3, 1])
        with col_filters:
            filtered_df, time_unit = date_filters(df, key_prefix="transactions_")
            filtered_df, selected_payment_methods = payment_methods_multiselect_filter(filtered_df, key_prefix="transactions_")

            metrics = calculate_metrics(filtered_df)
            st.sidebar.header("Metrics")
            display_metrics_sidebar(metrics)

        with col_charts:
            display_transaction_history_charts(filtered_df, time_unit, selected_payment_methods)

if __name__ == "__main__":
    transactions_page()