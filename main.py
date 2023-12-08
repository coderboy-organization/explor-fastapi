from fastapi import FastAPI

app = FastAPI()
fake_items_db:list[dict] = [
        {
            "item_name": "Foo"
        },
        {
            "item_name": "Bar"
        },
        {
            "item_name": "Baz"
        }
    ]

@app.get("/")
async def getPost(q:str, name: str = None):
    print(q)
    print(name)
    return {"message": "get post"}

@app.get("/fuck")
async def read(skip: int = 0, limit:int = 10)->list[dict]:
    print(skip)
    print(limit)
    print(fake_items_db[skip : skip + limit]) # spacially this line please explain me
    return {
        "message": "hello"
    }