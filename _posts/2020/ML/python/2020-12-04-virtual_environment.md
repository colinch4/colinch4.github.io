---
layout: post
title: "[파이썬] 파이썬 가상 환경"
description: " "
date: 2020-12-04
tags: [파이썬]
comments: true
share: true
---

## 파이썬 가상 환경

> 프로젝트별로 서로 다른 패키지의 버전이 요구되는 경우 반드시 필요

[참고문헌](https://docs.python.org/ko/3/tutorial/venv.html)

## 사용법

* 가상환경 생성

  * `venv` 라는 이름의 가상환경을 생성

  ```bash
  $ python -m venv {가상환경이름}
  $ python -m venv venv
  ```

  * 가상환경을 생성하는 해당 디렉토리에 `venv` 폴더가 생성된다.

* 가상환경 실행

  ```bash
  $ source ven/Scripts/activete      # git bash용
  $ source ven/Scripts/activete.bat  # cmd용
  $ source ven/Scripts/activete.psl  # 파워쉘 용
  
  (venv) $
  ```

  * 가상환경을 실행시킨 상태에서 파이썬 패키지(pip)를 설치하게 되면 venv 폴더의 Lib폴더에 설치를 하게 된다.
  * 해당 프로젝트를 위한 패키지들을 따라 관리 가능하다.



## pip

```bash
## requirements.txt 설치된 패키들을 설치
$ pip freeze > requirements.txt
```



### 참고사이트

