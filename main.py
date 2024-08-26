import streamlit as st
from ai_services import AIServices

# Initialize the AI services
ai_service = AIServices()

st.title("Country Budget Chatbot")

# Input field for the user query
user_query = st.text_input("Ask a question about the documents:")

if st.button("Get Answer"):
    if user_query:
        # Retrieve the answer using the AI service
        answer = ai_service.retrieve_answers(user_query)
        st.write("**Answer:**", answer["output_text"])
    else:
        st.write("Please enter a query to get an answer.")


