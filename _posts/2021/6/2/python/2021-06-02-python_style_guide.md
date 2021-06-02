---
layout: post
title: "[python] 추상화"
description: " "
date: 2021-06-02
tags: [python]
comments: true
share: true
---

# 추상화

## 상수 (constant)

> 프로그램에서 값이 바뀌지 않는 변수를 말한다.

### 대문자로 상수를 지정한다.

- ```python
  PI = 3.14
  ```
- Why?

  - 변수인지 상수인지 알아보기 위해서

  - 어떤일이 있더라도 수정하지 않겠다는 뜻.

<br>

## PEP 8 (파이썬 스타일)

### 이름 규칙

모든 변수와 함수 이름은 소문자로 쓰고, 여러 단어일 경우 `_`로 나눠 준다.

- ```python
    # 나쁜 예
    logicalVariableName = 314
    LogicalVariableName = 314

    def LogicalFunctionName():
        print("Hi Adam")

    # 좋은 예
    logical_variable_name = 314

    def logical_function_name():
        print("Hi Adam")
  ```

<br>

모든 상수 이름은 대문자로 쓰고, 여러 단어일 경우 `_`로 나눈다.

- ```python
    SOME_CONSTANT = 192
  ```

<br>

### 의미있는 이름

의미있게 변수명을 지어 가독성이 편리하도록 한다.

```python
radius = 2
pi = 3.14
print(pi * radius * radius)

def say_hello():
    print("Hello, World")
```

<br>

### 화이트 스페이스

들여쓰기는 무조건 4개를 사용한다.

```python
def say_hello():
    print("Hello, World")

```

<br>

### 함수 정의

함수 정의 위아래로 빈줄이 2개있어야된다. 하지만 파일의 첫줄의 함수인 경우, 해당 함수 위에는 빈줄이 없어도 된다.

```python
def first():
    print(1)
#
#
def second():
    print(2)
#
#
def third():
    print(3)
```

<br>

### 괄호 안

괄호안에는 띄어쓰기를 하지 않는다.

```python
# 나쁜 예
hamberger( patty[ 1 ], { eggs: 2 } )


# 좋은 예
hamberger(patty[1], {eggs: 2})
```

<br>

### 함수 괄호

함수를 정의하거나 호출할 때, 함수 이름과 괄호 사이에 띄어쓰기 하지 않는다.

```python
# 좋은 예
def hamberger (x):
    print (x + 2)


spam (1)


# 나쁜 예
def hamberger(x):
    print(x + 2)


spam(1)
```

<br>

## 쉼표

쉼표 앞에는 띄어쓰기를 하지 않는다.

```python
# 좋은 예
print(x , y)


# 나쁜 예
print(x, y)
```

<br>

### 지정 연산자

지정 연산자 앞뒤로 한칸만 띄어쓰기를 한다.

```python
# 나쁜 예
a=1
a        =  3


# 좋은 예
a = 1
```

### 연산자

기본적으로 연산자 앞뒤로 띄어쓰기를 한칸씩만 한다.

```python
# 나쁜 예
a=a+3
hamberger +=3


# 좋은 예
a = a + 3
b += 3
```

하지만 연산의"우선 순위"를 강조하기 위해 연산자 앞뒤를 붙이는 것을 권장한다.

```python
# 나쁜 예
a = a * 2 - 1
wifi = x * x + y * y
c = (a + b) * (a - b)


# 좋은 예
a = a*2 - 1
wifi = x*x + y*y
c = (a+b) * (a-b)
```

<br>

### 코멘트

일반 코드와 같은 줄에 코멘트를 사용할 경우, 코멘트 앞에 띄어쓰기를 최소 2개를 해준다.

```python
# 나쁜 예
x = x + 1# 코멘트


# 좋은 예
x = x + 1  # 코멘트
```

<br>

## Reference

- [코드잇 파이썬 프로그래밍 기초](https://www.codeit.kr/courses/intro-to-python-programming)
