"""
ingestion/splitter.py

Splits loaded documents into smaller chunks for embedding.
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter

from config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


class DocumentSplitter:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split_documents(self, documents):
        """
        Split LangChain documents into chunks.
        """
        chunks = self.splitter.split_documents(documents)

        return chunks

    def split_text(self, text):
        """
        Split raw text into chunks.
        """
        return self.splitter.split_text(text)


if __name__ == "__main__":

    from ingestion.loader import DocumentLoader

    loader = DocumentLoader()

    documents = loader.load_all_pdfs()

    splitter = DocumentSplitter()

    chunks = splitter.split_documents(documents)

    print(f"\nTotal Chunks: {len(chunks)}\n")

    print(chunks[0].page_content)

    print("\nMetadata:\n")

    print(chunks[0].metadata)