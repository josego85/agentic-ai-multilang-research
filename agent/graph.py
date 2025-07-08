from agent.state import ResearchState
from langgraph.graph.state import StateGraph
from service.search import SearchService
from service.summarize import Summarizer
from service.llm_agent import LLMAgent
from service.language import detect_language
from service.prompts.respond_templates import RESPOND_TEMPLATES

search_service = SearchService()
summarizer = Summarizer()
llm_agent = LLMAgent()

def detect_language_node(state: ResearchState) -> ResearchState:
    lang = detect_language(state["query"])
    new_state = dict(state)
    new_state["language"] = lang
    return new_state

def search_node(state: ResearchState) -> ResearchState:
    results = search_service.web_search(state["query"], lang=state["language"])
    new_state = dict(state)
    new_state["search_results"] = results
    return new_state

def summarize_node(state: ResearchState) -> ResearchState:
    summary = summarizer.summarize(
        question=state["query"],
        web_content=state["search_results"],
        lang=state.get("language", "en")
    )
    new_state = dict(state)
    new_state["summary"] = summary
    return new_state

def respond_node(state: ResearchState) -> ResearchState:
    lang = state.get("language", "en")
    template = RESPOND_TEMPLATES.get(lang, RESPOND_TEMPLATES["en"])
    
    final_prompt = template.format(
        summary=state["summary"],
        question=state["query"]
    )
    
    answer = llm_agent.run_prompt(final_prompt)
    
    new_state = dict(state)
    new_state["final_answer"] = answer
    return new_state


workflow = StateGraph(state_schema=ResearchState)

workflow.add_node("detect_language", detect_language_node)
workflow.add_node("search", search_node)
workflow.add_node("summarize", summarize_node)
workflow.add_node("respond", respond_node)

workflow.set_entry_point("detect_language")
workflow.add_edge("detect_language", "search")
workflow.add_edge("search", "summarize")
workflow.add_edge("summarize", "respond")

graph = workflow.compile()
