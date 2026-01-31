from typing import Literal
from pydantic import BaseModel, Field
from sqlalchemy import Column, String, Float
from database import Base

class ScoreInput(BaseModel):
    student_id: str = Field(..., description="Student ID", examples=["001"])
    name: str = Field(..., description="Name", examples=["John"])
    subject: Literal["Math", "Science", "Thai", "English", "Social"] = Field(..., description="Subject choice", examples=["Math"])
    score: float = Field(..., ge=0, le=100, description="Numerical score (0-100)", examples=[65])

class GradeOutput(BaseModel):
    grade: str = Field(..., description="Letter grade (e.g., A, B, C)", examples=["B+"])
    comment: str = Field(..., description="Comment", examples=["Good"])

class GradeRecordSQLAlchemy(Base):
    __tablename__ = "grade_records"

    student_id = Column(String, primary_key=True, index=True) # this is column in database (primary key)
    name = Column(String) # this is column in database
    subject = Column(String)
    grade = Column(String)
    score = Column(Float)