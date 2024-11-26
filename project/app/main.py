from fastapi import FastAPI
from typing import Optional

#FastAPI 인스턴스
app = FastAPI()

#기본 라우트
@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}

@app.get("/home")
def home():
    return {"message": "home"}
