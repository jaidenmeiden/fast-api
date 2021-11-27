# Python
from typing import Optional
from enum import Enum
# Pydantic
from pydantic import BaseModel, Field


class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"


class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    hair_color: Optional[HairColor] = Field(default=None)
    biography: Optional[str] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)
    age: int = Field(
        ...,
        gt=0,
        le=115
    )
    height: float = Field(
        ...,
        gt=0,
        le=300
    )
    weight: Optional[float] = None
