import requests
import mysql.connector
from bs4 import BeautifulSoup
import re

price_list=[]
work_list=[]
inp=input('enter car name:')
req=requests.get('https://www.truecar.com/used-cars-for-sale/listings/%s/' %inp)
soup=BeautifulSoup(req.text,'html.parser')

outlistprice=soup.find_all('div', attrs={'data-test':'vehicleCardPricingBlockPrice'})
for i in range(0,len(outlistprice)):
    vorodi=outlistprice[i]
    temp=re.findall(r"<div.*[<div class=\"text\-sm line-through\">+]\$(\d*\,\d+)" , str(vorodi) )
    price_list.append(str(temp).strip("[],'"))


outlistwork=soup.find_all('div',attrs={'data-test':'vehicleMileage'})
for j in range(0,len(outlistwork)):
    vorodi=outlistwork[j]
    temp=re.findall(r"(\d*\,\d+)", str(vorodi))
    work_list.append(str(temp).strip("[]\,'"))


mydb = mysql.connector.connect(host="localhost",
                                user="root",
                                password="12345678")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE cars (price VARCHAR[10], worked VARCHAR[10])")

for i in range(0,20):
    sql = "INSERT INTO cars (price, worked) VALUES (%s, %s)"
    val = (price_list[i], work_list[i])
    mycursor.execute(sql, val)
    mydb.commit()

mycursor.execute("SELECT * FROM cars")
myresult =mycursor.fetchall()
for x in myresult:
    print(x)
mydb.close()
