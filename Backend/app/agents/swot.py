from app.agents.llm import llm

def swot(state):
    print("Swot Agent Running")
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