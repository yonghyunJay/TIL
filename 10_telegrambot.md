# TeleramBot

### 1. 인증 키 받기

텔레그램 PC 설치

`@botfather` 검색

`/newbot` 입력

`[만들봇이름]_bot` 또는 `[만들봇이름]bot` 입력

`API Key` 확인 후 따로 저장 (숫자:영문 형태로 구성)



### 2. API 기본 사용법

token = API Key

``` shell
https://api.telegram.org/bot<token>/METHOD_NAME
```

나의 계정 ID 확인

봇으로 메시지 입력 후

```shell
https://api.telegram.org/bot<token>/getUpdates
```

from > id 확인 후 따로 저장



### 3. sendMessage 실습

html 에서 입력박은 메시지를 텔레그램 봇으로 보내기

sendMessage 기본 사용법

```shell
https://api.telegram.org/bot<token>/?chat_id=<나의 계정 ID>&text=<전송할TEXT>
```



> 인증 키 보안 part1
>
> 1. python-decouple 설치
>
>    ```shell
>    $ pip install python-decouple
>    ```
>
> 2. .env 파일 생성
>
>    ```shell
>    CHAT_ID="000000000"
>    TELEGRAM_BOT_TOKEN="111111111:gkjsdhgoihrgolwihflskhfsgkh"
>    ```
>
> 3. python source 에서 위 데이터 사용
>
>    ```shell
>    token = config('TELEGRAM_BOR_TOKEN')
>    chat_id = config('CHAT_ID')
>    ```



#### a. html 에 form 작성

```html
<form action="/send">
    <input type="text" name="text">
    <input type="submit" value="메세지 보내기">
</form>
```

#### b. app.py 적성

```python
from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('text')
    requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={text}')
    return render_template('send.html')

if __name__ == "__main__":
    app.run(debug=True)
```



> 인증키 보안 part2
>
> git push 할때 일부 파일들을 제외할 수 있도록 gitignore 사용
>
> gitignore.io 에서 venv, Flask, Python, Windows, VisualStudioCode 입력 후 생성버튼을 누르면 텍스트 파일이 화면에 출력
>
> <img src="10_telegrambot.assets\image-20191220111748670.png" alt="image-20191220111748670" style="zoom:50%;" />
>
> 텍스트를 복사 후 .gitignore 파일 생성 후 붙여넣기
>
> .gitignore 를 github에 push



### 4. webhook 실습

>  ngrok 설치

https://ngrok.com/

download ngrok

> 실행

cmd 창을 열고

```shell
> ngrok.exe http 5000
```

<img src="10_telegrambot.assets\image-20191220132225212.png" alt="image-20191220132225212" style="zoom:80%;" />

Forwarding https://f9acff4a.ngrok.io <= 요거 사용



#### 텔레그램 setWebhook API 사용

> webhook.py 작성

```python
from decouple import config
import requests

token = config("TELEGRAM_BOT_TOKEN")
url = "https://api.telegram.org/bot"
ngrok_url = "https://f9acff4a.ngrok.io"

data = requests.get(f'{url}{token}/setWebhook?url={ngrok_url}/{token}')
print(data)
```

> webhook.py 실행

```shell
$ python webhook.py
<Response [200]>
```

200 (OK) 응답 오면 완료



### 5. 로또번호 보내기

> app.py 내용에 추가

```python
@app.route('/{token}', methods=["POST"])
def telegram():
    if text == "로또":
        numbers = range(1, 46)
        ret_text = sorted(random.sample(numbers, 6))
    else :
        ret_text = "'로또' 만 일력 가능합니다."

    requests.get(f'{url}{token}/sendMessage?chat_id={t_chat_id}&text={ret_text}')

	return "ok", 200
```



### 6. pythonanywhere

> webhook을 사용하여 로컬 작업하다가 외부에서도 사용할 수 있도록 pythonanywhere 사용해 봅니다.
>
> https://www.pythonanywhere.com/

가입 \> web 탭 \> add \> flask \> 3.7

Files 탭 \> mysite 폴더

작업중인 app.py 붙여넣기

web 탭 \> reload

console 탭 \> bash \> $ pip3 install python-decouple --user

files 탭 \> .env 생성 \> 작업중인 내용 붙여넣기

>  webhook.py 수정 및 재실행

```pyuthon
paw_url = "https://yongnimm.pythonanywhere.com"
```

```shell
$ python webhook.py 
<Response [200]>
```



### 7. 추후 따라해보기

https://steemit.com/kr/@sifnax/python-5-telegram-api

https://bourbonkk.tistory.com/33

http://henryquant.blogspot.com/2019/03/r_13.html