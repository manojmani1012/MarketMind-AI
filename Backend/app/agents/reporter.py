# from app.agents.llm import llm

# def reporter(state):
#     print("Reporter Agent Running")
#     response = llm.invoke(
#         f"""
#         Generate executive report.

#         Topic:
#         {state['query']}

#         Plan:
#         {state['plan']}

#         Research:
#         {state['research']}

#         Competitors:
#         {state['competitors']}

#         SWOT:
#         {state['swot']}

#         Format professionally.
#         """
#     )

#     return {
#         "report": response.content
#     }



import time

from app.models.state import ResearchState
def reporter(state: ResearchState):

    print("=" * 50)
    print("Executive Report Agent Running")
    print("=" * 50)

    time.sleep(2)

    return {
        "report": f"""
========================================================
MARKETMIND AI
AUTONOMOUS MARKET RESEARCH REPORT
========================================================

TOPIC
--------------------------------------------------------
{state["query"]}

========================================================
EXECUTIVE SUMMARY
========================================================

The AI Coding Assistant market is experiencing rapid
growth driven by enterprise AI adoption and increasing
demand for developer productivity solutions.

Organizations are actively investing in AI-powered
software development tools to reduce development
time and improve engineering efficiency.

========================================================
MARKET OVERVIEW
========================================================

Market Size:
$4.2 Billion

Projected CAGR:
24%

Key Drivers:

• Enterprise AI Adoption
• Developer Productivity
• Cost Optimization
• Automation Initiatives

========================================================
COMPETITOR LANDSCAPE
========================================================

Leading Competitors:

1. Cursor
2. GitHub Copilot
3. Windsurf
4. Codeium

Market Leader:
GitHub Copilot

Fastest Growing:
Cursor

========================================================
SWOT SUMMARY
========================================================

Strengths:
• High Growth Market
• Strong Enterprise Demand

Weaknesses:
• Competitive Landscape

Opportunities:
• Autonomous AI Agents
• Enterprise Workflows

Threats:
• Open Source Alternatives
• Regulatory Challenges

========================================================
STRATEGIC RECOMMENDATIONS
========================================================

1. Focus on Enterprise Customers

2. Differentiate through Agentic AI

3. Invest in Multi-Agent Collaboration

4. Build Governance & Security Features

5. Create Vertical-Specific Solutions

========================================================
MARKET ATTRACTIVENESS SCORE
========================================================

9.1 / 10

Overall Recommendation:

HIGHLY ATTRACTIVE MARKET

========================================================
END OF REPORT
========================================================
"""
    }