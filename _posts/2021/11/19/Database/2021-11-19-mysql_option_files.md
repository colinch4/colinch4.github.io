---
layout: post
title: "[Database] MySQL Option Files"
description: " "
date: 2021-11-19
tags: [Database]
comments: true
share: true
---

## MySQL Option Files  
> Connection Parameters 입력 자동화 하기  

MySQL DB 사용시 입력하게 되는 연결 파라미터를 매번 수동으로 입력하는 수고를 덜어줄 수 있다.  
연결 파라미터를 Option Files 에 적어 놓음으로써 자동화 시킬 수 있다.  
- 중복된 파라미터가 존재 할 시 제일 하단에 위치한 파라미터가 사용됨.  

## `my.cnf`  
MySQL 의 Option File 명칭은 `my.cnf` 이다.  
- Window의 경우 `my.ini` 또는 `my.cnf`

### Location
`my.cnf` 파일의 위치. 글로벌로 적용된다.  
- **Unix-like**  
  - `/etc/mysql/my.cnf`
  - `/etc/my.cnf`  
    Homebrew로 MySql을 설치한 경우 해당 위치에 존재  
- **Window**  
  - `C:\my.ini`

### Example  
`key:value` 형태로 적어준다.  
```shell
## Default Homebrew MySQL server config

[mysqld]
## Only allow connections from localhost
bind-address = 127.0.0.1
mysqlx-bind-address = 127.0.0.1

## personal setup
[client]
host=xxx.x.x.x
user=XOXO
```  
- **`password`**   
  `password` 파라미터는 입력해 놓지 않는 것을 추천.  
  MySQL 시작시 `-p` 를 통해 직접 입력하자.  
- **Long Options**  
  Option File 에서는 짧은 형태의 파라미터는 사용 할 수 없다.  
  예를 들어 `host` 값을 입력하고자 한다면 `host=host_value` 형태로 적어주자.  
  - (X) `h=host_value`
  - (O) `host=host_value`
  - (X) `p=password_value`
  - (O) `password=password_value`
