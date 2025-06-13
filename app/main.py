from fastapi import FastAPI

from .api.v1.endpoints import health
from .api.v1.endpoints import members, books, loans

app = FastAPI()

app.include_router(health.router)
app.include_router(members.router)
app.include_router(books.router)
app.include_router(loans.router)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000)

