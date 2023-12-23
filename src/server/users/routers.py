from typing import List
from fastapi import APIRouter
from .models import User, UserId
from .resolvers import get_all_users, add_new_user, delete_user, check_user

router = APIRouter()


@router.get('/check')
def check_exists_user(user: User) -> User:
    return check_user(user)


@router.get('/')
def get_users() -> List[User]:
    return get_all_users()


@router.post('/')
def add_user(new_user: User) -> UserId:
    return add_new_user(new_user)


@router.get("/{user_id}")
def delete_corency_user(user_id: int) -> UserId:
    return delete_user(user_id)
