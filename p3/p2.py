import mysql.connector
import re 


mydb = mysql.connector.connect(user='root', password='',
                                host='127.0.0.1',
                                database='learn')
mydb.execute("CREATE TABLE emailpass (email VARCHAR(30), password VARCHAR(30))")
inp_count=int(input('how many you have email? :'))
for i in range(0,inp_count):
    mycursor = mydb.cursor()
    pattern = r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'
    inp_email=str()
    nf_loop=False
    while not re.match(pattern, inp_email):
        if nf_loop:    
            print('your email have problem! input example:expression@string.string')
        inp_email=input()
        nf_loop=True
    inp_password=input('enter password:')
    sql = "INSERT INTO email (email, password) VALUES (%s, %s)" %(inp_email,inp_password)
    mydb.commit()
query=("SELECT * FROM emailpass")

mydb.close()