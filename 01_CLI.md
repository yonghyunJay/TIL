# CLI

커맨드 라인 인터페이스

## 터미널 명령어들

- `ls` : 폴더 내부의 파일 & 폴더를 나열
- `ls -a` :  숨긴 폴더도 함께 나열
- `pwd` : 현대 폴더 경로 출력
- `mkdir [폴더명]` : 폴더 생성
- `cd [폴더명]` : 폴더 변경
- `cd ..` : 상위 폴더 이동
- `touch [파일명]` : 파일 생성
- `rm [파일명]` : 파일 삭제



``` shell
$ git --version
```

``` shell
$ git init
```

``` shell
$ git status
```

``` shell
$ git add [파일명]
```

``` shell
$ git commit
```

``` shell
$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"
```

email -> github 에 가입된 메일

``` shell
$ git commit -m "first commit"
```

``` shell
$ git log
```



``` shell
$ git checkout (commit log 의 앞 5자리)
```

``` shell
$ git checkout master
```



``` shell
$ git remote add origin https://github.com/yonghyunJay/TIL.git
```

origin : 저장소의 첫번째 별명 (자동)

위 동작 확인

``` shell
$ git remote -v
```

``` shell
$ git push origin master
```

and 로그인

