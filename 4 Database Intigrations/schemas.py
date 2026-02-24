from typing import Optional
from pydantic import BaseModel, EmailStr
class EmployeeBase(BaseModel):
    name:str
    email:EmailStr
    department:str
    
class EmployeeCreate(EmployeeBase):
    department: Optional[str] = None
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id:int
    # this class is used to define the output schema for the employee model, it includes the id field which is not required when creating or updating an employee but is included in the output when retrieving employee data from the database.
    class Config:
        orm_mode=True
    