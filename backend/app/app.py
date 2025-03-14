import streamlit as st
import time
from ingestion.ingestion import Ingestion
from inference.chain import Chain

def ingestion():
    try:
        new = Ingestion(st.session_state.collection, st.session_state.chunk_size, st.session_state.chunk_overlap, st.session_state.api_key)
        time.sleep(2)
        new.trigger(file)
        st.write(file.name)
    except Exception as e:
        st.write(e)

def inference():
    try:
        new = Chain(st.session_state.chat, st.session_state.system, st.session_state.k, st.session_state.api_key, st.session_state.collection, st.session_state.temperature)
        time.sleep(1)
        result = new.invoke_chain()
        st.write(result)
    except Exception as e:
        st.write(e)

st.text_input("System Prompt", value="You are a helpful QA system.", key="system")
st.text_input("Your question", key="chat", on_change=inference)

st.sidebar.text_input("Google API Key", type="password", key="api_key")
st.sidebar.header("LLM settings")
st.sidebar.subheader("Google Gemini 2.0 flash")
st.sidebar.number_input('Temperature', min_value=0.0, max_value=1.0, value=0.3, key="temperature")
st.sidebar.number_input('K', min_value=1, max_value=20, value=3, key="k")

st.sidebar.header("VDB settings")
st.sidebar.subheader("Embedding: Google Gemini text-embedding-004")
st.sidebar.subheader("Qdrant VDB size 768")
st.sidebar.text_input("VDB collection", key="collection")
st.sidebar.number_input('Chunk size', min_value=0, max_value=5000, value=1000, key="chunk_size")
st.sidebar.number_input('Chunk overlap', min_value=0, max_value=1000, value=100, key="chunk_overlap")
file = st.sidebar.file_uploader("Upload PDF file", on_change=ingestion, key="file")
