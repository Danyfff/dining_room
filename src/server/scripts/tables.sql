CREATE TABLE menu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_dish VARCHAR(50) NOT NULL,
    descript VARCHAR(50),
    prise INTEGER(10),
    time_cooking VARCHAR(50)
);

CREATE TABLE status_user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_status VARCHAR(50)
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fio VARCHAR(50) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    passport_info INTEGER(10),
    inn INTEGER(12),
    FOREIGN KEY(stat_user) REFERENCES status_user(name_status)
);

CREATE TABLE order_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_status VARCHAR(50)
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    num_order VARCHAR(50) NOT NULL,
    comment VARCHAR(18) NOT NULL,
    creat_time VARCHAR(50),
    issue_time VARCHAR(50),
    FOREIGN KEY(user_name) REFERENCES users(fio),
    FOREIGN KEY(staff_name) REFERENCES users(fio),
    FOREIGN KEY(name_dish) REFERENCES menu(name_dish),
    FOREIGN KEY(status_dish) REFERENCES order_status(name_status)
);
