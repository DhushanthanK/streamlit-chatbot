# Streamlit Chatbot

A Streamlit-based chatbot application utilizing the Groq API and Langchain for conversational AI.

## Description

This project features a chatbot application built with Streamlit. It integrates the Groq API and Langchain to provide real-time conversational responses. The chatbot is designed to retain conversation history and offer relevant answers based on previous interactions.

## Features

- Interactive chatbot interface using Streamlit
- Real-time conversation with a language model
- Conversation history management
- Configurable LLM parameters for focused responses

https://github.com/user-attachments/assets/10721e4d-01b5-4ddd-a6ea-3116c09c6470

## Technical Specifications

### Language Model

- **Model Name:** `llama-3.1-70b-versatile`
- **API Provider:** Groq
- **Temperature:** 0.7
  - **Description:** Controls the randomness of responses. A lower value results in more focused and deterministic responses.
- **Max Tokens:** 512
  - **Description:** Limits the number of tokens (words or characters) in the generated response. Ensures quicker responses.
- **Timeout:** 10 seconds
  - **Description:** Sets the maximum time to wait for a response from the API before timing out.
- **Max Retries:** 1
  - **Description:** Number of times to retry the request in case of failure.

### Streamlit Setup

- **Framework:** Streamlit
- **Purpose:** Provides the interactive web interface for the chatbot application.
- **Features:**
  - Real-time chat interface.
  - User-friendly input and display components.

### Memory Management

- **Memory Type:** `ConversationSummaryMemory`
- **Description:** Stores the conversation history and summarizes past interactions to maintain context and continuity in the conversation.

### Dependencies

- **Streamlit:** Used to create the interactive web interface.
- **python-dotenv:** Loads environment variables from a `.env` file.
- **langchain_groq:** Provides integration with Groq's language model API.

## Installation and Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/DhushanthanK/streamlit-chatbot.git
    cd streamlit-chatbot
    ```

2. **Create a Virtual Environment (Optional):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

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

4. **Configure Environment Variables:**

    Create a `.env` file in the project directory with the following content:

    ```env
    groq_API_KEY=your_groq_api_key_here
    ```

    Replace `your_groq_api_key_here` with your actual Groq API key.

5. **Run the Application:**

    ```bash
    streamlit run chat.py
    ```

    This will start the Streamlit server, and you can access the chatbot application in your web browser at `http://localhost:8501`.

## Usage

- Open the application in your web browser.
- Type your message in the input box and press Enter to start a conversation.
- The chatbot will respond based on previous interactions, and the conversation history will be managed automatically.

## License

- **License Type:** MIT License
- **Details:** See the [LICENSE](LICENSE) file for more information.

## Additional Information

- **Free to Use:** The application and its code are freely available for use and modification under the MIT License.
- **Language Model:** The application uses Groq's language model, which is versatile and can be configured to suit various conversational needs.
