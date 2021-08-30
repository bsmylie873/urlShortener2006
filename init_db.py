import mysql.connector as mysql
from mysql.connector import Error

from main import app

app.config.from_pyfile('config.py')

# First, set up the database itself.
try:
    db = mysql.connect(
        host=app.config['DB_HOST'],
        user=app.config['DB_USER'],
        passwd=app.config['DB_PASS']
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
        host=app.config['DB_HOST'],
        user=app.config['DB_USER'],
        database="urlshortener",
        passwd=app.config['DB_PASS']
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
