from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str
    
app = FastAPI()

@app.get('/user', response_model=User)
def get_user():
    return User(name="John", age=30, email="john@example.com")