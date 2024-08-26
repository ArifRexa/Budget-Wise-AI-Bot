
# Country Budget Chatbot

## Overview

Country Budget Chatbot is a Streamlit-based web application that allows users to query budget-related information from a set of documents, specifically PDFs containing budget data. The application utilizes LangChain for document processing, chunking, embedding, and vector search, along with OpenAI's GPT models to provide accurate answers to user queries.

## Features

- **PDF Document Loading**: Load and process PDF files from a specified directory.
- **Document Chunking**: Divide large documents into smaller, manageable chunks for better processing and embedding.
- **Embedding and Vector Search**: Use OpenAI embeddings and FAISS vector search to find the most relevant document chunks for a given query.
- **Question Answering**: Utilize LangChain's question-answering capabilities to retrieve accurate answers based on the documents provided.
- **Streamlit Interface**: User-friendly web interface for interacting with the chatbot.

## Project Structure

```
├── ai_services.py          # Contains the core AI logic for document processing and question answering
├── main.py                 # Streamlit-based UI for interacting with the chatbot
├── requirements.txt        # Required Python libraries for the project
├── .env                    # Environment variables, including OpenAI API key
├── logs/                   # Directory for storing logs
└── README.md               # Project documentation
```

## Prerequisites

- Python 3.8 or higher
- OpenAI API Key (stored in `.env` file)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/country-budget-chatbot.git
   cd country-budget-chatbot
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the `.env` file:**

   Create a `.env` file in the root directory and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your-openai-api-key
   ```

5. **Ensure the logs directory exists:**

   The `ai_services.py` script automatically creates a `logs/` directory if it doesn't exist.

6. **Add your PDF documents:**

   Place your PDF documents in a folder named `documents/` in the project root directory.

## Usage

1. **Running the Streamlit Application:**

   Run the application using the following command:

   ```bash
   streamlit run main.py
   ```

2. **Interacting with the Chatbot:**

   - Once the application is running, you can access it via your browser at `http://localhost:8501`.
   - Enter a query related to the budget documents (e.g., "How much will the agriculture target be increased by how many crore?").
   - Click "Get Answer" to retrieve the response based on the processed documents.

## Logging

- All operations are logged in `logs/ai_services.log`.
- The log file is useful for debugging and understanding the flow of operations within the application.

## Contributing

Contributions are welcome! If you have suggestions or find issues, please create a pull request or open an issue on GitHub.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- [LangChain](https://langchain.com/) for document processing and question answering.
- [Streamlit](https://streamlit.io/) for the easy-to-use web interface.
- [OpenAI](https://openai.com/) for their powerful GPT models.
