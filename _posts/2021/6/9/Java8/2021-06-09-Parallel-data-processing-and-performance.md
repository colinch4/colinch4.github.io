---
layout: post
title: "[Java8] 병렬 데이터 처리와 성능"
description: " "
date: 2021-06-09
tags: [java]
comments: true
share: true
---

병렬 데이터 처리와 성능
-----------------------

### 병렬 스트림

-	컬렉션 parallelStream을 호출하면 `병렬 스트림`이 생성된다. 병렬 스티림이란 각각의 스레드에서 처리할 수 있도록 스트림 요소를 여러 청크로 분할한 스트림이다. 따라서 병렬 스트림을 이용하면 모든 멀티코어 프로세서가 각각의 청크를 처리하도록 할당할 수 있다.

#### 순차 스트림을 병렬 스트림으로 변환

-	순차 스트림에 parallel 메서드를 호출하면 기존의 함수형 리듀싱 연산(숫자 합계 계산)이 병렬로 처리된다.

```java
public static long parallelSum(long n){
  return Stream.iterate(1L, i -> i + 1)
               .limit(n)
               .parallel() // 스트림을 병렬 스트림 전환
               .reduce(0L, Long::sum);
}
```

#### 스트림 성능 측정

-	병렬 프로그래밍을 오용하면 오히려 전체 프로그램의 성능이 더 나빠질 수도 있다.

#### 병렬 스트림의 올바른 사용법

-	병렬 스트림을 잘못 사용하면서 발생하는 많은 문제는 공유된 상태를 바꾸는 알고리즘을 사용하기 때문에 일어난다.
-	다수의 스레드에서 동시에 데이터 접근시 데이터에 문제가 일어난다.
-	상태 공유에 따른 부작용을 피해야 한다.

#### 병렬 스트림 효과적으로 사용하기

-	확신이 서지 않는다면 직접 측정하라.
-	언제나 병렬 스트림이 순차 스트림보다 빠른 것은 아니다.
-	박싱을 주의하라. 자동 박싱과 언박싱은 성능을 크게 저하시킬 수 있다. 기본형 특화 스티림을 사용하는 것이 좋다.
-	순차 스트림보다 병렬스트림에서 성능이 떨어지는 연산이 있다. 특히 limit나 findFirst처럼 요소의 순서에 의존하는 연산을 병렬 스트림에서 수행하려면 비싼 비용을 치러야 한다.
-	스트림에서 수행하는 전체 파이프라인 연산 비용을 고려해야 한다.
-	소량의 데이터에서는 병렬 스트림이 도움이 되지 않는다.
-	스트림을 구성하는 자료구조가 적절한지 확인하라. 예를 들어 ArrayList를 LinkedList 보다 효율적으로 분할할 수 있다.
-	스트림의 특성과 파이프라인의 중간 연산이 스트림의 특성을 어떻게 바꾸는지에 따라 분해 과정의 성능이 달라질 수 있다.
-	최종 연산의 병합 과정(예를 들면 Collector의 combiner 메서드) 비용을 살펴보라. 병합 과정의 비용이 비싸다면 병렬 스트림으로 얻는 성능의 이익이 서브스트림의 부분결과를 합치는 과정에서 상쇄될 수 있다.

![스트림 소스와 분해성](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzaUtFV2gzWUpIaTA)

### Spliterator

-	자바 8에서는 Spliterator라는 새로운 인터페이스를 제공한다. Spliterator는 `분할할 수 있는 반복자`라는 의미이다. Iterator 처럼 Spliterator는 소스의 탐색 기능을 제공한다는 점은 같지만 Spliterator는 병렬 작업에 특화되어 있다.

### 요약

-	내부 반복을 이용하면 명시적으로 다른 스레드를 사용하지 않고도 스트림을 병렬로 처리 할 수 있다.
-	간단하게 스트림을 병렬로 처리할 수 있지만 항상 병렬 처리가 빠른 것은 아니다. 병렬 소프트웨어 동작 방법과 성능은 직관적이지 않을 때가 많으므로 병렬 처리를 사용했을 때 성능을 직접 측정해봐야 한다.
-	병렬 스트림으로 데이터 집합을 병렬 실행할 때 특히 처리해야 할 데이터가 아주 많거나 각 요소를 처리하는 데 오랜 시간이 걸릴 때 성능을 높일 수 있다.
-	가능하면 기본형 특화 스트림을 사용하는 등 올바른 자료구조 선택이 어떤 연산을 병렬로 처리하는 것보다 성능적으로 더 큰 영향을 미칠 수 있다.
-	포크/조인 프레임워크에서는 병렬화할 수 있는 태스크를 작은 태스크로 분할한 다음에 분할된 태스크를 가각의 스레드로 실행하며 서브태스크 각각의 결과를 합쳐서 최종 결과를 생산한다.
-	Spliterator는 탐색하려는 데이터를 포함하는 스트림을 어떻게 병렬화할 것인지 정의한다.
