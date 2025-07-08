from typing import TypedDict

class ResearchState(TypedDict, total=False):
    query: str
    language: str
    search_results: str
    summary: str
    final_answer: str