from dotenv import load_dotenv
import os
from datetime import datetime

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from tools import search_tool, wiki_tool


# =========================
# LOAD ENV
# =========================
load_dotenv()


# =========================
# PUTER MODEL
# =========================
llm = ChatOpenAI(
    api_key=os.getenv("PUTER_API_KEY"),
    base_url="https://api.puter.com/puterai/openai/v1/",
    model="gpt-4.1-mini",
    temperature=0.3,
)


# =========================
# RESEARCH PIPELINE
# =========================
def run_research(query: str):

    print("\n🔎 Searching web...\n")
    web_data = search_tool.invoke(query)

    print("📚 Searching Wikipedia...\n")
    wiki_data = wiki_tool.invoke(query)

    system_prompt = """
You are a professional research assistant.

Your job:
- Analyze provided data
- Combine information clearly
- Write a structured report

Format:
1. Topic
2. Summary
3. Key Points
4. Sources
"""

    user_prompt = f"""
TOPIC: {query}

WEB RESULTS:
{web_data}

WIKIPEDIA RESULTS:
{wiki_data}
"""

    response = llm.invoke(
        [SystemMessage(content=system_prompt), HumanMessage(content=user_prompt)]
    )

    return response.content


# =========================
# MAIN
# =========================
def main():

    query = input("\nEnter research topic: ")

    try:
        result = run_research(query)

        print("\n==============================")
        print("RESEARCH OUTPUT")
        print("==============================\n")
        print(result)

        # Save automatically
        filename = f"outputs/research_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        os.makedirs("outputs", exist_ok=True)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(result)

        print(f"\n💾 Saved to: {filename}")

    except Exception as e:
        print("\n❌ ERROR:")
        print(str(e))


if __name__ == "__main__":
    main()
