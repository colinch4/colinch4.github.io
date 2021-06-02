---
layout: post
title: "[python] String Formatting"
description: " "
date: 2021-06-02
tags: [python]
comments: true
share: true
---

# String Formatting

## format

- 문자열에 변수를 넣어 출력하는 형식

- `문자열.format(변수)`

### 예시

```python
year = 2020
month = 12
date = 14

print("오늘은 {}년 {}월 {}일 입니다.".format(year, month, date))
# 오늘은 2020년 12월 14일 입니다.

date_string = "오늘은 {}년 {}월 {}일 입니다."
print(date_string.format(year, month, date))
# 오늘은 2020년 12월 14일 입니다.
```

<br>

### 변수 순서를 지정

- `{숫자}` 0부터 카운터해야되고 지정할 시 모두 순서를 넣어줘야됨

```python
print("저는 {2}, {1}, {0}를 가장 좋아합니다.".format("피자", "치킨", "소고기"))
# 저는 소고기, 치킨, 피자를 가장 좋아합니다.
```

<br>

### 특정 변수를 반올림 하고싶을 때

- {:.`반올림 하고싶은 자릿수`f}

```python
  num_1 = 1
  num_2 = 3

  print("{} 나누기 {}은 {:.2f}입니다.".format(num_1, num_2, num_1 / num_2))
  # 1 나누기 3은 0.33입니다.
```

## 새로운 방식 f-string

- 파이썬 3.6버전 부터 쓸 수 있는 새로운 문자열 포멧팅

```python
name = "adam"
age = 29

print(f"제이름은 {name}이고 {age}살 입니다.")
# 제이름은 adam이고 29살 입니다.
```
