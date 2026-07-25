"""
rag/retriever.py

Semantic Retriever using ChromaDB.
"""

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from config import TOP_K
from vectorstore.chroma import ChromaVectorStore


class SemanticRetriever:

    def __init__(self):

        self.vectorstore = ChromaVectorStore()

    def retrieve(
        self,
        query: str,
        k: int = TOP_K,
    ):
        """
        Retrieve top-k relevant documents.
        """

        documents = self.vectorstore.similarity_search(
            query=query,
            k=k,
        )

        return documents

    def retrieve_with_scores(
        self,
        query: str,
        k: int = TOP_K,
    ):
        """
        Retrieve top-k relevant documents with similarity scores.
        """

        documents = self.vectorstore.similarity_search_with_score(
            query=query,
            k=k,
        )

        return documents

    def print_results(
        self,
        query: str,
        k: int = TOP_K,
    ):

        results = self.retrieve_with_scores(query, k)

        print("\n")
        print("=" * 80)
        print("QUERY")
        print("=" * 80)
        print(query)

        print("\n")
        print("=" * 80)
        print(f"TOP {k} RESULTS")
        print("=" * 80)

        for index, (doc, score) in enumerate(results, start=1):

            print(f"\nResult #{index}")
            print("-" * 80)

            print(f"Similarity Score : {score}")

            print(
                f"Document         : {doc.metadata.get('source', 'Unknown')}"
            )

            print(
                f"Page             : {doc.metadata.get('page', 'Unknown')}"
            )

            preview = doc.page_content[:500].replace("\n", " ")

            print(f"\nContent:\n{preview}")

            print("\n")


if __name__ == "__main__":

    retriever = SemanticRetriever()

    while True:

        query = input("\nAsk a Question (type exit to quit): ")

        if query.lower() == "exit":
            break

        retriever.print_results(query)