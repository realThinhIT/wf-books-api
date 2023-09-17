from pydantic import BaseModel, Field


class Book(BaseModel):
    id: str
    author: str = Field(regex=r"^/authors/")  # Validate if author is in correct format of "/authors/..."
    name: str
    note: str
    serial: str


class BookIn(Book):
    id: None = None


class BookOut(Book):
    pass
