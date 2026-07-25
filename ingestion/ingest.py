"""
ingestion/ingest.py

Loads PDFs, splits them into chunks, generates embeddings,
and stores everything in ChromaDB.
"""

import sys
from pathlib import Path

# Allow imports from project root
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ingestion.loader import DocumentLoader
from ingestion.splitter import DocumentSplitter
from vectorstore.chroma import ChromaVectorStore


class DocumentIngestor:

    def __init__(self):
        self.loader = DocumentLoader()
        self.splitter = DocumentSplitter()
        self.vectorstore = ChromaVectorStore()

    def ingest(self):

        print("=" * 60)
        print("Loading PDF documents...")
        print("=" * 60)

        documents = self.loader.load_all_pdfs()

        if len(documents) == 0:
            print("\nNo PDF files found inside /data folder.\n")
            return

        print(f"Loaded {len(documents)} pages.")

        print("\nSplitting documents...\n")

        chunks = self.splitter.split_documents(documents)

        print(f"Generated {len(chunks)} chunks.")

        print("\nCreating embeddings and storing in ChromaDB...\n")

        self.vectorstore.add_documents(chunks)

        print("=" * 60)
        print("Ingestion Completed Successfully!")
        print("=" * 60)

        print(f"Pages Loaded  : {len(documents)}")
        print(f"Chunks Stored : {len(chunks)}")

    def reset_database(self):

        print("Deleting existing Chroma collection...")

        self.vectorstore.delete_collection()

        print("Database deleted successfully.")

    def re_ingest(self):

        self.reset_database()

        self.ingest()


if __name__ == "__main__":

    ingestor = DocumentIngestor()

    ingestor.ingest()