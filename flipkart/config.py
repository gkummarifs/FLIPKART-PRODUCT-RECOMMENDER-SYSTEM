import os
from dotenv import load_dotenv

load_dotenv()
# No need to include Hugging Face Token here as it is being used 
# directly from the environment variable

class Config:
    ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
    ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
    ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"
    # Below is from Grop, have been choosed from the below hyperlink
    # https://console.groq.com/docs/models
    RAG_MODEL = "llama-3.1-8b-instant"