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
│   │   ├── main.py            # FastAPI entrypoint
│   │   ├── routes/
│   │   ├── services/
│   │   └── models/
│   ├── vector_store/          # FAISS index and embedding logic
│   └── tests/
├── sample_docs/               # Mock files (markdown, pdf, txt)
├── .env.example
├── requirements.txt
└── README.md
```

---

## ⚠️ Disclaimer

This repository does **not** contain any internal documentation from BU Spark! or real retrospectives. All sample documents in `sample_docs/` are anonymized or fictitious for demo purposes only.

---

## 📄 License

MIT License. Free to use and modify for non-commercial and educational purposes.
