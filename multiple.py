from fastapi import FastAPI, Query, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str | None = None
    username: str
    password: str
    age: int | None = 19


@app.put("/{id}", tags=["update data"])
async def read_root(id: Annotated[int, Path(title="product id", ge=0, le=100)], query: Annotated[str | None, Query(title="search query")] = None, item: Item | None = None):
    print(id)
    print(query)
    print(item)
    result = {"user_id": id}
    if query:
        result.update({
            "query":query
        })
    if item:

        result.update({
            "item": jsonable_encoder(item) 
        })
    return JSONResponse(content=result, status_code=200)