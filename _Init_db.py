import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="fmls03",
    passwd="Schipilliti03!",
    )

my_cursor= mydb.cursor()

my_cursor.execute("CREATE DATABASE SquareNet")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)