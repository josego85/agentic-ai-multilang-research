import os
os.environ["OLLAMA_NUM_THREADS"] = "10"

import time
from langchain_ollama import ChatOllama 

class LLMAgent:
    def __init__(self, model_name: str = "gemma3:1b"):
        self.llm = ChatOllama(model=model_name, temperature=0)

    def run_prompt(self, prompt: str) -> str:
        start = time.time()
        response = self.llm.invoke(prompt)
        duration = time.time() - start
        print(f"⏱️ Model response time: {duration:.2f} seconds")
        return response.content