import streamlit as st
from openai import OpenAI
import os

# Define your OpenAI API key
openai_api_key = os.environ['OPENAI_API_KEY']
client = OpenAI(api_key=openai_api_key)

# Predefined data for Thoughtful AI
qa_data = {
    "questions": [{
        "question":
        "What does the eligibility verification agent (EVA) do?",
        "answer":
        "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
    }, {
        "question":
        "What does the claims processing agent (CAM) do?",
        "answer":
        "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
    }, {
        "question":
        "How does the payment posting agent (PHIL) work?",
        "answer":
        "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
    }, {
        "question":
        "Tell me about Thoughtful AI's Agents.",
        "answer":
        "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
    }, {
        "question":
        "What are the benefits of using Thoughtful AI's agents?",
        "answer":
        "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
    }]
}


# Function to get a response from OpenAI GPT-4o chat completions API
def get_llm_response(user_input):
    try:
        # Call OpenAI's GPT-4o API using the chat completions format
        response = client.chat.completions.create(
            model="gpt-4o",  # Ensure you're using the right model identifier
            messages=[{
                "role": "system",
                "content": "You are a helpful assistant."
            }, {
                "role": "user",
                "content": user_input
            }])
        return response.choices[0].message.content
    except Exception as e:
        return f"Error in fetching GPT-4o response: {str(e)}"


# Function to match user input with predefined questions and return the answer, or fallback to GPT-4o
def get_response(user_input):
    user_input = user_input.lower(
    )  # Convert user input to lowercase for better matching
    for qa in qa_data['questions']:
        if qa['question'].lower() == user_input:
            return qa['answer']
    # If no match, fallback to GPT-4o response
    return get_llm_response(user_input)


# Streamlit UI
st.title("Thoughtful AI Customer Support Chatbot")

# Text input box for user to ask questions
user_input = st.text_input("Ask a question about Thoughtful AI:", "")

# If the user submits a question
if user_input:
    # Get the response from the chatbot
    response = get_response(user_input)

    # Display the response
    st.write(f"**Answer:** {response}")
