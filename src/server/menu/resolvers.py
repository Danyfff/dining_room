from .models import Dish, DishID
from src.server.database.db_manager import base_manager


# Вывести все блюда
def get_all_dishes():
    res = base_manager.execute("SELECT id, name_dish, descript, prise, time_cooking "
                               "FROM menu ", many=True)
    groups = []
    for group in res['data']:
        groups.append(Dish(id=group[0], name_dish=group[1], descript=group[2], prise=group[3], time_cooking=group[4]))
    return groups


# Вывести одно блюдо
def get_dish(dish_id: int):
    res = base_manager.execute("SELECT id, name_dish, descript, prise, time_cooking "
                               "FROM menu "
                               "WHERE id = ?",
                               args=(dish_id,), many=False)
    print(res)
    return Dish(id=res[0], name_dish=res[1], descript=res[2], prise=res[3], time_cooking=res[4])


# Добавить новое блюдо
def add_new_dish(new_dish: Dish):
    res = base_manager.execute("INSERT INTO menu(name_dish, descript, prise, time_cooking) "
                               "VALUES (?, ?, ?, ?) "
                               "RETURNING id", args=(new_dish.name_dish, new_dish.descript, new_dish.prise, new_dish.time_cooking, ))
    print(res)
    return DishID(code=res['code'], id=res['data'][0][0])


# Обновить блюдо
def update_dish(dish_id: int, dish: Dish):
    res = base_manager.execute("UPDATE menu SET name_dish = ? WHERE id = ?",
                               args=(dish.name_dish, dish_id,))
    return DishID(code=res['code'], id=dish_id)


# Удалить блюдо
def delete_dish(dish_id: int):
    res = base_manager.execute("DELETE FROM menu WHERE id = ?",
                               args=(dish_id,))
    return DishID(code=res['code'], id=dish_id)
