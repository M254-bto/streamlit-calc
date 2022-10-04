import streamlit as st
import json
import requests


st.title("Fast Api backend Calculator")

st.write("This is a simple calculator that uses a Fast Api backend")

option = st.selectbox("Select an operation", ("Add", "Subtract", "Multiply", "Divide"))

x = st.slider("value of x", 0, 100, 10)

y = st.slider("value of y", 0, 100, 10)

inputs = {"operator": option, "x": x, "y": y}

if st.button("Calculate"):
    res = requests.post("http://localhost:8000/calculate", data = json.dumps(inputs))
    st.subheader(f"Result: {res.text}")