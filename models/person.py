# Python
from typing import Optional
# Pydantic
from pydantic import BaseModel


class Person(BaseModel):
    first_name: str
    last_name: str
    hair_color: Optional[str] = None
    biography: Optional[str] = None
    is_married: Optional[bool] = None
    age: int
    height: float
    weight: Optional[float] = None
