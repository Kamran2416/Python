import streamlit as st
import requests
import json
import base64
from PIL import Image

st.title("Ask SymptomScout")

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

prompt = st.chat_input("Ask SymptomScout")
uploaded_image = st.file_uploader("Upload an image (optional)", type=["jpg", "jpeg", "png"])

API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
API_KEY = "AIzaSyAWfOaA_zYrilK7uQeuC3Mh0552PaoMRzo"

def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

def get_gemini_response(user_input, image=None):
    headers = {
        'Content-Type': 'application/json',
    }

    # Prepare the payload
    data = {
        "model": "gemini-1.5-flash",
        "prompt": {
            "text": user_input
        }
    }

    # Add image if uploaded
    if image:
        encoded_image = encode_image(image)
        data["prompt"]["image"] = {"base64": encoded_image}

    try:
        response = requests.post(f"{API_URL}?key={API_KEY}", headers=headers, data=json.dumps(data))
        response.raise_for_status()
        api_response = response.json()
        print(json.dumps(api_response, indent=2))  # Debug response
        return api_response.get("candidates", [{}])[0].get("content", "No valid response received.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error contacting Gemini API: {e}")
        if hasattr(response, 'content'):
            print(f"Response content: {response.content.decode('utf-8')}")  # Debug error details
        return "I'm sorry, there was an error processing your request."

if prompt or uploaded_image:
    if prompt:
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({'role': 'user', 'content': prompt})

    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_container_width=True)

    response = get_gemini_response(prompt, image=uploaded_image if uploaded_image else None)

    if isinstance(response, str):
        st.chat_message("SymptomScout").markdown(response)
        st.session_state.messages.append({'role': 'SymptomScout', 'content': response})
    else:
        st.chat_message("SymptomScout").markdown("Response received but could not be parsed.")
