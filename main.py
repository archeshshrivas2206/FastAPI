from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return "First time properly running a backend server "\
    
greet()