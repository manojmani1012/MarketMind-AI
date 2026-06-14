from app.agents.llm import llm

def swot(state):

    response = llm.invoke(
        f"""
        Create SWOT analysis.

        Research:
        {state['research']}

        Competitors:
        {state['competitors']}
        """
    )

    return {
        "swot": response.content
    }