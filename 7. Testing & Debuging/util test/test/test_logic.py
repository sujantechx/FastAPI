import pytest 
from app.logic import is_eligible_for_loan


def test_eligible_user():
    assert is_eligible_for_loan ( 60000,25,'employed')== True
    

def test_under_age():
    assert is_eligible_for_loan(60000, 10,'employed')== False
    
def test_low_incom():
    assert is_eligible_for_loan(40000,34,'employed') == False
    
def test_unemployed_user():
    assert is_eligible_for_loan (6666665,34,'unemploed')== False 
    
    
def test_boundery_case():
    assert is_eligible_for_loan(50000,21,'employed')== True