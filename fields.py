from fastapi import FastAPI, Path, Body
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello, World!"}

class Item(BaseModel):
    name: str
    # start to use field embedding
    description: str | None = Field(None, title="The description of the item", max_length=300)
    price: float | None = Field(..., gt=0, description="The price must be greater than zero")
    tax: float | None = Field(...)
    # end field embedding


@app.put("/items/{item_id}")
async def update_item(
    item_id: int ,item: Item = Body(...,embed=True), # embed=True to embed the item under "item" key in the request body
    ):

    results = {"item_id": item_id, "item_name": item.name}

    return results