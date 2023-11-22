---
layout: post
title: "[Java8] 스트림으로 데이터 수집"
description: " "
date: 2021-06-09
tags: [java]
comments: true
share: true
---

스트림으로 데이터 수집
----------------------

목차
----

-	[컬렉터란 무엇인가?](#컬렉터란-무엇인가)
	-	[고급 리듀싱 기능을 수행하는 컬렉터](#고급-리듀싱-기능을-수행하는-컬렉터)
	-	[미리 정의된 컬렉터](#미리-정의된-컬렉터)
-	[리듀싱과 요약](#리듀싱과-요약)
	-	[스트림값에서 최댓값과 최솟값 검색](#스트림값에서-최댓값과-최솟값-검색)
	-	[요약 연산](#요약-연산)
	-	[문자열 연결](#문자열-연결)
	-	[범용 리듀싱 요약 연산](#범용-리듀싱-요약-연산)
-	[그룹화](#그룹화)
	-	[다수준 그룹화](#다수준-그룹화)
	-	[서브그룹으로 데이터 수집](#서브그룹으로-데이터-수집)
-	[분할](#분할)
	-	[분할의 장점](#분할의-장점)
-	[Collections에서 제공하는 정적 팩토리 메서드로 만들 수 있는 모든 컬렉터](#collections에서-제공하는-정적-팩토리-메서드로-만들-수-있는-모든-컬렉터)
-	[요약](#요약)

### 컬렉터란 무엇인가?

#### 고급 리듀싱 기능을 수행하는 컬렉터

-	스트림에 collect를 호출하면 스트림의 요소에(컬렉터로 파라미터화된) 리듀싱 연산이 수행된다.

![리듀싱 연산](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzUlV3ajNHRDNvbEE)

#### 미리 정의된 컬렉터

-	Collections에서 제공하는 메서드의 기능은 크게 세가지로 구분
	1.	스트림 요소를 하나의 값으로 리듀스하고 요약
	2.	요소 그룹화
	3.	요소 분할

### 리듀싱과 요약

#### 스트림값에서 최댓값과 최솟값 검색

-	Collections.maxBy, Collections.minBy 두 개의 메서드를 이용해서 스트림의 최댓값과 최솟값을 계산할 수 있다.

```java
Comparator<Dish> dishCaloriesComparator =
      Comparator.comparinglnt(Dish::getCalories);
Optional<Dish> mostCalorieDish =
                menu.stream()
                .collect(maxBy(dishCaloriesComparator));
```

#### 요약 연산

-	Collections 클래스는 Collections.sumingInt라는 특별한 요약 팩토리 메서드를 제공한다.

```java
int totalCalories = menu.stream().collect(summingInt(Dish::getCalories));
```

-	summingLong, summingDouble 등도 있다.
-	단순 합계 외의 계산 등의 연산도 요약 기능으로 제공된다.
-	Collections.averagingLong, Collections.averagingDouble,Collections.averagingInt 등으로 평균을 계산할 수 있다.
-	위의 연산을 한번에 수행도 가능하다. summarizingInt으로 할 수 있다.

```java
IntSummaryStatistics menuStatistics =
menu.stream().collect(summarizinglnt(Dish::getCalories));
// IntSummaryStatistics { count=9, sum=4388, min=128,average=477.777778, max=888 }
```

#### 문자열 연결

-	컬렉터에 joining 팩토리 메서드를 이용하면 모든 문자열을 하나의 문자열로 연결해서 반환한다.

```java
String shortMenu = menu.stream().map(Dish::getName).collect(joining(", "));
// pork, beef, chicken, french fries, rice, season fruit, pizza, prawns, salmon
```

#### 범용 리듀싱 요약 연산

-	지금까지 살펴본 모든 컬렉터는 reducing 팩토리 메서드로 정의 가능하다.

### 그룹화

```java
Map<Dish.Type, List<Dish>> dishesByType = menu.stream().collect(groupingBy(Dish::getType));
// {FISH=[prawns, salmon], OTHER=[french fries, rice, season fruit, pizza], MEAT=[pork, beef, chicken]}
```

#### 다수준 그룹화

```java
Map<Dish.Type, Map<CaloricLevel , List<Dish>>> dishesByTypeCaloricLevel =
  menu.stream().collect(
    groupingBy(Dish::getType,
      groupingBy(dish -> {
        if (dish.getCalories() <= 400) {
          return C때ricLevel.DIET;
        } else if (dish. getCalories () <= 700) {
          return CaloricLevel.NORMAL;
        } else {  
          return CaloricLevel.FAT;
        }
      })
  )
);
/*
{MEAT={DIET=[chicken], NORMAL=[beef], FAT=[pork]},
FISH={DIET=[prawns], NORMAL=[salmon]},
OTHER={DIET=[rice, seasonal fruit], NORMAL=[french fries, pizza]}}
*/
```

#### 서브그룹으로 데이터 수집

```java
Map<Dish.Type, Long> typesCount = menu.stream( ).collect(groupingBy(Dish::getType, counting()));
// {MEAT=3, FISH=2 , OTHER=4}
```

### 분할

-	분할은 `분할함수`라 불리는 프레디케이트를 분류 함수로 사용하는 특수한 그룹화 기능이다.

```java
Map<Boolean, List<Dish>> partitionedMenu =
                menu.stream().collect(partitioningBy(Dish::isVegetarian));
```

#### 분할의 장점

-	참, 거짓 두 가지 요소의 스티림 리스트를 모두 유지한다는 것이 분할의 장점이다.
-	두 번째 인수로 전달할 수 있는 오버로드 된 버전도 가능하다.

```java
Map<Boolean, Map<Dish.Type , List<Dish>>> vegetarianDishesByType =
menu.stream().collect(
                    partitioningBy(Dish::isVegetarian,
                    groupingBy(Dish::getType)));
// {false={FISH=[prawns, salmon], MEAT=[pork, beef, chicken]},true={OTHER=[french fries, rice, seasonfruit , pizza]}}
```

### Collections에서 제공하는 정적 팩토리 메서드로 만들 수 있는 모든 컬렉터

![Collections-1](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzbGtYNGd0dG5yVXM)

![Collections-2](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzSFFfM3ZqNjZ1V28)

### 요약

-	colect는 스트림의 요소를 요약 결과로 누적하는 다양한 방법(컬렉터라 불리는)을 인수로 갖는 최종 연산이다.
-	스트림의 요소를 하나의 값으로 리듀스하고 요약하는 컬렉터뿐 아니라 최솟값, 최댓값, 평균값을 계산하는 컬렉터 등이 미리 정의되어 있다.
-	미리 정의된 컬렉터인 groupingBy로 스트림의 요소를 그룹화하거나, partitioningBy로 스트림의 요소를 분할할 수 있다.
-	켈렉터는 다수준의 그룹화, 분할, 리듀싱 연산에 적합하게 설계되어 있다.
-	Collector 인터페이스에 정의된 메서드를 구현해서 커스텀 켈렉터를 개발할 수 있다.
