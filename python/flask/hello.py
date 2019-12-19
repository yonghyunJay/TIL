from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/hi')
def hi():
    # return "반갑습니다."
    # return "<h1>Hello</h1>"
    name = "Jason"
    return render_template('hi.html', html_name = name)

@app.route('/greeting/<string:name>')
def greeting(name):
    def_name = name
    return render_template('greeting.html', html_name = def_name)

@app.route('/cube/<int:num>')
def cube(num):
    cube_num = num**3
    return render_template('cube.html', cube_num = cube_num, num = num)

# @app.route('fstring')
# def fstring():
#     name = "Jay"
#     return f"제 이름은 {name} 입니다."

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

@app.route('/movies')
def movies():
    movies = ['조커', '겨울왕국2', '터미네이터', '어벤져스']
    return render_template('movies.html', html_movies = movies)

if __name__ == "__main__":
    app.run(debug=True)