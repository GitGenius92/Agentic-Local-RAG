"""
config.py

Central configuration file for the Local Agentic RAG System.
Modify values here instead of changing them throughout the project.
"""

from pathlib import Path

# ============================================================
# Project Paths
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
DB_DIR = BASE_DIR / "database"

DATA_DIR.mkdir(exist_ok=True)
DB_DIR.mkdir(exist_ok=True)

# ============================================================
# Embedding Model
# ============================================================

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

# ============================================================
# Ollama
# ============================================================

OLLAMA_MODEL = "llama3"

# Alternative:
# OLLAMA_MODEL = "mistral"

OLLAMA_BASE_URL = "http://localhost:11434"

# ============================================================
# Text Splitter
# ============================================================

CHUNK_SIZE = 800
CHUNK_OVERLAP = 150

# ============================================================
# Retrieval
# ============================================================

TOP_K = 5

# ============================================================
# Chroma
# ============================================================

COLLECTION_NAME = "technical_documents"

# ============================================================
# Generation
# ============================================================

TEMPERATURE = 0.2

MAX_TOKENS = 2048

# ============================================================
# Streamlit
# ============================================================

PAGE_TITLE = "Local Agentic RAG"

PAGE_ICON = "📚"

# ============================================================
# Supported Documents
# ============================================================

SUPPORTED_EXTENSIONS = [
    ".pdf"
]