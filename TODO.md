### Simple query explain

```py
@app.get("/items", tags=["get items"])
async def get_items(q: str | None = None):
# async def get_items(q: Annotated[str | None] = None):
    results: dict[str, list[dict[str, str]]] = {
        "items": [
            {"item_id": "Foo"},
            {"item_id": "Bar"}
        ]
    }
    if q:
        results.update({"query": q})
    return results
```

### Additional validation

- query Length validation
  - We can use 2 way our query validations (**Without `Annotated`**)
  ```bash
  q: str | None = None
  ```
  - With `Annotated`
  ```bash
  q: Annotated[str | None] = None
  ```
  - **Note:** Both of those versions mean the same thing
