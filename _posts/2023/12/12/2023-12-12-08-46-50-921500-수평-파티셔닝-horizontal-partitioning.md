---
layout: post
title: "[sql] 수평 파티셔닝 (Horizontal Partitioning)"
description: " "
date: 2023-12-12
tags: [sql]
comments: true
share: true
---

수평 파티셔닝은 데이터베이스에서 하나의 테이블을 나누어 저장하는 기술로, **테이블을 물리적으로 나누어 여러 개의 서버나 스토리지 공간에 데이터를 분산**시키는 방법입니다. 이를 통해 **읽고 쓰는 성능을 향상**시킬 수 있습니다.

## 수평 파티셔닝의 장점

수평 파티셔닝을 사용하면 다음과 같은 장점을 얻을 수 있습니다:
1. **성능 향상**: 데이터가 분산되어 있기 때문에 **읽기 및 쓰기 작업이 분산**되어 전반적으로 **성능이 향상**됩니다.
2. **스케일 아웃**: 서버 또는 스토리지 공간을 추가하여 **시스템을 쉽게 확장**할 수 있습니다.
3. **보안 및 접근 제어**: 특정 유형의 데이터를 분리하여 **보안 및 접근 제어를 강화**할 수 있습니다.

## 수평 파티셔닝의 예시

아래는 **고객 정보를 수평 파티셔닝하는 예시**입니다.

```sql
-- 고객 정보를 성별에 따라 수평 파티셔닝
CREATE TABLE customer (
    id INT,
    name VARCHAR(100),
    gender CHAR(1),
    age INT,
    ...
)
PARTITION BY LIST (gender) (
    PARTITION male VALUES IN ('M'),
    PARTITION female VALUES IN ('F')
);
```

위의 예시에서는 성별에 따라 고객 정보를 나누어 저장하고 있습니다.

수평 파티셔닝은 데이터베이스 시스템의 성능 및 확장성을 향상시키는 중요한 전략 중 하나입니다.
**수평 파티셔닝은 데이터베이스 설계 과정에서 고려**되어야 하며, 특정 비즈니스 요구 사항에 맞게 사용되어야 합니다.

## 참고 자료
- [MySQL 공식 문서 - Partitioning](https://dev.mysql.com/doc/refman/8.0/en/partitioning.html)
- [PostgreSQL 공식 문서 - Partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html)

위의 참고 자료에서는 MySQL 및 PostgreSQL에서의 파티셔닝 관련 정보를 확인할 수 있습니다.