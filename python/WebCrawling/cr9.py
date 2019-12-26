import requests
from bs4 import BeautifulSoup

r = requests.get("https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=100")
c = r.content
soup = BeautifulSoup(c, "html.parser")

all=soup.find("ul",{"class":"type06_headline"})
# print(all)

all2 = all.find_all("li")
# print(all2[0])

for item in all2:
    try:
        img = item.find("dt",{"class":"photo"})
        img2 = img.find("img")["src"]
        title = item.find("dt", "").find("a").text.strip("\n\t\r ")  # 뉴스 제목 추출하기
        body = item.find("span", {"class": "lede"}).text  # 뉴스 내용 요약 추출하기
        writer = item.find("span", {"class": "writing"}).text # 뉴스 제공자
        print(img2, title, body, writer)
    except:
        print("No image")