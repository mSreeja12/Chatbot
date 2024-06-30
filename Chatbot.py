#openai 1.35.7

#Path of json file: C:\Users\Sreeja Mondal\Desktop\Chatbot\config.json

import os
import json
import streamlit as st
import openai

# Load configuration
working_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(working_dir, "config.json")) as config_file:
    config_data = json.load(config_file)

# Set up OpenAI API key
OPENAI_API_KEY = config_data["API-KEY"]
openai.api_key = OPENAI_API_KEY

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Set up Streamlit page configuration
st.set_page_config(
    page_title="My Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🧠 GPT-4o - Chatbot 🤓💻")

# Display chat history
for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.text_input("Ask Me...", value=message["content"], key=message["content"])
    elif message["role"] == "assistant":
        st.markdown(message["content"])

# Input field for user's message
user_prompt = st.text_input("Ask Me...")
if user_prompt:
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Send user's message to model to get response
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                *st.session_state.chat_history
            ]
        )

        assistant_message = response['choices'][0]['message']['content']
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_message})

        st.markdown(assistant_message)
    
    except Exception as e:
        st.error(f"Error: {e}")
