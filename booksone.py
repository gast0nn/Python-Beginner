from fastapi import FastAPI

app = FastAPI()


BOOKS = {
    'book_1': {'title': 'Tittle One', 'author': 'Author One'},
    'book_2': {'title': 'Tittle Two', 'author': 'Author Two'},
    'book_3': {'title': 'Tittle Three', 'author': 'Author Three'},
    'book_4': {'title': 'Tittle Four', 'author': 'Author Four'},
    'book_5': {'title': 'Tittle Five', 'author': 'Author Five'},

}

@app.get("/")
async def read_all_books():
    return BOOKS

@app.get ("books/mybook")
async def read_my_favorite_book():
    return{"book_title": "My favorite book"}

@app.get("/books/{book_title}")
async def read_book(book_title):
    return {"book title": book_title}

