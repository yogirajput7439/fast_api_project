
from fastapi import FastAPI, Depends, HTTPException
from database import engine, Base, SessionLocal
from models import Student
from schemas import StudentResponse, StudentCreate
from sqlalchemy.orm import Session

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)


# Database dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# Home API
@app.get("/")
def home():
    return {
        "Message": "Student management API is running"
    }


# Add student
@app.post("/students", response_model=StudentResponse)
def add_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    new_student = Student(
        name=student.name,
        email=student.email,
        age=student.age,
        city=student.city
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


# Get all students
@app.get("/students", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):

    students = db.query(Student).all()

    return students


# Get student by ID
@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student

print("Table name:", Student.__tablename__)