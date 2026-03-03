from fastapi import FastAPI 
from pydantic import BaseModel

from app.logic import is_eligible_for_loan


app = FastAPI()


class Application(BaseModel):
    income:float
    age:int
    employement_status:str
    
    
    
@app.post('/loan_eligibility')
def check_eligibility(application:Application):
    eligibility= is_eligible_for_loan(
        incom=application.income,
        age= application.age,
        employment_status=application.employement_status
    )
    
    return {'eligible':eligibility}