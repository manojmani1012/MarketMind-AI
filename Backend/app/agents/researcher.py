import os

from tavily import TavilyClient

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def researcher(state):
    print("researcher Agent Running")
    query = state["query"]

    result = client.search(
        query=query,
        max_results=5
    )

    text = ""

    for item in result["results"]:

        text += item["content"] + "\n"

    return {
        "research": text
    }