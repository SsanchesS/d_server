CREATE TABLE roles(
  id INTEGER PRIMARY KEY,
  role TEXT
);
CREATE TABLE users(
  id INTEGER PRIMARY KEY,
  f_name TEXT,
  s_name TEXT,
  password TEXT,
  email TEXT UNIQUE,
  role_id INTEGER DEFAULT 1,

  FOREIGN KEY (role_id) REFERENCES roles (id)
);
CREATE TABLE sneakers( -- products
  id INTEGER PRIMARY KEY,
  des TEXT,
  price INTEGER,
  img TEXT,
  category_id INTEGER,
  promotion_id INTEGER,
  FOREIGN KEY (category_id) REFERENCES categories (id),
  FOREIGN KEY (promotion_id) REFERENCES promotions (id)
);
CREATE TABLE categories(
  id INTEGER PRIMARY KEY,
  name TEXT,
  des TEXT
);
CREATE TABLE promotions(
  id INTEGER PRIMARY KEY,
  name TEXT,
  des TEXT,
  discount INTEGER
);
CREATE TABLE delivery_methods(
  id INTEGER PRIMARY KEY,
  method_des TEXT
);
CREATE TABLE payment_methods(
  id INTEGER PRIMARY KEY,
  method_des TEXT
);
CREATE TABLE orders(
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  order_date TEXT, -- TIMESTAMP
  sum INTEGER,
  status TEXT,
  delivery_method_id INTEGER, -- способ доставки
  payment_method_id INTEGER, -- способ оплаты
  sneakers TEXT,
  FOREIGN KEY (user_id) REFERENCES users (id),
  FOREIGN KEY (delivery_method_id) REFERENCES delivery_methods (id),
  FOREIGN KEY (payment_method_id) REFERENCES payment_methods (id)
);
INSERT INTO roles (role) VALUES ('user');
INSERT INTO roles (role) VALUES ('admin');
INSERT INTO users (f_name, s_name, email, password, role_id) VALUES ('admin','admin', 'admin@test.ru', 'admin@test.ru', 2);
INSERT INTO users (f_name, s_name, email, password) VALUES ('user','user', 'user@test.ru', 'user@test.ru');

INSERT INTO categories (name, des) VALUES ('ПОВСЕДНЕВНЫЕ КРОССОВКИ','Повседневные кроссовки отличаются почти полным отсутствием специальных технологий. Основными характеристиками модели являются удобство и легкость. Обувь для пеших прогулок изготавливается из натуральных материалов, пропускающих воздух. Популярным покрытием также является мембрана, которая защищает ноги от промокания и ветра. Обычно кроссовки оснащены плоской подошвой из полиуретановой пены.');
INSERT INTO categories (name, des) VALUES ('БЕГОВЫЕ КРОССОВКИ','Кроссовки для бега обладают качественной амортизацией. В зависимости от нагрузки используется эластичный и упругий пеноматериал EVA или более плотный полиуретан. Подошва имеет протекторы для сцепления и разнонаправленные гибкие канавки для защиты от камней и грязи. Аутсоль обычно изготавливается из углеродистой или надувной резины. Первый вариант прочнее, но при этом жестче и тяжелее.');
INSERT INTO categories (name, des) VALUES ('БАСКЕТБОЛЬНЫЕ КРОССОВКИ','Верхняя часть обуви обычно состоит из кожи, парусины или синтетических материалов. Некоторые модели баскетбольных кроссовок оснащены дышащими сетчатыми панелями, усиленными жестким каркасом. Аутсоль имеет глубокий рельефный рисунок для надежного сцепления. Для игры в зале используется мягкая подошва, а на улице — более твердая.');

INSERT INTO sneakers (des, price, img, category_id,promotion_id) VALUES ('Мужские Кроссовки Nike Blazer Mid Suede',12999, './img/1.png', 1,1);
INSERT INTO sneakers (des, price, img, category_id,promotion_id) VALUES ('Женские Кроссовки Nike Air Max 270',12999, './img/2.png', 2,2);
INSERT INTO sneakers (des, price, img, category_id,promotion_id) VALUES ('Мужские Кроссовки Nike Gavaya Mid',8499, './img/3.png', 3,2);
INSERT INTO sneakers (des, price, img, category_id,promotion_id) VALUES ('Мужские Кроссовки Under Armour Curry 8',15199, './img/4.png', 1,1);
INSERT INTO sneakers (des, price, img, category_id,promotion_id) VALUES ('Женские Кроссовки Nike Kyrie 7',11299, './img/5.png', 1,1);
INSERT INTO sneakers (des, price, img, category_id,promotion_id) VALUES ('Мужские Кроссовки Jordan Air Jordan 11',12999, './img/6.png', 2,2);
INSERT INTO sneakers (des, price, img, category_id,promotion_id) VALUES ('Женские Кроссовки Nike Blazer Little Suede',10799, './img/7.png', 1,1);
INSERT INTO sneakers (des, price, img, category_id,promotion_id) VALUES ('Мужские Кроссовки Nike LeBron XVIII',16499, './img/8.png', 3,2);
INSERT INTO sneakers (des, price, img, category_id,promotion_id) VALUES ('Женские Кроссовки Nike Lebron XVIII Low',13999, './img/9.png', 3,2);
INSERT INTO sneakers (des, price, img, category_id,promotion_id) VALUES ('Мужские Кроссовки Nike Glazer Suede',8499, './img/10.png', 2,1);
INSERT INTO sneakers (des, price, img, category_id,promotion_id) VALUES ('Женские Кроссовки Puma X Aka Boku Future Rider',14199, './img/11.png', 1,1);
INSERT INTO sneakers (des, price, img, category_id,promotion_id) VALUES ('Мужские Кроссовки Nike Kyrie Flytrap IV',11399,'./img/12.png', 2,2);

INSERT INTO delivery_methods (method_des) VALUES ('Стандартная доставка');
INSERT INTO delivery_methods (method_des) VALUES ('Самовывоз из магазина');

INSERT INTO payment_methods (method_des) VALUES ('Кредитная карта');
INSERT INTO payment_methods (method_des) VALUES ('Банковский перевод'); 
INSERT INTO payment_methods (method_des) VALUES ('Оплата наличными'); 

INSERT INTO promotions (name, des, discount) VALUES ('Скидка 500р','Действует до 12-07-24', 500);
INSERT INTO promotions (name, des, discount) VALUES ('Скидка 2000р','Бессрочно', 2000);

-- tests
INSERT INTO orders (user_id, order_date, sum, status, delivery_method_id, payment_method_id) VALUES (2, '2024-05-07', 13900, 'В обработке', 1, 1);
INSERT INTO orders (user_id, order_date, sum, status, delivery_method_id, payment_method_id,sneakers) VALUES (2, '2024-12-12', 15300, 'В пути',2,2,"[1,5,2]");