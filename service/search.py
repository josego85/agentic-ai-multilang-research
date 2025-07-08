from config.settings import settings
from langchain_community.utilities import SerpAPIWrapper

class SearchService:
    def __init__(self, api_key: str = settings.SERPAPI_API_KEY):
        self.api_key = api_key

    def web_search(self, query: str, lang: str = "en") -> str:
        print(f"🔍 Searching the web for: {query} (lang={lang})")
        search_tool = SerpAPIWrapper(
            serpapi_api_key=self.api_key,
            params={"lr": f"lang_{lang}"}
        )
        return search_tool.run(query)