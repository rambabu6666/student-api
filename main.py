from fastapi import FastAPI
from sqlalchemy import create_engine,text
from sqlalchemy.orm import Session, sessionmaker
from database import Sessionlocal, engine
from models import Base, Student,Emp
from fastapi import Depends
Base.metadata.create_all(bind=engine)
dburl='postgress'
app=FastAPI()
# DataValidation
from pydantic import BaseModel
class StudValidation(BaseModel):
    name:str
    age:int

class EmpCreate(BaseModel):
    name: str
    dept: str
    sal: int
@app.post("/addEmps")
def addEmployees(emp_list: list[EmpCreate]):
    
    for emp in emp_list:
        empObj = Emp(name=emp.name, dept=emp.dept, sal=emp.sal)
        db.add(empObj)
    db.commit()
    return {"message": "Employees added"}    

db=Sessionlocal()
@app.post('/addStudJson')
def addStud(stud:StudValidation):
    std=Student(name=stud.name,age=stud.age)
    db.add(std)
    db.commit()
    return 'Student Added Successfully'
@app.post('/addEmpplyee')
def addEmp(emp:EmpCreate):
    empObj=Emp(name=emp.name,dept=emp.dept,sal=emp.sal)
    db.add(empObj)
    db.commit()
    return"Added Successfully"
# Readds
@app.get('/allEmp')
def getEmps():
    emps=db.query(Emp).all()
    return emps

@app.get('/hello')
def getmsg():
    return {'message':'hello welcome'}
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
@app.get('/getAll')
def getAll():
    return db.query(Student).all()
@app.delete('/deleteObj')
def removeObj(id:int):
    student=db.query(Student).filter(Student.id==id).first()
    if student is None:
        return {"Message":"Object Not Found"}
    db.delete(student)
    db.execute(text("truncate table students restart identity"))
    db.commit()
    return {student.name:'Object Deleted Successfully'}

@app.post('/addObj')
def addstud(name,age):
    student=Student(name=name,age=age)
    db.add(student)
    db.commit()
    return 'Added'      
@app.get('/addStud/{name}/{age}')
def addStud(name,age:int,db:Session=Depends(get_db)):
    student=Student(name=name,age=age)
    db.add(student)
    db.commit()
    return {'msg':'added'}
    
emp={}
#READ
@app.get('/all')
def emps():
    return emp
# ADD
@app.post('/add/{id}/{name}')
def addEmp(id:int,name):
    emp[id]=name



@app.get('/')
def getMsg():
    return 'Hello Welcome to FastApi'
# DELETE
@app.delete('/delete/{id}')
def removeEmp(id:int):
    emp.pop(id)   
# Login
user={
    'rambabu':"3006",
    'vinay':"9999"
}
@app.get('/login/{username}/{password}')
def login(username,password):
    if username in user and user[username]==password:
        return {'message':'Login sucessFull'}
    else:
        return {'Message':'Invalid Credentials'}

    
    




