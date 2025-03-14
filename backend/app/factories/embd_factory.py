import logging

from langchain_google_genai import GoogleGenerativeAIEmbeddings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_embedding_function(api_key):
    try:
        embedding_function = GoogleGenerativeAIEmbeddings(
            model="models/text-embedding-004",
            google_api_key=api_key,
        )
    
    except Exception as e:
        logger.error("embd connection failed %s", e)

    return embedding_function
