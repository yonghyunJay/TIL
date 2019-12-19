from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    # data = request.form.get('keyword')    # post 방식은 form.get()
    data = request.args.get('keyword')  # get 방식은 args.get()
    return render_template('pong.html', html_data = data)

@app.route('/naver')
def naver():
    data = request.args.get('query')
    return render_template('naver.html', html_data = data)

@app.route('/google')
def google():
    data = request.args.get('q')
    return render_template('google.html', html_data = data)

if __name__ == ("__main__"):
    app.run(debug=True)