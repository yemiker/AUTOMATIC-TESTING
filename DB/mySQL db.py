# Create tables

# # Connect to the database
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password="******",
    database="sakila"
)
print(db.cursor)
mycursur = db.cursor()

#  get the cursor for database

cur = db.cursor()
sql = 'show tables'
# query
cur.execute(sql)

for i in cur:
    print(i)
# --------------------------------
# Insert into tables


# Connect to the database
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password="******",
    database="sakila"
)
mycursur = db.cursor()
sql = "INSERT INTO actor(first_name,last_name)VALUES(%s,%s)"

actor1 = ("yemiker", "adonia")
mycursur.execute(sql, actor1)
db.commit()
# --------------------------------
# Select into tables


#Connect to the database
# import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password="******",
    database="sakila"
)
mycursur = db.cursor()
sql = "SELECT first_name FROM actor  WHERE first_name = 'yemiker' "
mycursur.execute(sql)
result = mycursur.fetchall()
for i in result:
    print(i)
# --------------------------------
# Delete into tables

import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password="******",
    database="sakila"
)
mycursur = db.cursor()
sql = "DELETE FROM actor WHERE first_name = %s "
data = ('yemiker',)
mycursur.execute(sql, data)
db.commit()








