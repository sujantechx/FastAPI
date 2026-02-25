from pydantic import BaseModel, Field, StrictInt

class InputSchema(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: int=Field(..., ge=0, le=100)
    total_rooms: int=Field(..., ge=0)
    total_bedrooms: int=Field(..., ge=0)
    population: int=Field(..., ge=0)
    households: int= Field(..., ge=0)
    median_income: float=Field(..., ge=0)
    
class OutputSchema(BaseModel):
    predicted_price: float
    
