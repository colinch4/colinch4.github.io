---
layout: post
title: "[리눅스] grep 명령어 정리"
description: " "
date: 2021-01-14
tags: [linux]
comments: true
share: true
---


## grep

리눅스 상에서 파일과 관련 된 검색을 하기 위해서 크게 쓰이는 명령어는 `find` , `grep` 이다.<br>`find` 는 파일을 검색할 때 쓰이는 명령어이고, `grep` 은 파일 내부의 문자열을 검색하기 위해 쓰인다. grep에 대해 조금 더 구체적으로 알아보자.

man grep을 해보면, <br>The grep utility searches any given input files, selecting lines that match one or more patterns.<br>이라고 나온다. 

grep을 통해서 파일 내부의 문자열을 검색해서, 찾고자 하는 문자열과 동일한 문자열을 가진 파일을 찾아주는 것이다.<br>명령어의 문법은 다음과 같다.

```
grep [-옵션] 문자열패턴 대상파일
```

### 옵션의 종류

- **-c :** 패턴이 `일치하는 행의 수` 를 출력 
- **-i :** 비교시 `대소문자를 구별 안함` 
- **-v : **지정한 `패턴과 일치하지 않는 행` 만 출력 
- **-n :** `파일의 이름` 과 `행의 번호` 를 함께 출력 
- **-l : **패턴이 포함된 `파일의 이름` 을 출력 
- **-w :** 패턴이 `전체 단어와 일치` 하는 행만 출력 
- **-r** : 현재 디렉토리 및 서브 디렉토리를 모두 살펴봄. <br>-r만 쓰면 일치하는 파일명만 나오는데, 일치하는 패턴을 담고 있는 행의 번호를 나타내는 -n옵션을 추가해 `-rn` 을 사용하면 파일명과 일치하는 행의 번호를 모두 확인할 수 있다.



### 문자열 패턴의 정규표현식

```shell
$ grep '^a' 파일명 
= ^는 파일의 시작을 나타냄. 파일에서 a로 시작하는 행을 찾는다. 

$ grep 'apple$' 파일명
= $는 파일의 끝을 나타냄. 파일에서 e로 끝나는 행을 찾는다. 

$ grep 'app*' 파일명 
= 파일에서 app로 시작하는 모든 단어를 찾는다. 

$ grep 'a.....e' 파일명 
= 파일에서 a로 시작하고 e로 끝나는 7자리 단어를 찾는다. 

$ grep [a-d] 파일명 
= 파일에서 a,b,c,d 로 시작하는 단어를 모두 찾는다. 

$ grep [aA]pple 파일명 
= 파일에서 apple 또는 Apple로 시작하는 단어를 모두 찾는다.

$ grep 'apple' d*
= d로 시작하는 모든 파일에서 apple 를 포함하는 모든 행을 찾는다. 

$ grep 'apple' 파일명1 파일명2 
= 지정된 두개의 파일에서 apple 를 포함하는 모든 행을 찾는다. 

$ grep '^[ab]' 파일명 
= 파일에서 a나 b로 시작되는 모든 행을 찾는다. 
```





### 참고URL

[grep & find 계열 명령어](http://pelican7.egloos.com/v/1471855)<br>[Unix/Linux 문자열 패턴 검색 (grep)](http://ra2kstar.tistory.com/100)<br>[리눅스 파일 검색 (find), 파일 내부 문자열 검색(grep 이용)](http://ngee.tistory.com/83)