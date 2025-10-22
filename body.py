#this API file is envolved with request body management
from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello, World!"}

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None

@app.put("/items/{item_id}")
async def update_item(
    *, # * indicates that all following parameters are keyword-only
    item_id: int = Path(..., title='Item Id', ge=0, le=100),
    query_param : str | None = None,
    item : Item | None = None,
    user: User | None = None,
    age : int = Body(..., gt=0, lt=90)
    ):

    result = {"item_id": item_id}
    if query_param:
        result.update({"query_param": query_param})
    if item:
        result.update({"item": item.model_dump()})
    if user:
        result.update({"user": user.model_dump()})
    if age:
        result.update({"age": age})
    return result
