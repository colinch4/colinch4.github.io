---
layout: post
title: "[sql] 인덱스 접근 방식 (Range Scan, Full Scan, Unique Scan 등)"
description: " "
date: 2023-12-07
tags: [sql]
comments: true
share: true
---

인덱스는 데이터베이스에서 효율적인 데이터 검색을 위해 사용됩니다. 인덱스 접근 방식은 인덱스의 종류와 데이터베이스 엔진의 최적화 방법에 따라 다르게 사용됩니다. 몇 가지 주요한 인덱스 접근 방식에 대해 살펴보겠습니다.

### 1. Range Scan

Range Scan은 인덱스의 범위를 스캔하여 조건에 맞는 데이터를 찾는 방식입니다. 예를 들어, `WHERE` 절에 `BETWEEN`이나 `>`와 같은 범위 조건이 있는 경우 Range Scan 방식이 사용됩니다. 이 방식은 인덱스의 일부를 스캔하므로 검색 속도가 빠릅니다. 하지만 인덱스의 일부만을 사용하기 때문에 전체 인덱스가 검색되는 것보다는 느릴 수 있습니다.

### 2. Full Scan

Full Scan은 인덱스의 전체를 스캔하여 조건에 맞는 데이터를 찾는 방식입니다. 이 방식은 인덱스 사용 여부와 상관없이 모든 데이터를 스캔하므로 검색 속도가 느립니다. Full Scan은 대량의 데이터를 처리할 때 주로 사용됩니다.

### 3. Unique Scan

Unique Scan은 인덱스의 유니크한 값을 통해 데이터를 검색하는 방식입니다. 이 방식은 인덱스의 유니크 조건을 만족하는 데이터를 찾을 때 사용됩니다. Unique Scan은 인덱스가 유니크하게 정의된 경우에만 사용되며, 검색 속도가 매우 빠릅니다.

인덱스 접근 방식은 데이터베이스 엔진의 최적화 방법과 인덱스의 종류에 따라 달라집니다. 따라서 효율적인 데이터 검색을 위해 적절한 인덱스를 선택하고 인덱스를 적절하게 활용하는 것이 중요합니다.

참고 문헌:
- [https://www.sqlshack.com/index-access-methods-in-sql-server/](https://www.sqlshack.com/index-access-methods-in-sql-server/)
- [https://www.sqlshack.com/index-types-overview-in-sql-server/](https://www.sqlshack.com/index-types-overview-in-sql-server/)