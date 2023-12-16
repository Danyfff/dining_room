from fastapi import APIRouter
from typing import List
from .models import InputUsers, OutputUsers

router = APIRouter()


@router.get('/')
def get_users() -> List[OutputUsers]:
    return ({'id': 1, 'name': 'Даничка'},
            {'id': 2, 'name': 'Сереженька'})

@router.get('/')
def get_user() -> OutputUsers:
    return {'id': 1, 'name': 'Даничка'}

