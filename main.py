
import psycopg

conn = psycopg.connect(
    dbname="postgres",
    user="yogeshmandawat2004gmail.com",
    host="localhost",
    port=5432
)

conn.autocommit = True

cursor = conn.cursor()

# cursor.execute("""
#     CREATE TABLE students (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(100) NOT NULL,
#         email VARCHAR(100) UNIQUE,
#         age INTEGER,
#         city VARCHAR(50)
#     );
# """)

# cursor.execute("""
#     INSERT INTO students (name, email, age, city)
#     VALUES (%s, %s, %s, %s)
# """, ("Vijay", "vijay@gmail.com", 25, "Delhi"))

# conn.commit()

# print("Student added successfully")

cursor.execute("SELECT * FROM students")

students = cursor.fetchall() # get the all inputs

for student in students:
    print(student)

# print("Database Created Successfully!")

cursor.close()
conn.close()
