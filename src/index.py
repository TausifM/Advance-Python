# make an api listerner route port 5000 using FastAPI
from fastapi import FastAPI
from routers import products
from routers import user
app = FastAPI()
app.include_router(products.router)
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)
    
# to run the app use the command: uvicorn index:app --host 0.0.0.0 --port 5000