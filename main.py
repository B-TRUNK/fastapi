from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

@app.get("/")
async def root():
    return {"Hello, World!"}

@app.post("/", deprecated=True)
async def post():
    return {"This is a POST request"}

@app.put("/" ,description="Handle PUT requests")
async def put():
    return {"This is a PUT request"}