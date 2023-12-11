---
layout: post
title: "[sql] 날짜 및 시간을 다루는 스칼라 함수 (DATE, YEAR, MONTH, DAY, HOUR, MINUTE 등)"
description: " "
date: 2023-12-11
tags: [sql]
comments: true
share: true
---

날짜 및 시간을 다루는 데 스칼라에서 많은 함수를 사용할 수 있습니다. 이러한 함수를 사용하여 날짜 및 시간을 추출하거나 형식을 지정할 수 있습니다.

## DATE 함수

`DATE` 함수는 날짜 부분만 반환합니다. 예를 들어, 다음 코드는 오늘의 날짜를 반환합니다.

```scala
SELECT DATE(current_date())
```

## YEAR, MONTH, DAY 함수

`YEAR`, `MONTH`, `DAY` 함수를 사용하여 날짜에서 연도, 월, 일을 추출할 수 있습니다.

```scala
SELECT YEAR('2022-06-15'), MONTH('2022-06-15'), DAY('2022-06-15')
```

## HOUR, MINUTE, SECOND 함수

`HOUR`, `MINUTE`, `SECOND` 함수는 시간에서 시, 분, 초를 추출합니다.

```scala
SELECT HOUR('14:30:00'), MINUTE('14:30:00'), SECOND('14:30:00')
```

## DATE_FORMAT 함수

`DATE_FORMAT` 함수를 사용하여 날짜 및 시간 형식을 지정할 수 있습니다.

```scala
SELECT DATE_FORMAT('2022-06-15', 'MM/dd/yyyy')
```

위에서 제시한 함수들을 사용하여 다양한 날짜 및 시간 연산을 수행할 수 있습니다.

참고자료: [MySQL DATE and TIME Functions](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html)