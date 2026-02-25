import streamlit as st
import requests
import uuid

API_URL = "https://ai-agent-backend-3db9.onrender.com"

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []


st.title("AI Agent Chatbot")


if st.button("New Chat"):
    st.session_state.session_id = str(uuid.uuid4())
    st.session_state.messages = []


for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


user_input = st.chat_input("Type message")


if user_input:

    st.chat_message("user").write(user_input)

    res = requests.post(
        API_URL,
        json={
            "session_id": st.session_state.session_id,
            "message": user_input
        }
    )

    response = res.json()["response"]

    st.chat_message("assistant").write(response)

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

