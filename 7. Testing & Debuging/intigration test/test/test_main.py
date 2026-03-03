from fastapi.testclient import TestClient

from app.main import app

clint=TestClient(app)


def test_eligibility_pass():
    payload= {
        'income':60000,
        'age':23,
        'employment':'employed'
    }
    response=clint.post('/loan_eligibility', json=payload)
    
    assert response.status_code==200
    assert response.json() =={'eligible':True}
    
    
    
def test_eligibility_fail():
    payload={
        'income':30000,
        'age':20,
        'employment':'unemloyed'
    }
    
    
    response=clint.post('/loan_eligibility',json=payload)
    assert response.status_code==200
    assert response.json() == {'eligible':False}