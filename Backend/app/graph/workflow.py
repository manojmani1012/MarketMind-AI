from langgraph.graph import StateGraph
from langgraph.graph import END

from app.models.state import ResearchState

from app.agents.planner import planner
from app.agents.researcher import researcher
from app.agents.competitor import competitor
from app.agents.swot import swot
from app.agents.reporter import reporter

builder = StateGraph(ResearchState)

builder.add_node(
    "planner",
    planner
)

builder.add_node(
    "researcher",
    researcher
)

builder.add_node(
    "competitor",
    competitor
)

builder.add_node(
    "swot",
    swot
)

builder.add_node(
    "reporter",
    reporter
)

builder.set_entry_point("planner")

builder.add_edge(
    "planner",
    "researcher"
)

builder.add_edge(
    "researcher",
    "competitor"
)

builder.add_edge(
    "competitor",
    "swot"
)

builder.add_edge(
    "swot",
    "reporter"
)

builder.add_edge(
    "reporter",
    END
)

graph = builder.compile()