from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents):
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = []

    for doc in documents:
        splits = splitter.split_text(doc["text"])

        for s in splits:
            chunks.append({
                "text": s,
                "metadata": doc["metadata"]
            })

    return chunks