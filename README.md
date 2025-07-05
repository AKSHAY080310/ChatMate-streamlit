# 🤖 ChatMate - Streamlit Hugging Face Chat Assistant

ChatMate is a lightweight AI-powered assistant built using **Streamlit** and an open-source **Hugging Face language model**. The app provides an interactive chat interface that connects to Hugging Face's inference API to deliver intelligent responses.

---

## 🚀 Features

- 🧠 Uses powerful Hugging Face models (e.g. Mixtral-8x7B)
- ⚡ Fast and responsive Streamlit UI
- 🔐 Hugging Face API key managed securely via `.streamlit/secrets.toml`
- 🧪 Easy to customize or expand with your own models

---

## 🛠 Requirements

Install dependencies:

```bash
pip install -r requirements.txt

---

## 📁 Project Structure

ChatMate-streamlit/
├── app1.py               # Main Streamlit app
├── .gitignore            # Ignore list
├── requirements.txt      # Python dependencies
└── .streamlit/
    └── secrets.toml      # Hugging Face API token (not tracked in Git)

