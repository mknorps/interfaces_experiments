from typing import Optional

from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: Optional[int]