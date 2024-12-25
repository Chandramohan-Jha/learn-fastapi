from fastapi import FastAPI
from src.books.routes import book_router

version = "v1"

app = FastAPI(
  version=version,
  title="Book API",
  description="A simple API to manage books",
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["Books"])
