-- 9-full_creation.sql
CREATE TABLE IF NOT EXISTS second_table (
  id INT,
  name VARCHAR(256),
  score INT);

INSERT INTO second_table (id, name, socre) VALUES (1, “John”, 10);
INSERT INTO second_table (id, name, socre) VALUES (2, “Alex”, 3);
INSERT INTO second_table (id, name, socre) VALUES (3, “Bob”, 14);
INSERT INTO second_table (id, name, socre) VALUES (4, “George”, 8);
