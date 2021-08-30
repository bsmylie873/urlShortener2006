import mysql.connector as mysql
from mysql.connector import Error

# First, set up the database itself.
try:
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="password"
    )

    with open('db.sql', 'r') as f:
        with db.cursor() as cursor:
            cursor.execute(f.read(), multi=True)
        cursor.close()
        db.commit()
# Error handling
except Error as e:
    print("Error while connecting to MySql", e)

# Now, set up table inside urlshortener database.
try:
    db = mysql.connect(
        host="localhost",
        user="root",
        database="urlshortener",
        passwd="password"
    )
    print("Connection successful!")

    with open('schema.sql', 'r') as f:
        with db.cursor() as cursor:
            cursor.execute(f.read(), multi=True)
        cursor.close()
        db.commit()
# Error handling
except Error as e:
    print("Error while connecting to MySql, database created", e)
