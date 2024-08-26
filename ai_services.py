import logging
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
import os

# Load environment variables
from dotenv import load_dotenv
# Configure logging
# Ensure the logs directory exists
log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"{log_directory}/ai_services.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
load_dotenv()


class AIServices:
    def __init__(self, directory='documents/'):
        logger.info("Initializing AIServices with directory: %s", directory)
        self.llm = OpenAI(temperature=0.5)
        self.embeddings = OpenAIEmbeddings(api_key=os.environ['OPENAI_API_KEY'])
        self.index = None

        # Load and process documents
        self.documents = self.read_doc(directory)
        self.chunked_documents = self.chunk_data(self.documents)
        self.create_index()

    def read_doc(self, directory):
        """Read all PDF documents from a directory."""
        logger.info("Loading documents from directory: %s", directory)
        file_loader = PyPDFDirectoryLoader(directory)
        documents = file_loader.load()
        logger.info("Loaded %d documents", len(documents))
        return documents

    def chunk_data(self, docs, chunk_size=800, chunk_overlap=50):
        """Split documents into smaller chunks."""
        logger.info("Splitting documents into chunks of size %d with overlap %d", chunk_size, chunk_overlap)
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        docs = text_splitter.split_documents(docs)
        logger.info("Created %d chunks from documents", len(docs))
        return docs

    def create_index(self):
        """Create a FAISS index from the chunked documents."""
        logger.info("Creating FAISS index from documents")
        self.index = FAISS.from_documents(self.chunked_documents, self.embeddings)
        logger.info("FAISS index created successfully")

    def retrieve_query(self, query, k=2):
        """Retrieve documents using cosine similarity."""
        logger.info("Retrieving top %d documents for query: %s", k, query)
        matching_results = self.index.similarity_search(query, k=k)
        logger.info("Retrieved %d matching documents", len(matching_results))
        return matching_results

    def retrieve_answers(self, query):
        """Use the QA chain to retrieve answers to the query."""
        logger.info("Retrieving answer for query: %s", query)
        chain = load_qa_chain(self.llm, chain_type="stuff")
        doc_search = self.retrieve_query(query)

        # Pass the input as a dictionary containing both input_documents and question
        response = chain.invoke({
            "input_documents": doc_search,
            "question": query
        })

        logger.info("Answer retrieved successfully")
        return response


if __name__ == "__main__":
    # Example usage
    ai_service = AIServices()

    # Example query
    our_query = "How much will the agriculture target be increased by how many crore?"
    answer = ai_service.retrieve_answers(our_query)
    logger.info("Answer: %s", answer["output_text"])
