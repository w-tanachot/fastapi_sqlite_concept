# FastAPI Grade Calculator (fastapi_sqlite_model)

A FastAPI application to calculate grades from numerical scores and persist student records in a SQLite database using SQLAlchemy.

## Features

- **Grade Conversion**: Converts numerical scores (0-100) to letter grades (A, B+, B, etc.).
- **Persistence**: Saves student records (ID, Name, Subject, Grade, Score) to a SQLite database.
- **Upsert Logic**: Automatically updates existing records if the same `student_id` is used.
- **Analytics**: Calculate the average score of all students in the database.
- **Management**: List all records or delete specific records by Student ID.

## Requirements

- Python 3.8+
- FastAPI
- SQLAlchemy
- Uvicorn
- Pydantic

## Installation

1. Clone the repository.
2. Create and activate the Conda environment:
   ```bash
   conda create -n python_course python=3.12
   conda activate python_course
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the API

Run the server with:

```bash
python main.py
```

The API will be available at `http://127.0.0.1:8000`.
Interactive API documentation (Swagger UI): `http://127.0.0.1:8000/docs`.

## API Endpoints

### 1. `POST /check_grade`
Calculates the grade and saves/updates the record in the database.
**Request Body:**
```json
{
  "student_id": "001",
  "name": "John Doe",
  "subject": "Math",
  "score": 85
}
```

### 2. `GET /grades`
Retrieve all stored grade records.

### 3. `GET /average_score`
Retrieve the average score of all students.

### 4. `DELETE /grades/{student_id}`
Delete a student record by ID.

## Project Structure

- `main.py`: Entry point and API endpoints.
- `models.py`: Pydantic schemas and SQLAlchemy models.
- `database.py`: Database connection and session management.
- `utilities.py`: Logic for grade conversion and comments.
