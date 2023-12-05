---
layout: post
title: "[sql] DELETE 문에서 사용하는 CASCADE, SET NULL, SET DEFAULT 등의 제약 조건 설정 방법"
description: " "
date: 2023-12-05
tags: [sql]
comments: true
share: true
---

SQL에서 DELETE 문을 사용하여 데이터를 삭제할 때, 종종 제약 조건을 설정해야 할 경우가 있습니다. 이러한 제약 조건은 CASCADE, SET NULL, SET DEFAULT 등과 같은 옵션을 사용하여 설정할 수 있습니다. 각각의 옵션은 다음과 같이 사용됩니다:

### CASCADE

CASCADE 옵션은 삭제된 레코드와 관련된 모든 레코드를 자동으로 삭제하는 기능을 제공합니다. 예를 들어, "부서" 테이블에서 "부서 번호"가 "1"인 부서를 삭제할 경우, "부서 번호"가 "1"인 모든 직원도 함께 삭제됩니다.

```sql
DELETE FROM 부서 WHERE 부서번호 = 1 CASCADE;
```

### SET NULL

SET NULL 옵션은 삭제된 레코드와 관련된 모든 레코드의 특정 필드 값을 NULL로 설정하는 기능을 제공합니다. 예를 들어, "회원" 테이블에서 "회원 번호"가 "1"인 회원을 삭제할 경우, "주문" 테이블에서 해당 회원과 관련된 모든 주문의 "회원 번호" 필드 값을 NULL로 설정할 수 있습니다.

```sql
DELETE FROM 회원 WHERE 회원번호 = 1 SET NULL 주문.회원번호;
```

### SET DEFAULT

SET DEFAULT 옵션은 삭제된 레코드와 관련된 모든 레코드의 특정 필드 값을 해당 필드의 기본값으로 설정하는 기능을 제공합니다. 예를 들어, "주문" 테이블에서 "상품 번호"가 "1"인 상품을 삭제할 경우, "주문" 테이블에서 해당 상품과 관련된 모든 주문의 "상품 번호" 필드 값을 해당 필드의 기본값으로 설정할 수 있습니다.

```sql
DELETE FROM 상품 WHERE 상품번호 = 1 SET DEFAULT 주문.상품번호;
```

위의 예제에서 "주문" 테이블의 "상품 번호" 필드는 기본값이 설정되어야 합니다.

위에서 소개한 CASCADE, SET NULL, SET DEFAULT 등의 제약 조건 설정 방법은 SQL에서 DELETE 문을 실행할 때 유용하게 활용할 수 있습니다.

---

참고 문서:

- [SQL DELETE 문](https://www.w3schools.com/sql/sql_delete.asp)
- [SQL CASCADE 제약 조건](https://www.w3schools.com/sql/sql_foreignkey.asp)
- [SQL SET NULL 옵션](https://www.w3schools.com/sql/sql_foreignkey.asp)
- [SQL SET DEFAULT 옵션](https://www.w3schools.com/sql/sql_foreignkey.asp)