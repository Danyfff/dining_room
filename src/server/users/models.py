from pydantic import BaseModel
# from typing import Optional


class InputUsers(BaseModel):
    name: str


class OutputUsers(BaseModel):
    id: int
    name: str
