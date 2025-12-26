from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

books = [
    {"id": 1, "title": "Окаянные дни", "author": "Бунин И.А."},
    {"id": 2, "title": "Дни Турбиных", "author": "Булгаков М.С."},
]


@app.get("/")
def main_page():
    return "Hello world"


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
        else:
            raise HTTPException(status_code=404)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
