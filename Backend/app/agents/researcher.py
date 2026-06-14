from tavily import TavilyClient

client = TavilyClient()

def researcher(state):

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