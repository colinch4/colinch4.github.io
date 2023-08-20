---
layout: post
title: "[파이썬] 2. 깃허브 보충"
description: " "
date: 2021-06-18
tags: [파이썬]
comments: true
share: true
---


## 파이썬(2) 0121

## Github

### (1)  깃허브 보충

- git 사용
  1. 폴더 ~/TIL
  2. `git` 으로 관리되는 폴더 아래에는 새로운 `git` 이 있으면 안된다.
  3. `git` 은 무조건 최상위 폴더에 하나만 있어야 한다.
  4. `git init` 명령어를 치면 `.git` 폴더가 생긴다.
  5. 하나의 기능을 가진 프로젝트를 하나의 `git` 으로 만들어라.
- 타이포라
  1. 이미지 설정 경로 - 설정에서 바꿔야함



### (2) Git bash 명령어

- 명령어

  - `vi .bashrc`  

    >  jupyter notebook 쓰기 귀찮아서 약어로 쓰려고 

    - `i` 끼워넣기 : 입력모드
    - `alias  jn="jupyter notebook"` 입력 ( = 사이에 공백 넣지 말 것 )
    - Esc 누르면 끼워넣기 모드 해제됨
    - `:`  vim 창에게 옵션 주는 것

  - ```shell
    $ cd ~
    $ vi .bashrc
    
    # vim 창으로 이동 후
    i		# insert 모드
    alias jn="jupyter notebook"
    Esc		# insert 모드 해제
    : wq		# vim 에게 옵션주기
    
    source ~/.bashrc		# 변경사항을 터미널에 반영하기
    
    # 숙제 깃랩이랑 깃허브에 한꺼번에 보내기
    # bash 창에서 ssafy 명령어 치면 이제 숙제 두개 다 업로드 가능해짐.
    alias ssafy="git push origin master && git push hub master"
    ```

  - `cat .bash_history`  : .bash_history 파일 내용 보기

  - `source` : 변경사항 반영

  - `vim` : **vim adventure** 게임으로 vim 명령어 익히기 가능...



- 숙제 github 와 gitlab 으로 동시에 보내기

  ```shell
  $ vi. bashrc
  
  alias ssafy="git push origin master && git push hub master"
  ```




- 숙제 받아오기

```shell
## master_pyhton 에서 pull 해서 파일 받아오고
## /python 파일로 옮겨서 사용한다.

$ cd ~/master_pyhton
$ ls    # 현재 디렉토리에 파일 확인
$ git pull origin master    # 깃허브에서 remote 저장소인 master_python 내용 pull 해옴
$ ls    # pull 해온거 확인

$ cd ~/python
$ cp ~/master_python/02.~~ .    # master_python 폴더내에 02.~~ 파일을 . 현재 폴더에 복사
```





## 파이썬 기본 문법(2)

### 1. 연산자

- 산술 연산자

  - divmod(a, b)

    - a를 b로 나눈 몫과 나머지 리턴

    - ```python
      quotient, remainder = divmod(5, 2)    # 몫과 나머지를 리턴함
      print(quotient)
      print(remainder)
      ```

- ㅇ



### 2. 형변환 (데이터 타입 변환)

- 기초 형변환
  - 
- 암시적 형변환
  - 
- 명시적 형변환
  - 





### 3. 시퀀스  / 비시퀀스 자료형

1. 리스트
2. 튜플
   - 파이썬이 파이썬스럽게 하도록 만든 자료형
3. 딕



- **숫자 0 이 6개 있는 list 를 만들어봅시다. (  )**

  - ```
    [0] * 6
    ```



- 저장
  - 어떻게(연산자) : =
  - 무엇을(데이터타입 == 자료형)
    - 숫자
    - 글자
    - bool
  - 어디에(변수 / 컨테이너)
    - 변수
    - 시퀀스형 자료 - string, tuple, list, range   `순서가 있다.`
    - 비시퀀스형 - dict, set `순서가 없다.` 



- **식(expression) & 문(statement)**

  - 식(expression)

    - value(값) & operator(연산자)

    - evaluate (연산자를 통한 값의 평가)

    - `*변수에 할당가능` (== 변수에 바인딩 가능)

    - 예시

      ```python
      ex)
      1 + 2
      True and False
      ```

      

  - 문(statement)

    - expression(식) 으로 구성.. 
    - 변수에 할당불가
    - 세미콜론 포함( : )



## 스코프

![image-20200124131350543](img/image-20200124131350543.png)















## **TDD ( Test Driven Development )**

- 하재승 ( 던파를 3배 빠르게 한 남자.... )







