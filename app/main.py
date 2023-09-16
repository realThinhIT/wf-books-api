from fastapi import FastAPI
from app.routers.books import router as books_router
from app.routers.authors import router as authors_router

app = FastAPI()

# Init routers for books and authors
app.include_router(books_router)
app.include_router(authors_router)
