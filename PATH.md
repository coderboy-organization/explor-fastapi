### Recap

We can also declare numeric validations:

- `gt` : greater than
- `ge` : greater than or equal
- `lt` : less than
- `le` : less than or equal

#### Path if we metion it then it alawys will requird

Here is very simple way

```py
@app.get("/{id}")
def get(id: int):
    print(type(id))
    results = {"id": id}
    return results
```

#### 0.2 Path metadata with `Annotated`

```py
@app.get("/{id}")
def get(id: Annotated[int, Path(title="The ID of the item")]):
    print(type(id))
    results = {"id": id}
    return results
```

#### 0.3 Path with Query at the same times

```py
@app.get("/{id}")
def get(id: Annotated[int, Path(title="The ID of the item")],
        q: Annotated[str | None, Query(alias="query")] = None):
    print(type(id))
    results = {"id": id}
    if q:
        results.update({"q": q})
    return results
```

#### 0.4 Path number validation

```py
@app.get("/item/{item_id}")
async def item_id(item_id: Annotated[int, Path(title="10", ge=0, le=20)], q: str):
    if item_id and q:
        return {
            "item_id": item_id,
            "query": q
        }
    return {"dont": 'have'}
```
