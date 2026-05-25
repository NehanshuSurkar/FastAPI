from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str 
    age: int
    city: str


@app.put("/students/{student_id}")
def student_data(Student_id: int, student: Student):
    return {"message": "Data updated successfully",
            "student_id": Student_id,
            "updated data": student  
            }

