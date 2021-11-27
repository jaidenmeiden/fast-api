# Python
from tkinter.scrolledtext import example
from typing import Optional
from enum import Enum
# Pydantic
from pydantic import BaseModel, Field


class HairColor(Enum):  # Example not working with this
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"


class PersonBase(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Adriana"  # Example values
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    hair_color: Optional[HairColor] = Field(default=None)  # Example not working with this
    biography: Optional[str] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)
    age: int = Field(
        ...,
        gt=0,
        le=115,
        example="37"  # Example values
    )
    height: float = Field(
        ...,
        gt=0,
        le=300
    )
    weight: Optional[float] = None


class Person(PersonBase):
    password: str = Field(..., min_length=8)

    # Example values
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "first_name": "Jaiden",
    #             "last_name": "Riaño Leiva",
    #             "hair_color": "black",
    #             "biography": "Machine Learning developer",
    #             "is_married": False,
    #             "age": 40,
    #             "height": 185,
    #             "weight": 95
    #         }
    #     }


class PersonOut(PersonBase):
    pass
