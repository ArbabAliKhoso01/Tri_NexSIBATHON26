CREATE DATABASE smart_exam_db;

USE smart_exam_db;






CREATE TABLE subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE topics (
    topic_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_id INT,
    name VARCHAR(50),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

CREATE TABLE questions (
    question_id INT AUTO_INCREMENT PRIMARY KEY,
    topic_id INT,
    question_text TEXT,
    option1 VARCHAR(100),
    option2 VARCHAR(100),
    option3 VARCHAR(100),
    option4 VARCHAR(100),
    correct_option VARCHAR(5),
    FOREIGN KEY (topic_id) REFERENCES topics(topic_id)
);
CREATE DATABASE smart_exam;
USE smart_exam;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(20)
);

CREATE TABLE subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);
SELECT user, host, plugin FROM mysql.user WHERE user = 'root';



