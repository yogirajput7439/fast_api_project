import psycopg

conn = psycopg.connect(
    dbname="postgres",
    user="yogeshmandawat2004gmail.com",
    host="localhost",
    port=5432
)

conn.autocommit = True

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE,
        age INTEGER,
        city VARCHAR(50)
    );
""")

cursor.execute("""
    INSERT INTO students (name, email, age, city)
    VALUES (%s, %s, %s, %s)
""", ("Vijay", "vijay@gmail.com", 25, "Delhi"))

conn.commit()

print("Student added successfully")

cursor.execute("SELECT * FROM students")

students = cursor.fetchall() # get the all inputs

for student in students:
    print(student)

# INSERT INTO THE TABLE

cursor.execute("""
    INSERT INTO students (name, email, age, city)
    VALUES (%s, %s, %s, %s)
""",
("Kanan", "karan@gmail.com", 23, "Goa"))

conn.commit()

# SELECT FROM TABLE

cursor.execute("""
    SELECT * FROM students
""")

students = cursor.fetchall()

for student in students:
    print(student)

# WHERE - Filter records 

cursor.execute(
    "SELECT * FROM students WHERE city = %s",
    ("Pune",))

print(cursor.fetchall())

# UPDATE - Modify Records

cursor.execute("""
    UPDATE students
    SET city = %s
    WHERE name = %s
""", ("Rajur", "Kanan"))

conn.commit()

# DELETE - Remove recods

cursor.execute(
    "DELETE FROM students WHERE name = %s", 
    ("Rahul",))

conn.commit()



print("Database Created Successfully!")

cursor.close()
conn.close()

