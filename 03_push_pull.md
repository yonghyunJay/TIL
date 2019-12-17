## git push pull



<img src="C:\Users\student\Desktop\git push pull.jpg" style="zoom: 50%;" />



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



