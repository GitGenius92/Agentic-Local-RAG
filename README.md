# 📚 Local Agentic RAG System for Technical Documentation

> An offline, privacy-focused **Agentic Retrieval-Augmented Generation (RAG)** system that enables semantic search and question answering over technical documentation using **LangChain, Ollama, ChromaDB, Hugging Face Embeddings, and Streamlit**.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Agentic-green)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-orange)
![ChromaDB](https://img.shields.io/badge/Vector%20DB-ChromaDB-purple)
![License](https://img.shields.io/badge/License-MIT-blue)

---

# 🚀 Overview

Large Language Models often generate incorrect or hallucinated responses when answering questions outside their knowledge base.

This project solves that problem by implementing an **Agentic Retrieval-Augmented Generation (RAG)** pipeline that retrieves relevant information from local PDF documents before generating responses.

Unlike cloud-based solutions, the entire system runs **100% offline** using **Ollama**, making it suitable for privacy-sensitive environments.

---

# ✨ Features

* 📄 Multi-PDF document ingestion
* 🧠 Semantic Search using Hugging Face Embeddings
* 📚 ChromaDB Vector Database
* 🔍 Query Rewriting for improved retrieval
* ⭐ Cross-Encoder Document Re-ranking
* 🤖 Local LLM inference with Ollama (Llama 3 / Mistral)
* 💬 Interactive Chat Interface (Streamlit)
* 📖 Source-aware Answers
* 🔒 Fully Offline
* ⚡ Fast Local Inference
* 🧩 Modular Project Architecture
* 🚀 Easy to Extend

---

# 🏗️ System Architecture

```text
                    User Query
                        │
                        ▼
              Query Rewriting Agent
                        │
                        ▼
              Semantic Retrieval
                (ChromaDB)
                        │
                        ▼
           Cross Encoder Re-Ranker
                        │
                        ▼
         Context Construction Agent
                        │
                        ▼
             Ollama (Llama3/Mistral)
                        │
                        ▼
               Grounded AI Response
                        │
                        ▼
             Streamlit Chat Interface
```

---

# 🛠️ Tech Stack

| Category        | Technology                          |
| --------------- | ----------------------------------- |
| Language        | Python                              |
| Framework       | LangChain                           |
| Local LLM       | Ollama                              |
| Models          | Llama 3, Mistral                    |
| Embeddings      | Hugging Face BAAI/bge-small-en-v1.5 |
| Vector Database | ChromaDB                            |
| Re-ranking      | Sentence Transformers CrossEncoder  |
| PDF Processing  | PyMuPDF                             |
| Frontend        | Streamlit                           |

---

# 📂 Project Structure

```text
LOCAL_RAG/
│
├── app.py
├── config.py
├── requirements.txt
│
├── data/
├── database/
│
├── embeddings/
│   └── embedding.py
│
├── ingestion/
│   ├── loader.py
│   ├── splitter.py
│   └── ingest.py
│
├── vectorstore/
│   └── chroma.py
│
├── rag/
│   ├── retriever.py
│   ├── query_rewriter.py
│   ├── reranker.py
│   └── prompt.py
│
├── agents/
│   └── answer_agent.py
│
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/local-agentic-rag.git

cd local-agentic-rag
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 📥 Install Ollama

Download Ollama

https://ollama.com

Pull a model

```bash
ollama pull llama3
```

or

```bash
ollama pull mistral
```

Verify

```bash
ollama list
```

---

# 📚 Add Documents

Place your PDF files inside the **data/** directory.

Example

```text
data/

Python.pdf

LangChain.pdf

React.pdf

NextJS.pdf
```

---

# 📦 Build the Vector Database

```bash
python -m ingestion.ingest
```

The pipeline will

* Load PDFs
* Split Documents
* Generate Embeddings
* Store Vectors inside ChromaDB

---

# 🚀 Run the Application

```bash
streamlit run app.py
```

Open

```text
http://localhost:8501
```

---

# 💬 Example Questions

* What is Retrieval-Augmented Generation?
* Explain LangChain Agents.
* How does Python List Comprehension work?
* What is Prompt Engineering?
* Explain React Hooks.
* What are Vector Databases?
* How does ChromaDB work?

---

# 🔄 Pipeline Workflow

```text
PDF Documents
      │
      ▼
PyMuPDF Loader
      │
      ▼
Recursive Text Splitter
      │
      ▼
Hugging Face Embeddings
      │
      ▼
ChromaDB Vector Store
      │
      ▼
Query Rewriting
      │
      ▼
Semantic Search
      │
      ▼
Cross Encoder Re-Ranking
      │
      ▼
Context Generation
      │
      ▼
Ollama LLM
      │
      ▼
Grounded AI Answer
```

---

# 📈 Future Improvements

* LangGraph Agent Workflow
* Hybrid Search (BM25 + Vector Search)
* Conversation Memory
* Streaming Responses
* Docker Deployment
* Authentication
* Chat Export
* Multi-user Support
* RAG Evaluation (RAGAS)
* Source Highlighting
* Citation Validation
* Model Switching
* REST API

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Retrieval-Augmented Generation (RAG)
* Agentic AI Workflows
* Local LLM Deployment
* Semantic Search
* Vector Databases
* Embedding Models
* Document Processing
* Prompt Engineering
* Cross-Encoder Re-ranking
* Offline AI Systems

---

# 📸 Screenshots

> Add screenshots of:

* Home Page
* PDF Upload
* Chat Interface
* Retrieved Sources
* Final AI Response

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Muhammad Faizan Imran**

Computer Engineer | Full Stack Developer | AI & GenAI Enthusiast

* GitHub: https://github.com/yourusername
* LinkedIn: https://linkedin.com/in/yourusername

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
