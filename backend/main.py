# from typing import Union
import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Moview Review Service", description="API to predict sentiment of movie review")



@app.post("predict")
def get_number(textinput):
    return(textinput)
