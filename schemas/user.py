from pydantic import BaseModel
from utils import Role

class User(BaseModel):
    name: str | None = None
    age: int
    role: Role = Role.USER
    email: str
    password: str
