---
layout: post
title: "[sql] 날짜 및 시간 데이터 타입 (date, datetime, timestamp)"
description: " "
date: 2023-12-05
tags: [sql]
comments: true
share: true
---

데이터베이스에서는 날짜와 시간을 다룰 수 있는 여러 데이터 타입을 제공합니다. 이러한 데이터 타입은 날짜 및 시간 정보를 저장하고 처리하는 데 사용됩니다. 흔히 사용되는 세 가지 데이터 타입은 `DATE`, `DATETIME`, `TIMESTAMP`입니다. 각각의 데이터 타입은 다음과 같은 특징을 가지고 있습니다.

## DATE

`DATE` 데이터 타입은 날짜 정보만을 저장합니다. 이 데이터 타입은 연월일 형식으로 표현되며, 시간 정보는 포함되지 않습니다. 예를 들어, "2021-10-18"과 같은 형식으로 날짜를 저장할 수 있습니다.

## DATETIME

`DATETIME` 데이터 타입은 날짜와 시간 정보를 모두 저장합니다. 연월일과 시분초 형식으로 표현되며, 시간대도 함께 저장됩니다. 예를 들어, "2021-10-18 09:30:00"과 같은 형식으로 날짜와 시간을 저장할 수 있습니다.

## TIMESTAMP

`TIMESTAMP` 데이터 타입도 날짜와 시간 정보를 모두 저장합니다. `DATETIME`과 유사한 형식으로 표현되지만, 일반적으로 1970년 1월 1일부터 현재까지 경과한 초 단위로 값을 저장합니다. 이는 일반적으로 유닉스 시간이라고도 알려져 있습니다.

## 데이터 타입 선택 가이드

어떤 데이터 타입을 사용해야 할지 선택하는 데는 몇 가지 고려사항이 있습니다.

- DATE 타입은 날짜 정보만 필요한 경우 사용됩니다.
- DATETIME 타입은 날짜와 시간 정보가 모두 필요한 경우 사용됩니다.
- TIMESTAMP 타입은 날짜와 시간 정보가 필요하지만, 특정 시간대에 대한 정보는 필요하지 않은 경우 사용됩니다. 또는 시간대 정보를 저장하지 않고 상대적인 시간 정보를 저장해야 할 때 유용합니다.

데이터베이스 시스템에 따라 데이터 타입의 세부 사항이 다를 수 있으므로, 해당 데이터베이스의 문서를 참조하여 사용하는 것이 좋습니다.

더 자세한 내용은 아래 참고 자료를 참조하시기 바랍니다.

## 참고 자료
- [MySQL Reference Manual - Date and Time Types](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-types.html)
- [PostgreSQL Documentation - Date/Time Types](https://www.postgresql.org/docs/current/datatype-datetime.html)
- [Oracle Database SQL Language Reference - Date and Time Data Types](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Date-and-Time-Data-Types.html)
- [Microsoft SQL Server Documentation - Date and Time Data Types](https://docs.microsoft.com/en-us/sql/t-sql/data-types/date-and-time-data-types?view=sql-server-ver15)