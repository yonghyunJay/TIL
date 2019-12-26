import requests
from bs4 import BeautifulSoup as BS

url = 'http://www.weather.go.kr/weather/observation/currentweather.jsp'

response = requests.get(url)

if response.status_code != 200:
    print("%d 에러가 발생했습니다." % response.status_code)
    quit()

soup = BS(response.content, 'html.parser')
table = soup.find('table', {'class' : 'table_develop3'})

data = []
for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds:
        if td.find('a'):
            point = td.find('a').text
            temperature = tds[5].text
            humidity = tds[9].text
            data.append([point, temperature, humidity])

with open('weather.csv', 'w', encoding='utf-8', newline='\n') as file:
    file.write('지역, 기온, 습도\n')
    for i in data:
        file.write('{0}, {1}, {2}\n'.format(i[0], i[1], i[2]))