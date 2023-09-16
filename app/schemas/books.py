from pydantic import BaseModel


class Book(BaseModel):
    id: str
    author: str
    name: str
    note: str
    serial: str


class BookIn(Book):
    id: None = None


class BookOut(Book):
    pass
