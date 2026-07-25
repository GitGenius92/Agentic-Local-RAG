"""
agents/answer_agent.py

Generates the final grounded answer using Ollama.
"""

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from langchain_ollama import ChatOllama

from config import (
    OLLAMA_MODEL,
    OLLAMA_BASE_URL,
    TEMPERATURE,
)

from rag.prompt import (
    SYSTEM_PROMPT,
    ANSWER_TEMPLATE,
)


class AnswerAgent:

    def __init__(self):

        self.llm = ChatOllama(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_BASE_URL,
            temperature=TEMPERATURE,
        )

    def build_context(self, ranked_documents):

        context = []

        for document, score in ranked_documents:

            source = document.metadata.get("source", "Unknown")

            page = document.metadata.get("page", "Unknown")

            text = document.page_content

            context.append(

                f"""
Document : {source}

Page : {page}

{text}
"""
            )

        return "\n\n".join(context)

    def generate_answer(
        self,
        question,
        ranked_documents,
    ):

        context = self.build_context(
            ranked_documents
        )

        prompt = ANSWER_TEMPLATE.format(
            context=context,
            question=question,
        )

        messages = [

            (
                "system",
                SYSTEM_PROMPT,
            ),

            (
                "human",
                prompt,
            ),

        ]

        response = self.llm.invoke(messages)

        return response.content


if __name__ == "__main__":

    from rag.retriever import SemanticRetriever
    from rag.reranker import DocumentReranker

    retriever = SemanticRetriever()

    reranker = DocumentReranker()

    agent = AnswerAgent()

    while True:

        question = input("\nQuestion : ")

        if question.lower() == "exit":
            break

        docs = retriever.retrieve(
            question,
            k=10,
        )

        ranked_docs = reranker.rerank(
            question,
            docs,
            top_k=5,
        )

        answer = agent.generate_answer(
            question,
            ranked_docs,
        )

        print("\n")
        print("=" * 80)
        print("FINAL ANSWER")
        print("=" * 80)

        print(answer)

        print("\n")