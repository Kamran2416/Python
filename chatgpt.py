import streamlit as st

st.title("SymptomScout")

if 'messages' not in st.session_state:
    st.session_state.messages = []

for messages in st.session_state.messages:
    st.chat_message(messages['role']).markdown(messages['content'])

prompt = st.chat_input("Ask SymptomScout")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({'role':'user', 'content':prompt})
    response = "I'm sorry, I don't understand. Please ask me something else."
    st.chat_message("bot").markdown(response)
    st.session_state.messages.append({'role':'bot', 'content':response})
