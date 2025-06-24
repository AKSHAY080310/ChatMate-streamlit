import streamlit as st
import requests

# Title
st.title("🤖 Hugging Face Chat Assistant")

# Input box
user_input = st.text_input("You:", "")

# If user enters a message
if user_input:
    with st.spinner("Talking to assistant..."):
        API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"

    headers = {
        "Authorization": f"Bearer {st.secrets['hf_token']}",
        "Content-Type": "application/json"
    }

    prompt = f"<s>[INST] {user_input} [/INST]"

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.7
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        full_output = result[0]["generated_text"]
        reply = full_output.replace(prompt, "").strip()
        st.write("Assistant:", reply)
    else:
        st.error("❌ Something went wrong!")
        st.text("Details:")
        st.code(response.text)
