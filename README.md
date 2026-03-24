# 💰 RAG-Based Personal Finance Advisor Chatbot

An intelligent financial advisor chatbot built using RAG (Retrieval-Augmented Generation) architecture, specifically designed for Indian users.

## Features
- Conversational AI chatbot for personal finance
- RAG pipeline with FAISS vector search
- India-specific financial advice (SEBI, RBI, NSE, BSE)
- Source citation for every response
- Topic filtering (Mutual Funds, Tax, Stocks, etc.)
- Powered by LLaMA 3.3 70B via Groq API
- Completely free to run

## Tech Stack
- Frontend: Streamlit
- LLM: LLaMA 3.3 70B via Groq
- RAG Framework: LangChain
- Vector Store: FAISS (Meta AI)
- Embeddings: HuggingFace all-MiniLM-L6-v2
- Language: Python 3.9

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/MansiNegi281/rag-finance-chatbot.git
cd rag-finance-chatbot

### 2. Install dependencies
pip install -r requirements.txt

### 3. Get FREE Groq API key
- Go to https://console.groq.com
- Sign up and create API key
- Create .env file and add: GROQ_API_KEY=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

### 4. Ingest knowledge base
python3 ingest.py

### 5. Run the app
python3 -m streamlit run app.py

### 6. Open browser
http://localhost:8501

## Topics Covered
- Mutual Funds (SIP, ELSS, Index Funds)
- Stock Market (NSE, BSE, Nifty50)
- Tax Planning (80C, 80D, NPS, HRA)
- Insurance (Term, Health, ULIP)
- Fixed Deposits
- Emergency Fund
- Cryptocurrency
- Budgeting (50-30-20 rule)
- Retirement Planning (EPF, PPF, NPS)
- Debt Management (CIBIL, EMI)

## Disclaimer
This chatbot provides AI-generated financial advice for educational purposes only.
Always consult a SEBI-registered financial advisor before investing.

## Author
Mansi Negi
