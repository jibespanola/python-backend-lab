import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import json

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello World!"}

@app.get("/languages")
def staticList():
    file_like = open("index.html")
    return StreamingResponse(file_like)

@app.get("/files/{file_path}")
def fruit_list(file_path):
    with open(file_path, "r") as fh:
        fruits = fh.read().splitlines()
        return fruits

#endpoint accepting path parameters
@app.get("/isEven/{num}")
async def read_item(num: int):
    r = "odd" if int(num) % 2 else "even"
    return f"{num} is {r}"

