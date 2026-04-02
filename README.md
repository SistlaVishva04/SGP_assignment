# 📄 Document Intelligence Pipeline (RAG-Based)

## 🚀 Overview

This project implements a **Document Intelligence Pipeline** using **Retrieval-Augmented Generation (RAG)** to simulate real-world **eDiscovery use cases**.

The system ingests documents (PDFs, emails, text), processes them, and enables **natural language querying with metadata-aware retrieval**.

---

## 🧠 Key Features

- 📥 Document ingestion (PDF, TXT, Emails)
- ✂️ Custom chunking strategy
- 🔍 Semantic search using embeddings (FAISS)
- 🧾 Metadata-aware filtering (date, type, author)
- 🤖 RAG-based response generation (Gemini)
- ⚠️ Fallback handling for API failures
- 🧹 Noise handling for messy real-world data

---

## 🏗️ Project Structure

```

venio-rag/
│
├── data/
│ ├── documents/ # All input documents (PDF, TXT, emails)
│ └── metadata.csv # Metadata for documents
│
├── app/
│ ├── loader.py # Document loading + metadata attachment
│ ├── chunker.py # Chunking logic
│ ├── vectorstore.py # Embeddings + FAISS
│ ├── rag_pipeline.py # Query + retrieval + generation
│ └── utils.py # Text cleaning utilities
│
├── main.py # CLI entry point
├── api.py # Optional FastAPI endpoint
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

2️⃣ Install dependencies
```
pip install -r requirements.txt
```

▶️ Run the Application
```
python main.py
```

Example queries:

Find financial discussions from 2021
Show emails from 2020
Show reports from 2022
## 🧠 System Architecture ##

```
Documents → Cleaning → Chunking → Embeddings → FAISS
↓
User Query → Retrieval → Metadata Filtering → LLM → Answer
```
---

## 🔍 Design Decisions ##

### 1. Chunking Strategy ###

Used **RecursiveCharacterTextSplitter**
Chunk size: 500, overlap: 100

Why?

Preserves semantic context
Handles noisy documents better
Avoids breaking important information
### 2. Handling Noisy / Messy Documents ###

**Dataset contained**:

Random symbols ($$$, ###)

Irregular spacing

Mixed content (HR + financial)

**Solution**:

- Regex-based cleaning
- Removed noise tokens
- Normalized whitespace
-Extracted relevant email body content

### 3. Improving Retrieval Quality ###

Several improvements were applied:

- Increased retrieval size (k=20)
- Metadata-aware filtering:
- Date (year)
- Document type (email, report, contract)
- Document-level deduplication (using document_id)
- Limiting final results to reduce noise
- Query expansion (e.g., financial → revenue, finance)

### 4. What Breaks at Scale (1M Documents)? ###

At large scale:

❌ FAISS in-memory becomes inefficient

❌ High latency in retrieval

❌ Metadata filtering becomes costly

❌ Embedding computation overhead

**Solutions**:

Use vector DBs like Pinecone / Weaviate
Use hybrid search (BM25 + embeddings)
Pre-index metadata filters
Distributed retrieval pipelines

### 5. Hallucination Risks & Fixes ###

Where hallucination occurs:
When retrieved context is weak or empty
When LLM tries to infer missing info
Mitigation:
Strict prompting: "Use only provided context"
Fallback response if LLM fails
Metadata filtering to improve context relevance

---

## ⚠️ Important Observation ##

The dataset contains inconsistencies between:

- Metadata dates
- Dates inside document content

**Decision**:

Metadata is treated as the source of truth.

**Reason**:

- Structured and reliable
- Content may be noisy or inconsistent

---

## 🛠️ Tech Stack ##

- Python
- LangChain
- FAISS (Vector DB)
- Sentence Transformers (Embeddings)
- Gemini (LLM)
- Pandas

---

### 🔥 Example Query ### 

Input:
```
Find financial discussions from 2021
```

Output:

```
Retrieves relevant documents
Filters by metadata (year = 2021)
Generates summary (or fallback if API fails)
```

---

## ⚠️ Known Limitations
- Gemini API quota may limit responses
- Some retrieval noise due to small dataset
- No UI (CLI-based interaction)

---

## 🚀 Future Improvements
- Add reranking (Cross-Encoder)
- Hybrid search (keyword + semantic)
- UI dashboard
- Better document classification
- Caching embeddings

---

## 📌 Conclusion

This project demonstrates a real-world RAG pipeline with:
- Robust document processing
- Metadata-aware retrieval
- Handling of messy data
- Practical system design considerations

---

## 👤 Author
```
S V Vishnu Vamsi
vishvasistla04@gmail.com
```
