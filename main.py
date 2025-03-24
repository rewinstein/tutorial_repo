from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI app
app = FastAPI()

# Define a Pydantic model for data validation
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

# Create a root endpoint
@app.get("/")
def read_root():
    return {"Hello": "Worldqqqqq MARCH 24!"}

# Create an endpoint with path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Create a POST endpoint using the Pydantic model
@app.post("/items/")
def create_item(item: Item):
    return item

# Run with: uvicorn main:app --reload
# Where 'main' is the name of this Python file