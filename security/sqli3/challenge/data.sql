BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    address TEXT,
    email TEXT
);

INSERT INTO users (username, address, email) VALUES
    ('Finn Carson', '123 Main St', 'finn@example.com'),
    ('Aldo Young', '456 Elm St', 'aldo@example.com'),
    ('Joy Holt', '789 Oak St', 'joy@example.com'),
    ('Kenyon Nicholson', '101 Pine St', 'kenyon@example.com'),
    ('Elsa Reyes', '234 Maple St', 'elsa@example.com'),
    ('Leonel Townsend', '567 Cedar St', 'leonel@example.com'),
    ('Chad Fletcher', '890 Birch St', 'chad@example.com'),
    ('Erika Li', '111 Spruce St', 'erika@example.com'),
    ('Aryan Lynch', '222 Walnut St', 'aryan@example.com'),
    ('Sara Johnson', '333 Cherry St', 'sara@example.com'),
    ('Oliver Smith', '444 Pine St', 'oliver@example.com'),
    ('Sophia Brown', '555 Maple St', 'sophia@example.com'),
    ('Noah Wilson', '666 Elm St', 'noah@example.com'),
    ('Emma Martinez', '777 Oak St', 'emma@example.com'),
    ('Liam Anderson', '888 Cedar St', 'liam@example.com'),
    ('Olivia Thomas', '999 Birch St', 'olivia@example.com'),
    ('William Jackson', '111 Walnut St', 'william@example.com'),
    ('Ava White', '222 Spruce St', 'ava@example.com'),
    ('James Harris', '333 Walnut St', 'james@example.com'),
    ('Isabella Martin', '444 Spruce St', 'isabella@example.com'),
    ('Ethan Garcia', '555 Elm St', 'ethan@example.com'),
    ('Mia Rodriguez', '666 Oak St', 'mia@example.com'),
    ('Benjamin Lopez', '777 Pine St', 'benjamin@example.com'),
    ('Charlotte Perez', '888 Maple St', 'charlotte@example.com'),
    ('Alexander Williams', '999 Elm St', 'alexander@example.com'),
    ('Harper Carter', '111 Oak St', 'harper@example.com'),
    ('Daniel Sanchez', '222 Maple St', 'daniel@example.com'),
    ('Avery Ramirez', '333 Elm St', 'avery@example.com');

CREATE TABLE IF NOT EXISTS flags (
    flag TEXT
);

INSERT INTO flags (flag) VALUES
    ('not flag1'),
    ('not flag2'),
    ('not flag3'),
    ('not flag4'),
    ('not flag5'),
    ('not flag6'),
    ('not flag7'),
    ('not flag8'),
    ('not flag9'),
    ('zzzingeneer{PR0FE5S!ONal_BUg_BOuNTy_huNTer}zzz'),
    ('not flag10'),
    ('not flag11'),
    ('not flag12'),
    ('not flag13'),
    ('not flag14'),
    ('not flag15');

COMMIT;
