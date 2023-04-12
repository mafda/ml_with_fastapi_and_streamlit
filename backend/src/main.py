"""
This is a FastAPI application that receives an HTTP GET request at the root
endpoint ("/") and returns the classification probability of a digit image.
"""

import numpy as np
from fastapi import FastAPI, Request
from model.predict import classify_digit

# Create FastAPI instance
app = FastAPI()


# Define GET route to classify the digit
@app.get("/")
async def get_classify_digit(info: Request):
    # Parse input image from the request
    req_info = await info.json()
    img = np.array(req_info["image"])

    # Classify the digit using the imported function
    prob = classify_digit(img)

    # Return probability of each class in a JSON format
    return {"prob": prob.tolist()}
