from fastapi import FastAPI
from configs.settings import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.get("/health")
def health():
    return {"status": "running"}
