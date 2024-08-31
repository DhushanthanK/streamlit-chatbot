## Streamlit Chatbot

A Streamlit-based chatbot application utilizing the Groq API and Langchain for conversational AI.

### Description

This project features a chatbot application built with Streamlit. It integrates the Groq API and Langchain to provide real-time conversational responses. The chatbot is designed to retain conversation history and offer relevant answers based on previous interactions.

### Features

- Interactive chatbot interface using Streamlit
- Real-time conversation with a language model
- Conversation history management
- Configurable LLM parameters for focused responses

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/DhushanthanK/streamlit-chatbot.git
    cd streamlit-chatbot
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    Create a `requirements.txt` file with the following content:

    ```txt
    streamlit
    python-dotenv
    langchain_groq
    ```

    Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the project directory with the following content:

    ```env
    groq_API_KEY=your_groq_api_key_here
    ```

    Replace `your_groq_api_key_here` with your actual Groq API key.

5. **Run the Streamlit app:**

    ```bash
    streamlit run chat.py
    ```

    This will start the Streamlit server, and you can access the chatbot application in your web browser at `http://localhost:8501`.

### Usage

- Open the application in your web browser.
- Type your message in the input box and press Enter to start a conversation.
- The chatbot will respond based on previous interactions, and the conversation history will be managed automatically.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
