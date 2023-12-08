---
layout: post
title: "[sql] Serializable, Repeatable Read, Read Committed, Read Uncommitted 격리 단계의 차이점은 무엇인가요?"
description: " "
date: 2023-12-08
tags: [sql]
comments: true
share: true
---

1. **Read Uncommitted**:
   - 이 격리 수준에서는 다른 트랜잭션이 아직 완료되지 않은 데이터를 읽을 수 있습니다.
   - 따라서 이론적으로 일관성이 없는 결과를 얻을 수 있습니다.

2. **Read Committed**:
   - 다른 트랜잭션이 수정 중인 데이터를 읽을 수 없습니다.
   - 이로 인해 쓰기 작업을 통해 데이터가 변경되는 경우 일관성이 유지됩니다.

3. **Repeatable Read**:
   - 한 트랜잭션 내에서 같은 쿼리를 실행해도 같은 결과를 보장합니다.
   - 따라서 읽기 작업 중에 다른 트랜잭션에서의 수정이 반영되지 않습니다.

4. **Serializable**:
   - 가장 높은 수준으로, 트랜잭션 간에 격리를 완전히 보장합니다.
   - 이로 인해 모든 읽기 및 쓰기 작업은 순차적으로 수행되어 데이터 일관성이 유지됩니다.

각 격리 수준은 동시성과 일관성 사이의 균형을 유지하며, 데이터의 정확성과 신뢰성을 보장하기 위해 선택되어야 합니다.