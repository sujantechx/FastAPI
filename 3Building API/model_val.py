from pydantic import BaseModel, Field
from typing import Optional 
from pydantic import EmailStr


class Employee(BaseModel):
    id:int = Field(..., get=0, title="Employee ID", description="Unique identifier for the employee")
    name:str = Field(..., title= "Employee Name", description="Full name of the employee")
    # email:str = Field(..., 
    # pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9]{2,}$",
    # title="Employee Email", 
    # description="Email address of the employee")
    email:EmailStr = Field(..., title="Employee Email", description="Email address of the employee")
    department:str = Field(..., title="Employee Department", description="Department where the employee works")
    age:Optional[int] = Field(None, title="Employee Age", description="Age of the employee")