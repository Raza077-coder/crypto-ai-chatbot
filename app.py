# crypto-ai-chatbot
import streamlit as st
from openai import OpenAI

# 🔐 API KEY (Streamlit secrets se ayegi)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Crypto AI Bot", page_icon="💰")

st.title("💰 Crypto AI Chat Bot")

# Memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a crypto expert AI. Explain coins simply, risks included."}
    ]

# Chat history show
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Ask about any crypto coin...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
