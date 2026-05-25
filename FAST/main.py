from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = {}

class Student(BaseModel):

    name: str
    age: int
    city: str

# CREATE
@app.post("/students/{student_id}")
def create_student(student_id: int, student: Student):

    students[student_id] = student

    return {
        "message": "Student created successfully"
    }

# READ
@app.get("/students/{student_id}")
def get_student(student_id: int):

    return students.get(student_id)

# UPDATE
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    students[student_id] = student

    return {
        "message": "Student updated successfully"
    }

# DELETE
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    students.pop(student_id)

    return {
        "message": "Student deleted successfully"
    }
