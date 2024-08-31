import os
import streamlit as st
from dotenv import find_dotenv, load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationSummaryMemory

# Load environment variables from .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Initialize Groq client with API key from environment variables
API_KEY = os.getenv("groq_API_KEY")

# Set up the LLM with optimized parameters
llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0.7,  # Slightly lower temperature for more focused responses
    max_tokens=512,  # Limited tokens for quicker responses
    timeout=10,  # Reasonable request timeout
    max_retries=1,  # Fewer retries to reduce delays
    groq_api_key=API_KEY
)

# Streamlit app setup
st.title("Chat with Me!")

# Initialize conversation state if not already present
if 'conversation_chain' not in st.session_state:
    st.session_state.memory = ConversationSummaryMemory(llm=llm)
    st.session_state.conversation_chain = ConversationChain(
        llm=llm,
        memory=st.session_state.memory,
        verbose=False  # Less verbose output
    )

# Display previous messages if any
if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

# Input from the user
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Show user input in chat
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({'role': 'user', 'content': user_input})

    # Generate and display the assistant's response
    response = st.session_state.conversation_chain.predict(input=user_input)
    st.chat_message("assistant").markdown(response)

    # Update conversation history
    st.session_state.messages.append({'role': 'assistant', 'content': response})