from embeddings.embedding import EmbeddingModel


def main():

    print("=" * 50)
    print("Loading Embedding Model...")
    print("=" * 50)

    embedding = EmbeddingModel.get_model()

    print("✅ Model Loaded Successfully\n")

    query = "Explain Retrieval Augmented Generation"

    vector = embedding.embed_query(query)

    print(f"Query: {query}\n")

    print(f"Embedding Length: {len(vector)}\n")

    print("First 10 Values:")

    print(vector[:10])


if __name__ == "__main__":
    main()