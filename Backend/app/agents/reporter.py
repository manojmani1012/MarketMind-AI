from app.agents.llm import llm

def reporter(state):

    response = llm.invoke(
        f"""
        Generate executive report.

        Topic:
        {state['query']}

        Plan:
        {state['plan']}

        Research:
        {state['research']}

        Competitors:
        {state['competitors']}

        SWOT:
        {state['swot']}

        Format professionally.
        """
    )

    return {
        "report": response.content
    }