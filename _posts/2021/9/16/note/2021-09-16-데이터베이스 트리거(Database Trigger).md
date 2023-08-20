---
layout: post
title: "[용어정리] 데이터베이스 트리거(Database Trigger)"
description: " "
date: 2021-09-16
tags: [용어정리]
comments: true
share: true
---


## 데이터베이스 트리거(Database Trigger)

테이블에 대한 이벤트에 반응해 자동으로 실행되는 작업을 의미한다. 트리거는 데이터 조작 언어(DML)의 데이터 상태의 관리를 자동화하는 데 사용된다. 트리거를 사용하여 데이터 작업 제한, 작업 기록, 변경 작업 감사 등을 할 수 있다.

트리거는 크게 나누어 행 트리거, 열 트리거 두 종류가 있다.

- 행 트리거 : 테이블 안의 영향을 받은 행 각각에 대해 실행된다. 변경 전 또는 변경 후의 행은 OLD,NEW 라는 가상 줄 변수를 사용하여 읽을 수 있다. 
- 문장 트리거 : INSERT, UPDATE , DELETE 문에 대해 한번만 실행된다. 

쉽게 말해 데이터 테이블에 이벤트에 반응하는 것!

오라클, Microsoft SQL Server, PostgreSQL, MySQL 등 각 SQL 마다 다른 트리거를 가지고 있다.

​	