---
layout: post
title: "[python] 스파크 RDD(Resilient Distributed Dataset) 개념과 활용법"
description: " "
date: 2023-12-07
tags: [python]
comments: true
share: true
---

## 소개

스파크 RDD(Resilient Distributed Dataset)는 스파크에서 가장 기본적이고 강력한 추상화 개념 중 하나입니다. RDD는 불변(immutable)하며, 여러 분산 노드에 분산되어 저장되는 데이터 구조입니다. 이를 통해 스파크는 대규모 데이터 처리를 효과적으로 수행할 수 있습니다.

## RDD 개념

### RDD 생성하기

RDD는 크게 두 가지 방법으로 생성할 수 있습니다.

1. 외부 데이터 소스로부터 생성: 스파크는 다양한 데이터 소스를 지원하며, 이를 통해 RDD를 생성할 수 있습니다. 예를 들어, 텍스트 파일, CSV 파일, JSON 파일 등을 사용할 수 있습니다.

2. 기존 RDD로부터 생성: 이미 생성된 다른 RDD를 사용하여 새로운 RDD를 생성할 수 있습니다. 이를 통해 구조적이고 유연한 데이터 처리 파이프라인을 구축할 수 있습니다.

### RDD 변환하기

RDD는 불변이므로 변환 연산을 통해 새로운 RDD를 생성합니다. 주요 RDD 변환 연산은 다음과 같습니다.

- map: 각 요소에 함수를 적용하여 새로운 RDD를 생성합니다.
- filter: 조건에 맞는 요소로만 구성된 새로운 RDD를 생성합니다.
- flatMap: 각 요소에 대해 여러 결과를 반환하는 함수를 적용하여 새로운 RDD를 생성합니다.
- union: 두 개의 RDD를 합치는 연산을 수행하여 새로운 RDD를 생성합니다.
- distinct: 중복된 요소를 제거하여 새로운 RDD를 생성합니다.

### RDD 액션

RDD는 변환 연산과 함께 액션 연산을 사용하여 계산을 수행합니다. 주요 RDD 액션 연산은 다음과 같습니다.

- collect: RDD의 모든 요소를 로컬 컬렉션으로 가져옵니다.
- count: RDD의 요소 개수를 반환합니다.
- reduce: 요소를 반복적으로 결합하여 단일 값을 반환합니다.
- saveAsTextFile: RDD의 요소를 텍스트 파일로 저장합니다.
- foreach: 각 요소에 대해 지정된 함수를 실행합니다.

## 활용법

스파크 RDD는 대규모 데이터 처리 작업에 널리 사용됩니다. 예를 들어, 다음과 같은 작업에 사용할 수 있습니다.

- 데이터 필터링: filter 연산을 사용하여 특정 조건에 맞는 레코드를 필터링할 수 있습니다.
- 데이터 변환: map 연산을 사용하여 각 요소를 변환하거나, flatMap 연산을 사용하여 여러 결과를 생성할 수 있습니다.
- 그룹화 및 집계: groupByKey 및 reduceByKey 연산을 사용하여 데이터를 그룹화하고 집계할 수 있습니다.
- 정렬: sortByKey 연산을 사용하여 키에 따라 RDD를 정렬할 수 있습니다.

## 결론

스파크 RDD는 대규모 데이터 처리를 위한 강력한 도구입니다. 이를 통해 병렬로 작업을 처리하고, 효율적인 데이터 처리 파이프라인을 구축할 수 있습니다. RDD 개념과 활용법을 익히고 적절하게 활용한다면, 스파크를 통해 빠르고 강력한 데이터 분석 및 처리 작업을 수행할 수 있습니다.

[참고 문서]: 
- [스파크 공식 문서](https://spark.apache.org/docs/latest/rdd-programming-guide.html)
- [스파크 RDD 개요](https://data-flair.training/blogs/apache-spark-rdd-operations-transformations-actions/)