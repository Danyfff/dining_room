from fastapi import APIRouter
from typing import List
from .models import User, InputUser, NewId
from .resolvers import get_users, add_new_user, delete_current_user, check_user

router = APIRouter()



@router.get('/check')
def check_exists_user(user: InputUser) -> User:
    return check_user(user)


@router.get('/')
def get_group() -> List[User]:
    return get_users()


@router.post('/')
def add_group(new_user: InputUser) -> NewId:
    return add_new_user(new_user)


@router.delete("/{user_id}")
def delete_group(user_id: int) -> NewId:
    return delete_current_user(user_id)

