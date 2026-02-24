import database,models, schemas, crud
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session 
from database import SessionLocal, engine, Base
from typing import List

Base.metadata.create_all(bind=engine) # this line creates the database tables based on the models defined in the models.py file. It uses the metadata from the Base class to create the tables in the database.

app= FastAPI()

# Dependency with the DB

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
# API Endpoints

#1 Create Employee
@app.post("/employees", response_model=schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: Session= Depends(get_db)):
    return crud.create_employee(db, employee)

#2 Get All Employees
@app.get("/employees", response_model=List[schemas.EmployeeOut])
def get_employees(db: Session= Depends(get_db)):
    return crud.get_employee(db)

#3 Get Employee by ID

@app.get("/employees/{emp_id}", response_model=schemas.EmployeeOut)
def get_emplyee_by_d(emp_id: int, db: Session= Depends(get_db)):
    db_employee= crud.get_employee_by_id(db, emp_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee
#4 Update Employee
@app.put("/employees/{emp_id}", response_model=schemas.EmployeeOut)
def update_employee(emp_id: int, employee: schemas.EmployeeUpdate, db: Session=Depends(get_db)):
    db_employee= crud.update_employee(db,emp_id,employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee
#5 Delete Employee
@app.delete("/emmployees/{emp_id}",response_model=schemas.EmployeeOut)
def delete_employee(emp_id:int, db: Session= Depends(get_db)):
    db_employee=crud.delete_employee(db,emp_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee