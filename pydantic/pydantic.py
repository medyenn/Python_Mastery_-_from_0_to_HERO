from pydantic import BaseModel, validator
# from typing import Emailstr, TYPE_CHECKING


class Space_Station(BaseModel):
    name: str
    age: int
    height: float

    @classmethod
    @validator('name')
    def name_valid(cls, name):
        if name == 'john':
            return 'Meow'


first = Space_Station(name='john', age='22', height=1.65)
print(first.model_dump_json())
print(first.model_dump())
print(first)
