# Agentic AI Multilang Research

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/josego85/agentic-ai-multilang-research/releases)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Ollama](https://img.shields.io/badge/Ollama-supported-brightgreen)](https://ollama.com/)
[![Issues](https://img.shields.io/github/issues/josego85/agentic-ai-multilang-research)](https://github.com/josego85/agentic-ai-multilang-research/issues)

🌍🤖 **AI-powered multilingual research assistant for instant web search and summaries** ✨

---

## Overview

**agentic-ai-multilang-research** is an advanced, agentic research assistant that empowers you to ask questions in any language and receive concise, insightful answers—instantly.  
It leverages state-of-the-art language models, agentic workflows, and real-time web search to deliver up-to-date, multilingual research summaries.

- **Ask in any language:** The assistant detects your language and responds accordingly.
- **Always up-to-date:** Integrates with Google Search for the latest information.
- **Powered by LLMs:** Uses Ollama and LangChain for local, private, and fast LLM inference.
- **Agentic reasoning:** Employs graph-based agent workflows for multi-step synthesis.

---

## Features

- 🌐 **Multilingual Input & Output:** Seamlessly handles questions and answers in any language.
- 🔍 **Automated Web Search:** Retrieves and summarizes relevant web content in your language.
- 🧠 **Agentic Reasoning:** Uses graph-based workflows for advanced, multi-step synthesis.
- 📝 **Concise Summaries:** Delivers clear, actionable answers using LLM-powered summarization.
- 🛠️ **Customizable & Modular:** Easily swap models, search providers, or summarization logic.
- 🏃 **Runs Locally:** All LLM inference is performed locally via Ollama for privacy and speed.

---

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone git@github.com:josego85/agentic-ai-multilang-research.git
   cd agentic-ai-multilang-research
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Download an LLM model with Ollama:**
   ```bash
   ollama pull gemma3:1b
   ```
   *(Or use another supported model, e.g., llama2)*

5. **Configure API keys:**  
   This project **requires** a SerpAPI key for Google Search integration.  
   Visit [SerpAPI](https://serpapi.com/) to create an account and obtain your API key.  
   Add your credentials to a `.env` file in the project root:

   ```
   SERPAPI_API_KEY=your_api_key_here
   ```

6. **Run the assistant:**
   ```bash
   python main.py
   ```

---

## Example Usage

```bash
python main.py
```

**Sample interaction:**

```
AI Agent: Ask your question in any language and get a summarized answer.
Your question:

--> Was ist der Einfluss von KI-Agenten auf die Arbeitswelt?

🔍 Searching the web for: Was ist der Einfluss von KI-Agenten auf die Arbeitswelt? (lang=de)

⏱ Model response time: 3.92 seconds
⏱ Model response time: 5.96 seconds

Final Response: 

Laut der Zusammenfassung hat der Einfluss von KI-Agenten auf die Arbeitswelt folgende Auswirkungen:

*   **Aufgabeübernahme:** KI-Agenten übernehmen Aufgaben, die bisher menschliche Mitarbeiter erledigten.
*   **Einstiegshürden senken:** Sie machen es einfacher, neue Berufe zu erlernen und zu ergreifen.

Kurz gesagt, KI-Agenten verändern die Arbeitswelt, indem sie Aufgaben automatisieren und so neue Möglichkeiten für Menschen schaffen.
```

**Try questions in any language:**

- *English:*  
  `How will AI agents impact the future of education?`
- *Español:*  
  `¿Qué impacto tendrán los agentes de IA en la medicina moderna?`
- *Français:*  
  `Quel est l'effet des agents IA sur la productivité des entreprises ?`

---

## Project Structure

- `main.py` — Entry point; handles user queries and displays responses.
- `agent/graph.py` — Defines the agentic workflow and orchestration logic.
- `service/llm_agent.py` — LLM interface using LangChain and Ollama.
- `service/summarize.py` — Summarization service for multilingual output.
- `.env` — (Optional) API keys and environment variables.

---

## Configuration

- **Model Selection:**  
  Change the model name in `service/llm_agent.py` to use a different LLM with Ollama.

- **Environment Variables:**  
  Place your `.env` file in the project root with any required API keys or configuration.

---

## Requirements

- Python 3.11+
- [Ollama](https://ollama.com/) installed and running for local LLM inference

---

## Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open an issue or submit a pull request.

---

## License

GNU General Public License v3.0

---

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [Ollama](https://ollama.com/)
- [Google Search Results API](https://serpapi.com/)

---

## Contact

For questions or support, open an issue on [GitHub](https://github.com/josego85/agentic-ai-multilang-research/issues).
