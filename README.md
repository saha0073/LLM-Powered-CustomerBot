# Customer Support Chatbot with LLM Integration

This project is a customer support chatbot designed to answer questions about Thoughtful AI's automation agents. The chatbot uses predefined responses for common questions and leverages OpenAI's GPT-4o model to provide intelligent fallback responses for more complex queries.

## Features

- **Predefined Responses**: The chatbot contains hardcoded answers to frequently asked questions related to Thoughtful AI.
- **GPT-4o Fallback**: If a user's question doesn't match a predefined answer, the chatbot falls back to OpenAI's GPT-4o model to generate a response.
- **User-Friendly Interface**: Built using Streamlit, the chatbot provides an easy-to-use web interface for interacting with the AI.

## Tech Stack

- **Streamlit**: Used for building the front-end UI of the chatbot.
- **OpenAI GPT-4o**: Provides fallback responses when the question doesn't match any predefined answers.
- **Python**: The core programming language used to build the project.

## Usage

- When the app is running, you can ask questions in the input field about Thoughtful AI's agents, such as:
  - *What does the eligibility verification agent (EVA) do?*
  - *Tell me about Thoughtful AI's agents.*
  - If the question matches one in the predefined dataset, the corresponding answer will be displayed.
  - If no match is found, the chatbot will use OpenAI GPT-4o to generate a response.

## Example Questions

Here are some example questions you can ask the chatbot:

- "What does the eligibility verification agent (EVA) do?"
- "What does the claims processing agent (CAM) do?"
- "How does the payment posting agent (PHIL) work?"

Happy Coding!
