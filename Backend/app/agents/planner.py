from app.agents.llm import llm

def planner(state):

    query = state["query"]

    response = llm.invoke(
        f"""
        Create a market research plan.

        Topic:
        {query}

        Include:
        - Market overview
        - Competitors
        - Trends
        - SWOT
        """
    )

    return {
        "plan": response.content
    }