from bs4 import BeautifulSoup
import requests
r=requests.get('https://divar.ir/s/tehran')
soup=BeautifulSoup(r.text,'html.parser')
import csv

all_link=soup.find_all('article')
result=[]
for i in all_link:
    if 'kt-post-card__discription'in i:
        result.append(i)
for i in result:
    print(i)        

