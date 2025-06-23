import streamlit as st
import requests

# Load the secret Hugging Face API token
HF_API_TOKEN = st.secrets["HF_API_TOKEN"]
ASSISTANT_ID = "68543ce16237dcbb171ec9cd"  # Replace with your actual Assistant ID

def query_huggingface(message):
    url = f"https://api.huggingface.co/chat/conversations"
    headers = {
        "Authorization": f"Bearer {HF_API_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "assistant_id": ASSISTANT_ID,
        "inputs": {"text": message}
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()["generated_text"]

st.title("🤖 Hugging Face Chat Assistant")
user_input = st.text_input("You: ", "")

if user_input:
    reply = query_huggingface(user_input)
    st.write(f"Assistant: {reply}")
