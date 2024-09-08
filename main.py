from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class BookBase(BaseModel):
    book_serial: int
    title: str
    author: str
    is_rented: bool


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/add_book/")
async def add_book(book: BookBase, db: db_dependency):
    db_book = models.Books(book_serial = book.book_serial, 
                           title = book.title,
                           author = book.author)
    db.add(db_book)
    db.commit()

@app.get("/")
def index():
    return {"details": "Hello, World!"}