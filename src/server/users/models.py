from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[int] = None
    fio: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[int] = None
    email: Optional[str] = None
    stat_user: Optional[str] = None


class UserId(BaseModel):
    code: int
    id: int
