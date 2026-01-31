from fastapi import FastAPI, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from models import ScoreInput, GradeOutput, GradeRecordSQLAlchemy
from utilities import convert_score_to_grade, convert_grade_to_comment
from database import engine, Base, get_db
import uvicorn

# --- Create the database tables ---

Base.metadata.create_all(bind=engine)

# --- FastAPI App ---

app = FastAPI(
    title="Grade Converter API",
    description="API for converting numerical scores to letter grades and storing them in SQLite.",
    version="1.1.0"
)

@app.get("/health")
async def health():
    return {"status": "ok"}

# --- API Endpoints ---

@app.post("/check_grade", response_model=GradeOutput)
async def check_grade(
    payload: ScoreInput = Body(..., description="Numerical score to convert"),
    db: Session = Depends(get_db)
):
    grade = convert_score_to_grade(payload.score)
    comment = convert_grade_to_comment(payload.student_id, payload.name, payload.subject, grade)
    
    db_record = GradeRecordSQLAlchemy(
        student_id=payload.student_id,
        name=payload.name,
        subject=payload.subject,
        grade=grade,
        score=payload.score
    )
    db.merge(db_record)  # merge handles update if student_id exists
    db.commit()
    
    return GradeOutput(grade=grade, comment=comment)

@app.get("/grades")
async def get_all_grades(db: Session = Depends(get_db)):
    return db.query(GradeRecordSQLAlchemy).all()

@app.get("/average_score")
async def get_average_score(db: Session = Depends(get_db)):
    average = db.query(func.avg(GradeRecordSQLAlchemy.score)).scalar()
    return {"average_score": average if average is not None else 0}

@app.delete("/grades/{student_id}")
async def delete_grade(student_id: str, db: Session = Depends(get_db)):
    deleted_count = db.query(GradeRecordSQLAlchemy).filter(GradeRecordSQLAlchemy.student_id == student_id).delete()
    
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail=f"Student ID {student_id} not found")
        
    db.commit()
    return {"message": f"Grade for student ID {student_id} deleted successfully"}

# --- Run the server ---

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)