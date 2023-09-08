import mysql.connector

mydb = mysql.connector.connect(user='root', password='A102030m',
                              host='127.0.0.1',
                              database='learn')

cursor = mydb.cursor()

cursor.execute=("select * from tbltest order by Height desc, Weight")

myresult = cursor.fetchall()

for x in myresult:
  print(x)

mydb.close()