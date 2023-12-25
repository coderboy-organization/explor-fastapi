from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()

"""
@app.get("/{id}")
def get(id: Annotated[int, Path(title="The ID of the item")]):
    # Path params if is alawys required
    print(type(id))
    results = {"id": id}
    return results


@app.get("/{id}")
def get(id: Annotated[int, Path(title="The ID of the item")],
        q: Annotated[str | None, Query(alias="query")] = None):
    print(type(id))
    results = {"id": id}
    if q:
        results.update({"q": q})
    return results
"""


@app.get("/item/{item_id}")
async def item_id(item_id: Annotated[int, Path(title="10", ge=0, le=20)], q: str):
    if item_id and q:
        return {
            "item_id": item_id,
            "query": q
        }
    return {"dont": 'have'}
