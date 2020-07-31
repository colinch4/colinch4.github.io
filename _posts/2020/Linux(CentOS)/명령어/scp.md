## scp

- Secure copy
- ssh를 이용해 네트워크로 연결된 호스트간에 파일을 주고받는 명령어

### 사용법

- ```shell
  $ scp [options ...] [source] [target]
  ```

  - sourec, target은 원격, 로컬 어느 것이든 상관없다



#### 옵션

- -r : 재귀적으로 모든 폴더들을 복사. 보통 폴더를 복사하기 위해 사용
- -P : ssh 포트 지정
- -i : ssh키파일과 같은 idendity file의 경로를 지정하는 옵션
- -v : verbose모드로 상세내용을 보며 디버깅할때 사용
- -p : 파일의 수정 시간과 권한 유지

## 예제

### 로컬 -> 리모트

- 패스워드 사용하는 경우

``` shell
$ scp ~/test.txt twpower@[IP주소]:/home/twpower
```

- `-i` 옵션
- identity file을 지정해서 사용할 때

``` shell
$ scp -i ~/.ssh/twpower-private-server ~/test.txt twpower@[IP주소]:/home/twpower
```

- `-r` 옵션
- 폴더를 복사하는 경우

``` shell
$ scp -r ~/test_folder/ twpower@[IP주소]:/home/twpower
```

- `-P` 옵션

``` shell
$ scp -P 22 ~/test.txt twpower@[IP주소]:/home/twpower
```



### 리모트 -> 로컬

- 패스워드 사용하는 경우

``` shell
$ scp twpower@[IP주소]:/home/twpower/test.txt /Users/taewoo
```

- `-i` 옵션
- identity file을 지정해서 사용할 때

``` shell
$ scp -i ~/.ssh/twpower-private-server twpower@[IP주소]:/home/twpower/test.txt /Users/taewoo
```

- `-r` 옵션
- 폴더를 복사하는 경우

``` shell
$ scp -r twpower@[IP주소]:/home/twpower/test_folder /Users/taewoo
```

- `-P` 옵션

``` shell
$ scp -P 22 twpower@[IP주소]:/home/twpower/test.txt /Users/taewoo
```

