---
layout: post
title: "[data] 디자인 패턴인 MVC, MVP, MVVM을 비교"
description: " "
date: 2021-06-02
tags: [data]
comments: true
share: true
---

1. [MVC, MVP, MVVM](#-mvc,-mvp,-mvvm-비교-조사)
2. [반복자(iterator)와 for문의 차이점](<#-반복자(iterator)와-for문의-차이점>)

<br>

<br>

# MVC, MVP, MVVM 비교 조사

### 디자인 패턴인 MVC, MVP, MVVM을 비교

- **M : Model**
  - 어플리케이션에서 사용되는 데이터와 그 데이터를 처리하는 부분
- **V : View**
  - 사용자에게 보여지는 UI 부분
- **C : Controller**
  - 사용자의 입력(Action)을 받고 처리하는 부분
- **P : Presenter**
  - View에서 요청한 정보로 Model을 가공하여 View에 전달해 주는 부분
  - View와 Model을 붙여주는 접착제 역할
- **VM : View Model**
  - View를 표현하기 위해 만든 View를 위한 Model
  - View를 나타내 주기 위한 Model이자 View를 나타내기 위한 데이터 처리를 위한 부분

이렇게 역활을 나뉘는 이유는 각각의 역할을 나누어 관리하기 쉽고 유지보수에 용이하도록 한 것인데요, 이제 각 패턴들에 대해 비교해보도록 하겠습니다.

<br>

## 1. MVC

### MVC

- MVC 패턴은 Model + View + Controller 를 합친 용어입니다.

  ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/852124aa-7971-435e-969b-70a77fe0b085/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/852124aa-7971-435e-969b-70a77fe0b085/Untitled.png)

  MVC 패턴 구조

### 동작

1. 사용자의 Action들은 Controller에 들어옵니다.
2. Controller는 사용자의 Action을 확인하고, Model을 업데이트 합니다.
3. Controller는 Model을 나타내줄 View를 선택합니다.
4. View는 Model을 이용하여 화면을 나타냅니다.

### 특징

- Controller는 여러개의 View를 선택할 수 있는 1:n 구조(일대다)
- Controller는 View를 선택할 뿐 직접 업데이트 하지 않는다.(View는 Controller를 알지 못한다.)

<br>

## 2. MVP

### MVP

- MVP 패턴은 Model + View + Presenter를 합친 용어
- Model과 View는 MVC와 동일하나 Controller 대신 Presenter가 존재한다.

  ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/740ed9d2-1f54-4827-9584-4077eff2bae7/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/740ed9d2-1f54-4827-9584-4077eff2bae7/Untitled.png)

  MVP 구조

### 동작

1. 사용자의 Action들은 View를 통해 들어오게 됩니다.
2. View는 데이터를 Presenter에 요청합니다.
3. Presenter는 Model에게 데이터를 요청합니다.
4. Model은 Presenter에서 요청바든 데이터를 응답합니다.
5. Presenter는 View에게 데이터를 응답합니다.
6. View는 Presenter가 응답한 데이터를 이용하여 화면을 나타냅니다.

<br>

## 3. MVVM

### MVVM

- Model + View + View Model를 합친 용어
- Model과 View는 다른 패턴과 동일하다.

  ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e865b478-5803-41d9-a92a-aaf2826d7b0e/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e865b478-5803-41d9-a92a-aaf2826d7b0e/Untitled.png)

### 동작

1. 사용자의 Action들은 View를 통해 들어오게 됩니다.
2. View에 Action이 들어오면, Command 패턴으로 View Model에 Action을 전달합니다.
3. View Model은 Model에게 데이터를 요청
4. Model은 View Model에게 요청받은 데이터를 응답
5. View Model은 응답 받은 데이터를 가공하여 저장
6. View는 View Model과 Data Binding하여 화면을 나타냄

[디자인 패턴 비교](https://www.notion.so/1bf6e220045c4b3e8fcfc2960edeac73)

<br>

<br>

# 반복자(iterator)와 for문의 차이점

## Iterator

이터레이터는 값을 순차적으로 꺼내올 수있는 객체입니다.

## For 문

이터러블 객체를 순회할 때 사용하는 반복문

- For문을 활용한 순차적 순회

```python
a = [1, 2, 3]

for i in a:
	print(i)

# Out:
# 1
# 2
# 3
```

- Iterator 객체를 이용한 순차적 순회

```python
a = [1, 2, 3]
iterator_a = iter(a)

print(next(iterator_a))
print(next(iterator_a))
print(next(iterator_a))

# Out:
# 1
# 2
# 3
```

- 위의 예시를 통해 for문은 반복가능한 객체를 한번에 순회하지만, iterator는 한 루프만 사용하여 반복을 할 수 있습니다.
- 또한 Iterator의 경우 객체를 가져오는 과정이 있다보니 For 문보다는 성능이 좋지는 않다.
