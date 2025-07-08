from langchain.prompts import PromptTemplate
from service.llm_agent import LLMAgent
from service.prompts.summary_templates import SUMMARY_TEMPLATES

class Summarizer:
    def __init__(self):
        self.llm_agent = LLMAgent()
        self.templates = SUMMARY_TEMPLATES
        self.default_lang = "en"

    def get_prompt_template(self, lang: str) -> PromptTemplate:
        template_str = self.templates.get(lang)
        if not template_str:
            print(f"⚠️ Idioma '{lang}' no soportado, usando inglés por defecto.")
            template_str = self.templates[self.default_lang]
        return PromptTemplate.from_template(template_str)

    def summarize(self, question: str, web_content: str, lang: str = "en") -> str:
        full_text = f"Question: {question}\nContent:\n{web_content}"
        prompt = self.get_prompt_template(lang).format(text=full_text)
        return self.llm_agent.run_prompt(prompt)
