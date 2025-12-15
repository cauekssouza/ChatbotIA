import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection(name="chat_context")


def add_to_vector_store(text: str, metadata: dict):
    collection.add(
        documents=[text],
        metadatas=[metadata],
        ids=[str(len(collection.get()["ids"]) + 1)]
    )


def query_vector_store(query: str) -> str:
    results = collection.query(query_texts=[query], n_results=3)

    if results["documents"]:
        return " ".join(results["documents"][0])

    return ""
