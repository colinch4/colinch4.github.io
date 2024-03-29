---
layout: post
title: "[파이썬] VS Code에서 Jupyter 돌리기"
description: " "
date: 2021-06-17
tags: [python]
comments: true
share: true
---

## VS Code에서 Jupyter 돌리기

## 배경

데이터 과학이라는 이름 하에 엑셀을 탈피해서 python 환경으로 넘어 오려는 시도를 하고 있다.
RStudio와 유사한 환경이 필요한데, 썩 마음에 드는 조합이 없다.

Jupyter 프로젝트가 딱 원하는 형태이나, 웹 브라우저에서 작업을 하다보니, 반응도 느리고, 무엇보다 자동완성같은 IDE 기능이 매우 취약하다.

JetBrains사의 Pycharm이 가장 좋은 선택일 것이라고 생각했으나, 다소 무거운 환경과, 몇 달만에 열어본 Jupyter 노트북 파일이 안 열리고 계속 프리징 상태로 머물고 있어서, 최근 관심있게 사용하고 있는 VS Code 상에서 환경을 구축해보고자 하였다.

## 설치 방법

설치 방법은 간단하다.

* Anaconda 배포판
  * 설치시 Program Files 아래에 설치되지 않도록 하자, 경로에 스페이스 포함된 것 때문에 피곤하다.
* VS Code의 Extensions: Jypyter, Python (Don Jayamanne), MagicPython
* VS Code 상에서 설정 메뉴에 들어가서, python 경로를 잡아줘야 한다.
  * 예시: `"python.pythonPath": "c:/Anaconda3/python.exe"`

## 장점과 한계

Jupyter 환경이라는 점에서 셀 단위로 실행이 가능하고, pandas 테이블이나 matplot 같은 그래프를 그려서 바로 볼 수 있다.

반면 완벽한 Jupyter 환경이 아니기 때문에, 코드 외에 다른 요소를 넣을 수가 없다. 노트북은 코드와 문서를 일체화하여 그 자체로 하나의 보고서가 되도록 하는 데 목적이 있는 반면, VSCode 상에서는 이러한 목적을 이루기가 어렵다.

그러나 이러한 단점은 한편으로 장점이 되기도 한다. ipynb 파일형태를 쓰지 않고, py 형태로 직접 코드를 사용하기 때문에, 버전 관리가 쉽고 가볍다.(ipynb 파일 같은 경우, 실행결과를 함께 저장하고 있어, 돌릴 때마다 라인번호가 바뀌거나 하면, 실제 코드가 바뀌지 않았음에도 불구하고, 파일 변경이 발생한다.)

<vue-disqus/>
