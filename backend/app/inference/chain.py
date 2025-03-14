from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from logging import info as log

from factories.vdb_factory import get_vdb_client
from factories.llm_factory import get_llm_client


class Chain:
    def __init__(self, query: str, system: str, k: int, api_key: str, collection: str, temperature: float) -> None:
        self.query = query
        self.vector_storage = get_vdb_client(api_key, collection)
        self.llm = get_llm_client(api_key, temperature)
        self.k = k
        self.system = system

    def _get_qa_prompt(self):
        system_prompt = self.system
        system_prompt += "\n\ncontext: {context}"
        log(f"System Prompt: {system_prompt}")

        qa_prompt = ChatPromptTemplate.from_messages(
           [
               ("system", system_prompt),
               ("human", "{input}"),
           ]
        )
        return qa_prompt
    
    def _get_retriever(self):
        retriever = self.vector_storage.as_retriever(
            search_type="similarity", 
            search_kwargs={"k": self.k}
        )
        return retriever
    
    def invoke_chain(self):
        qa_prompt = self._get_qa_prompt()
        retriever = self._get_retriever()
        document_prompt = PromptTemplate(input_variables=["page_content"], template="{page_content}")
        question_answer_chain = create_stuff_documents_chain(self.llm, qa_prompt, document_prompt = document_prompt)
        rag_chain = create_retrieval_chain(retriever, question_answer_chain)
        result = rag_chain.invoke({"input": f"{self.query}"})
        return result['answer']
