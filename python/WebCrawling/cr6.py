import re
import requests
from bs4 import BeautifulSoup

res = requests.get('http://media.daum.net/economic/')

soup = BeautifulSoup(res.content, 'html.parser')

# a태그이면서 href 속성을 갖는 경우 탐색, 리스트 타입으로 links 변수에 저장됨
links = soup.select('a[href]')
   
for link in links:
    # print (link) # <a class="link_services link_services2" href="http://sports.media.daum.net/sports">스포츠</a>
    # print (link['href']) # http://sports.media.daum.net/sports
    if re.search('http://\w+', link['href']):  # http:// 문자열 이후에 숫자 또는 문자[a-zA-Z0-9_]가 한 개 이상 있는 데이터와 매치됨 
        print (link['href'])