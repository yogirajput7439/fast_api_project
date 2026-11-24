
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

cursor.execute("""
    INSERT INTO students (name, email, age, city)
    VALUES (%s, %s, %s, %s)
""", ("Yogesh", "yogesh@gmail.com", 22, "Sambhajinagar"))

conn.commit()

print("Database Created Successfully!")

cursor.close()
conn.close()
