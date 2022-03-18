DROP TABLE bookings;
DROP TABLE lessons;
DROP TABLE members;

INSERT TABLE members {
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
};

INSERT TABLE lessons {
    id SERIAL PRIMARY KEY,
    title VARCHAR(255)
};

INSERT TABLE bookings {
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    lesson_id INT REFERENCES lesson(id) ON DELETE CASCADE
};