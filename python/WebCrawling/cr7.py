import re
import requests
from bs4 import BeautifulSoup

res = requests.get('http://land.naver.com/article/divisionInfo.nhn?rletTypeCd=A01&tradeTypeCd=A1&hscpTypeCd=A01%3AA03%3AA04&cortarNo=1168000000&articleOrderCode=&cpId=&minPrc=&maxPrc=&minWrrnt=&maxWrrnt=&minLease=&maxLease=&minSpc=&maxSpc=&subDist=&mviDate=&hsehCnt=&rltrId=&mnex=&siteOrderCode=&cmplYn=')

soup = BeautifulSoup(res.content, 'html.parser')

# a 태그이면서 href 속성 값이 특정한 값을 갖는 경우 탐색
link_title = soup.select("#depth4Tab0Content > div > table > tbody > tr > td.align_l.name > div > a.sale_title")
link_price = soup.select("#depth4Tab0Content > div > table > tbody > tr > td.num.align_r > div > strong")

for num in range(len(link_price)):
    print(link_title[num].get_text(), link_price[num].get_text())