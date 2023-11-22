---
layout: post
title: "[Java8] 스트림 소개"
description: " "
date: 2021-06-09
tags: [java]
comments: true
share: true
---

스트림 소개
-----------

목차
----

-	[스트림이란 무엇인가?](#스트림이란-무엇인가)
-	[스트림 시작하기](#스트림-시작하기)
-	[스트림과 컬렉션](#스트림과-컬렉션)
	-	[딱 한 번만 탐색할 수 있다.](#딱-한-번만-탐색할-수-있다)
	-	[외부 반복과 내부 반복](#외부-반복과-내부-반복)
-	[스트림 연산](#스트림-연산)
	-	[중간 연산](#중간-연산)
	-	[최종 연산](#최종-연산)
	-	[스트림 이용하기](#스트림-이용하기)
-	[요약](#요약)

### 스트림이란 무엇인가?

-	`스트림`은 자바 API에 새로 추가된 기능으로, 스트림을 이용하면 선언형(즉, 데이터를 처리하는 임시 구현 코드 대신 질의로 표현할 수 있다.)
-	데이터를 투명하게 병렬로 처리할 수 있다.

```java
// 기존 자바 코드
// 누적 자료 필터링
List<Dish> lowCaloricDishes = new ArrayList<>();
for(Dish d : menu) {
  lowCaloricDishes.add(d);
}
// 익명 클래스로 요리 정렬
Collections.sort(lowCaloricDishes, new Comparator<Dish>() {
  public int compare(Dish dl, Dish d2) {
    return Integer.compare(dl.getCalories(), d2.getCalories());
  }
});
// 정렬된 리스트를 처리하면서 요리 이름 선택
List(String> lowCaloricDishesName = new ArrayList<>();
for(Dish d : lowCaloricDishes) {
  lowCaloricDishesName.add(d.getName());
}


// 최신 자바 8 코드
List<String> lowCaloricDishesName =
                menu.stream()
                        .filter(d -> d.getCalories() < 400)
                        .sorted(comparing(Dish::getCalories))
                        .map(Dish::getName)
                        .collect(toList());            
```

-	선언형으로 코드를 구현할 수 있다.
-	이전 코드보다 쉽게 구현할 수 있다.
-	여러 빌딩 블록 연산을 연결해서 복잡한 데이터 처리 파이프라인을 만들 수 있다.

![파이프라인](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzMFFJVVI0bGRuVk0)

-	우리는 데이터 처리 과정을 병렬화하면서 스레드와 락을 걱정할 필요가 없다.
-	스트림 API특징
	-	선언형 : 더 간결하고 가독성이 좋아진다.
	-	조립할 수 있음 : 유연성이 좋아진다.
	-	병렬화 : 성능이 좋아진다.

### 스트림 시작하기

-	스팀림이란 '데이터 처리 연산을 지원하도록 소스에서 추출된 연속된 요소'로 정의할 수 있다.
-	연속된 요소
	-	컬렉션은 자료구조이므로 컬렉션에서는 요소 저장 및 접근 연산이 주로 이룬다.
	-	스트림은 filter, sorted, map처럼 표현 계산식이 주를 이룬다.
	-	즉, 컬렉션은 주제는 데이터, 스트림의 주제는 계산이다.
-	데이터 처리 연산
	-	스트림은 데이터베이스와 비슷한 연산을 지원한다. 스트림 연산은 순차적으로 또는 병렬로 실했할 수 있다.
-	파이프라이닝
	-	대부분의 스트림 연산은 스트림 연산끼리 연결해서 커다란 파이프라인을 구성할 수 있도록 스트림 자신을 반환한다.
-	내부 반복
	-	내부반복을 지원한다.
-	`filter`
	-	람다를 인수로 받아 스트림에서 특정 요서를 제외시킨다.
-	`map`
	-	람다를 이용해서 한 요소를 다른 요소로 변환하거나 정보를 추출한다.
-	`limit`
	-	정해진 개수 이상의 요소가 스트림에 저장되지 못하게 스트림 크기를 축소한다.
-	`collect`
	-	스트림을 다른 형식으로 변환한다.

![스티림 시작하기](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzYmFodGR3MWhwNWs)

### 스트림과 컬렉션

![스트림과 컬렉션](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzMHZKZEIza3UtaTg)

#### 딱 한 번만 탐색할 수 있다.

```java
List(String) title = Arrays.asList("Java8", "In", "Action");
Stream(String) s = title.stream();
s.forEach(System.out::println); // title 단어 출력
s.forEach(System.out::println); // Excepsion 발생.
```

#### 외부 반복과 내부 반복

-	for-each 사용 : `외부반복`
-	스트림 라이브로리로 반복 : `내부 반복`
-	내부 반복은 병렬성 구현을 자동으로 선택하나, 외부 반복은 병렬성을 스스로 관리해야 한다.

### 스트림 연산

-	연결할 수 있는 스트림 연산을 `중간 연산`이라하고, 스트림을 닫는 연산을 `최종 연산`이라고 한다.

![중간 연산과 최종 연산 ](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzTzU1OVBhMEJQWE0)

#### 중간 연산

-	중간 연산의 중요한 특징은 단말 연산을 스트림 파이프라인에 실행하기 전까지는 아무 연산도 수행하지 않는다는 것, 즉 게이르다는 것이다. 중간 연산을 합친 다음에 함쳐진 중간 연산을 최종 연산으로 한 번에 처리하기 때문이다.

#### 최종 연산

-	최종 연산은 스트림 파이프라인에서 결과를 도출한다. 스트림 이외의 결과가 반환된다.

#### 스트림 이용하기

> -	질의를 수행할 (컬렉션 같은) `데이터 소스`
> -	스티림 파이프라인을 구성할 `중간 연산` 연결
> -	스트림 파이프라인을 실행하고 결과를 만들 `최종 연산`

![중간 연산과 최종 연산-2](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzTFZhSm9wWmZXNzg)

### 요약

-	스트림은 소스에서 추출된 연속 요소로, 데이터 처리 연산을 지원한다.
-	스트림은 내부 반복을 지원한다. 내부 반복은 filter, map, sorted 등의 연산으로 반복을 추상화한다.
-	스트림에는 중간연산과 최종 연산이 있다.
-	filter와 map처럼 스트림을 반환하면서 다른 연산과 연결될 수 있는 연산을 중간연산이라고 한다. 중간 연산을 이용해서 파이프라인을 구성할 수 있지만 중간 연산으로는 어떤 결과도 생성할 수 없다.
-	forEach나 count처럼 스트림 파이프라인을 처리해서 스트림이 아닌 결과를 반환하는 연산을 최종 연산이라고 한다.
-	스트림의 요소는 요청할 때만 계산된다.
