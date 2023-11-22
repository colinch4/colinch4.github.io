---
layout: post
title: "[파이썬] 로지스틱 회귀(Logistic Regression)"
description: " "
date: 2021-09-16
tags: [python]
comments: true
share: true
---

## 로지스틱 회귀(Logistic Regression)

로지스틱회귀는 범주형 변수를 예측하는데 쓰이는 모델이다

선형회귀는 설명변수, 종속변수가 연속형, 수치형이여야 좋은 결과를 가져올 수 있다.

그에 반에 범주형 변수에 대해선 안좋은 결과를 가져올수밖에없다.

이러한 문제 때문에 로지스틱 회귀 모델이 제안되었다.

## 1. 로지스틱 함수, Odds

**로지스틱함수(Logistic Function), 승산(Odds)**을 먼저 알아보자, 로지스틱 회귀의 뼈대가 되는 것들이다

실제로 많은 데이터들은 특정 변수에 대한 확률값이 선형이 아닌 **S-curve type** 을 따르는 경우가 많다. 이러한 **S-curve** 를 표현해낸 것이 바로 로지스틱 함수이다. 상황, 분야에 따라 **시그모이드함수**라고 불리기도 함.

**로지스틱 함수**는 x값으로 어떤 값이든 받을 수가 있지만 출력결과는 항상 0에서 1사이의 값이 된다.즉, **확률밀도함수(probability density function)** 요건을 충족시키는 함수이다.

확률밀도함수(probability density function)의 식과 그래프모양이다.


$$
y=\frac{1}{1+e^-x}
$$


![http://i.imgur.com/E0eI8OU.png](C:\Users\sungyun\Desktop\etc\img\probability density function.png)



**승산(Odds)** 이란 임의의 사건 A가 발생하지 않을 확률 대비 일어날 확률의 비율을 뜻하는 개념이다. 아래와 같은 식으로 쓸 수 있다.
$$
odds = \dfrac{P(A)}{P(A^c)} = \dfrac{P(A)}{1-P(A)}
$$


P(A)가 1에 가까울 수록 그래프는 치솟는다. P(A)가 0이라면 0이 된다. 아래 그래프 참조하자

![](C:\Users\sungyun\Desktop\etc\img\odds(승산).png)

## 2. 이항 로지스틱 회귀

범주가 두 개인 분류문제를 풀어야 할 시,  위에서 설명했듯이 **종속변수 Y가 연속형 숫자가 아닌 범주일 때는 기존 회귀 모델을 적용할 수 없다.**

문제를 바꿔서 풀어야한다. 회귀식의 장점은 그대로 유지하되 종속변수 Y를 범주가 아니라 범주1이될 확률로 두고 식을 세워 풀어간다. 우변(X)은 그대로 두고 좌변만 확률로 바꾸자
$$
P(Y = 1 | X = \overrightarrow{x}) = \beta_1 + \beta_1x_1 + \beta_2x_2 ... +\beta_px_p
$$





