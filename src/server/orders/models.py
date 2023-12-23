from pydantic import BaseModel
from typing import Optional


class Order(BaseModel):
    id: Optional[int]
    comment: Optional[str] = None
    creat_time: Optional[str] = None
    issue_time: Optional[str] = None
    user_name: Optional[str] = None
    staff_name: Optional[str] = None
    name_dish: Optional[str] = None
    status_dish: Optional[str] = None


class NewId(BaseModel):
    code: int
    id: int
