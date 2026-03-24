import streamlit as st
from rag_pipeline import get_rag_response
from ingest import ingest_documents
import os

st.set_page_config(page_title="💰 AI Finance Advisor", page_icon="💰", layout="wide")

st.title("💰 RAG-Based Personal Finance Advisor")
st.caption("Powered by LLaMA3 + FAISS + LangChain")

with st.sidebar:
    st.header("⚙️ Settings")
    topic = st.selectbox("📂 Filter Topic", [
        "All Topics", "Mutual Funds", "Stock Market",
        "Tax Planning", "Insurance", "Fixed Deposits",
        "Cryptocurrency", "Emergency Fund"
    ])
    st.markdown("---")
    if st.button("🔄 Load Knowledge Base", use_container_width=True):
        with st.spinner("Loading documents..."):
            ingest_documents()
        st.success("✅ Knowledge base loaded!")
    st.markdown("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.markdown("---")
    st.markdown("⚠️ AI-generated advice only. Consult a SEBI-registered advisor.")

if not os.path.exists("vectorstore"):
    st.warning("⚠️ Knowledge base not loaded! Click Load Knowledge Base in sidebar first!")
else:
    st.success("✅ Knowledge base ready!")

st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("Ask your financial question...")

if question:
    if topic != "All Topics":
        enhanced = f"[Topic: {topic}] {question}"
    else:
        enhanced = question

    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("🔍 Searching knowledge base..."):
            response, sources = get_rag_response(enhanced, st.session_state.messages)
        st.write(response)
        if sources:
            with st.expander("📄 Sources Used"):
                for source in set(sources):
                    st.write(f"• {source}")
        st.caption("⚠️ AI-generated advice. Consult a SEBI-registered advisor.")

    st.session_state.messages.append({"role": "assistant", "content": response})
