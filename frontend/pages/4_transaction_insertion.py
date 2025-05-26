import streamlit as st
import requests
from datetime import datetime
from app.config import BACKEND_URL

clients = [{"id":id} for id in range(101,111)]
payment_methods = [
    {"id": 1, "name": "Tranferencia"},
    {"id": 2, "name": "Nequi"},
    {"id": 3, "name": "Daviplata"}
]

st.title("Create dummy transaction")

client_ids = [client["id"] for client in clients]
client_id = st.selectbox("Select client id", client_ids)

method_names = [f"{m['name']}" for m in payment_methods]
selected_method_index = st.selectbox("Selecciona método de pago", range(len(payment_methods)), format_func=lambda i: method_names[i])
payment_method_id = payment_methods[selected_method_index]["id"]

amount = st.number_input("Transaction amoun", min_value=0.0, step=1000.0)


selected_date = st.date_input("transaction date", datetime.today())
formatted_date = selected_date.strftime("%Y-%m-%d")


if st.button("Create transaction"):
    payload = {
        "date": formatted_date,
        "client_id": client_id,
        "amount": amount,
        "payment_method_id": payment_method_id
        
    }

    try:
        response = requests.post(f"{BACKEND_URL}/create-transaction", json=payload)
        if response.status_code == 201:
            st.success("✅ Success transaction created")
        else:
            st.error(f"❌ Error creating transaction: {response.text}")
    except Exception as e:
        st.error(f"❌ Connection failure with backend: {str(e)}")