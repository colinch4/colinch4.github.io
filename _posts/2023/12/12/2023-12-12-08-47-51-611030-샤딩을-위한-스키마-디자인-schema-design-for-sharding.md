---
layout: post
title: "[sql] 샤딩을 위한 스키마 디자인 (Schema Design for Sharding)"
description: " "
date: 2023-12-12
tags: [sql]
comments: true
share: true
---

데이터베이스 시스템을 운영하다보면 대량의 데이터가 쌓이게 되는데, 이를 처리하기 위해서는 **샤딩(sharding)**이라는 기술이 필요합니다. 샤딩은 데이터를 수평적으로 분할하여 여러 대상에 분산 저장함으로써 데이터베이스의 처리 능력을 향상시키는 방법입니다. 이를 위해서는 효율적인 스키마 디자인이 매우 중요합니다.

## 샤딩을 위한 스키마 디자인 고려 사항

1. **분산된 데이터**: 각 샤드에 데이터가 고르게 분산되도록 설계해야 합니다.
2. **조인의 회피**: 쿼리가 여러 샤드에 걸쳐 조인이 필요 없도록 설계합니다.

## 샤딩을 위한 스키마 디자인 패턴

### 해싱을 기반으로 한 파티셔닝

해싱을 통해 특정 데이터 엔티티(예: 유저 ID)를 해시 함수에 넣어서 샤드 번호를 계산하고 해당 샤드에 저장합니다.

```sql
CREATE TABLE user (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    ...
) PARTITION BY HASH(id)
PARTITIONS 8;
```

### 범위 기반 파티셔닝

특정 엔티티(예: 날짜)의 값의 범위에 따라 여러 샤드 중 하나에 데이터를 저장하는 방식입니다.

```sql
CREATE TABLE log (
    id INT PRIMARY KEY,
    log_time TIMESTAMP,
    ...
) PARTITION BY RANGE (YEAR(log_time)) (
    PARTITION p0 VALUES LESS THAN (2010),
    PARTITION p1 VALUES LESS THAN (2011),
    ...
);
```

### 지연 복제(Lazy Replication)

일부 샤드의 데이터를 늦게 동기화하는 방식으로, 데이터베이스의 처리량을 높이는 방법 중 하나입니다.

이러한 패턴과 관련해서는 관련 문서와 블로그를 참고할 것을 권장합니다.

--- 

위의 내용은 샤딩을 위한 스키마 디자인 고려 사항과 패턴에 대한 간략한 소개입니다. SQLAlchemy, Hibernate 등의 ORM 프레임워크에서도 샤딩을 지원하는 기능을 제공하고 있으니 이용할 경우 해당 라이브러리의 문서를 참고하시기 바랍니다.