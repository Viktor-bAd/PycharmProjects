
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

@app.get("/hello_world")
def hello_world():
    return {"message": "Hello World"}


@app.post("/register/{username}")
def register(username: str):
    return {
        "username": username,
        "is_registered" : True
    }


data:dict [str,str]




class Response(BaseModel):
    message: str

@app.post("/hello")
def hello_world()->Response:
    return Response(
        message="Hello World"
    )
#


class Response(BaseModel):
    message: str

@app.get("/greeting")
def greeting()-> Response:
    return Response(
         message="Привіт з сервера1",
    )



class Book(BaseModel):
    id: int
    title: str
    autor: str
    year: int
    pages: int


@app.get("/books/")
def all_books() -> List[Book]:
    with open("books.json") as file:
        books = json.load(file)
        return books


@app.get("/books/{id}")
def get_book(id: int):
    with open("books.json") as file:
        books = json.load(file)

    for book in books:
        if book["id"] == id:
            return book


@app.post("/books/")
def create_book(book: Book) -> dict[str, str]:
    with open("books.json") as file:
        books = json.load(file)

    books.append(book.model_dump())

    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)
    return {"message": "Книга додана успішно"}
