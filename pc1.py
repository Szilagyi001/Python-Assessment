#pip install mysql-connector-python

import mysql.connector

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bkb",
    port=3306
)

mycursor = mydb.cursor()

sql = "SELECT * FROM events"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


