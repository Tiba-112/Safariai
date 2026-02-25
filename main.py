from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
import random

app = FastAPI(title="Safariai AI Scanner")

# Serve de homepage met jouw HTML-bestand
@app.get("/")
async def home():
    return FileResponse("html.html")  # LET OP: gebruik de volledige naam incl. .html

# Dummy AI endpoint
labels = ["leeuw", "olifant", "neushoorn", "cheeta", "giraffe", "buffel", "andere"]

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    prediction = random.choice(labels)
    return JSONResponse({"predicted_dier": prediction})
