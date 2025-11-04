from fastapi import FastAPI
from app.core.config import get_settings

settings = get_settings()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Initial": "Commit"}

@app.get("/health")
def health_check():
    return {"status": "ok", "environment": settings.environment}