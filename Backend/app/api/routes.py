# from fastapi import APIRouter

# from app.graph.workflow import graph

# router = APIRouter()

# @router.post("/research")
# def run_research(data: dict):

#     result = graph.invoke(
#         {
#             "query": data["query"]
#         }
#     )

#     return result



from fastapi import APIRouter

from app.graph.workflow import graph

router = APIRouter()


@router.post("/research")
def run_research(data: dict):

    print("\n")
    print("=" * 60)
    print("NEW MARKET RESEARCH REQUEST")
    print("=" * 60)
    print(data["query"])
    print("=" * 60)

    result = graph.invoke(
        {
            "query": data["query"]
        }
    )

    print("WORKFLOW COMPLETED")

    return result