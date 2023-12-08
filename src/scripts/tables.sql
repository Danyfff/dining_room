CREATE TABLE menu (
    id INTEGER PRIMARY KEY,
    name_dish VARCHAR(50) NOT NULL,
    descript VARCHAR(50),
    prise INTEGER(10),
    act VARCHAR(50),
    percent_ord VARCHAR(50)
);

CREATE TABLE staff (
    id INTEGER PRIMARY KEY,
    fio VARCHAR(50) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    pass VARCHAR(50),
    col_orders INTEGER(10),
    passport_info INTEGER(10) NOT NULL,
    inn INTEGER(12) NOT NULL
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    phone VARCHAR(18) NOT NULL,
    email VARCHAR(50) NOT NULL,
    pass VARCHAR(50)
);

CREATE TABLE order_status (
    id INTEGER PRIMARY KEY,
    name_status VARCHAR(50)
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    num_order VARCHAR(50) NOT NULL,
    comment VARCHAR(18) NOT NULL,
    creat_time VARCHAR(50),
    issue_time VARCHAR(50),
    FOREIGN KEY(user_name) REFERENCES users(name),
    FOREIGN KEY(staff_name) REFERENCES staff(fio),
    FOREIGN KEY(name_dish) REFERENCES menu(name_dish),
    FOREIGN KEY(status_dish) REFERENCES order_status(name_status)
);

INSERT INTO menu(id, name_dish, descript, prise, act, percent_ord) VALUES (1, 'Кисель', 'Студенистое блюдо, в качестве загущающего вещества в котором используется крахмал (крупяной, мучной, картофельный, кукурузный)', 50, '5 мин', 'Почти не заказывают');
INSERT INTO menu(id, name_dish, descript, prise, act, percent_ord) VALUES (2, 'Компот', 'Десертный напиток из фруктов или ягод, либо отвар фруктов в сиропе, а также смесь сухофруктов или сушёных ягод и фруктов, либо фруктовые или ягодные консервы.', 50, '5 мин', 'Заказывают чаще всего');
INSERT INTO menu(id, name_dish, descript, prise, act, percent_ord) VALUES (3, 'Пюре с катлетами', 'Традиционное блюдо артековского рациона', 200, '20 мин', 'Заказывают чаще всего');
INSERT INTO menu(id, name_dish, descript, prise, act, percent_ord) VALUES (4, 'Макороны с катлетами', 'Простое и очень вкусное блюдо', 200, '20 мин', 'Заказывают часто');
INSERT INTO menu(id, name_dish, descript, prise, act, percent_ord) VALUES (5, 'Борщ', 'Горячий заправочный суп на основе свёклы, которая придаёт ему характерный красный цвет', 220, '30 мин', 'Заказывают часто');
INSERT INTO menu(id, name_dish, descript, prise, act, percent_ord) VALUES (6, 'Грибной суп', 'Грибной суп — это вкусное и совсем не скучное первое блюдо, которое хочется есть в любую погоду', 220, '30 мин', 'Заказывают не часто');

INSERT INTO menu(id, fio, phone, email, pass, col_orders, passport_info, inn) VALUES (1, 'Аксенов Елисей Эдуардович', '89044322288', 'aksenow@gmail.com', 'staf1', 20, 1818304752, 130273957463);
INSERT INTO menu(id, fio, phone, email, pass, col_orders, passport_info, inn) VALUES (2, 'Ивлев Алексей Нурланович', '89040487335', 'ivleev@gmail.com', 'staf2', 49, 1818330426, 130302857483);

INSERT INTO users(id, name, phone, email, pass) VALUES (1, 'Витя', '89035489835', 'vita228@gmail.com', 'user1');
INSERT INTO users(id, name, phone, email, pass) VALUES (2, 'Алеша', '89035830535', 'alosha8@gmail.com', 'user2');
INSERT INTO users(id, name, phone, email, pass) VALUES (3, 'Сергей', '89030398435', 'Sergo@gmail.com', 'user3');

INSERT INTO order_status(id, name_status) VALUES (1, 'На обработке');
INSERT INTO order_status(id, name_status) VALUES (2, 'Готовится');
INSERT INTO order_status(id, name_status) VALUES (3, 'Готов к выдаче');
