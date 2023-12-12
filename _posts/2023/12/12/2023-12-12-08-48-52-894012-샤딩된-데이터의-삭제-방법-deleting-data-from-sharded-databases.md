---
layout: post
title: "[sql] 샤딩된 데이터의 삭제 방법 (Deleting Data from Sharded Databases)"
description: " "
date: 2023-12-12
tags: [sql]
comments: true
share: true
---

샤딩은 대규모의 데이터베이스를 분할하여 저장하고 조회 성능을 향상시키는 방법으로, 많은 기업에서 사용하고 있습니다. 샤딩된 데이터베이스에서 특정 데이터를 삭제하는 방법은 몇 가지 주의해야 할 점이 있습니다. 이번 글에서는 샤딩된 데이터베이스에서 데이터를 안전하게 삭제하는 방법을 알아보겠습니다.

## 1. 데이터베이스 스키마 파악

먼저 삭제하려는 데이터가 어느 샤드에 저장되어 있는지 파악해야 합니다. 각 샤드에 저장된 데이터베이스 스키마를 확인하여 삭제 대상 데이터가 어디에 있는지 확인합니다.

```sql
USE shard1;
DELETE FROM table1 WHERE id=1;
```

위의 예제에서 `shard1`은 삭제할 데이터가 저장된 샤드를 나타내며, `table1`은 삭제할 데이터 테이블을 의미합니다.

## 2. 외부 키 제약 조건 고려

데이터를 삭제할 때는 외부 키 제약 조건을 신중하게 고려해야 합니다. 다른 테이블과 관계가 있는 경우, 해당 관계를 고려하여 데이터를 삭제해야 합니다.

```sql
DELETE FROM table1 WHERE id=1;
DELETE FROM table2 WHERE table1_id=1; 
```

위의 예제에서 `table1`과 `table2`가 외부 키 제약 조건으로 연결되어 있는 경우, `table1`의 데이터를 삭제하기 전에 `table2`의 관련 데이터를 먼저 삭제해야 합니다.

## 3. 백업 및 롤백 절차 마련

데이터를 삭제하기 전에는 항상 백업을 수행하고 롤백 절차를 마련해야 합니다. 실수로 중요한 데이터를 삭제했을 때를 대비하여 데이터의 안전을 위해 백업과 롤백을 준비해 두어야 합니다.

## 4. 삭제 로그 기록

삭제된 데이터의 로그를 기록하는 것은 매우 중요합니다. 삭제 시간, 삭제한 사용자, 삭제된 데이터 등을 로그로 남겨두어 추후에 데이터 복구나 오류 파악에 도움이 됩니다.

위의 과정을 통해 샤딩된 데이터베이스에서 안전하게 데이터를 삭제할 수 있습니다.

## 참고 자료

- [Oracle - Managing Data in Sharded Databases](https://www.oracle.com/database/technologies/sharding.html)
- [MySQL - Sharding and Partitioning](https://dev.mysql.com/doc/refman/8.0/en/sharding.html)