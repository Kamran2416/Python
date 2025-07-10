
import streamlit as st
import requests
import json


st.title("Ask SymptomScout")

if 'messages' not in st.session_state:
    st.session_state.messages = []


for messages in st.session_state.messages:
    st.chat_message(messages['role']).markdown(messages['content'])


prompt = st.chat_input("Ask SymptomScout")


API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
API_KEY = ""  


def get_gemini_response(user_input):
    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        "contents": [{
            "parts": [{"text": user_input}]
        }]
    }

    # Send the request to the Gemini API
    try:
        response = requests.post(f"{API_URL}?key={API_KEY}", headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an error if the request fails
        api_response = response.json()  # Parse the JSON response

        # Print the raw response to debug the structure (in case of errors)
        print(json.dumps(api_response, indent=2))  # Log the raw response

        # Accessing the correct structure in the response
        if 'candidates' in api_response and len(api_response['candidates']) > 0:
            return api_response['candidates'][0]['content']['parts'][0]['text']
        else:
            return "I'm sorry, I didn't get a valid response."
    except requests.exceptions.RequestException as e:
        st.error(f"Error contacting Gemini API: {e}")
        return "I'm sorry, there was an error processing your request."

# If a prompt is entered, handle the response
if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    
    # Get the response from Gemini API
    response = get_gemini_response(prompt)
    
    st.chat_message("SymptomScout").markdown(response)
    st.session_state.messages.append({'role': 'SymptomScout', 'content': response})



