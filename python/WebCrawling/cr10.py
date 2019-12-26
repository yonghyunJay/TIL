import requests
from bs4 import BeautifulSoup as BS

def refine_price(text):
    price = int(text.replace(",", ""))
    return price

url = "https://finance.naver.com/item/sise_day.nhn?code=005930"
response = requests.get(url)
text = response.text
html = BS(text, 'html.parser')
tr_list = html.find_all("tr", {"onmouseover":"mouseOver(this)"})

for tr in tr_list:
   date = tr.find_all("td")[0].text
   temp = []
   for td in tr.find_all("td")[1:]:
      price = refine_price(td.text)
      temp.append(price)
   del temp[1]
   print([date] + temp)
   """
   closing = refine_price(tr.find_all("td")[1].text)
   opening = refine_price(tr.find_all("td")[3].text)
   max = refine_price(tr.find_all("td")[4].text)
   min = refine_price(tr.find_all("td")[5].text)
   volume = refine_price(tr.find_all("td")[6].text)
   print([date, closing, opening, max, min, volume])
   """