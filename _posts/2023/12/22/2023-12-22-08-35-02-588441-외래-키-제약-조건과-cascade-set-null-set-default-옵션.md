---
layout: post
title: "[sql] 외래 키 제약 조건과 CASCADE, SET NULL, SET DEFAULT 옵션"
description: " "
date: 2023-12-22
tags: [sql]
comments: true
share: true
---

외래 키 제약은 데이터 무결성을 보장하며, 데이터베이스에서 데이터 일관성을 유지하는 데 중요한 역할을 합니다.

외래 키가 있는 테이블에 데이터를 삽입, 업데이트, 삭제할 때 발생하는 동작을 제어하기 위해 ON DELETE 및 ON UPDATE로 세부 조건을 설정할 수 있습니다.

가장 일반적으로 사용되는 외래 키 제약 조건 중 세 가지 옵션은 CASCADE, SET NULL, SET DEFAULT 입니다.

- **CASCADE**: 부모 키가 업데이트되거나 삭제될 때, 자식 키도 함께 업데이트되거나 삭제됩니다. 
- **SET NULL**: 부모 키가 업데이트되거나 삭제될 때, 자식 키가 NULL로 설정됩니다.
- **SET DEFAULT**: 부모 키가 업데이트되거나 삭제될 때, 자식 키가 기본값으로 설정됩니다.

예를 들어, "주문" 테이블이 "고객" 테이블의 외래 키를 참조하고 있을 때, CASCADE 옵션을 설정하면 고객이 삭제되면 해당 고객과 관련된 모든 주문 또한 삭제됩니다.

이와 같이 외래 키 제약 조건과 옵션들은 데이터 관련 작업을 수행할 때 발생할 수 있는 부작용을 제어하는 데 도움이 됩니다.

참고 문헌:
- https://www.postgresql.org/docs/9.2/ddl-constraints.html