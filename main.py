from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
import random

app = FastAPI(title="Safariai AI Scanner")

# Laat index.html zien op de homepage
@app.get("/")
async def home():
    return FileResponse("index.html")  # index.html moet in dezelfde map staan als main.py

# Dummy AI predictie
labels = ["leeuw", "olifant", "neushoorn", "cheeta", "giraffe", "buffel", "andere"]

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    prediction = random.choice(labels)
    return JSONResponse({"predicted_dier": prediction})
