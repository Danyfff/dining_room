from .models import User, UserId
from src.server.database.db_manager import base_manager


# Для проверки пароля и телефона получения статуса
def check_user(login: User) -> User:
    res = base_manager.execute("SELECT id, stat_user "
                               "FROM users "
                               "WHERE password = ? AND phone = ? ", args=(login.password, login.phone, ), many=False)
    print(res)
    if res['data']:
        return User(id=res['data'][0][0], stat_user=res['data'][1])
    else:
        return User(id=0, stat_user=None)


# Все пользователи по статусу
def get_all_users():
    res = base_manager.execute("SELECT id, fio, phone, email, stat_user "
                               "FROM users ", many=True)
    users = []
    for user in res['data']:
        users.append(User(id=user[0], fio=user[1], phone=user[2], email=user[3], stat_user=user[4]))
    return users


# Все пользователи по статусу
def add_new_user(new_user: User):
    res = base_manager.execute("INSERT INTO users(fio, password, phone, email, stat_user) "
                               "VALUES (?, ?, ?, ?, ? ) "
                               "RETURNING id", args=(new_user.fio, new_user.password, new_user.phone, new_user.email, new_user.stat_user, ))
    return UserId(code=res['code'], id=res['data'][0][0])


# Удаление поьзователя
def delete_user(user_id: int):
    res = base_manager.execute("DELETE FROM users WHERE id = ? ",
                               args=(user_id, ))
    return UserId(code=res['code'], id=user_id)
