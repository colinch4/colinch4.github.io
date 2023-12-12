---
layout: post
title: "[sql] 샤딩 키 선택 방법 (Sharding Key Selection method)"
description: " "
date: 2023-12-12
tags: [sql]
comments: true
share: true
---

데이터베이스 샤딩은 대용량의 데이터를 여러 개의 데이터베이스로 분산하여 저장하는 방법입니다. 이를 통해 시스템의 확장성을 향상시키고 성능을 개선할 수 있습니다. **샤딩 키(sharding key)**는 데이터를 분산 저장하는 기준이 되는 열이나 필드를 가리킵니다. 이 포스트에서는 여러 가지 샤딩 키 선택 방법에 대해 살펴보겠습니다.

## 1. 단일 컬럼 기준

**단일 컬럼 기준**은 하나의 열을 샤딩 키로 선택하는 방법입니다. 일반적으로 데이터의 분포를 균등하게 나눌 수 있는 열을 선택합니다. 예를 들어, 주문 시스템에서는 주문 ID나 고객 ID를 사용할 수 있습니다.

```sql
CREATE TABLE orders (
    order_id INT NOT NULL,
    customer_id INT NOT NULL,
    ...
    PRIMARY KEY (order_id)
) ENGINE = InnoDB
```

## 2. 복합 키 기준

**복합 키 기준**은 여러 열을 결합하여 샤딩 키로 선택하는 방법입니다. 데이터 분포를 더욱 세밀하게 제어할 수 있으며, 관련된 데이터를 함께 저장할 수 있습니다. 예를 들어, 주문 시스템에서는 주문 날짜와 고객 ID를 결합하여 사용할 수 있습니다.

```sql
CREATE TABLE orders (
    order_id INT NOT NULL,
    order_date DATE NOT NULL,
    customer_id INT NOT NULL,
    ...
    PRIMARY KEY (order_date, customer_id)
) ENGINE = InnoDB
```

## 3. 해싱 기준

**해싱 기준**은 데이터의 해시 값을 사용하여 샤딩 키로 선택하는 방법입니다. 데이터가 균등하게 분산되도록 해싱 알고리즘을 사용하여 샤딩 키를 생성합니다. 이 방법은 데이터의 분포를 미리 알 수 없는 경우에 유용합니다.

```sql
CREATE TABLE user_data (
    user_id INT NOT NULL,
    username VARCHAR(255) NOT NULL,
    ...
    PRIMARY KEY (user_id)
) ENGINE = InnoDB
PARTITION BY HASH(user_id)
PARTITIONS 4;
```

## 결론

데이터베이스 샤딩을 위한 적절한 샤딩 키 선택은 시스템의 성능과 확장성에 매우 중요합니다. 각 방법마다 장단점이 있으며, 데이터의 특성과 사용 사례에 맞게 적절한 방법을 선택해야 합니다.

참고문헌:
- [MySQL 공식 문서](https://dev.mysql.com/doc/refman/8.0/en/partitioning-overview.html)