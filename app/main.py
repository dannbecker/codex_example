from fastapi import FastAPI

from .api.v1.endpoints import health

app = FastAPI()

app.include_router(health.router)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000)

