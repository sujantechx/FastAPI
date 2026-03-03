from fastapi import FastAPI 
from pydantic import BaseModel

from app.logic import is_eligible_for_loan


app = FastAPI()


class Application(BaseModel):
    income:float
    age:int
    employement_status:str
    
    
    
@app.post('/loan_eligibility')
def check_eligibility(applicant:Application):
   if(applicant.income >= 50000 ) and (applicant.age >=21) and (applicant.employement_status == 'employment'):
       return {'eligible':True}
   else:
       return {'eligible':False}