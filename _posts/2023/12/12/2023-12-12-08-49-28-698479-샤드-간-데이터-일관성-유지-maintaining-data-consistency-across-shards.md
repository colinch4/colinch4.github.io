---
layout: post
title: "[sql] 샤드 간 데이터 일관성 유지 (Maintaining Data Consistency Across Shards)"
description: " "
date: 2023-12-12
tags: [sql]
comments: true
share: true
---

데이터베이스 시스템에서 **샤딩 (Sharding)** 은 대량의 데이터를 여러 물리적 서버에 분산하여 저장하는 방법을 말합니다. 샤딩을 통해 시스템의 성능을 향상시키고 확장성을 향상시킬 수 있지만, 샤드 간 데이터 일관성을 유지하는 것은 복잡한 문제입니다.

## 샤딩의 동작

**샤딩**이란 데이터베이스 테이블의 행을 여러 서버로 분할하는 것을 말합니다. 각 서버에는 특정 범위의 데이터가 저장되고, 이러한 방식으로 시스템의 읽기 및 쓰기 요청을 분산시킬 수 있습니다. 그러나 확장성과 성능을 향상시키는 동시에 데이터 일관성 문제가 발생할 수 있습니다.

## 데이터 일관성 유지

샤딩된 데이터베이스 시스템에서 **데이터 일관성**은 항상 중요한 문제입니다. 다른 샤드에 데이터를 쓰는 동안 일관성을 보장하기위한 방법으로는 **분산 트랜잭션** 을 활용하거나 **단일화 및 복제판단 (Single Source of Truth)** 을 유지합니다.

## 분산 트랜잭션

**분산 트랜잭션**은 다른 샤드 간에 데이터 일관성을 유지하기 위한 방법으로, 모든 관련된 샤드에 대해 트랜잭션을 시작하고 커밋하는 것을 의미합니다. 이는 여러 샤드에 걸친 작업을 원자적으로 수행할 수 있는 방법을 제공합니다.

```sql
BEGIN TRANSACTION;
-- 샤드 간 작업 수행
COMMIT TRANSACTION;
```

## 단일화 및 복제판단

데이터 일관성을 유지하기 위해 **단일화 및 복제판단 (Single Source of Truth)** 을 유지할 수도 있습니다. 이 방법은 데이터 변경 사항이 발생할 때마다 샤드 간에 데이터를 동기화하는 방법으로, **중앙화된 복제본 (Replica)** 을 유지하여 일관성을 유지합니다.

## 결론

샤딩된 데이터베이스 시스템에서 **데이터 일관성**을 유지하는 것은 복잡한 문제이지만, **분산 트랜잭션**과 **단일화 및 복제판단**을 통해 이를 극복할 수 있습니다. 이러한 기술들을 효과적으로 활용하여 데이터 일관성을 유지하는 것이 중요합니다.

Internal-reference: Final thoughts
# Final thoughts

샤딩된 데이터베이스 시스템에서 **데이터 일관성**을 유지하는 것은 복잡한 문제이지만, **분산 트랜잭션**과 **단일화 및 복제판단**을 통해 이를 극복할 수 있습니다. 이러한 기술들을 효과적으로 활용하여 데이터 일관성을 유지하는 것이 중요합니다.

[date=2021-12-07]
Internal-reference: Relevant references
# Relevant references

- [Principles of Distributed Database Systems](https://www.goodreads.com/book/show/1713082.Principles_of_Distributed_Database_Systems)
- [Scaling MongoDB to Billions of Transactions](https://www.mongodb.com/presentations/scaling-mongodb-to-billions-of-transactions)