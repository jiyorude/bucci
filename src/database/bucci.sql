CREATE DATABASE IF NOT EXISTS bucci;

CREATE TABLE cms (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    short_description TEXT NOT NULL, 
    intro TEXT NOT NULL,
    image_link VARCHAR(2083),
    publish_date DATE NOT NULL,
    mins_read INT, 
    author VARCHAR(100) NOT NULL,
    main_content TEXT NOT NULL
);