from fastapi import FastAPI

app = FastAPI()

students = []

@app.get("/")
def home():
    return {"message": "Student API"}

@app.post("/add/{name}/{age}")
def add_student(name: str, age: int):
    student = {"name": name, "age": age}
    students.append(student)
    return {"student": student}

@app.get("/students")
def get_students():
    return students