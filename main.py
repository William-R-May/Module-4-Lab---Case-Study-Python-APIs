from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Book model
class Book(BaseModel):
    id: int
    book_name: str
    author: str
    publisher: str

# In-memory "database"
books = []

# CREATE
@app.post("/books/")
def create_book(book: Book):
    books.append(book)
    return {"message": "Book added successfully", "book": book}

# READ (all)
@app.get("/books/")
def get_books():
    return books

# READ (by id)
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# UPDATE
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books):
        if book.id == book_id:
            books[i] = updated_book
            return {"message": "Book updated successfully", "book": updated_book}
    raise HTTPException(status_code=404, detail="Book not found")

# DELETE
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            deleted_book = books.pop(i)
            return {"message": "Book deleted successfully", "book": deleted_book}
    raise HTTPException(status_code=404, detail="Book not found")
