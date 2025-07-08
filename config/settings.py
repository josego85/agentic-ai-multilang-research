from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / '.env')

class Settings:
    SERPAPI_API_KEY: str = os.getenv("SERPAPI_API_KEY")

    def __post_init__(self):
        assert self.SERPAPI_API_KEY, "SERPAPI_API_KEY is required"

settings = Settings()
