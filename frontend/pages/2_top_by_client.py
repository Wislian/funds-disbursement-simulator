import streamlit as st
from app.api import fetch_info_by_client
from utils.data_proccesing import (
    load_and_preprocess_data,
    calculate_metrics,
)
from components.filters import date_filters, payment_method_filter
from components.charts import display_top_clients_charts, display_metrics_sidebar

def top_total_client_page():
    st.header("Total Disbursed by Client")

    df = load_and_preprocess_data(fetch_info_by_client())

    with st.container():
        col_charts, col_filters = st.columns([3, 1])
        with col_filters:
            filtered_df, time_unit = date_filters(df, key_prefix="top_")
            filtered_df,_ = payment_method_filter(filtered_df, key_prefix="top_")
            metrics = calculate_metrics(filtered_df)
            st.sidebar.header("Metrics")
            display_metrics_sidebar(metrics)

        with col_charts:
            display_top_clients_charts(filtered_df, time_unit)

if __name__ == "__main__":
    top_total_client_page()