import streamlit as st
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain
from langchain_openai import ChatOpenAI
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Конституция РК")
st.title("📜 AI Assistant по Конституции РК")

uploaded_files = st.file_uploader("Загрузите PDF-документы", accept_multiple_files=True)

if uploaded_files:
    all_text = ""
    for file in uploaded_files:
        reader = PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                all_text += page_text

    # Уменьшенные чанки
    text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    texts = text_splitter.split_text(all_text)

    embeddings = OpenAIEmbeddings(openai_api_key=openai_key)
    db = Chroma.from_texts(texts, embedding=embeddings, persist_directory="db")
    retriever = db.as_retriever(search_kwargs={"k": 3})

    llm = ChatOpenAI(openai_api_key=openai_key, model="gpt-4-1106-preview")


    qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="map_reduce",  # ← тут ключевое изменение
    retriever=retriever,
    return_source_documents=False
)
    query = st.text_input("Задай вопрос:")
    if query:
        try:
            result = qa_chain.run(query)
            st.write("Ответ:", result)
        except Exception as e:
            st.error(f"Ошибка: {str(e)}")
