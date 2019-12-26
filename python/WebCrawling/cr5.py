import requests
from bs4 import BeautifulSoup

res = requests.get('http://v.media.daum.net/v/20170615203441266')
soup = BeautifulSoup(res.content, 'html.parser')

# 태그 검색
soup.find('title')

# select 함수는 리스트 형태로 전체 반환
title = soup.select('title')[0]
print (title)
print (title.get_text())

print('---------------------------------')
# 띄어쓰기가 있다면 하위 태그를 검색
title = soup.select('html head title')[0]
print (title.get_text())

print('---------------------------------')
# 띄어쓰기가 있다면 하위 태그를 검색
# 이때 바로 직계의 자식이 아니여도 관계없음
title = soup.select('html title')[0]
print (title.get_text())

# print('---------------------------------')
# > 를 사용하는 경우 바로 아래의 자식만 검색
# 바로 아래 자식이 아니기 때문에 에러 발생
# title = soup.select('html > title')[0]
# print (title.get_text())

print('---------------------------------')
# 바로 아래 자식을 검색
title = soup.select('head > title')[0]
print (title.get_text())

print('---------------------------------')
# .은 태그의 클래스를 검색
# class가 article_view인 태그 탐색
body = soup.select('.article_view')[0]
print (type(body), len(body))
for p in body.find_all('p'):
    print (p.get_text())

print('---------------------------------')
# div태그 중 class가 article_view인 태그 탐색
body = soup.select('div.article_view')[0]
print (type(body), len(body))
for p in body.find_all('p'):
    print (p.get_text())

print('---------------------------------')
# div 태그 중 id가 harmonyContainer인 태그 탐색
container = soup.select('#harmonyContainer')
print (container)

print('---------------------------------')
# div태그 중 id가 mArticle 인 태그의 하위 태그 중 아이디가 article_title인 태그
title = soup.select('div#mArticle  div#harmonyContainer')[0]
print (title.get_text())