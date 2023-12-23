from typing import List
from fastapi import APIRouter
from .models import Order
from .resolvers import get_all_orders, update_status_order, add_new_order, delete_order

router = APIRouter()


@router.get('/')
def get_orders() -> List[Order]:
    return get_all_orders()


@router.post('/')
def add_order_new(new_order: Order):
    return add_new_order(new_order)


@router.get('/')
def add_group(id, status_dish):
    return update_status_order(id, status_dish)
#
#
@router.put('/{group_id}')
def order_delete(id: int):
    return delete_order(id)
