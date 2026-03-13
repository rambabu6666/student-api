from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas
# changed in local servr
# create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Home API
@app.get("/")
def home():
    return {"message": "Employee API Running"}


# Create Employee
@app.post("/employees/")
def create_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    new_emp = models.Employee(name=emp.name, age=emp.age, department=emp.department)
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp


# Get all Employees
@app.get("/employees/")
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(models.Employee).all()
    return employees


# Get employee by ID
@app.get("/employees/{emp_id}")
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    return employee


# Update employee
@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()

    employee.name = emp.name
    employee.age = emp.age
    employee.department = emp.department

    db.commit()
    return employee


# Delete employee
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()

    db.delete(employee)
    db.commit()

    return {"message": "Employee deleted"}
