import streamlit as st
from app.api import fetch_info_by_client_id
from utils.data_proccesing import (
    load_and_preprocess_data,
    calculate_metrics,
)
from components.filters import date_filters, payment_methods_multiselect_filter
from components.charts import display_transaction_history_charts, display_metrics_sidebar
import requests

def client_details_page():
    st.header("Client Transaction History")
    client_id = st.text_input("Enter Client ID:")

    if client_id:
        try:
            client_data = fetch_info_by_client_id(client_id)
            if client_data:
                df = load_and_preprocess_data(client_data)
                client_name = df['name'].iloc[0] if not df.empty else None
                if client_name:
                    st.subheader(f"Transactions for: {client_name}")
                    with st.container():
                        col_charts, col_filters = st.columns([3, 1])
                        with col_filters:
                            filtered_df, time_unit = date_filters(df, key_prefix=f"client_{client_id}_")
                            filtered_df, selected_payment_methods = payment_methods_multiselect_filter(filtered_df, key_prefix=f"client_{client_id}_")

                            metrics = calculate_metrics(filtered_df)
                            st.sidebar.header("Metrics")
                            display_metrics_sidebar(metrics)

                        with col_charts:
                            display_transaction_history_charts(filtered_df, time_unit, selected_payment_methods)
                else:
                    st.info(f"No transaction data available for client ID '{client_id}'.")
            else:
                st.info(f"No data returned for client ID '{client_id}'.")
        except requests.exceptions.RequestException as e:
            st.error(f"Could not retrieve client information. ")

if __name__ == "__main__":
    client_details_page()