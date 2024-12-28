from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.db.main import init_db
from src.books.routes import book_router


@asynccontextmanager
async def lifespan(app: FastAPI):
  print("Server is starting...")
  await init_db()
  yield
  print("Server is shutting down...")


version = "v1"

app = FastAPI(
  version=version,
  title="Book API",
  description="A simple API to manage books",
  lifespan=lifespan
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["Books"])
