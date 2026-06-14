from app.agents.llm import llm

def competitor(state):

    research = state["research"]

    response = llm.invoke(
        f"""
        Analyze competitors.

        Research:
        {research}

        Return:

        Company
        Features
        Pricing
        Strengths
        Weaknesses
        """
    )

    return {
        "competitors": response.content
    }