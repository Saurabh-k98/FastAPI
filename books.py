from fastapi import FastAPI
from enum import Enum

class Direction(str, Enum):
    south = "South"
    north = "North"
    east = "East"
    west = "West"


app = FastAPI()

BOOKS = {
    "book1":{"title":"title-1","author":"author-2"},
    "book2":{"title":"title-2","author":"author-2"},
    "book3":{"title":"title-3","author":"author-3"},
    "book4":{"title":"title-4","author":"author-4"},
    "book5":{"title":"title-5","author":"author-5"}
}

@app.get("/")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
def read_book(book_title):
    return({"Book Title":BOOKS.get(book_title)})

@app.get("/direction/direction_name")
def get_direction(direction_name:Direction):
    if direction_name== Direction.east:
        return {"Direction":direction_name,"Sub":"RIGHT"}
    if direction_name== Direction.west:
        return {"Direction":direction_name,"Sub":"LEFT"}
    if direction_name== Direction.south:
        return {"Direction":direction_name,"Sub":"DOWN"}
    if direction_name== Direction.north:
        return {"Direction":direction_name,"Sub":"UP"}

