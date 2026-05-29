from langchain.tools import tool
from duckduckgo_search import DDGS
import wikipedia
import os
from datetime import datetime


# ============================================
# INTERNET SEARCH TOOL
# ============================================


@tool
def search_tool(query: str) -> str:
    """
    Search the internet for information.
    """

    results = []

    try:
        with DDGS() as ddgs:
            searches = ddgs.text(query, max_results=5)

            for item in searches:
                results.append(
                    f"""
Title: {item.get("title")}

Link: {item.get("href")}

Snippet: {item.get("body")}
"""
                )

        return "\n".join(results)

    except Exception as e:
        return f"Search Error: {str(e)}"


# ============================================
# WIKIPEDIA TOOL
# ============================================


@tool
def wiki_tool(query: str) -> str:
    """
    Search Wikipedia for factual information.
    """

    try:
        return wikipedia.summary(query, sentences=5)

    except Exception as e:
        return f"Wikipedia Error: {str(e)}"


# ============================================
# SAVE TOOL
# ============================================


@tool
def save_tool(content: str) -> str:
    """
    Save research content into a text file.
    """

    try:
        # Create outputs folder if it does not exist
        os.makedirs("outputs", exist_ok=True)

        # Create filename with timestamp
        filename = f"outputs/research_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        # Save content
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

        return f"Research saved successfully to {filename}"

    except Exception as e:
        return f"Save Error: {str(e)}"


# ============================================
# TEST SECTION
# ============================================

if __name__ == "__main__":
    query = input("Enter a topic to research: ")

    print("\nSEARCH RESULTS\n")
    print(search_tool.invoke(query))

    print("\nWIKIPEDIA RESULTS\n")
    print(wiki_tool.invoke(query))

    save = input("\nDo you want to save the result? (yes/no): ")

    if save.lower() == "yes":
        combined_content = f"""
SEARCH RESULTS:

{search_tool.invoke(query)}

WIKIPEDIA RESULTS:

{wiki_tool.invoke(query)}
"""

        result = save_tool.invoke(combined_content)

        print(result)
