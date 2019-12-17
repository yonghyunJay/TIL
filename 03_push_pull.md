## git push pull

> (학습 참고1) [devzunky](https://velog.io/@devzunky/wecode-TIL-6일차-Git-Basic-2-5xk1dcgfob)
>
> (학습 참고2) [duzum](https://duzun.me/tips/git)



### 1. Working side

`b.txt` 파일 생성 후 remote repo. 에 push

```shell
$ touch b.txt

$ git add b.txt

$ git commit -m "Add b.txt"

$ git remote add origin https://github.com/yonghyunJay/test_project.git

$ git push origin master
```



### 2. Home side

remote repo. 의 내용을 내여받고, `c.txt` 파일 생성 후 push

``` shell
$ git clone https://github.com/yonghyunJay/test_project.git

$ git add c.txt

$ git commit -m "Add c.txt"

$ git push origin maste
```



### 3. Working side again

Home side 에서 update 된 내용을 내려받음

``` shell
$ git pull origin master
```



### 4. push pull 2인 연습 - 끝말잇기

#### 1. `README.md` 생성 및 push

``` shell
$ git init

(README.md 추가)

$ git add README.md

$ git commit -m "Add README.md"

$ git remote add origin http://github.com/yonghyunjay/wordchain.git

$ git push origin master

```



#### 2. 팀원 권한 부여

팀원이 해당 내용 clone 받고 수정 후 push하면 실패 -> 권한 부여 필요

1. 해당 repo. 의 setting > collaborators 설정에서 초대장 발급
2. 팀원이 초대 수락



#### 3. 업데이트 내용 pull

``` shell
$ git pull origin master
```

