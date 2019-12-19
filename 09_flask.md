# Flask

Flask는 Python으로 구동할 수 있는 서버 프레임워크입니다.



### 1. flask 설치

``` shell
$ pip install flask==1.0.0
```



> hello.py

``` python
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
```



```shell
$ env FLASK_APP=hello.py flask run
```



### 2. 예제

#### 1. 기본 구조

app.py 가 아닌경우 아래와 같이 작업 후 실행 가능

``` python
from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

... 여기에 추가 작업 ...

if __name__ == "__main__":
    app.run(debug=True)
```



![image-20191219132541541](../TIL/09_flask.assets/image-20191219132541541.png)



#### 2. hello.py

##### hello.py 추가 작업 내용 1

``` python
@app.route('/hi')
def hi():
    # return "반갑습니다."
    # return "<h1>Hello</h1>"
    name = "Jason"
    return render_template('hi.html', html_name = name)
```

``` html
<body>
    <h1>{{html_name}}</h1>
    <ul>
        <li>스타벅스</li>
        <li>투썸플레이스</li>
        <li>엔제리너스</li>
        <li>이디야</li>
        <li>빽다방</li>
    </ul>
</body>
```

![image-20191219202818497](../TIL/09_flask.assets/image-20191219202818497.png)



##### hello.py 추가 작업 내용 2

``` python
@app.route('/greeting/<string:name>')
def greeting(name):
    def_name = name
    return render_template('greeting.html', html_name = def_name)
```

``` html
<body>
    <h1>만나서 반갑습니다, {{html_name}} 님</h1>
</body>
```

![image-20191219202947362](../TIL/09_flask.assets/image-20191219202947362.png)



##### hello.py 추가 작업 내용 3

``` python
@app.route('/cube/<int:num>')
def cube(num):
    cube_num = num**3
    return render_template('cube.html', cube_num = cube_num, num = num)
```

``` html
<body>
    <h1>{{num}}의 3제곱은 {{cube_num}}</h1>
    <!-- 아래처럼 html 에서 연산하는 행위는 안정성에 안좋음 -->
    <!-- <h1>{{num}}의 3제곱은 {{num**3}}</h1> -->
</body>
```

![image-20191219203132386](../TIL/09_flask.assets/image-20191219203132386.png)



##### hello.py 추가 작업 내용 4

```python
@app.route('/dinner')
def dinner():
    menu = ['삼각김밥', '컵라면', '스테이크', '마라탕', '훠궈']
    menu_img = {'삼각김밥' : 'http://recipe1.ezmember.co.kr/cache/recipe/2018/08/06/087c110e0149b1ce06b22fcc765d5694.jpg',
                '컵라면' : 'https://cdn.crowdpic.net/detail-thumb/thumb_d_378BA60B966894DC61DCEC443E424FA3.jpg',
                '스테이크' : 'http://recipe1.ezmember.co.kr/cache/recipe/2017/07/09/6741acc7f6bf0f7d04245851fb365c311.jpg',
                '마라탕' : 'https://t1.daumcdn.net/cfile/tistory/9990F0395BBD84EA01',
                '훠궈' : 'https://funshop.akamaized.net/products/0000062075/vs_image800.jpg'
                }

    dinner = random.choice(menu)
    return render_template('dinner.html', html_dinner = dinner, html_url = menu_img[dinner])
```

``` html
<body>
    <h1>오늘 저녁은 {{html_dinner}} 입니다.</h1>
    <img src="{{html_url}}" alt="{{html_dinner}}" width="400">
</body>
```

![image-20191219203225459](../TIL/09_flask.assets/image-20191219203225459.png)



##### hello.py 추가 작업 내용 5

```python
@app.route('/movies')
def movies():
    movies = ['조커', '겨울왕국2', '터미네이터', '어벤져스']
    return render_template('movies.html', html_movies = movies)
```

``` html
<body>
    <ul>
    {# jinja 주석입니다. #}
    {% for movie in html_movies %}
        {% if movie == '조커' %}
            <li>{{movie}} || 재밌음</li>
        {% elif movie == '겨울왕국2' %}
            <li>{{movie}} || 올라프 귀염 </li>
        {% else %}
            <li>{{movie}}</li>
        {% endif %}
    {% endfor %}
    </ul>
</body>
```

![image-20191219203322087](../TIL/09_flask.assets/image-20191219203322087.png)



#### 3. ping_pong.py

##### ping_pong.py 추가 작업 내용 1 and 2

```python
@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    # data = request.form.get('keyword')    # post 방식은 form.get()
    data = request.args.get('keyword')  # get 방식은 args.get()
    return render_template('pong.html', html_data = data)
```

> ping.html
>
> ``` html
> <body>
>  <h1>Here is Ping!!</h1>
>  <form action="/pong">
>      <input type="text" name="keyword">
>      <input type="submit">
>  </form>
> </body>
> ```



> pong.html
>
> ```html
> <body>
>  <h1>Here is Pong!!</h1>
>  {{html_data}}
> </body>
> ```
>
> 

![image-20191219203721015](../TIL/09_flask.assets/image-20191219203721015.png)

![image-20191219203729468](../TIL/09_flask.assets/image-20191219203729468.png)



##### ping_pong.py 추가 작업 내용 3 and 4

``` python 
@app.route('/naver')
def naver():
    data = request.args.get('query')
    return render_template('naver.html', html_data = data)

@app.route('/google')
def google():
    data = request.args.get('q')
    return render_template('google.html', html_data = data)
```

> naver.html
>
> ```html
> <body>
>  <h1>Naver</h1>
>  <form action="https://search.naver.com/search.naver">
>      <input type="text" name="query">
>      <input type="submit">
>  </form>
> </body>
> ```



> google.html
>
> ```html
> <body>
>  <h1>Google</h1>
>  <form action="https://www.google.com/search">
>      <input type="text" name="q">
>      <input type="submit">
>  </form>
> </body>
> ```

![image-20191219203947148](../TIL/09_flask.assets/image-20191219203947148.png)

![image-20191219203955071](../TIL/09_flask.assets/image-20191219203955071.png)

![image-20191219204016404](../TIL/09_flask.assets/image-20191219204016404.png)

![image-20191219204021972](../TIL/09_flask.assets/image-20191219204021972.png)



#### 4. op_gg.py

##### op_gg.py 추가 작업 내용 1 and 2

``` python
@app.route('/search')
def search():
    return render_template('search_opgg.html')

@app.route('/opgg')
def opgg():
    userName = request.args.get('userName')
    url = f"http://www.op.gg/summoner/userName={userName}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    
    tier = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank')

    win = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')

    return render_template('opgg.html', name = userName, tier = tier.text, win = win.text[: - 1], url = url)
```

> search_opgg,html
>
> ```html
> <body>
>  <h1>Hide on bush</h1>
>  <form action="/opgg">
>      <input type="text" name="userName">
>      <input type="submit" value="검색">
>  </form>
> </body>
> ```



> opgg.py
>
> ```html
> <body>
>  <h1> {{name}} 님의 랭크는 </h1>
>  <h2> {{tier}} 입니다. </h2>
>  <h3> {{win}} 승 하셨습니다. </h3>
>  <h4> {{url}} </h4>
> </body>
> ```

![image-20191219204600554](../TIL/09_flask.assets/image-20191219204600554.png)

![image-20191219204608352](../TIL/09_flask.assets/image-20191219204608352.png)

