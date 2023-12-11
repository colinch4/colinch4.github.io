---
layout: post
title: "[sql] 컬럼값의 비교를 위한 스칼라 함수 (EQUALS, GREATER THAN, LESS THAN 등)"
description: " "
date: 2023-12-11
tags: [sql]
comments: true
share: true
---

## 스칼라 함수의 예시
1. **EQUALS(같음)**: 두 값이 동일한지 확인
    ```sql
    SELECT * FROM 테이블 WHERE 컬럼 = 값;
    ```

2. **GREATER THAN(크다)**: 첫 번째 값이 두 번째 값보다 큰지 확인
    ```sql
    SELECT * FROM 테이블 WHERE 컬럼 > 값;
    ```

3. **LESS THAN(작다)**: 첫 번째 값이 두 번째 값보다 작은지 확인
    ```sql
    SELECT * FROM 테이블 WHERE 컬럼 < 값;
    ```

4. **GREATER THAN OR EQUALS(크거나 같음)**: 첫 번째 값이 두 번째 값보다 크거나 같은지 확인
    ```sql
    SELECT * FROM 테이블 WHERE 컬럼 >= 값;
    ```

5. **LESS THAN OR EQUALS(작거나 같음)**: 첫 번째 값이 두 번째 값보다 작거나 같은지 확인
    ```sql
    SELECT * FROM 테이블 WHERE 컬럼 <= 값;
    ```

위의 예시를 통해 스칼라 함수를 사용하여 컬럼값을 비교하는 방법을 이해할 수 있습니다. 이러한 스칼라 함수를 효과적으로 활용하여 SQL 쿼리를 작성할 수 있습니다.