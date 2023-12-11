---
layout: post
title: "[sql] 데이터의 결합을 위한 스칼라 함수 (JOIN, INNER JOIN, OUTER JOIN 등)"
description: " "
date: 2023-12-11
tags: [sql]
comments: true
share: true
---

데이터베이스에서는 종종 여러 테이블에서 데이터를 가져와 결합해야 하는 경우가 있습니다. SQL에서는 이를 위해 **JOIN**이라는 스칼라 함수를 사용합니다. **JOIN**은 두 개 이상의 테이블에서 데이터를 가져와 조합하는 데 사용됩니다. 일반적으로는 **INNER JOIN**, **OUTER JOIN** 등의 다양한 유형이 있습니다. 

## INNER JOIN

가장 기본적으로 사용되는 JOIN 유형 중 하나로, 일치하는 값을 가진 두 테이블의 행만 반환합니다. 다음은 간단한 INNER JOIN의 예제입니다.

```sql
SELECT * FROM 테이블1 
INNER JOIN 테이블2 ON 테이블1.열 = 테이블2.열;
```

## OUTER JOIN

**OUTER JOIN**은 두 테이블 간의 모든 행을 반환하고, 일치하지 않는 경우에는 NULL 값을 반환합니다. LEFT JOIN, RIGHT JOIN, FULL JOIN 등 **OUTER JOIN**에는 여러 가지 유형이 있습니다. 

```sql
SELECT * FROM 테이블1 
LEFT OUTER JOIN 테이블2 ON 테이블1.열 = 테이블2.열;
```

이러한 스칼라 함수를 사용하여 여러 테이블의 데이터를 결합하고 필요한 정보를 추출할 수 있습니다.

위에 언급된 예시는 가장 일반적인 방법이며, 데이터베이스 시스템에 따라 문법이 약간 다를 수 있습니다. 코드를 실행하기 전에 해당 데이터베이스의 문서를 참조하는 것이 좋습니다.

이렇게 스칼라 함수를 사용하여 여러 테이블의 데이터를 결합하고 필요한 정보를 추출할 수 있습니다.

## 요약

- **INNER JOIN**은 일치하는 값이 있는 행만 반환합니다.
- **OUTER JOIN**은 일치하지 않는 행도 포함하여 반환합니다.

이러한 SQL 스칼라 함수를 사용하면 다양한 데이터 소스에서 원하는 정보를 효율적으로 가져와 조합할 수 있습니다.

참고 자료: [MySQL Official Documentation](https://dev.mysql.com/doc/refman/8.0/en/join.html)