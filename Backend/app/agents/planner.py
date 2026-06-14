# from app.agents.llm import llm

# def planner(state):
#     print("Planner Agent Running")

#     query = state["query"]

#     response = llm.invoke(
#         f"""
#         Create a market research plan.

#         Topic:
#         {query}

#         Include:
#         - Market overview
#         - Competitors
#         - Trends
#         - SWOT
#         """
#     )

#     return {
#         "plan": response.content
#     }

import time

from app.models.state import ResearchState

def planner(state: ResearchState):

    print("=" * 50)
    print("Planner Agent Running")
    print("=" * 50)

    time.sleep(2)

    return {
        "plan": """
1. Analyze Market Size
2. Identify Key Competitors
3. Analyze Pricing Strategy
4. Evaluate Customer Sentiment
5. Generate SWOT Analysis
6. Create Executive Report
"""
    }