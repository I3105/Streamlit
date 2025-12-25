import streamlit as st

st.title("Hello from Streamlit on GitHub 👋")
st.write("This app is deployed directly from a GitHub repo!")
name = st.text_input("Enter your name")
if name:
    st.success(f"Hi, {name}! 🚀")

