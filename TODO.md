### Query Validation

What we will cover? (**Recap**)

- Generic validations and metadata:
  1. alias -> **Show as placeholder**
  2. title -> **Show as title**
  3. description -> **show as params description**
  4. deprecated (ডেফরিকেটেট) -> **make disable**
- Strings Validations:
  1. min_length -> **set min length of string**
  2. max_length -> **set max length of string**
  3. pattern -> **regular ex**

#### Simple query validation

```py
@app.get("/items", tags=["get items"])
async def get_items(q: str | None = None):
# async def get_items(q: Annotated[str] = None):
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
  - With Query `fastapi` method
  ```bash
  q: Annotated[str | None, Query(max_length=10)] = None
  ```
  - **Note:** Both of those versions mean the same thing

### Add more validations

- We can also add min_length for validation
  ```bash
  q: Annotated[str | None, Query(min_length=3, max_length=50)] = None
  ```

#### Add regular expressions

We can also define a regular expression pattern that the parameter should match. **We can also call this `parameter parttern`**

```bash
Query(min_length=3, max_length=50, pattern="^sabbir$")
```

`^`: starts with the following characters, doesn't have characters before.
`sabbir`: has the exact value sabbir.
`$`: ends there, doesn't have any more characters after sabbir.

### Query List/multiple value

```bash
query: Annotated[list[str] | None, Query()] = None
```
