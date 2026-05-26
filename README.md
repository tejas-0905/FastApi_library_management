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
