---
layout: post
title: "[python] 기본 개념"
description: " "
date: 2021-06-02
tags: [python]
comments: true
share: true
---

# 기본 개념

<br>

## 추상화(Abstraction)

> 복잡한 내용은 숨기고, 주요기능에만 신경 쓰는 것을 추상화(Abstraction)이라 한다.

추상화에는 3가지있다.

- 변수 (Variable)

- 함수 (Function)

- 객체 (Object)

### 변수 (Variable)

> 값을 저장하는 것

```python
basic = "basic"
one = 1234
```

- 여기서 `=` 등호는 프로그래밍에서 등호연산자라고 하여 오른쪽에있는 변수를 등호 왼쪽에 있는 변수에 지정한다는 뜻.

### 함수 (Function)

> 명령을 저장하는 것

- 내장 함수 : 자주쓰이는 함수들을 미리 구현해 놓은 것.

- syntax

  ```python
  def 함수이름():
      code..

  함수이름()
  ```

### return 문의 역할

- 함수 즉시 종료하기

- 값 돌려주기

<br>

## 자료형

### 숫자형

- floor division(버림 나눗셈) : 나머지는 버리고 나누어지는 숫자만 리턴 (단 소수가 있으면 소수로 리턴 ex. 3.0 // 2 = 1.0)

- round (반올림)

  ```python
  print(round(3.141592))    # 3

  # round(소수, 반올림하고싶은 소수의 자릿수)
  print(round(3.141592, 2))   # 3.14
  ```

### 문자형

- "" 또는 '' 로 감싸져 있는 것 들을 문자형이라 한다.

- 문자열안에 `'` 있거나 `"`를 넣고싶을 때

  - `\'` 역슬래쉬를 옆에 붙이면 오류없이 출력

  - `"""` 문장 `"""` """ (따움표) 3개씩 양쪽에 붙이면 된다
