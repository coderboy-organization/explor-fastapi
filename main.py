from fastapi import FastAPI
from db._data import fake_items_db

app = FastAPI()

@app.get("/")
async def getPost(q:str, name: str = None):
    print(q)
    print(name)
    return {"message": "get post"}

@app.get("/fuck")
async def read(skip: int = 0, limit:int = 10)->list[dict]:
    print(skip)
    print(limit)
    print(fake_items_db[skip : skip + limit])
    return {
        "message": "hello"
    }