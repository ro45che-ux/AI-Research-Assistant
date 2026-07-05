"""from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(chunks):

    texts = [chunk.page_content for chunk in chunks]

    embeddings = model.encode(texts)

    return embeddings"""
import os

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=os.getenv("GEMINI_API_KEY"),
)


def generate_embeddings(chunks):

    texts = [chunk.page_content for chunk in chunks]

    embeddings = embeddings_model.embed_documents(texts)

    return embeddings


def generate_query_embedding(query):

    embedding = embeddings_model.embed_query(query)

    return embedding