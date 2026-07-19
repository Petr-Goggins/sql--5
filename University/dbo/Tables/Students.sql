-- database: :memory:
CREATE TABLE Students (
    StudentID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL
);

CREATE TABLE Courses (
    CourseID INTEGER PRIMARY KEY,
    CourseName TEXT NOT NULL,
    Credits INTEGER NOT NULL
);

CREATE TABLE Enrollments (
    StudentID INTEGER,
    CourseID INTEGER,
    PRIMARY KEY (StudentID, CourseID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

INSERT INTO Students (StudentID, FirstName, LastName) VALUES
(1, 'Иван', 'Иванов'),
(2, 'Петр', 'васечкин'),
(3, 'Вася', 'Пупкин');

INSERT INTO Courses (CourseID, CourseName, Credits) VALUES
(01, 'Матеша', 5),
(02, 'Физра', 4),
(03, 'Химия', 3);

INSERT INTO Enrollments (StudentID, CourseID) VALUES
(1, 101),
(1, 102),
(2, 101),
(3, 103);

SELECT 
    s.FirstName,
    s.LastName,
    c.CourseName
FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID
JOIN Courses c ON e.CourseID = c.CourseID
ORDER BY s.LastName, s.FirstName, c.CourseName;