---
layout: post
title: "[Fluent Python] 5장 일급 함수"
description: " "
date: 2021-06-17
tags: [book]
comments: true
share: true
---

## 5장 일급 함수

"일급 객체로서의 함수"를 줄여서 "일급 함수"라고 한다.

일급 객체는 다음과 같이 정의한다.

* 런타임에 생성할 수 있다.
* 데이터 구조체의 변수나 요소에 할당할 수 있다.
* 함수 인수로 전달할 수 있다.
* 함수 결과로 반환할 수 있다.

## 고위함수(Higher-order function)

고위함수: 함수를 인수로 받거나, 함수를 결과로 반환하는 함수

```apply()```는 파이썬 2.3에서 중단이 예고되고, 파이썬3에서 제거되었다. ```apply(fn, args, kwargs)``` 대신 ```fn(*args, **kwargs)```로 작성하면 된다.

map(), filter(), reduce() 는 지능형 리스트나 제너레이터로 표현가능하고, 후자가 가독성이 더 좋다.

익명함수인 람다는 고위함수의 인수로 주로 이용된다. 그 외에는 가독성이 떨어져서 잘 쓰이지 않는다. 람다 본체에는 할당문이나 while, try 등을 사용할 수 없다.

## 콜러블 객체

콜러블 객체는 내장함수인 ```callable()```로 평가할 수 있다. 파이썬 데이터 모델 문서에 다음 일곱 가지 콜러블을 제시하고 있다.

* 사용자 정의 함수
* 내장함수
* 내장 메서드
* 메서드
* 클래스
* 클래스 객체: ```__call__()``` 메서드를 구현하면 쓸 수 있다.
* 제너레이터 함수

## 함수 인트로스펙션

객체 속성을 검사할 수 있다. 다음과 같은 코드로 함수와 일반 객체와 달리 추가적으로 가지고 있는 속성을 확인할 수 있다.

```python
>>> class C: pass
>>> obj = C()
>>> def func(): pass
>>> sorted(set(dir(func)) - set(dir(obj)))
```

위치매개 변수와 키워드 전용 매개변수: 함수에서 ```*``` 혹은 ```**```를 이용해서 다수의 매개변수를 받을 수 있다.

```inspect``` 모듈을 이용하면 좀 더 깔끔하게 매개변수를 알아내고 이용할 수 있다. ```signature``` 함수가 있다.

## 함수 애너테이션

함수 매개변수 뒤에 콜론(:)을 붙여서 애너테이션 표현식을 추가할 수 있다. 그리고 함수 괄호와 콜론 사이에 ```->```를 추가하여 리턴형을 써줄 수 있다. 하지면 현 시점에는 이들 정보는 메타 정보로만 저장될 뿐이고, 이 메타 정보를 활용하는 표준 라이브러리는 없다. 향후 형변환을 하거나, 인수를 변환하고 검증(예를 들어, > 0)할 때, 이용할 수 있다.

## 함수형 프로그래밍을 위한 패키지

operator와 functools를 이용하여 함수형 코딩 스타일을 이용할 수 있다.

```reduce()```함수를 이용하여, ```reduce(mul, range(1, n+1))```로 팩토리얼을 구현할 수 있다.

```itemgetter()```와 ```attrgetter()``` 함수를 이용하여 람다함수를 대체할 수 있다. ```itemgetter(1)```은 ```lamda fields: fields[1]```과 동일하다.

```methodcaller()```는 런타임에 함수를 생성할 수 있는데, ```functools.partial()```함수와 유사하게 일부 인수를 고정할 수 있다.

## 더 읽을거리

* [파이썬 3의 함수 애너테이션을 어디에 쓰면 좋을까?](http://bit.ly/1FHiOXf)
* [파이썬 함수 애너테이션은 어떤 장점이 있을까?](http://bit.ly/1FHiN5F)
* [파이썬에 functools.partial()이 필요한 이유는?](http://bit.ly/1FHiTdh)