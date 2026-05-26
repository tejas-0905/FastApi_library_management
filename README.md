# 📚 Library Management System using FastAPI & PostgreSQL

A backend-only Library Management System built using FastAPI and PostgreSQL that performs CRUD operations on books.

---

# 🚀 Features

- Add a new book
- View all books
- View a single book by ID
- Update book details
- Delete a book
- PostgreSQL database integration
- Interactive Swagger UI documentation

---

# 🛠️ Tech Stack

- Python
- FastAPI
- PostgreSQL
- Psycopg
- Uvicorn
- Pydantic

---

# 📁 Project Structure

```bash
library_project/
│
├── app.py
├── README.md
└── venv/
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <your-repository-url>
cd library_project
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install fastapi uvicorn psycopg pydantic
```

---

# 🗄️ PostgreSQL Setup

## Create Database

```sql
CREATE DATABASE library_db;
```

---

## Create Table

```sql
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    published_year INT
);
```

---

# 🔗 Database Connection

Update PostgreSQL credentials inside `app.py`

```python
conn = psycopg.connect(
    host="localhost",
    dbname="library_db",
    user="postgres",
    password="your_password",
    port="5432"
)
```

---

# 📄 app.py

```python
from fastapi import FastAPI
from pydantic import BaseModel
import psycopg

app = FastAPI()

# PostgreSQL Connection
conn = psycopg.connect(
    host="localhost",
    dbname="library_db",
    user="postgres",
    password="your_password",
    port="5432"
)

cur = conn.cursor()

# Pydantic Model
class Book(BaseModel):
    title: str
    author: str
    published_year: int

# Home Route
@app.get("/")
def home():
    return {"message": "Library Management System"}

# Add Book
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

# Get All Books
@app.get("/books")
def get_books():

    query = "SELECT * FROM books"

    cur.execute(query)

    books = cur.fetchall()

    return {"books": books}

# Get Book By ID
@app.get("/books/{book_id}")
def get_book(book_id: int):

    query = "SELECT * FROM books WHERE id = %s"

    cur.execute(query, (book_id,))

    book = cur.fetchone()

    return {"book": book}

# Update Book
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

# Delete Book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    query = "DELETE FROM books WHERE id = %s"

    cur.execute(query, (book_id,))

    conn.commit()

    return {"message": "Book deleted successfully"}
```

---

# ▶️ Run the Project

```bash
python -m uvicorn app:app --reload
```

---

# 🌐 API Documentation

Open Swagger UI:

```bash
http://127.0.0.1:8000/docs
```

---

# 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home Route |
| POST | `/books` | Add Book |
| GET | `/books` | Get All Books |
| GET | `/books/{id}` | Get Book By ID |
| PUT | `/books/{id}` | Update Book |
| DELETE | `/books/{id}` | Delete Book |

---

# 🧪 Example JSON Input

```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "published_year": 2018
}
```

---

# ✅ Sample Response

```json
{
  "message": "Book added successfully"
}
```

---

# 🔮 Future Improvements

- Authentication & Authorization
- SQLAlchemy ORM Integration
- Search Functionality
- Docker Deployment
- Pagination
- Frontend Integration

---

# 👨‍💻 Author

Tejas J
