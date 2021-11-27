# Python
from tkinter.scrolledtext import example
from typing import Optional
# fastAPI
from fastapi import FastAPI, Body, Path, Query
# Own classes
from models import person
from models.location import Location
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
        person_id: str = Query(
            ...,
            title="The ID of the person",
            description="This is the ID of the person. It's a value that start with one",
            example="21"
        ),  # This is an example (A Query parameter never is mandatory)
        first_name: Optional[str] = Query(
            None,
            min_length=1,
            max_length=50,
            title="Person first name",
            description="This is the person first name. It's between 1 and 50 characters",
            example="Daniela"
        ),
        age: Optional[str] = Query(
            None,
            min_length=1,
            max_length=50,
            title="Person age",
            description="This is the person age. It's a value greater than zero",
            example=13
        ),
):
    return {person_id, first_name, age}


# Path Parameters and Numeric Validations
@app.get("/persons/detail/{person_id}")
async def show_person(
        person_id: int = Path(
            ...,
            gt=0,
            title="The ID of the person to get",
            description="This is the ID of the person. It's a value that start with one",
            example="21"
        )
):
    return {person_id: "It exists!"}


# Validations: Request body
@app.put("/persons/{person_id}")
async def update_person(
        person_id: int = Path(
            ...,
            gt=0,
            title="The ID of the person to get",
            description="This is the ID of the person. It's a value that start with one",
            example="21"
        ),
        person: Person = Body(...),
        location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return {person_id: results}


@app.put("/persons/example/{person_id}")
async def update_person(
        person_id: int = Path(
            ...,
            gt=0,
            title="The ID of the person to get",
            description="This is the ID of the person. It's a value that start with one",
            example="21"
        ),
        person: Person = Body(...)
):
    return {person_id: person}
