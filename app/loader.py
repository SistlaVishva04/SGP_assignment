import pandas as pd
import os
from app.utils import clean_text, extract_email_body
from langchain_community.document_loaders import PyPDFLoader

def load_documents(data_path="data"):
    df = pd.read_csv(os.path.join(data_path, "metadata.csv"))

    df["date"] = pd.to_datetime(df["date"], dayfirst=True)

    documents = []

    for _, row in df.iterrows():
        file_path = os.path.join(data_path, "documents", row["file_name"])

        
        if row["document_type"] == "irrelevant":
            continue

        
        if file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
                text = extract_email_body(text)

        elif file_path.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
            pages = loader.load()
            text = " ".join([p.page_content for p in pages])

        
        text = clean_text(text)

        documents.append({
    "text": text,
    "metadata": {
        "document_id": row["document_id"],
        "file_name": row["file_name"],  
        "date": row["date"],
        "author": row["author"],
        "document_type": row["document_type"]  
    }
})

    return documents