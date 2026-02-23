from fastapi import FastAPI, HTTPException

from model_val import Employee
# from models import Employee

from typing import List
employee_db: List[Employee] = []

app= FastAPI()

# read all employees

@app.get('/employees', response_model=List[Employee])
def get_employees():
    return employee_db

# read employee by id

@app.get('/employees/{employee_id}', response_model=Employee)
def get_employee(employee_id: int):
    for index, employee in enumerate(employee_db):
        if employee.id == employee_id:
            return employee_db[index]
    raise HTTPException(status_code=404, details=f"Employee with id {employee_id} not found")
# add an employee to the database

@app.post('/employees', response_model=Employee)
def add_employee(new_emp: Employee):
    for employee in employee_db:
        if employee.id == new_emp.id:
            raise HTTPException(status_code=400, detail=f"Employee with id {new_emp.id} already exists")
    employee_db.append(new_emp)
    return new_emp

# update employee

@app.put('/employees/{employee_id}', response_model=Employee)
def update_employee(employee_id: int, updated_emp: Employee):
    for index, empployee in enumerate(employee_db):
        if empployee.id== employee_id:
            employee_db[index] = updated_emp
            return employee_db[index]
        raise HTTPException(status_code=404, details=f"Employee with id {employee_id} not found")
    
    # delete employee
# @app.delete('/employees/{employee_id}')
# def delete_employee(employee_id: int):
#     global employee_db
#     for index, emp in enumerate(employee_db):
#         if emp.id == employee_id:
#             employee_db.pop[index]
#             return {"message": f"Employee with id {employee_id} deleted successfully"}
#     raise HTTPException(status_code=404, details=f"Employee with id {employee_id} not found")

@app.delete('/employees/{employee_id}')
def delete_employee(employee_id: int):
    global employee_db
    for index, emp in enumerate(employee_db):
        if emp.id == employee_id:
            employee_db.pop(index)
            return {"message": f"Employee with id {employee_id} deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Employee with id {employee_id} not found")

# create employee

@app.post('/employees', response_model=Employee)
def create_emmployee(employee: Employee):
    employee_db.append(employee)
    return employee



