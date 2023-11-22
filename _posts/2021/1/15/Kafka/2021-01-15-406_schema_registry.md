---
layout: post
title: "[Kafka] 6장. 스키마 레지스트리"
description: " "
date: 2021-01-15
tags: [kafka]
comments: true
share: true
---

## Kafka 기초 다지기

 **출처 : [카프카 핵심 가이드 (O'Reilly)](https://book.naver.com/bookdb/book_detail.nhn?bid=14093855)**

#### 목차

1. [카프카 훑어보기](https://colinch4.github.io/2021-01-15/401_Intro/)
2. [범용 메시지 큐와 비교하기](https://colinch4.github.io/2021-01-15/402_compare/)
3. [카프카 프로듀서 : 카프카에 메시지 쓰기](https://colinch4.github.io/2021-01-15/403_producer/)
4. [카프카 컨슈머 : 중요 개념](https://colinch4.github.io/2021-01-15/404_consumer_core/)
5. [카프카 컨슈머 : 카프카에서 데이터 읽기](https://colinch4.github.io/2021-01-15/405_consumer_use/)
6. **스키마 레지스트리**
7. [카프카 내부 메커니즘](https://colinch4.github.io/2021-01-15/407_inside/)
8. [신뢰성 있는 데이터 전달](https://colinch4.github.io/2021-01-15/408_reliability/)
9. [데이터 파이프라인 구축하기](https://colinch4.github.io/2021-01-15/409_data_pipeline/)

- [confluent 예제](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2021/1/15/Kafka/2021-01-15-99_confluent_example)
- [schema registry 예제](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2021/1/15/Kafka/2021-01-15-99_schema_registry_example)



------

## 스키마 레지스트리

### 1. 

