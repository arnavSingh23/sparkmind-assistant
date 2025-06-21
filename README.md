# SparkMind Assistant

> A lightweight, open-source AI knowledge assistant for organizations. Built with FastAPI, FAISS, and LangChain, it enables non-technical users to query internal documentation using semantic search and LLM-generated answers.

---

## 🔍 Features

- **Semantic Search** over documents using FAISS and MiniLM
- **LLM-powered Responses** with LangChain and OpenAI (or any model)
- **Citation-aware Answers** that reference source snippets
- **FastAPI Backend** to expose `/query` endpoints
- **Web Interface** (Optional) for lightweight access by PMs and staff

---

## 🏗️ Architecture Overview

```text
User Query
    ↓
[Frontend UI]
    ↓ (POST /query)
[FastAPI Backend] ─→ [FAISS Vector Store]
         ↓                      ↑
     [LangChain]         [Embedded Docs]
         ↓
     LLM Answer + Sources
```

---

## 🚀 Getting Started

```bash
# Clone repo
$ git clone https://github.com/your-username/sparkmind-assistant.git
$ cd sparkmind-assistant

# Install dependencies
$ python3 -m venv venv && source venv/bin/activate
$ pip install -r requirements.txt

# Run the app
$ uvicorn app.main:app --reload
```

---

## 📁 Folder Structure

```
sparkmind-assistant/
├── backend/
│   ├── app/
│   │   ├── main.py            # Entrypoint for FastAPI
│   │   ├── routes/            # Future route handlers
│   │   ├── services/          # Business logic (e.g., querying FAISS)
│   │   └── models/            # Pydantic schemas and internal models
│   ├── vector_store/          # FAISS indexing logic
│   └── tests/                 # Future unit/integration tests
├── frontend/                  # Optional interface for PMs/staff
│   └── (placeholder.md)       # Add real code later
├── sample_docs/               # Fictitious markdown/pdfs for testing
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚠️ Disclaimer

This repository does **not** contain any internal documentation from BU Spark! or real retrospectives. All sample documents in `sample_docs/` are anonymized or fictitious for demo purposes only.

---

## 📄 License

MIT License. Free to use and modify for non-commercial and educational purposes.
