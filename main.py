from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

# Create FastAPI instance
app = FastAPI()

@app.get("/")
async def root():
    return {"Hello, World!"}

@app.post("/")
async def post():
    return {"This is a POST request"}

@app.put("/" ,description="Handle PUT requests" """,deprecated=True""")
async def put():
    return {"This is a PUT request"}

@app.get("/users")
async def list_user():
    return {"message": "List of users"}

#passing a path parameter

@app.get("/users/1" ,include_in_schema=False)
async def get_user():
    return {"message": "This is Admin Portal"}


@app.get("/users/{user_id}")
async def get_user(user_id : int):
    return {"user_id": user_id}

class UserList(str, Enum):
    admin = 1
    manager = 2
    employee = 3

@app.get("/{user_type}/{user_id}")
async def get_user_by_type(user_type: UserList ,user_id):
    return {"user": {user_type.name, user_id}}


#passing a query parameter ,used for filtering incoming data
items = [
    {"id": 1, "name": "book", "price": 100, "stock": True},
    {"id": 2, "name": "game" , "price": 200, "stock": False},
    {"id": 3, "name": "cd" , "price": 150, "stock": True},
    {"id": 4, "name": "magazine" , "price": 50, "stock": True},
    {"id": 5, "name": "item5" , "price": 300, "stock": False},
    {"id": 6, "name": "item6" , "price": 400, "stock": True}
    ]

@app.get("/items")
async def get_items(
    start: int = 0,
    end: int = 10,
    id : int = None,
    name: str = None,

    ):
    #filtered_items = [item for item in items if min_price <= item["price"] <= max_price]

    if id:
        item = next((item for item in items if item["id"] == id), None)
        if item:
            return item
        return {"message": "Item not found"}
    
    if name:
        filtered = []
        for item in items:
            if item["name"] == name:
                filtered.append(item)
        return filtered

    return items[start:start+end]

@app.get("/items_sorted")
async def sort_prices(range: int = None):
    sorted_price = sorted(items, key=lambda x: x["price"] ,reverse=False)

    if range:
        price_range = [item for item in sorted_price if item["price"] <= range]
        return price_range
    else:
        return sorted_price
    
@app.get("/stock")
async def get_shortaged_items(stock: bool = True):
    if not stock:
        item = [item for item in items if item["stock"] == False]
        return item
    #http://127.0.0.1:8000/stock?stock=off
    else:
        return {"message": "All items are in stock"}
    
#==========================================================================================================
#Passing request body

#import pydantic 

class Item(BaseModel):
    name: str
    description: str| None = None
    price: float
    tax: float | None = None

@app.post("/item")
async def create_item(item: Item):
    item_dict = item.model_dump()

    price_with_tax = item.price + (item.price * item.tax) if item.tax else item.price

    item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/item/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}

   
