### 실습

(venv) 가상환경 내에서

requests 설치

``` shell
$ pip install requests
```

beautifulsoup4 설치

```shell
$ pip install beautifulsoup4
```



#### 1. KOSPI 정보 가져오기

![image-20191219104004624](../TIL/07_python_example.assets/image-20191219104004624.png)

``` python
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
```



#### 2. 환율 정보 가져오기

![image-20191219105125077](../TIL/07_python_example.assets/image-20191219105125077.png)

``` python
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"

req = requests.get(url).text

soup = BeautifulSoup(req, 'html.parser')
exchange = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value")

print(exchange.text)
```



#### 3.  실시간 검색어 가져오기

![image-20191219114811123](../TIL/07_python_example.assets/image-20191219114811123.png)

``` python
import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"

req = requests.get(url).text

soup = BeautifulSoup(req, 'html.parser')

search = soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k")

for item in search :
    print(item.text)
```



> Tip.
>
> 영화 정보 API
>
> https://www.themoviedb.org/?language=ko-KR
>
> https://developers.themoviedb.org/3/getting-started/introduction
>
> 텔레그램 API
>
> https://core.telegram.org/api