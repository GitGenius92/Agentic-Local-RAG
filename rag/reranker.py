"""
rag/reranker.py

Cross Encoder based document reranker.
"""

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from sentence_transformers import CrossEncoder


class DocumentReranker:

    def __init__(
        self,
        model_name="cross-encoder/ms-marco-MiniLM-L-6-v2",
    ):

        self.model = CrossEncoder(model_name)

    def rerank(
        self,
        query,
        documents,
        top_k=5,
    ):
        """
        Re-rank retrieved documents using CrossEncoder.
        """

        if len(documents) == 0:
            return []

        pairs = [
            (query, doc.page_content)
            for doc in documents
        ]

        scores = self.model.predict(pairs)

        ranked = sorted(
            zip(documents, scores),
            key=lambda x: x[1],
            reverse=True,
        )

        return ranked[:top_k]

    def print_results(
        self,
        query,
        documents,
        top_k=5,
    ):

        ranked_docs = self.rerank(
            query,
            documents,
            top_k,
        )

        print("\n")
        print("=" * 80)
        print("RERANKED DOCUMENTS")
        print("=" * 80)

        for i, (doc, score) in enumerate(ranked_docs, 1):

            print(f"\nRank #{i}")

            print("-" * 80)

            print(f"Score : {score:.4f}")

            print(
                f"Source : {doc.metadata.get('source')}"
            )

            print(
                f"Page : {doc.metadata.get('page')}"
            )

            print("\n")

            print(doc.page_content[:500])

            print("\n")


if __name__ == "__main__":

    from rag.retriever import SemanticRetriever

    retriever = SemanticRetriever()

    reranker = DocumentReranker()

    while True:

        query = input("\nAsk Question (exit to quit): ")

        if query.lower() == "exit":
            break

        docs = retriever.retrieve(query, k=10)

        reranker.print_results(
            query,
            docs,
            top_k=5,
        )