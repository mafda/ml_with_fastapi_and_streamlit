import numpy as np
from fastapi import FastAPI, Request
from model.predict import classify_digit

app = FastAPI()


@app.get("/")
async def getClassify_digit(info: Request):
    req_info = await info.json()
    img = np.array(req_info["image"])
    prob = classify_digit(img)
    return {"prob": prob.tolist()}
