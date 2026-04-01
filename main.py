from app.loader import load_documents
from app.chunker import chunk_documents
from app.vectorstore import create_vectorstore
from app.rag_pipeline import query_rag

def main():
    print("Loading documents...")
    docs = load_documents()

    print("Chunking...")
    chunks = chunk_documents(docs)

    print("Creating vector DB...")
    vs = create_vectorstore(chunks)

    while True:
        q = input("\nEnter query: ")
        if q == "exit":
            break

        answer = query_rag(vs, q)
        print("\nAnswer:", answer)


if __name__ == "__main__":
    main()