import logging

from langchain_google_genai import ChatGoogleGenerativeAI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_llm_client(api_key, temperature):
    try: 
        llm = ChatGoogleGenerativeAI(
            model="models/gemini-2.0-flash",
            google_api_key=api_key,
            temperature=temperature
        )
    except Exception as e:
        logger.error("llm connection failed %s", e)

    return llm
