from langdetect import detect

def detect_language(text: str) -> str:
    """Detects the language of the input text. Returns ISO 639-1 code (e.g. 'en', 'es')."""
    return detect(text)