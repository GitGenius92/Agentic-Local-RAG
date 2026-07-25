"""
vectorstore/chroma.py

Persistent ChromaDB vector store manager.
"""

from langchain_chroma import Chroma

from config import (
    DB_DIR,
    COLLECTION_NAME,
)

from embeddings.embedding import EmbeddingModel


class ChromaVectorStore:

    def __init__(self):
        self.embedding_model = EmbeddingModel.get_model()

        self.vectorstore = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=self.embedding_model,
            persist_directory=str(DB_DIR),
        )

    def add_documents(self, documents):
        """
        Add documents to ChromaDB.
        """
        self.vectorstore.add_documents(documents)

    def similarity_search(self, query, k=5):
        """
        Basic similarity search.
        """
        return self.vectorstore.similarity_search(
            query=query,
            k=k,
        )

    def similarity_search_with_score(self, query, k=5):
        """
        Similarity search with scores.
        """
        return self.vectorstore.similarity_search_with_score(
            query=query,
            k=k,
        )

    def as_retriever(self, k=5):
        """
        Return LangChain retriever.
        """
        return self.vectorstore.as_retriever(
            search_kwargs={
                "k": k
            }
        )

    def delete_collection(self):
        """
        Delete entire collection.
        """
        self.vectorstore.delete_collection()

    def get_collection(self):
        return self.vectorstore