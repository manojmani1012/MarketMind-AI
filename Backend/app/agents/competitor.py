# from app.agents.llm import llm

# def competitor(state):

#     research = state["research"]

#     response = llm.invoke(
#         f"""
#         Analyze competitors.

#         Research:
#         {research}

#         Return:

#         Company
#         Features
#         Pricing
#         Strengths
#         Weaknesses
#         """
#     )

#     return {
#         "competitors": response.content
#     }



import time
from app.models.state import ResearchState

def competitor(state: ResearchState):

    print("=" * 50)
    print("Competitor Agent Running")
    print("=" * 50)

    time.sleep(2)

    return {
        "competitors": """
COMPETITOR ANALYSIS

1. Cursor

Pricing:
$20 / Month

Strengths:
- AI First IDE
- Excellent UX

Weaknesses:
- Limited Enterprise Features

------------------------------------------------

2. GitHub Copilot

Pricing:
$10 / Month

Strengths:
- Microsoft Ecosystem
- Enterprise Adoption

Weaknesses:
- Limited Agentic Workflows

------------------------------------------------

3. Windsurf

Pricing:
$15 / Month

Strengths:
- Agentic Development

Weaknesses:
- Smaller User Base

------------------------------------------------

4. Codeium

Pricing:
Freemium

Strengths:
- Affordable

Weaknesses:
- Lower Accuracy
"""
    }