---
layout: post
title: "[Database] Connect Database From Commandline"
description: " "
date: 2021-11-19
tags: [sql]
comments: true
share: true
---

## Connect Database From Commandline
> MySQL 또는 MariaDB에 접속하기  

터미널을 통해 Database에 접속하는 법을 알아보자.  

```MariaDB``` 를 만든 사람은 ```MySQL``` 을 만든 사람(Monty Widenius)과 동일하다.  
그리하여 MySQL 을 사용하는 것처럼 동일한 명령어를 MariaDB 에서 사용할 수 있다.

## Connect DB
### For Local Server
```
mysql -u <userName> -p
```
* host name 을 기입하지 않으면 localhost 로 결정된다.

### For Remote Server
```
mysql -h <hostName> -P <portNumber> -u <userName> -p
```
* h : Host Name
* P : Port Number 
* u : User Name
* p : Password


## Show Database
```
SHOW databases;
```
현재 사용 가능한 데이터베이스 보기

## Use Database
```
USE <dbName>;
```
```dbName``` 이라는 이름을 가진 데이터 베이스 사용하기
