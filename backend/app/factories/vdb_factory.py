import logging

from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from langchain_qdrant import QdrantVectorStore

from .embd_factory import get_embedding_function

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_vdb_client( api_key, collection):
    embedding_function = get_embedding_function(api_key)
    try: 
        host, port = "qdrant_vdb", 6333
        client = QdrantClient(host=host, port=port, timeout=30)

        if not client.collection_exists(collection):
            client.create_collection(
                collection_name=collection,
                vectors_config=VectorParams(size=768, distance=Distance.COSINE))
            
        vector_db = QdrantVectorStore(
            client=client,
            collection_name=collection,
            embedding=embedding_function,
            )

    except Exception as e:
        logger.error("vdb connection failed %s", e)

    return vector_db
