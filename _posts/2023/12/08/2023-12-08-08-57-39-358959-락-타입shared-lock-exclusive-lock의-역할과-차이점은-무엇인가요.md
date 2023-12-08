---
layout: post
title: "[sql] 락 타입(Shared Lock, Exclusive Lock)의 역할과 차이점은 무엇인가요?"
description: " "
date: 2023-12-08
tags: [sql]
comments: true
share: true
---

### 역할

- **Shared Lock**: 여러 트랜잭션이 동시에 데이터를 읽을 수 있도록 허용하며, 다른 트랜잭션이 동시에 해당 데이터를 수정하지 못하도록 합니다.
  
- **Exclusive Lock**: 하나의 트랜잭션만 데이터를 읽고 쓸 수 있도록 허용하여, 다른 트랜잭션이 동시에 해당 데이터를 읽거나 수정하지 못하도록 합니다.

### 차이점

- **데이터 수정 가능 여부**: Shared Lock은 여러 트랜잭션이 데이터를 읽을 수 있지만, Exclusive Lock은 해당 데이터를 읽고 쓰는 트랜잭션이 있을 때 다른 트랜잭션이 해당 데이터를 수정할 수 없습니다.

- **동시성 처리**: Shared Lock은 데이터 읽기를 동시에 허용하여 읽기 동시성을 높이지만, Exclusive Lock은 데이터를 읽거나 쓸 때 다른 트랜잭션을 차단하여 동시성을 낮출 수 있습니다.

- **락 충돌**: Shared Lock은 여러 트랜잭션이 읽을 수 있으므로 충돌이 적지만, Exclusive Lock은 데이터를 수정 중인 트랜잭션이 있을 때 다른 트랜잭션이 해당 데이터를 수정하려고 하면 충돌이 발생합니다.

이러한 역할과 차이점으로 인해 데이터베이스 시스템은 효율적으로 동작하고 데이터 일관성을 유지할 수 있습니다.

### 참조
- [데이터베이스 락](https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4_%EB%A1%9D)
- [데이터베이스 락에 대한 기본 사항](https://docs.microsoft.com/ko-kr/sql/relational-databases/sql-server-locks?view=sql-server-ver15)