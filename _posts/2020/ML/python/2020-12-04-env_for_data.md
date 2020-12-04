---
layout: post
title: "[python] 데이터 분석을 위한 파이썬 환경설정 "
description: " "
date: 2020-12-04
tags: [머신러닝]
comments: true
share: true
---

# 데이터 분석을 위한 파이썬 환경설정 

> ### 데이터 분석쪽은

* 개발IDE은 `jupyter notebook`

* 개발환경은 `anaconda` 가상환경을 만들어서 사용

  

## Anaconda

- 무료로 사용가능
- python과 다수의 유용한 package를 사용자가 사용하기 쉽게 제공해주는 플랫품



## jupyter notebook

* web 기반의 개발툴



## Anaconda 설치 및 가상환경 설정

1. [Anaconda](https://www.anaconda.com/products/individual)의 open source 버전을 다운로드 한다.
   
   * open source version = individual edition
   
2. Anaconda 설치한다.

3. Anaconda Prompt를 관리자 권한으로 실행한다.

4. 제일 먼저 해야 할 작업은 pip를 최신버전으로 upgrade부터 해야 한다.

  ```bash
  (base) python -m pip install --upgrade pip
  ```

5. 가상환경을 생성해야 해요!!

   ```bash
   (base) conda create -n data_env python=3.7 openssl
   ```

   * `-n` : name
   * `data_env` : 원하는 이름
   * `python=3.7` 이라는 option을 주지 않으면 최신버전이 깔린다. 
     * 최신버전은 tensorflow를 지원하지 않는다.
   * `openssl` : openssl 이라는 package도 포함해 다운로드
   * proceed([y]/n)? y

6. 정상적으로 가상환경이 만들어졌는지 확인해 보자.

   ```bash
   (base) C:\windows\system32>conda info --envs
   # conda environments:
   #
   base                  *  C:\ProgramData\Anaconda3
   data_env                 C:\ProgramData\Anaconda3\envs\data_env
   
   (base) C:\windows\system32>python -V
   Python 3.7.6
   ```

   * `conda info --envs ` : 모든 가상환경을 보여준다.
     * `envs` : environments
   * `python -V` :  python version 을 보여준다.
     * `-V` : 대문자이다 

7. 새로운 가상환경으로 전환해요

   ```bash
   (base) C:\windows\system32>activate data_env
   
   (data_env) C:\windows\system32>python -V
   Python 3.7.7
   ```

   * `activate data_env` : 가상환경`(base)` 에서 위에서 만든 가상환경 `(data_env)` 로 이동한다.
   * `python -V` : 각각의 가상환경의 python version이 다른것을 알수 있다.

   

## jupyter notebook 설치 및 설정

1. 개발 도구인 IDE중 하나인 jupyter notebook을 설치한다.

2. 현재 `data_env` 가상환경에서 jupyter notebook을 설치한다.

   ```bash
   (data_env) C:\windows\system32>conda install nb_conda
   ```

   * Proceed ([y]/n)?  y

3. jupyter notebook이 사용 할 기본 디렉토리(`working directory`)를 설정한다.

   이 작업을 하기 위해 환경설정파일을 하나 설정해서 기본 디렉토리를 지정해서 사용한다.

   * jupyter notebook --generate-config

     ```_bash
     (data_env) C:\windows\system32>jupyter notebook --generate-config
     Writing default config to: C:\Users\User\.jupyter\jupyter_notebook_config.py
     ```

     * configure 해주는 동시에 configure 파일의 경로를 알려준다.

4. config file을 수정해서 jupyter notebook의 working directory를 설정한다.

   ```bash
   #(269번째줄)
   c.NotebookApp.notebook_dir = 'C:/notebook_dir'
   ```

   * 269번째줄의 주석을 없애고 위와 같이 경로를 설정한다.
   * `C:/notebook_dir` : `C:/` 경로에 `notebook_dir` 폴더를 똑같이 만들어준다.

5. IDE를 실행시켜 보자.

   ```bash
   (data_env) C:\windows\system32>jupyter notebook
   ```

   ![실행](markdown-images/실행.PNG)

   * 위의 화면과 같이 `New` 를 눌러보면 `Python[conda env:data_env]`에 * 가 체크 되어 있는것을 볼수 있다.

6. 다음과 같이 코드를 작성하고 잘 작동하는 확인해보자.

   ![cell](markdown-images/cell.PNG)
   
   

## 기타

* exit() : 빠져나올때 