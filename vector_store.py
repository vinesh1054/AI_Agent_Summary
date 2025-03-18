from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

DB_FAISS_PATH = "vectorstore/db_faiss"

def create_chunks(text, chunk_size=1000, chunk_overlap=100):
    """Splits text into overlapping chunks for better context retention."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_text(text)

def store_text_in_faiss(text):
    """Converts text into embeddings and stores in FAISS."""
    text_chunks = create_chunks(text)
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Create FAISS vector store
    db = FAISS.from_texts(text_chunks, embedding_model)
    db.save_local(DB_FAISS_PATH)  # Save locally
    return db

def load_faiss_db():
    """Loads stored FAISS database."""
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)
