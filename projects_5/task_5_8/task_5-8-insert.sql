DELETE FROM suppliers;
DELETE FROM prices;
DELETE FROM products;

INSERT INTO products (name, category) VALUES
('Ноутбук', 'Электроника'),
('Мышь', 'Электроника'),
('Книга', 'Образование'),
('Ручка', 'Канцелярия');

INSERT INTO prices (product_id, price) VALUES
(1, 50000.00),
(2, 1500.00),
(3, 800.00),
(4, 50.00);

INSERT INTO suppliers (name, product_id) VALUES
('ООО "ТехноПост"', 1),
('ООО "ТехноПост"', 2),
('ИП Иванов', 3),
('ООО "КанцТрейд"', 4);