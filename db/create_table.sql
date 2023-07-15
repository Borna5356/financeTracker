Create Table users(
    user_id         SERIAL PRIMARY KEY,
    username        TEXT NOT NULL,
    email           TEXT NOT NULL,
    password        TEXT NOT NULL
);