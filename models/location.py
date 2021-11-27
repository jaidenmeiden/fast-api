# Python
from typing import Optional
# Pydantic
from pydantic import BaseModel


class Location(BaseModel):
    city: str
    state: str
    country: str
