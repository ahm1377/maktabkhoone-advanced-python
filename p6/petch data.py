import requests
import mysql.connector
from bs4 import BeautifulSoup

E2P_map = {'1' : '۱', '2' : '۲', '3' : '۳', '4' : '۴', '5' : '۵', '6' : '۶', '7' : '۷', '8' : '۸', '9' : '۹', '0' : '۰' }

def convert_number_to_persian(strIn : str):
    a = map(lambda ch: E2P_map[ch] if ch in E2P_map else ch, strIn)
    return ''.join(list(a))


colornum = {'سفید': '1', 'مشکی': '2', 'خاکستری': '3', 'نقرهای': '4', 'تیتانیوم': '5', 'دلفینی': '6', 'آبی': '7', 'قرمز': '8', 'زرد': '9'}

def convert_color_to_colorcode(strIn: str):
    result = ''
    for color in strIn:
        if color in colornum:
            result += colornum[color]
        else:
            result += color
    return result



req=requests.get('https://divar.ir/s/tehran/car/dena/plus')
soup=BeautifulSoup(req.text,'html.parser')
href_texts = []
links = soup.find_all('a', href=lambda href: href and href.startswith('/v/'))
for link in links:
    href_texts.append(link['href'])
  
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user='root',
  password='',
  database="learn"
)
mycursor = mydb.cursor()
for alink in href_texts:
    try:
        link=(f'https://divar.ir{alink}')
        req2=requests.get(link)
        soup2=BeautifulSoup(req2.text,'html.parser')
        page_data=soup2.find_all("div",attrs={'class':'post-page__section--padded'})
        kilometr_model_color = page_data[0].find_all('span', attrs={'class': 'kt-group-row-item__value'})
        data_finder = page_data[0].find_all('p', attrs={'class': 'kt-unexpandable-row__value'})
        kilometerage = int(convert_number_to_persian(kilometr_model_color[0].text).replace("٬",'').strip())
        model = int(convert_number_to_persian(kilometr_model_color[1].text))
        color = convert_color_to_colorcode( kilometr_model_color[2].text)
        price=int(convert_number_to_persian(data_finder[(len(data_finder)-1)].text).replace("تومان","").replace("٬",'').strip())
    
    
        description = str(page_data[1].text).strip()
    
        sql = "INSERT INTO DenaPlus (link,kilometerage,model,color,price,description) VALUES (%s, %s, %s, %s, %s, %s) ;"
        val = (link,kilometerage,model,color,price,description)
        mycursor.execute(sql, val)
        mydb.commit()
    except:
        continue

mycursor.close()
mydb.close()
