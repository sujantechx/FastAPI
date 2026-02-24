from sqlalchemy import Column,  Integer, String
from database import Base # importing the Base class from database.py

class Employee(Base):
    __tablename__="employeed" # name of the table in the database
    
    id=Column(Integer, primary_key= True, index=True) # primary key and indexed column
    name=Column(String, index=True) # name column of type String and indexed
    email=Column(String, unique=True, index=True) # email column of type String, unique and indexed
    department=Column(String,index=True) # department column of type String and indexed
    