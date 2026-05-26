from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()

# PostgreSQL Connection
conn = psycopg2.connect(
    host="localhost",
    dbname="library_db",
    user="postgres",
    password="tejas",
    port="5432"
)

cur = conn.cursor()

# -----------------------------
# Pydantic Model
# -----------------------------
class Book(BaseModel):
    title: str
    author: str
    published_year: int

# -----------------------------
# HOME ROUTE
# -----------------------------
@app.get("/")
def home():
    return {"message": "Library Management System"}

# -----------------------------
# ADD BOOK
# -----------------------------
@app.post("/books")
def add_book(book: Book):

    query = """
    INSERT INTO books (title, author, published_year)
    VALUES (%s, %s, %s)
    """

    cur.execute(
        query,
        (book.title, book.author, book.published_year)
    )

    conn.commit()

    return {"message": "Book added successfully"}

# -----------------------------
# GET ALL BOOKS
# -----------------------------
@app.get("/books")
def get_books():

    query = "SELECT * FROM books"

    cur.execute(query)

    books = cur.fetchall()

    return {"books": books}

# -----------------------------
# GET BOOK BY ID
# -----------------------------
@app.get("/books/{book_id}")
def get_book(book_id: int):

    query = "SELECT * FROM books WHERE id = %s"

    cur.execute(query, (book_id,))

    book = cur.fetchone()

    return {"book": book}

# -----------------------------
# UPDATE BOOK
# -----------------------------
@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):

    query = """
    UPDATE books
    SET title = %s,
        author = %s,
        published_year = %s
    WHERE id = %s
    """

    cur.execute(
        query,
        (
            book.title,
            book.author,
            book.published_year,
            book_id
        )
    )

    conn.commit()

    return {"message": "Book updated successfully"}

# -----------------------------
# DELETE BOOK
# -----------------------------
@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    query = "DELETE FROM books WHERE id = %s"

    cur.execute(query, (book_id,))

    conn.commit()

    return {"message": "Book deleted successfully"}
