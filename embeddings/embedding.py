"""
embeddings/embedding.py

Loads the HuggingFace embedding model.
Uses Singleton Pattern so the model loads only once.
"""

from langchain_huggingface import HuggingFaceEmbeddings
from config import EMBEDDING_MODEL


class EmbeddingModel:
    """
    Singleton wrapper for HuggingFace Embeddings.
    """

    _instance = None

    @classmethod
    def get_model(cls):
        if cls._instance is None:

            cls._instance = HuggingFaceEmbeddings(
                model_name=EMBEDDING_MODEL,
                model_kwargs={
                    "device": "cpu"
                },
                encode_kwargs={
                    "normalize_embeddings": True
                }
            )

        return cls._instance