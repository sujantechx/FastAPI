

def is_eligible_for_loan(incom:float,age:int, employment_status:str) ->bool:
    return (incom >= 50000) and (age>=21) and ( employment_status == 'employed')

