from typing import Optional

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "My world"}

@app.get("/hi")
def read_hi():
    return {"Hello": "hi"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0')    
