# from typing import Union
import uvicorn
from fastapi import FastAPI

LOADED_MODEL = load_model('movie_sent.h5')

app = FastAPI(title="Moview Review Service", description="API to predict sentiment of movie review")



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
