from typing import List
from fastapi import APIRouter
from .models import Dish, DishID
from .resolvers import get_all_dishes, get_dish, add_new_dish, update_dish, delete_dish

router = APIRouter()


@router.get('/')
def get_groups() -> List[Dish]:
    return get_all_dishes()


@router.get('/{dish_id}')
def get_current_dish(dish_id: int) -> Dish:
    return get_dish(dish_id)


@router.post('/')
def add_dish(new_dish: Dish) -> DishID:
    return add_new_dish(new_dish)


@router.put('/{dish_id}')
def update_current_group(dish_id: int, new_dish: Dish) -> DishID:
    return update_dish(dish_id, new_dish)


@router.delete("/{dish_id}")
def delete_current_dish(dish_id: int) -> DishID:
    return delete_dish(dish_id)
