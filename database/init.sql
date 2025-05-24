CREATE TABLE IF NOT EXISTS clients (
    client_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS payment_methods (
    payment_method_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE iF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP NOT NULL,
    client_id INT NOT NULL,
    amount NUMERIC(12, 2) NOT NULL,
    payment_method_id INT NOT NULL,
    CONSTRAINT fk_transactions_client FOREIGN KEY (client_id) REFERENCES clients(client_id),
    CONSTRAINT fk_transactions_payment_method FOREIGN KEY (payment_method_id) REFERENCES payment_methods(payment_method_id)
);

INSERT INTO clients (client_id, name) VALUES
(101, 'Ana Torres'),
(102, 'Luis Gómez'),
(103, 'Laura Ruiz'),
(104, 'Pedro Mejía');


INSERT INTO payment_methods (payment_method_id, name) VALUES
(1, 'Transferencia'),
(2, 'Nequi'),
(3, 'Daviplata');


INSERT INTO transactions (id, date, client_id, amount, payment_method_id) VALUES
(1, '2025-05-01', 101, 45000.00, 1),
(2, '2025-05-02', 102, 30000.00, 2),
(3, '2025-05-03', 101, 20000.00, 3),
(4, '2025-05-04', 103, 50000.00, 1),
(5, '2025-05-05', 104, 10000.00, 2);

SELECT setval('clients_client_id_seq', 104, true);
SELECT setval('payment_methods_payment_method_id_seq', 3, true);
SELECT setval('transactions_id_seq', 5, true);