---
layout: post
title: "[Database] postgreSQL"
description: " "
date: 2021-11-19
tags: [Database]
comments: true
share: true
---

## postgreSQL
Postgre의 기본 포트는 ```5432```
 
 ### Table of Contents
 * [Installation](#installation)
    * [via Brew](#via-brew)
    * [via Installer](#via-installer)
 * [Start server](#start-server)
    * [via Terminal](#via-terminal)
    * [via PSequel](#via-psequel)
 * [postgreSQL Commands](#commands)  

## Installation

### via Brew
```brew install postgresql```

### via Installer
Download it from EnterpriseDB Website.
* [PostgreSQL Database Download](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)



## Start Server

### via Terminal
**Start Server**  
```pg_ctl -D /usr/local/var/postgres start```  
* ```/usr/local/var/postgres``` 에 위치한 postgre 서버 실행.

* success result
    ```bin
    waiting for server to start....2020-06-04 09:47:44.887 KST [56815] LOG:  starting PostgreSQL 12.2 on x86_64-apple-darwin19.4.0, compiled by Apple clang version 11.0.3 (clang-1103.0.32.59), 64-bit
    2020-06-04 09:47:44.888 KST [56815] LOG:  listening on IPv6 address "::1", port 5432
    2020-06-04 09:47:44.889 KST [56815] LOG:  listening on IPv4 address "127.0.0.1", port 5432
    2020-06-04 09:47:44.889 KST [56815] LOG:  listening on Unix socket "/tmp/.s.PGSQL.5432"
    2020-06-04 09:47:44.912 KST [56816] LOG:  database system was shut down at 2020-03-30 07:04:48 KST
    2020-06-04 09:47:44.918 KST [56815] LOG:  database system is ready to accept connections
    done
    server started
    ```

**Access Server**  
```psql postgres```

* success result
    ```
    psql (12.2)
    Type "help" for help.

    postgres=#
    ```

**Stop Server**  
```pg_ctl -D /usr/local/var/postgres stop```  
서버를 시작하는 명령어와 같지만, 마지막 부분에 ```start``` 대신 ```stop```을 타이핑한다.  


### via PSequel 
PSequel 은 MacOS 유저용 GUI 툴.  
Terminal 보다 GUI 를 선호한다면 PSequel 을 인스톨하여 사용하도록 하자.

**Installation**
* [Install PSequel](http://www.psequel.com/)

**Input Database Info**  
PSequel 을 실행하여, 하기 정보를 입력 후 사용
 * Host
 * User
 * Password
 * Database  

<img width="500" alt="PSequel" src="https://user-images.githubusercontent.com/48475824/83836658-1cff0d00-a72f-11ea-9fd9-dfd5c2e02a0a.png">

[↑ return to TOC](#table-of-contents)

## Commands

### Change
* Change User  
    ```\c - userName```

### Choose
* Choose Database  
   선택한 데이터베이스 사용  
   ```\c databaseName;```

### Create
* Create Database  
  새로운 DB 생성.  
  ```CREATE DATABASE “databaseName”;```
  * ```;``` 를 첨부하지 않을시  ```ERROR:  syntax error``` 를 만나게 된다.

* Create User  
  새 유저 생성.  
  ```CREATE USER "userName";```


### Describe
* Describe Table  
```\d tableName;```  
```\d+ tableName;```   
  ```bash
  # example
  # \d tokens;
                    Table "public.tokens"
    Column   |  Type  | Collation | Nullable | Default 
  ------------+--------+-----------+----------+---------
  token      | text   |           | not null | 
  created_at | bigint |           | not null | 
  Indexes:
      "tokens_pkey" PRIMARY KEY, btree (token)
  ```
  ```bash
  # example
  # \d+ tokens;
                            Table "public.tokens"
    Column   |  Type  | Collation | Nullable | Default | Storage  | Stats target | Description 
  ------------+--------+-----------+----------+---------+----------+--------------+-------------
  token      | text   |           | not null |         | extended |              | 
  created_at | bigint |           | not null |         | plain    |              | 
  Indexes:
      "tokens_pkey" PRIMARY KEY, btree (token)
  Access method: heap
  ```


### Drop
* Drop Table  
```DROP TABLE tableName```

* Drop Table which has dependency to other table  
```DROP TABLE tableName CASCADE;```


### Dump
* Dump SQL File Into the Database   
```\i '\file\path\fileName.sql'```  
```psql databaseNAme < fileName.sql```  


### Explain
```EXPLAIN``` 을 통하여 Optimizer 의 실행 계획을 살펴볼 수 있다.
* **Explain**   
  Optimizer 의 실행계획 예측 보기  
  ```EXPLAIN <yourQuery>;```
* **Explain Analyze**  
  Optimizer 의 실행계획대로 실제 실행한 결과 보기  
  ```EXPLAIN ANALYZE <yourQuery>;```

  ```sql
  # EXPLAIN ANALYZE SELECT * FROM items ORDER BY created_at DESC  LIMIT 3;
                              QUERY PLAN
   -------------------------------------------------------------------
   Limit  (cost=0.28..0.86 rows=3 width=245) (actual time=1.626..1.630 rows=3 loops=1)
   ->  Index Scan Backward using idx_items_created_at on items  (cost=0.28..551.08 rows=2864 width=245) (actual time=1.624..1.628 rows=3 loops=1)
   Planning Time: 0.145 ms
   Execution Time: 1.655 ms
   (4 rows)
  ```

* **Explain w/ Buffers**  
  버퍼 관련 정보가 포함된 실행계획 보기  
  ```EXPLAIN (BUFFERS, ANALYZE) <yourQuery>;```

  ```sql
  # EXPLAIN (BUFFERS, ANALYZE) SELECT * FROM items;
                              QUERY PLAN
   ------------------------------------------------------------------
   Seq Scan on items  (cost=0.00..128.64 rows=2864 width=245) (actual time=0.019..0.669 rows=2864 loops=1) 
   Buffers: shared hit=100 Planning Time: 0.091 ms 
   Execution Time: 0.933 ms
   (4 rows)
  ```


### Grant
* 선택한 Database 의 Owner 설정  
    ```grant all privileges on database "databaseName" to "userName";```

### Info
* Connection Info  
연결된 postgres DB의 상세 정보 보기.  
```\conninfo```  
    ```
    you are connected to database “postgres” as user <userName> via socket in “/tmp” at port “5432”
    ```

### List
* List Databases  
```\list```  
```\l```

* List Tables  
```\dt```  
```\dt *```  → 모든 DB의 tables 보기.  
```\dg```  

  테이블이 존재하지 않을 시
  ```
  Did not find any relations.
  ```

* List Database Users  
```\du```  
```\du+``` → Description 정보까지 보기.

[↑ return to TOC](#table-of-contents)
