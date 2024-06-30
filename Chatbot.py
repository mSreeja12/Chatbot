#openai 1.35.7

#Path of json file: C:\Users\Sreeja Mondal\Desktop\Chatbot\config.json

import streamlit as st
import openai

# Set your OpenAI API key here
OPENAI_API_KEY = "sk-proj-RSt3sA96bw3Eec8CwdBaT3BlbkFJx9FdrrYOqoJf3fH9qHMm"

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Set up OpenAI API key
openai.api_key = OPENAI_API_KEY

# Set up Streamlit page configuration
st.set_page_config(
    page_title="My Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🧠 GPT Chatbot 🤓💻")

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
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # Adjust the engine name as needed
            prompt="Translate the following English text into French: Hello, how are you?",
            max_tokens=150
        )

        assistant_message = response['choices'][0]['text']
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_message})

        st.markdown(assistant_message)
    
    except openai.OpenAIError as e:
        st.error(f"OpenAI API error: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
