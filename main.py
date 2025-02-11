from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()

# Define a route using decorator
@app.get("/")
async def hello_world():
  return {"message": "Hello World"}

# Define another route with a parameter
@app.get("/hello/{name}")
async def hello_name(name: str):
  return {"message": f"Hello {name}"}

# To run this code:
# 1. Install FastAPI: pip install fastapi uvicorn
# 2. Run server: uvicorn main:app --reload
