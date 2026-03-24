from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_rag_response(user_question, chat_history=[]):
    try:
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        vectordb = FAISS.load_local(
            "vectorstore",
            embeddings,
            allow_dangerous_deserialization=True
        )
        relevant_docs = vectordb.similarity_search(user_question, k=3)
        context = "\n\n".join([doc.page_content for doc in relevant_docs])
        sources = [doc.metadata.get("source", "Knowledge Base") for doc in relevant_docs]

        prompt = f"""You are an expert Indian Personal Financial Advisor.
Use the context below to answer the question clearly and practically.
If unsure, say "I don't have enough information on this topic."
Always give advice relevant to Indian users (INR, SEBI, RBI, NSE, BSE).

Context:
{context}

Give a clear, structured, practical answer."""

        formatted_history = []
        for msg in chat_history[-6:]:
            formatted_history.append({"role": msg["role"], "content": msg["content"]})

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": prompt},
                *formatted_history,
                {"role": "user", "content": user_question}
            ],
            max_tokens=1024,
            temperature=0.7
        )
        return response.choices[0].message.content, sources
    except Exception as e:
        return f"❌ Error: {str(e)}", []
