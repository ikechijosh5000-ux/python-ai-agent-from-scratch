
# 🧠 AI Research Assistant Pipeline

This project is a lightweight AI-powered research assistant built using **LangChain**, **OpenAI-compatible APIs (Puter AI)**, and external tools like web search and Wikipedia. It automates research by gathering information from multiple sources and generating a structured report using an LLM.

---

## 🚀 Features

* 🔍 Web search integration (`search_tool`)
* 📚 Wikipedia lookup (`wiki_tool`)
* 🤖 AI-powered summarization using LangChain + ChatOpenAI
* 🧾 Structured research report generation
* 💾 Automatic saving of results as `.txt` files
* 🕒 Timestamped output files for organization

---

## 🏗️ Project Structure

```
project/
│
├── main.py                # Main research pipeline script
├── tools.py              # Contains search_tool and wiki_tool
├── .env                  # Environment variables (API keys)
├── outputs/              # Auto-generated research reports
└── README.md             # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-research-assistant.git
cd ai-research-assistant
```

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install langchain langchain-openai python-dotenv
```

---

## 🔑 Environment Setup

Create a `.env` file in the root directory:

```env
PUTER_API_KEY=your_api_key_here
```

---

## ▶️ How to Run

Run the application using:

```bash
python main.py
```

You will be prompted to enter a research topic:

```
Enter research topic: Artificial Intelligence in Healthcare
```

---

## 🧠 How It Works

1. User enters a research query
2. System performs:

   * Web search via `search_tool`
   * Wikipedia search via `wiki_tool`
3. Results are sent to an LLM (Puter AI via LangChain)
4. AI generates a structured report:

   * Topic
   * Summary
   * Key Points
   * Sources
5. Output is displayed in terminal
6. Result is saved automatically in `/outputs`

---

## 📄 Output Example

```
RESEARCH OUTPUT
----------------
1. Topic: Artificial Intelligence in Healthcare

2. Summary:
AI in healthcare improves diagnosis, treatment planning, and patient monitoring...

3. Key Points:
- Machine learning in diagnostics
- AI-assisted surgery
- Predictive analytics

4. Sources:
- Web search results
- Wikipedia article
```

---

## 💾 File Saving System

All outputs are automatically saved as:

```
outputs/research_YYYYMMDD_HHMMSS.txt
```

Example:

```
outputs/research_20260528_162530.txt
```

---

## 🛠️ Technologies Used

* Python 🐍
* LangChain 🧠
* OpenAI-compatible API (Puter AI)
* Wikipedia API (via tool)
* dotenv

---

## 📌 Notes

* Ensure your API key is valid before running
* Internet connection is required for search tools
* You can extend the system with:

  * PDF export
  * Voice output (TTS)
  * Streamlit UI
  * Vector database (RAG system)

---

## 🚀 Future Improvements

* Add memory for previous searches
* Add citation formatting (APA/MLA)
* Convert reports to PDF/Word
* Build web interface with FastAPI or Streamlit
* Add multi-agent research system

---

## 👨‍💻 Author

Built as an AI research automation project using LangChain and OpenAI-compatible APIs.




