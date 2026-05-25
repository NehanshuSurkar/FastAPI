from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Students(BaseModel):
    name: str
    age: int
    city: str

students = list(dict())

@app.post("/students")
def create_student(student: Students):
    std = student.model_dump()
    students.append(std)
    
    return {
        "message": "Student created successfully",
        "student_data": std
    }

@app.get('/students')
def get_studs():
    return students