import sqlite3

conn = sqlite3.connect("example.db")
# conn.execute(
#     """
#     CREATE TABLE students
#     (id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     age INTEGER NOT NULL);
# """
# )


# conn.execute("INSERT INTO students (id, name, age) VALUES (1, 'Alice', 20)")
# conn.execute("INSERT INTO students (id, name, age) VALUES (2, 'Bob', 22)")
# conn.execute("INSERT INTO students (id, name, age) VALUES (3, 'Charlie', 21)")

# conn.commit()


cursor = conn.execute("SELECT * FROM students")
for row in cursor:
    print(row)
