import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def display_top_clients_charts(filtered_df, time_unit, number = 5):

    st.subheader(f"Fund disbursement by {time_unit}")

    if not filtered_df.empty:
        top_clients_transactions = filtered_df['name'].value_counts().nlargest(number).reset_index()
        top_clients_transactions.columns = ['name', 'num_transactions']
        st.subheader(f"Top {number} clients by Number of Transactions")
        st.bar_chart(top_clients_transactions, x="name", y="num_transactions")

        top_clients_amount = filtered_df.groupby('name')['amount'].sum().nlargest(number).reset_index()
        top_clients_amount.columns = ['name', 'total_disbursed']
        st.subheader(f"Top {number} clients by Total Disbursed Amount")
        st.bar_chart(top_clients_amount, x="name", y="total_disbursed")
    else:
        st.info("No data found for the chosen period and filter setting.")



def display_transaction_history_charts(filtered_df, time_unit, selected_payment_methods):

    if not filtered_df.empty:
        st.subheader("Amount Over Time")
        df_grouped_amount = filtered_df.groupby([pd.Grouper(key='date', freq=time_unit[0].upper()), 'payment_method'])['amount'].sum().reset_index()
        df_total_amount = filtered_df.groupby(pd.Grouper(key='date', freq=time_unit[0].upper()))['amount'].sum().reset_index()

        fig_amount = go.Figure()
        for method in selected_payment_methods:
            df_method = df_grouped_amount[df_grouped_amount['payment_method'] == method]
            fig_amount.add_trace(go.Scatter(x=df_method['date'], y=df_method['amount'], name=f'{method} Amount', mode='lines+markers'))
        fig_amount.add_trace(go.Bar(x=df_total_amount['date'], y=df_total_amount['amount'], name='Total Amount', opacity=0.3))
        fig_amount.update_layout(yaxis_title="Amount")
        st.plotly_chart(fig_amount)

        st.subheader("Number of Transactions Over Time")
        df_grouped_count = filtered_df.groupby([pd.Grouper(key='date', freq=time_unit[0].upper()), 'payment_method'])['amount'].count().reset_index()
        df_total_count = filtered_df.groupby(pd.Grouper(key='date', freq=time_unit[0].upper()))['amount'].count().reset_index()

        fig_count = go.Figure()
        for method in selected_payment_methods:
            df_method_count = df_grouped_count[df_grouped_count['payment_method'] == method]
            fig_count.add_trace(go.Scatter(x=df_method_count['date'], y=df_method_count['amount'], name=f'{method} Transactions', mode='lines+markers'))
        fig_count.add_trace(go.Bar(x=df_total_count['date'], y=df_total_count['amount'], name='Total Transactions', opacity=0.3))
        fig_count.update_layout(yaxis_title="Number of Transactions")
        st.plotly_chart(fig_count)

        st.subheader("Distribution by Payment Method")
        col_payment_dist_amount, col_payment_dist_count = st.columns(2)

        with col_payment_dist_amount:
            st.subheader("Amount Distribution")
            payment_amount = filtered_df.groupby('payment_method')['amount'].sum().reset_index()
            fig_amount_pie = px.pie(payment_amount, names='payment_method', values='amount', hover_data=['amount'], labels={'amount':'Total Amount'})
            st.plotly_chart(fig_amount_pie)

        with col_payment_dist_count:
            st.subheader("Transaction Count Distribution")
            payment_count = filtered_df['payment_method'].value_counts().reset_index()
            payment_count.columns = ['payment_method', 'count']
            fig_count_pie = px.pie(payment_count, names='payment_method', values='count', hover_data=['count'], labels={'count':'Number of Transactions'})
            st.plotly_chart(fig_count_pie)
    else:
        st.info("No transactions found for this client.")

def display_metrics_sidebar(metrics):
    st.sidebar.subheader("Métrics")
    st.sidebar.metric("Total Dispersed", f"${metrics.get('total_dispersed', 0):,.2f}")
    st.sidebar.metric("Total transactions", metrics.get('total_transactions', 0))
    st.sidebar.metric("Average", f"${metrics.get('average_amount', 0):,.2f}")
    st.sidebar.metric("Min amount", f"${metrics.get('min_amount', 0):,.2f}")
    st.sidebar.metric("Máx amoun", f"${metrics.get('max_amount', 0):,.2f}")