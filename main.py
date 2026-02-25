from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import random

app = FastAPI(title="Safariai AI Scanner")

# Dummy labels van Safariai-dieren
labels = ["leeuw", "olifant", "neushoorn", "cheeta", "giraffe", "buffel", "andere"]

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Kies willekeurig een dier als placeholder
    prediction = random.choice(labels)
    return JSONResponse({"predicted_dier": prediction})
