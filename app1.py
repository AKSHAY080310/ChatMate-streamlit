import streamlit as st
import requests

# Title
st.title("🤖 Hugging Face Chat Assistant")

# User Input
user_input = st.text_input("You:", "")

# API setup
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {
    "Authorization": f"Bearer {st.secrets['HUGGINGFACE_TOKEN']}",  # Use the exact key from secrets.toml
    "Content-Type": "application/json"
}

# On input, send to model
if user_input:
    with st.spinner("Talking to assistant..."):

        # Format prompt using Hugging Face instruction format
        prompt = f"<s>[INST] {user_input} [/INST]"

        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 200,
                "temperature": 0.7,
                "return_full_text": True
            }
        }

        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()
            full_output = result[0]["generated_text"]
            # Clean assistant reply by removing prompt part
            reply = full_output.replace(prompt, "").strip()
            st.markdown(f"**Assistant:** {reply}")
        else:
            st.error("❌ Something went wrong!")
            st.code(response.text)
