import requests
import streamlit as st

api_url = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {
    "Authorization": f"Bearer {st.secrets['hf_token']}"
}
response = requests.post(api_url, headers=headers, json={"inputs": "Hello"})
st.write("Response:", response.status_code, response.text)
