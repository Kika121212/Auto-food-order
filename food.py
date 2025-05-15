import streamlit as st
import requests

st.title("Auto Food Ordering App")

platform = st.selectbox("Choose Platform", ["Swiggy", "Zomato"])
cuisine = st.selectbox("Select Cuisine", ["North Indian", "South Indian", "Chinese", "Pizza"])
location = st.text_input("Your Location")
upi_id = st.text_input("Your UPI ID (e.g. yourname@upi)")

if st.button("Place Order"):
    payload = {
        "platform": platform,
        "cuisine": cuisine,
        "location": location,
        "upi_id": upi_id
    }
    response = requests.post("http://localhost:5678/webhook/order", json=payload)
    st.success("Order initiated! Wait for UPI request.")
