from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
import random

app = FastAPI(title="Safariai AI Scanner")

# Laat jouw HTML-bestand zien op de homepage
@app.get("/")
async def home():
    return FileResponse("html")  # gebruik hier de naam van jouw HTML bestand

# Dummy AI endpoint
labels = ["leeuw", "olifant", "neushoorn", "cheeta", "giraffe", "buffel", "andere"]

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    prediction = random.choice(labels)
    return JSONResponse({"predicted_dier": prediction})
