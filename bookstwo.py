from fastapi import FastAPI
from enum import Enum
app = FastAPI()


BOOKS = {
    'book_1': {'title': 'Tittle One', 'author': 'Author One'},
    'book_2': {'title': 'Tittle Two', 'author': 'Author Two'},
    'book_3': {'title': 'Tittle Three', 'author': 'Author Three'},
    'book_4': {'title': 'Tittle Four', 'author': 'Author Four'},
    'book_5': {'title': 'Tittle Five', 'author': 'Author Five'},

}

class DirectionName(str, Enum)
    north = "North"
    south = "South"
    east = "East"
    west = "West"


@app.get("/")
async def read_all_books():
    return BOOKS

@app.get("/directions/{direction_name}")
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "sub": "up"}
    if direction_name == DirectionName.south:
        return {"Direction": direction_name, "sub": "down"}
    if direction_name == DirectionName.east:
        return {"Direction": direction_name, "sub": "right"}
    if direction_name == DirectionName.west:
        return {"Direction": direction_name, "sub": "left"}



