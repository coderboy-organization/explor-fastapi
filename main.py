from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from constants._data import fake_items_db
from schemas.user import UserSchema

app = FastAPI()

@app.post("/create", tags=["Create User"])
async def create(user:UserSchema)->UserSchema:
    print(user)
    encoded = jsonable_encoder(user)
    # return encoded
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=encoded)


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