---
layout: post
title: "[sql] 트랜잭션 함수 (COMMIT, ROLLBACK, SAVEPOINT 등)"
description: " "
date: 2023-12-11
tags: [sql]
comments: true
share: true
---

SQL에서 **트랜잭션(transaction)**은 하나 이상의 데이터베이스 작업을 그룹화하는 데 사용됩니다. 트랜잭션 함수는 이러한 트랜잭션을 제어하는 데 사용됩니다. 일반적으로 다음과 같은 트랜잭션 함수가 사용됩니다.

1. **COMMIT**: 이 함수는 트랜잭션에 대한 모든 변경 사항을 영구적으로 반영하고, 데이터베이스를 업데이트합니다.
2. **ROLLBACK**: 이 함수는 트랜잭션을 취소하고, 변경사항을 이전의 상태로 되돌립니다.
3. **SAVEPOINT**: 이 함수는 현재 트랜잭션 내에서 일시적인 저장 지점을 만듭니다. 이를 통해 특정 시점으로 롤백할 수 있습니다.

이러한 함수를 사용하여 데이터베이스 트랜잭션을 안전하게 제어할 수 있습니다.

참고 문헌:
- [Oracle Database - Managing Transactions](https://docs.oracle.com/cd/B19306_01/server.102/b14220/transact.htm)
- [MySQL - COMMIT](https://dev.mysql.com/doc/refman/8.0/en/commit.html)
- [PostgreSQL - ROLLBACK](https://www.postgresql.org/docs/9.1/sql-rollback.html)