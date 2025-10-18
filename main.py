from fastapi import FastAPI
from enum import Enum

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