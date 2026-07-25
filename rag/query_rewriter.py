"""
rag/query_rewriter.py

Rewrites user queries before retrieval using a local Ollama model.
"""

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from langchain_ollama import ChatOllama

from config import (
    OLLAMA_MODEL,
    OLLAMA_BASE_URL,
)


class QueryRewriter:

    def __init__(self):

        self.llm = ChatOllama(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_BASE_URL,
            temperature=0.0,
        )

    def rewrite(self, query: str) -> str:

        prompt = f"""
You are an expert search query optimizer.

Your task is to rewrite the user's query to improve semantic document retrieval.

Rules:
- Keep the original meaning.
- Expand abbreviations if necessary.
- Add technical keywords when appropriate.
- Do NOT answer the question.
- Return ONLY the rewritten query.
- Do not use bullet points.
- Do not explain your reasoning.

User Query:
{query}
"""

        response = self.llm.invoke(prompt)

        return response.content.strip()


if __name__ == "__main__":

    rewriter = QueryRewriter()

    while True:

        query = input("\nEnter Query (exit to quit): ")

        if query.lower() == "exit":
            break

        rewritten = rewriter.rewrite(query)

        print("\nOriginal Query:")
        print(query)

        print("\nRewritten Query:")
        print(rewritten)