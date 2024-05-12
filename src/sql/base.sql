CREATE TABLE role(
  id INTEGER PRIMARY KEY,
  role TEXT
);
CREATE TABLE users(
  id INTEGER PRIMARY KEY,
  f_name TEXT,
  s_name TEXT,
  password TEXT,
  email TEXT UNIQUE,
  role_id INTEGER,
  FOREIGN KEY (role_id) REFERENCES role (id)
);
CREATE TABLE products(
  id INTEGER PRIMARY KEY,
  name TEXT,
  description TEXT,
  price INTEGER,
  category_id INTEGER,
  FOREIGN KEY (category_id) REFERENCES categories (id)
);
CREATE TABLE categories(
  id INTEGER PRIMARY KEY,
  name TEXT,
  description TEXT
);
CREATE TABLE promotions(
  id INTEGER PRIMARY KEY,
  name TEXT,
  description TEXT,
  discount INTEGER
);
CREATE TABLE delivery_methods(
  id INTEGER PRIMARY KEY,
  method_description TEXT
);
CREATE TABLE payment_methods(
  id INTEGER PRIMARY KEY,
  method_description TEXT
);
CREATE TABLE orders(
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  order_date DATE, -- TIMESTAMP
  sum INTEGER,
  status TEXT,
  delivery_method_id INTEGER, -- способ доставки
  payment_method_id INTEGER, -- способ оплаты
  FOREIGN KEY (user_id) REFERENCES users (id),
  FOREIGN KEY (delivery_method_id) REFERENCES delivery_methods (id),
  FOREIGN KEY (payment_method_id) REFERENCES payment_methods (id)
);
INSERT INTO role (role) VALUES ('user');
INSERT INTO role (role) VALUES ('admin');
INSERT INTO users (f_name, s_name, email, password, role_id) VALUES ('admin','admin', 'admin@test.ru', 'admin', 1);
INSERT INTO users (f_name, s_name, email, password, role_id) VALUES ('user','user', 'user@test.ru', 'user', 0);