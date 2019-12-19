import requests
from bs4 import BeautifulSoup

url = "http://finance.naver.com/sise"

# req = requests.get(url)
# print(req)
req = requests.get(url).text
# print(req)

soup = BeautifulSoup(req, 'html.parser')
kospi = soup.select_one("#KOSPI_now")

print(kospi.text)