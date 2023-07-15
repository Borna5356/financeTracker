Create Table users(
    user_id         SERIAL PRIMARY KEY,
    username        TEXT NOT NULL,
    email           TEXT NOT NULL,
    password        TEXT NOT NULL
);

INSERT INTO users(username, email, password) VALUES
    ('Borneo', 'bornakevin1@gmail.com', 'Tehran13!');