from fastapi import FastAPI

from .api.v1.endpoints import health

app = FastAPI()

app.include_router(health.router)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

