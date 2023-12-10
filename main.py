from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from constants._data import fake_items_db
from schemas import user

app = FastAPI()

@app.post("/")
async def create(user:user.User)-> user.User:
    print(user)
    JSONResponse(status_code=200, content={
        user
    })

@app.get("/")
async def getPost(q:str, name: str = None):
    print(q)
    print(name)
    return {"message": "get post"}

@app.get("/find")
async def read(skip: int = 0, limit:int = 10)->list[dict]:
    print(skip)
    print(limit)
    print(fake_items_db[skip : skip + limit])
    return {
        "message": "hello"
    }