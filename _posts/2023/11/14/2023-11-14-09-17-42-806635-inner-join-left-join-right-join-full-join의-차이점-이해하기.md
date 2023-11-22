---
layout: post
title: "INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN의 차이점 이해하기"
description: " "
date: 2023-11-14
tags: [sql]
comments: true
share: true
---

데이터베이스에서 JOIN 연산은 둘 이상의 테이블을 결합하여 하나의 결과 집합을 생성하는 데 사용됩니다. 데이터베이스에서는 INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN 네 가지 주요 JOIN 유형이 있으며, 각각은 다른 방식으로 테이블을 조합합니다.

## INNER JOIN
INNER JOIN은 두 개의 테이블에서 일치하는 행을 선택하여 결과를 반환합니다. 일치하는 행이 없는 경우, 해당 행은 결과에 포함되지 않습니다. INNER JOIN은 테이블 간 관계가 있는 경우에 주로 사용됩니다. 예를 들어, 주문 테이블과 제품 테이블에서 주문한 제품의 정보를 가져올 때 INNER JOIN을 사용할 수 있습니다.

```sql
SELECT *
FROM 주문
INNER JOIN 제품 ON 주문.제품ID = 제품.ID;
```

## LEFT JOIN
LEFT JOIN은 왼쪽 테이블의 모든 행을 선택하고, 오른쪽 테이블에서 일치하는 행을 선택하여 결과를 반환합니다. 일치하는 행이 없는 경우, NULL 값을 반환합니다. LEFT JOIN은 왼쪽 테이블의 모든 레코드를 포함해야 할 때 유용합니다. 예를 들어, 사원 테이블과 부서 테이블이 있을 때, 각 사원의 부서 정보를 가져올 때 LEFT JOIN을 사용할 수 있습니다.

```sql
SELECT *
FROM 사원
LEFT JOIN 부서 ON 사원.부서ID = 부서.ID;
```

## RIGHT JOIN
RIGHT JOIN은 LEFT JOIN과 반대로 오른쪽 테이블의 모든 행을 선택하고, 왼쪽 테이블에서 일치하는 행을 선택하여 결과를 반환합니다. LEFT JOIN과 마찬가지로 일치하는 행이 없는 경우 NULL 값을 반환합니다. RIGHT JOIN은 일반적으로 오른쪽 테이블의 모든 레코드를 포함해야 할 때 사용됩니다.

```sql
SELECT *
FROM 사원
RIGHT JOIN 부서 ON 사원.부서ID = 부서.ID;
```

## FULL JOIN
FULL JOIN은 왼쪽 테이블과 오른쪽 테이블의 모든 행을 선택하여 결과를 반환합니다. 일치하는 행이 없는 경우 NULL 값을 반환합니다. FULL JOIN은 두 테이블 간의 모든 레코드를 포함해야 할 때 사용됩니다.

```sql
SELECT *
FROM 사원
FULL JOIN 부서 ON 사원.부서ID = 부서.ID;
```

## 요약
다음은 INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN의 차이점을 요약한 표입니다.

| JOIN 유형    | 결과에 포함되는 행                                 |
|--------------|----------------------------------------------------------|
| INNER JOIN   | 두 테이블에서 일치하는 행만 포함                        |
| LEFT JOIN    | 왼쪽 테이블의 모든 행과 일치하는 행을 포함               |
| RIGHT JOIN   | 오른쪽 테이블의 모든 행과 일치하는 행을 포함              |
| FULL JOIN    | 두 테이블의 모든 행을 포함                               |

이렇게 JOIN 연산을 사용하면 여러 테이블의 데이터를 조합하여 원하는 결과를 얻을 수 있습니다. JOIN의 사용법을 익히고, 각 JOIN 유형의 특징을 이해하면 데이터베이스에서 효과적인 쿼리를 작성할 수 있습니다.

> 참고 자료:
> - [데이터베이스 - JOIN](https://en.wikipedia.org/wiki/Join_(SQL)) #데이터베이스 #JOIN