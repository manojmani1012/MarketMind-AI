from typing import TypedDict, NotRequired

class ResearchState(TypedDict):
    query: str

    plan: NotRequired[str]
    research: NotRequired[str]
    competitors: NotRequired[str]
    swot: NotRequired[str]
    report: NotRequired[str]