
# Insurance Doc Analyser 🧠

A web application designed to **upload**, **process**, and **analyze** insurance-related documents (PDF, DOCX, TXT, CSV, JSON, etc.) using a Retrieval‑Augmented‑Generation (RAG) pipeline built with LLMs, document processors, and vector databases.

---

## 🚀 Features

- Upload multiple file types: PDF, DOCX, TXT, RTF, CSV, JSON.
- Extract and chunk document content intelligently.
- Generate embeddings and store in ChromaDB.
- Perform semantic search and Q&A via LLM (Ollama-based).
- Context-aware: handle multiple documents in one session.
- Choose analysis “roles” (e.g. Legal, Financial, Technical).
- Built with FastAPI (backend) and Gradio (frontend) for seamless UX.

---

## ⚙️ Prerequisites

To run the project locally:

1. **Create Uploads Folder**
   ```bash
   mkdir uploads
   ```

2. **Set Up Python Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```
4. **Replace your API_KEY**
   Generate API_KEY in the url 
   ```bash
   https://aistudio.google.com/apikey 
   ```
   and replace your GEMENI_API_KEY in /utils/document_processor.py
   
---


```bash
python server.py
```

- This starts the main application using the `server.py` file.
- Make sure your virtual environment is activated and all requirements are installed.

---
