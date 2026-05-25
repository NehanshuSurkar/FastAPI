from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# GET
@app.get("/")
def home():

    return {
        "message": "Welcome to Digital Academy"
    }


@app.get("/students")
def students():

    return {
        "students": [
            "Rahul",
            "Aman",
            "Shivam"
        ]
    }

@app.get("/courses")
def courses():

    return {
        "courses": [
            "Python",
            "Java",
            "Flutter"
        ]
    }

@app.get("/trainers")
def trainers():

    return {
        "trainers": [
            "Mr Sharma",
            "Ms Priya"
        ]
    }


# POST

class Student(BaseModel):
    
    name: str
    age: int
    city: str
    email: str

class Course(BaseModel):
    course_name: str
    price: int    

class Trainer(BaseModel):
    name: str
    experience: int
    specialization: str    

@app.post("/students/register")
def register_student(student: Student):

    return {
        "message": "Student Registered",
        "data": student
    }  

@app.post("/courses/create")
def create_course(course: Course):

    return {
        "message": "Course Created",
        "course": course
    }

@app.post("/trainers/create")
def create_trainer(trainer: Trainer):

    return {
        "message": "Trainer Created",
        "trainer": trainer
    }

# PART 3 — QUERY PARAMETERS
@app.get("/students/search")
def search_students(city: str = "Nagpur"):

    return {
        "city": city
    }

@app.get("/courses/filter")
def filter_courses(price: int = 0):

    return {
        "price": price
    }

@app.get("/trainers/search")
def search_trainers(experience: int):

    return {
        "experience": experience
    }

# PART 4 — PATH PARAMETERS

@app.get("/students/{student_id}")
def get_student(student_id: int):

    return {
        "student_id": student_id
    }

@app.get("/courses/{course_id}")
def get_course(course_id: int):

    return {
        "course_id": course_id
    }

@app.get("/trainers/{trainer_id}")
def get_trainer(trainer_id: int):

    return {
        "trainer_id": trainer_id
    }

# PHASE 5 — PUT APIs

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    return {
        "message": "Student Updated",
        "student_id": student_id,
        "updated_data": student
    }

@app.put("/courses/{course_id}")
def update_course(course_id: int, course: Course):

    return {
        "message": "Course Updated",
        "course_id": course_id,
        "updated_course": course
    }

@app.put("/trainers/{trainer_id}")
def update_trainer(trainer_id: int, trainer: Trainer):

    return {
        "message": "Trainer Updated",
        "trainer_id": trainer_id,
        "updated_trainer": trainer
    }