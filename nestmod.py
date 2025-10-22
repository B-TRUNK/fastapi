# this module is dealing with nested models
from fastapi import FastAPI, Path, Body
from pydantic import BaseModel, HttpUrl as spe #speial type for URL

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello, World!"}

class Image(BaseModel):
    url: spe
    description: str

class Item(BaseModel):
    name: str
    description: str 
    price: float | None = None
    tax: float
    image :Image

class Product(BaseModel):
    item : Item
    image : Image

@app.put("/items/{item_id}")
async def update_item(
    item_id: int ,
    item: Item,
):
    results = {"item_id": item_id, "item": item}
    return results

@app.post("/products/{item_id}")
async def update_product(item : Item, image : Image):

    product = {"item": item, "image": image},
    return product