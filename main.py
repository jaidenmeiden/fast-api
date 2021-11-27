# Python
from typing import Optional
# fastAPI
from fastapi import FastAPI, Body, Query
# Own classes
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


# Validations query parameters
@app.get("/persons/detail")
async def show_person(
        id_person: str = Query(...),  # This is an example (A Query parameter never is mandatory)
        first_name: Optional[str] = Query(None, min_length=1, max_length=50),
        age: Optional[str] = Query(None, min_length=1, max_length=50),
):
    return {id_person, first_name, age}
