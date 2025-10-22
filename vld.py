from fastapi import FastAPI,Query, Path

# Create FastAPI instance
app = FastAPI()

#==========================================================================================================
#string validation for query parameters
#from fastapi import Query, Path

@app.get("/val")
async def validate_string(name: str=Query(..., requiered = True, min_length=3, max_length=10, regex="^[a-zA-Z]+$")
                          ,email: str = Query(..., requiered = True, min_length=5, max_length=50, regex="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$",
                                              title="Email Parameter", description="The email must be a valid email address format")):
   return {"name": name , "email": email}

#number validation for path parameters
@app.get("/vld/{age}")
async def get_age(age: int = Path(..., ge=1, le=100, title="Age Parameter", description="The age of the user, must be greater than or equal to 1")):
    return {"age = ": age}

@app.get("/val/{price}")
async def validate_price(price: float = Path(..., gt=0.0, lt=10000.0, title="Price Parameter", description="The price must be greater than 0.0 and less than 10000.0")):
    return {"price": price}