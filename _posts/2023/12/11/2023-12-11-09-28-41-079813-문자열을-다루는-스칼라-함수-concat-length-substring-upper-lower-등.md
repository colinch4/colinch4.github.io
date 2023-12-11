---
layout: post
title: "[sql] 문자열을 다루는 스칼라 함수 (CONCAT, LENGTH, SUBSTRING, UPPER, LOWER 등)"
description: " "
date: 2023-12-11
tags: [sql]
comments: true
share: true
---

SQL에서 문자열을 다루는 스칼라 함수는 데이터를 조작하고 분석하는 데 유용합니다. 이러한 함수들은 문자열을 조작하거나 변환하는 등의 작업을 수행할 수 있습니다.

## CONCAT 함수

`CONCAT` 함수는 두 개 이상의 문자열을 연결하여 하나의 문자열로 반환합니다.

예를 들어:

```sql
SELECT CONCAT('Hello', 'World');
```
결과: `HelloWorld`

## LENGTH 함수

`LENGTH` 함수는 문자열의 길이를 반환합니다.

예를 들어:

```sql
SELECT LENGTH('Hello');
```
결과: `5`

## SUBSTRING 함수

`SUBSTRING` 함수는 문자열에서 특정 부분을 추출하여 반환합니다.

예를 들어:

```sql
SELECT SUBSTRING('Hello World', 1, 5);
```
결과: `Hello`

## UPPER 함수와 LOWER 함수

`UPPER` 함수는 문자열을 모두 대문자로 변환하고, `LOWER` 함수는 문자열을 모두 소문자로 변환합니다.

예를 들어:

```sql
SELECT UPPER('hello');
```
결과: `HELLO`

```sql
SELECT LOWER('HELLO');
```
결과: `hello`

이러한 스칼라 함수들을 활용하여 문자열 데이터를 효과적으로 다룰 수 있습니다.

더 많은 정보는 아래의 참고 자료를 참고하세요.

## 참고 자료
- [SQL 문자열 함수 - Oracle 공식 문서](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/SQL-functions.html#GUID-5A8D999A-B3CE-429F-B052-38C60F959B07)
- [SQL 문자열 함수 - Microsoft SQL Server 공식 문서](https://docs.microsoft.com/en-us/sql/t-sql/functions/string-functions-transact-sql)