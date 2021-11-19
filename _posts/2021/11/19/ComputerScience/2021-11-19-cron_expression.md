---
layout: post
title: "[CS] Cron Expression"
description: " "
date: 2021-11-19
tags: [CS]
comments: true
share: true
---

# Cron Expression
크론 표현식

### Table of Contents
- [Cron Expression](#cron-expression)
    - [Table of Contents](#table-of-contents)
  - [About Cron Expression](#about-cron-expression)
    - [Syntax](#syntax)
    - [Examples](#examples)

## About Cron Expression
크론 표현식은 스케쥴 기반으로 프로그래밍을 하고자 할 때 유용하게 쓰인다.  
- 특정 작업을 주기적으로 실행 시키고자 할 때 사용.

**예)**  
  AWS CloudWatch에서 Cron Expression을 통해 Events 에 스케쥴을 걸어줄 수 있다.  
  <img width="600" alt="Screen Shot 2020-08-04 at 7 03 31 PM" src="https://user-images.githubusercontent.com/48475824/89281549-37992800-d685-11ea-9781-0fcd5624c8ca.png">

  CloudWatch에서 '매주 월요일 0시 0분 0초' 스케쥴링을 건 결과 모습  
  <img width="542" alt="cron every monday" src="https://user-images.githubusercontent.com/48475824/89363538-6954d200-d70b-11ea-88bc-420dd450d3ca.png">  

  만약 잘 못된 cron expression을 입력한다면 예상 ```Trigger Date``` 이 보이지 않으며 다음 스탭을 진행하는 과정에서 아래와 같은 오류를 만나게 된다.  

  <img width="495" alt="invalid cron expression" src="https://user-images.githubusercontent.com/48475824/89363620-9ef9bb00-d70b-11ea-8e3f-1e92dd9cf7d9.png">

  Error Message : ```Parameter ScheduleExpression is not valid```

**[Fields]**  
크론 표현식은 보통 6~7 개의 필드가 사용된다.  
```sql
* * * * * * * 
1 2 3 4 5 6 7
```
* 1 번째 필드  
  초 Second
* 2 번째 필드  
  분 Minute
* 3 번째 필드  
  시 Hour
* 4 번째 필드  
  일 Day  
* 5 번째 필드  
  월 Month
* 6 번째 필드  
  주 Week  
  요일은 숫자와 문자로 표현 가능하다.  
    * 0-6
    * SUN-SAT (case-insensitive)
* 7 번째 필드 (Optional)  
  년 Year

이를 알기 쉽게 이미지로 표현하자면 아래와 같다.  

<img width="550" alt="Screen Shot 2020-08-04 at 6 56 39 PM" src="https://user-images.githubusercontent.com/48475824/89280929-47643c80-d684-11ea-8c2c-b80b1264c4d4.png">


[↑ return to TOC](#table-of-contents)


### Syntax  
크론 표현식의 문법을 자세히 살펴보자.  

* **\***  
  모든 값  
  예) 초 자리에 위치했을 시 '매 초(ever second)' 를 의미
* **-**  
  범위를 지정해 줄 때   
  예) 1시부터 3시까지   
* **?**  
  특정값이 없을 때  
* **,**  
  여러 값(Mutiple Values)를 지정해 줄 때  
  예) ```MON, WED, FRI``` '월, 수, 금 마다'를 의미  
* **L**  
  Last 마지막을 의미  
  예) ```3L``` '달의 마지막 수요일'을 의미
* **W**  
  Weekday (Mon-Fri) 가장 가까운 평일  
  예) ```12W``` '이달의 12일과 가장 가까운 평일' 을 의미  
* **#**  
  Day of Week 몇번째 특정 요일  
  예) ```0#3``` '세번째 주 일요일'을 의미  
* **\/**   
  증가 값  

[↑ return to TOC](#table-of-contents)



### Examples  
```
0 0 0 ? * SUN * 
```
└─ At 12:00 AM, only on Sunday

```
0 0/10 * * * *
```
└── Every 10 Minutes  

```
0 24 ? * MON-FRI
```
└── At 12:00 PM, Monday through Friday

```
0 30 10 12 * ?
```
└── At 10:30 AM, on day 12 of the month

```
0 0 0 * * ? 2022
```
└── At 12:00 AM, only in 2022

```
0 0 11 L-1 * ?
```
└── At 11:00 AM, 1 days before the last day of the month


[↑ return to TOC](#table-of-contents)
