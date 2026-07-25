"""
ingestion/loader.py

Loads PDF documents from the data directory.
"""

from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader

from config import DATA_DIR


class DocumentLoader:

    def __init__(self):
        self.data_dir = Path(DATA_DIR)

    def load_pdf(self, pdf_path):
        """
        Load a single PDF.
        """
        loader = PyMuPDFLoader(str(pdf_path))
        return loader.load()

    def load_all_pdfs(self):
        """
        Load all PDFs from the data directory.
        """
        documents = []

        pdf_files = list(self.data_dir.glob("*.pdf"))

        for pdf in pdf_files:
            docs = self.load_pdf(pdf)

            for doc in docs:
                doc.metadata["source"] = pdf.name

            documents.extend(docs)

        return documents

    def get_pdf_files(self):
        """
        Return all PDF files.
        """
        return list(self.data_dir.glob("*.pdf"))


if __name__ == "__main__":

    loader = DocumentLoader()

    documents = loader.load_all_pdfs()

    print(f"Loaded {len(documents)} pages.\n")

    if documents:
        print(documents[0].page_content[:500])
        print(documents[0].metadata)