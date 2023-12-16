INSERT INTO menu(id, name_dish, descript, prise, time_cooking) VALUES (1, 'Кисель', 'Студенистое блюдо, в качестве загущающего вещества в котором используется крахмал (крупяной, мучной, картофельный, кукурузный)', 50, '5 мин');
INSERT INTO menu(id, name_dish, descript, prise, time_cooking) VALUES (2, 'Компот', 'Десертный напиток из фруктов или ягод, либо отвар фруктов в сиропе, а также смесь сухофруктов или сушёных ягод и фруктов, либо фруктовые или ягодные консервы.', 50, '5 мин');
INSERT INTO menu(id, name_dish, descript, prise, time_cooking) VALUES (3, 'Пюре с катлетами', 'Традиционное блюдо артековского рациона', 200, '20 мин');
INSERT INTO menu(id, name_dish, descript, prise, time_cooking) VALUES (4, 'Макороны с катлетами', 'Простое и очень вкусное блюдо', 200, '20 мин');
INSERT INTO menu(id, name_dish, descript, prise, time_cooking) VALUES (5, 'Борщ', 'Горячий заправочный суп на основе свёклы, которая придаёт ему характерный красный цвет', 220, '30 мин');
INSERT INTO menu(id, name_dish, descript, prise, time_cooking) VALUES (6, 'Грибной суп', 'Грибной суп — это вкусное и совсем не скучное первое блюдо, которое хочется есть в любую погоду', 220, '30 мин');

INSERT INTO users(id, fio, phone, email, pass, passport_info, inn, status_user)) VALUES (1, 'Аксенов Елисей Эдуардович', '89044322288', 'aksenow@gmail.com', 'staf1', 1818304752, 130273957463, 'Продавец');
INSERT INTO users(id, fio, phone, email, pass, passport_info, inn, status_user)) VALUES (2, 'Ивлев Алексей Нурланович', '89040487335', 'ivleev@gmail.com', 'staf2', 1818330426, 130302857483, 'Продавец');
INSERT INTO users(id, fio, phone, email, pass, passport_info, inn, status_user)) VALUES (3, 'Димитров Витя Сергеевич', '89035489835', 'vita228@gmail.com', 'user1', 1, 1, 'Покупатель');
INSERT INTO users(id, fio, phone, email, pass, passport_info, inn, status_user)) VALUES (4, 'Анничкин Алеша Даниилович', '89035830535', 'alosha8@gmail.com', 'user2', 1, 1, 'Покупатель');
INSERT INTO users(id, fio, phone, email, pass, passport_info, inn, status_user)) VALUES (5, 'Королев Сергей Кирилов', '89030398435', 'Sergo@gmail.com', 'user3', 1, 1, 'Покупатель');

INSERT INTO order_status(id, name_status) VALUES (1, 'На обработке');
INSERT INTO order_status(id, name_status) VALUES (2, 'Готовится');
INSERT INTO order_status(id, name_status) VALUES (3, 'Готов к выдаче');

INSERT INTO order_status(id, name_status) VALUES (1, 'Покупатель');
INSERT INTO order_status(id, name_status) VALUES (2, 'Продавец')
