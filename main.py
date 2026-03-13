from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

students = []

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/add/{name}/{age}")
def add_student(name: str, age: int):
    students.append({"name": name, "age": age})
    return {"message": "Student added", "students": students}


@app.get("/students", response_class=HTMLResponse)
def view_students(request: Request):
    return templates.TemplateResponse("students.html",
                                      {"request": request, "students": students})