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



### 3. sendMessage 실습1

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
> <img src="C:\Users\YH\TIL\10_telegrambot.assets\image-20191220111748670.png" alt="image-20191220111748670" style="zoom:50%;" />
>
> 텍스트를 복사 후 .gitignore 파일 생성 후 붙여넣기
>
> .gitignore 를 github에 push



