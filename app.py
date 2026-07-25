import streamlit as st

from ingestion.ingest import DocumentIngestor

from rag.query_rewriter import QueryRewriter
from rag.retriever import SemanticRetriever
from rag.reranker import DocumentReranker
from agents.answer_agent import AnswerAgent

from config import (
    PAGE_TITLE,
    PAGE_ICON,
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
)

# --------------------------------------------------
# SESSION
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# COMPONENTS
# --------------------------------------------------

retriever = SemanticRetriever()

reranker = DocumentReranker()

rewriter = QueryRewriter()

agent = AnswerAgent()

ingestor = DocumentIngestor()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("📚 Local Agentic RAG")

    uploaded_files = st.file_uploader(
        "Upload PDFs",
        type=["pdf"],
        accept_multiple_files=True,
    )

    if uploaded_files:

        import os

        os.makedirs("data", exist_ok=True)

        for file in uploaded_files:

            with open(
                f"data/{file.name}",
                "wb",
            ) as f:

                f.write(file.read())

        if st.button("Index Documents"):

            with st.spinner(
                "Creating embeddings..."
            ):

                ingestor.ingest()

            st.success(
                "Documents Indexed Successfully!"
            )

    st.divider()

    use_rewrite = st.checkbox(
        "Enable Query Rewriting",
        value=True,
    )

    top_k = st.slider(
        "Retrieved Documents",
        1,
        10,
        5,
    )

    rerank_k = st.slider(
        "Final Documents",
        1,
        10,
        3,
    )

    st.divider()

    if st.button("Reset Database"):

        ingestor.reset_database()

        st.success("Database Cleared.")

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🤖 Local Agentic RAG")

st.caption(
    "Offline Technical Documentation Assistant"
)

# --------------------------------------------------
# CHAT HISTORY
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------

query = st.chat_input(
    "Ask anything about your documents..."
)

if query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query,
        }
    )

    with st.chat_message("user"):

        st.markdown(query)

    with st.chat_message("assistant"):

        status = st.empty()

        status.info("Thinking...")

        search_query = query

        if use_rewrite:

            search_query = rewriter.rewrite(query)

        docs = retriever.retrieve(
            search_query,
            top_k,
        )

        ranked = reranker.rerank(
            search_query,
            docs,
            rerank_k,
        )

        answer = agent.generate_answer(
            query,
            ranked,
        )

        status.empty()

        st.markdown(answer)

        with st.expander(
            "Retrieved Sources"
        ):

            for i, (doc, score) in enumerate(ranked):

                st.markdown(
                    f"### Result {i+1}"
                )

                st.write(
                    f"Score : {score:.4f}"
                )

                st.write(
                    f"Source : {doc.metadata.get('source')}"
                )

                st.write(
                    f"Page : {doc.metadata.get('page')}"
                )

                st.write(
                    doc.page_content[:700]
                )

                st.divider()

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )