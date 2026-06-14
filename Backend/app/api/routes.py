from fastapi import APIRouter

from app.graph.workflow import graph

router = APIRouter()

@router.post("/research")
def run_research(data: dict):

    result = graph.invoke(
        {
            "query": data["query"]
        }
    )

    return result