from fastapi import FastAPI, Depends

app = FastAPI()

# Dependency functions
def get_db():
    db = {'connections':'mock_db_connection'}
    try:
        yield db
    finally:
        db.close()


#endpoints

@app.get("/")
def home(db= Depends(get_db)):
    return {'db_status': db['connections']}