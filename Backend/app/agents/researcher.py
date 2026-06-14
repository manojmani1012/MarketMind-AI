# import os

# from tavily import TavilyClient

# client = TavilyClient(
#     api_key=os.getenv("TAVILY_API_KEY")
# )

# def researcher(state):
#     print("researcher Agent Running")
#     query = state["query"]

#     result = client.search(
#         query=query,
#         max_results=5
#     )

#     text = ""

#     for item in result["results"]:

#         text += item["content"] + "\n"

#     return {
#         "research": text
#     }


import time

from app.models.state import ResearchState
def researcher(state: ResearchState):

    print("=" * 50)
    print("Research Agent Running")
    print("=" * 50)

    time.sleep(2)

    return {
        "research": """
MARKET RESEARCH FINDINGS

Market:
AI Coding Assistants

Estimated Market Size:
$4.2 Billion

Projected CAGR:
24%

Target Users:
- Software Engineers
- Enterprises
- Startups
- Product Teams

Growth Drivers:
- Increased AI Adoption
- Software Automation
- Enterprise Transformation
- Developer Productivity

Emerging Trends:
- Agentic AI
- Autonomous Coding
- AI Pair Programming
- Multi-Agent Development Systems
"""
    }