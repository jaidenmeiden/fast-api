from fastapi import FastAPI, Body
from models.person import Person

app = FastAPI()


# app.get decorator
@app.get("/")
def home():
    return {"Hello": "World"}


"""
The three points (...) into Body class (Class from fastapi), where it 
send the person information, means that is mandatory
"""

# Request and response body
@app.post("/persons/new")
async def create_person(person: Person = Body(...)):
    return person
