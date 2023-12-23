from pydantic import BaseModel
from typing import Optional


class Dish(BaseModel):
    id: Optional[int] = None
    name_dish: Optional[str] = None
    descript: Optional[str] = None
    prise: Optional[int] = None
    time_cooking: Optional[str] = None


class DishID(BaseModel):
    code: int
    id: int
