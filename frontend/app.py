import streamlit as st
import requests

# FastAPI URL
API_URL = "https://backend-4-gsat.onrender.com/chat"

st.title("💬FAQ Bot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
user_query = st.chat_input("Ask me a question...")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    
    with st.chat_message("user"):
        st.markdown(user_query)

    # Send query to FastAPI backend
    try:
        response = requests.post(API_URL, json={"query": user_query})

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Try to parse the JSON response
            try:
                response_data = response.json()
                bot_response = response_data.get("response", "Error: No response from server.")
            except ValueError:
                bot_response = f"Error: Unable to parse JSON. Raw response: {response.text}"
        else:
            bot_response = f"Error: {response.status_code} - {response.text}"

    except requests.exceptions.RequestException as e:
        # Handle request exceptions like network issues
        bot_response = f"Request error: {str(e)}"

    # Append the bot's response to the chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
    with st.chat_message("assistant"):
        st.markdown(bot_response)

