import pypdf
import uuid
from logging import info as log
from langchain.text_splitter import RecursiveCharacterTextSplitter

from factories.vdb_factory import get_vdb_client

class Ingestion():
    def __init__(self, collection, chunk_size, chunk_overlap, api_key) -> None:
        self.collection = collection
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.api_key = api_key

        self.vector_db = get_vdb_client(self.api_key, self.collection)

    def trigger(self, file):
        text = self.extract_text(file)
        self.add_documents(text)

    def extract_text(self, file):
        pdf_reader = pypdf.PdfReader(file)
        log("Read uploaded file ..")
        text = ""
        for page in pdf_reader.pages:
           text = text + page.extract_text()
        return text
    
    def add_documents(self, docs: str) -> list:
        new_docs = self.chunk_documents(docs)
        for ix, doc in enumerate(new_docs):
            ids = str(uuid.uuid1())
            self.vector_db.add_documents(documents=[doc], ids=[ids])
            log("Processing write VDB %s/%s", ix, len(new_docs))
            log(
                "Added documents to Qdrant with IDs %s to collection %s", ids, self.collection)

    def chunk_documents(self, text: str):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )
        documents = text_splitter.create_documents([text])
        chunks = text_splitter.split_documents(documents)
        return chunks