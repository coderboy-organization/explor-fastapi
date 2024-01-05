# from __future__ import annotations
from fastapi import FastAPI, Path, Query
from fastapi.responses import JSONResponse
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str or None = None
    price: float
    tax: float or None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str or None = None,
    item: Item or None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results
