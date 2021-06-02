---
layout: post
title: "[python] Optional Parameter"
description: " "
date: 2021-06-02
tags: [python]
comments: true
share: true
---

# Optional Parameter

파라미터에게 '기본값(default value)을 설정할 수 있는데, 기본 값을 설정해 두면, 함수를 호출할 때 꼭 파라미터 값을 안줘도 된다. 이런 파라미터를 `옵셔널 파라미터(optional parameter)` 라고 한다.

## 예시

```python
def myProfile(name, age, gender="male"):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("성별은 {}이다".format(gender))

# optional parameter를 제공하지 않는 경우
myProfile("Adam", 29)

# 내 이름은 Adam
# 나이는 29살
# 성별은 male이다

# optional parameter를 제공하는 경우
myProfile("Adam", 29, "female")

# 내 이름은 Adam
# 나이는 29살
# 성별은 female이다

```

## 옵셔널 파라미터는 꼭 마지막에

옵셔널 파라미터를 마지막에 넣지 않으면 오류가 나온다. 그래서 꼭 위치는 마지막이어야 된다.

## Reference

- [코드잇 프로그래밍 기초 in Python](https://www.codeit.kr/dashboard)
