import streamlit as st
import requests

st.title("Auto Order Food App")

platform = st.selectbox("Choose Platform", ["Swiggy", "Zomato"])
item = st.text_input("Enter Food Item")
upi_id = st.text_input("Enter Your UPI ID")

if st.button("Place Order"):
    payload = {
        "platform": platform.lower(),
        "item": item,
        "upi_id": upi_id
    }
    response = requests.post("http://localhost:5678/webhook-test/order", json=payload)

    if response.status_code == 200:
        st.success("Order Placed Successfully!")
    else:
        st.error("Failed to place order.")
