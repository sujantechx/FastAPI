from fastapi import FastAPI

app=FastAPI()

# @app.get("/")
@app.get("/")
def root():
    return {"message": "Hello, World"}

# uvicorn main:app --reload  this are the command to run the server and --reload is used to automatically reload the server when we make changes to the code.