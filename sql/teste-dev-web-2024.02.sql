-- Tabela de Produtos
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Vendas
CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    sale_price DECIMAL(10, 2) NOT NULL,
    sale_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products (product_id)
);

INSERT INTO products (name, description, price)
VALUES('Camiseta', 'Camiseta branca de algodão', 19.99),('Calça Jeans', 'Calça jeans azul escura', 29.99),('Tênis', 'Tênis preto esportivo', 39.99);

INSERT INTO products (name, description, price)
VALUES('Tênis', 'Tênis preto esportivo', 39.99);

INSERT INTO sales (product_id, quantity, sale_price, sale_date)
VALUES(1, 2, 10.99, '2024-03-01'),(2, 1, 25.50, '2024-03-02'),(3, 1, 35.99, '2024-03-03');

INSERT INTO sales (product_id, quantity, sale_price, sale_date)
VALUES(5, 1, 35.99, '2024-03-30');

SELECT s.*
FROM sales s
JOIN products p ON s.product_id = p.product_id
WHERE p.name = 'Tênis'
    AND s.sale_date >= '2024-02-01'
    AND s.sale_date <= '2024-03-29';

