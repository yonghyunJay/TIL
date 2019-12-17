## git push pull

> (학습 참고1) [@devzunky]([https://velog.io/@devzunky/wecode-TIL-6%EC%9D%BC%EC%B0%A8-Git-Basic-2-5xk1dcgfob](https://velog.io/@devzunky/wecode-TIL-6일차-Git-Basic-2-5xk1dcgfob))
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



