-- database: :memory:
CREATE TABLE Authors (
    AuthorID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT
);

CREATE TABLE Books (
    BookID INTEGER PRIMARY KEY,
    Title TEXT,
    AuthorID INTEGER,
    Price REAL,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);

INSERT INTO Authors (AuthorID, FirstName, LastName) VALUES
(1, 'Лев', 'Толстой'),
(2, 'Фёдор', 'Достоевский');

INSERT INTO Books (BookID, Title, AuthorID, Price) VALUES
(1, 'Война и мир', 1, 500),
(2, 'Анна Каренина', 1, 450),
(3, 'Преступление и наказание', 2, 400);

DELETE FROM Books;
DELETE FROM Authors;