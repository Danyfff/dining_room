from .models import Order, NewId
from src.server.database.db_manager import base_manager


# Вывод всех заказов
def get_all_orders():
    res = base_manager.execute("SELECT id, name_dish, comment, creat_time, issue_time, user_name, staff_name "
                               "FROM orders ", many=True)
    orders = []
    print(res)
    for order in res['data']:
        orders.append(Order(id=order[0], name_dish=order[1], comment=order[2], creat_time=order[3], issue_time=order[4], user_name=order[5], staff_name=order[6]))
    return orders


# Создание нового заказа
def add_new_order(new_order: Order):
    res = base_manager.execute("INSERT INTO orders(name_dish, comment, creat_time, issue_time, user_name, staff_name) "
                               "VALUES (?, ?, ?, ?, ?, ?) "
                               "RETURNING id", args=(new_order.name_dish, new_order.comment, new_order.creat_time, new_order.issue_time, new_order.user_name, new_order.staff_name,))
    return NewId(code=res['code'], id=res['data'][0][0])


# Обновление статуса заказа
def update_status_order(id: int, status_dish: str):
    res = base_manager.execute("UPDATE orders SET status_dish = ?"
                               "WHERE id = ?", args=(status_dish, ))
    return NewId(code=res['code'], id=id)


# Обновление статуса заказа
def delete_order(id: int):
    res = base_manager.execute("DELETE FROM orders WHERE id = ?",
                               args=(id, ))
    return NewId(code=res['code'], id=id)
