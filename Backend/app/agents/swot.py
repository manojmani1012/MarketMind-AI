# from app.agents.llm import llm

# def swot(state):
#     print("Swot Agent Running")
#     response = llm.invoke(
#         f"""
#         Create SWOT analysis.

#         Research:
#         {state['research']}

#         Competitors:
#         {state['competitors']}
#         """
#     )

#     return {
#         "swot": response.content
#     }


import time
from app.models.state import ResearchState

def swot(state: ResearchState):

    print("=" * 50)
    print("SWOT Agent Running")
    print("=" * 50)

    time.sleep(2)

    return {
        "swot": """
SWOT ANALYSIS

STRENGTHS
----------
• High Market Growth
• Strong Investor Interest
• Increasing Enterprise Adoption

WEAKNESSES
-----------
• Intense Competition
• Hallucination Risks
• Security Concerns

OPPORTUNITIES
--------------
• Enterprise AI Agents
• Internal Developer Platforms
• AI Governance Solutions

THREATS
---------
• Open Source Models
• Regulatory Changes
• Price Competition
"""
    }