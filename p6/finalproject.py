import mysql.connector
from sklearn import tree
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="learn"
        )

mycursor = mydb.cursor()
mycursor.execute('select kilometerage,model,color from denaplus;')
x=mycursor.fetchall()
mycursor.execute('select price from denaplus;')
y=mycursor.fetchall()

clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)

inp_carwork=input('how many your car is worked:')
inp_color=input('your car color is\n(1:white,2:black,3:Gray,4:silver,5:Titanium,\n6:Dolphin,7:blue,8:red,9:yellow):')
inp_model=input('write your car model:')
new_data=[[inp_carwork,inp_color,inp_model]]
answer=clf.predict(new_data)
print(answer)
mycursor.close()
mydb.close()
