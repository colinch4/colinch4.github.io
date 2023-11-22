---
layout: post
title: "[Java8] 스트림 활용"
description: " "
date: 2021-06-09
tags: [java]
comments: true
share: true
---

스트림 활용
-----------

목차
----

-	[필터링과 슬라이싱](#필터링과-슬라이싱)
	-	[프레디케이트로 필터링](#프레디케이트로-필터링)
	-	[고유 요소 필터링](#고유-요소-필터링)
	-	[스트림 축소](#스트림-축소)
	-	[요소 건너뛰기](#요소-건너뛰기)
-	[매핑](#매핑)
	-	[스트림의 각 요소에 함수 적용하기](#스트림의-각-요소에-함수-적용하기)
	-	[스트림 평면화](#스트림-평면화)
-	[검색과 매칭](#검색과-매칭)
	-	[프레디케이트가 적어도 한 요소와 일치하는지 확인](#프레디케이트가-적어도-한-요소와-일치하는지-확인)
	-	[프레디케이트가 모든 요소와 일치하는지 검사](#프레디케이트가-모든-요소와-일치하는지-검사)
	-	[noneMatch](#nonematch)
	-	[요소 검색](#요소-검색)
	-	[첫 번째 요소 찾기](#첫-번째-요소-찾기)
-	[리듀싱](#리듀싱)
	-	[요소의 합](#요소의-합)
	-	[초기값 없음](#초기값-없음)
	-	[최댓값과 최솟값](#최댓값과-최솟값)
-	[전체 연산 요약](#전체-연산-요약)
-	[숫자형 스트림](#숫자형-스트림)
	-	[기본 특화 스트림](#기본-특화-스트림)
	-	[숫자 스트림으로 매핑](#숫자-스트림으로-매핑)
	-	[객체 스트림으로 복원](#객체-스트림으로-복원)
	-	[기본값: OptionalInt](#기본값-optionalint)
	-	[숫자 범위](#숫자-범위)
-	[스트림 만들기](#스트림-만들기)
	-	[값으로 스트림 만들기](#값으로-스트림-만들기)
	-	[배열로 스트림 만들기](#배열로-스트림-만들기)
	-	[파일로 스트림 만들기](#파일로-스트림-만들기)
	-	[함수로 무한 스트림 만들기](#함수로-무한-스트림-만들기)
-	[요약](#요약)

	### 필터링과 슬라이싱

#### 프레디케이트로 필터링

-	`filter` 메서드는 `프리디케이트`를 인수로 받아서 프레디케이트와 일치하는 모든 요소를 포함하느 스트림을 반환한다.

```java
List<Dish> vegetarianMenu =
                menu.stream()
                      .filter(Dish::isVegetarian)
                      .collect(toList());
```

![프레디케이트로 필터링](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzeDBOdjkzekZKdTA)

#### 고유 요소 필터링

-	스트림은 고유 요소로 이루어진 스트림을 반환하는 `distinct`라는 메서드도 지원한다.

```java
List<Integer> numbers = Arrays.asList(1, 2 ,1, 3, 3, 2, 4);
numbers.stream().filter (i -> i % 2 == 0)
                .distinct()
                .forEach(System.out::println);
```

![고유 요소 필터링](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzd2pqQWtKalp4Smc)

#### 스트림 축소

-	스트림은 주어진 사이즈 이하의 크기를 갖는 새로운 스트림을 반환하는 `limit(n)` 메서드를 지원한다.

```java
List<Dish> dishes = menu.stream()
                            .filter(d -> d.getCalories() > 300)
                            .limit(3)
                            .collect(toList());
```

![스트림 축소](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzcXFDcHBoZUtiYTg)

#### 요소 건너뛰기

-	스트림은 처음 n개 요소를 제외한 스트림을 반환하는 skip(n) 메서드를 지원한다.

```java
List<Dish> dishes = menu.stream()
                            .filter(d -> d.getCalories() > 300)
                            .skip(2)
                            .collect(toList());
```

### 매핑

-	SQL의 테이블에서 특정 열만 선택할 수 있다. 스트림 API의 map과 flatMap 메서드를 이용해 특정 데이터를 선택할 수 있다.

#### 스트림의 각 요소에 함수 적용하기

```java
// 요리명 추출하는 코드
List<Dish> dishes = menu.stream()
                            .map(Dish::getName)
                            .collect(toList());

// 요리명의 길이도 구하고  싶다면
List<Dish> wordLengths = menu.stream()
                                .map(Dish::getName)
                                .map(String::length)
                                .collect(toList());

```

#### 스트림 평면화

-	map과 Arrays.Stream 활용
-	flatMap 사용

```java
List<String> uniqueCharacters =
                  words.stream()
                          .map(w -> w.split(""))
                          .flatMap(Arrays::stream)
                          .distinct()
                          .collect(toList());
```

-	Stream<Stream[String]> 문제 해결을 위해 flatMap 사용.

![flatMap](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzLXcwaHZsMjNMYWM)

### 검색과 매칭

#### 프레디케이트가 적어도 한 요소와 일치하는지 확인

-	`anyMatch`를 이용한다. anyMatch는 불린을 반환하므로 최종 연산이다.

```java
if(menu.stream().anyMatch(Dish::isVegetarian)) {
  System.out.println("The menu is (somewhat) vegetarian friendly!!");
}
```

#### 프레디케이트가 모든 요소와 일치하는지 검사

-	`allMatch` 메서드는 anyMatch와 달리 스트림의 모든 요소가 주어진 프레디케이트와 일치하는지 검사한다.

```java
boolean isHealthy = menu.stream()
                            .allMatch(d -> d.getCalories() < 1000 );
```

#### noneMatch

-	allMatch 와 반대로 일치하는 요소가 없음을 확인한다.

```java
boolean isHealthy = menu.stream()
                            .noneMatch(d -> d.getCalories() >= 1000);
```

#### 요소 검색

-	`findAny` 메서드는 현재 스트림에서 임의의 요소를 반환한다. filter와 findAny를 이용해서 채식 요리를 선택할 수 있다.

```java
Optional<Dish> dish =
                 menu.stream()
                        .filter(Dish::isVegetarian)
                        .findAny();
```

#### 첫 번째 요소 찾기

-	`findFirst` 메서드 사용.

```java
List<Integer> someNumbers = Arrays.asList(1, 2, 3, 4, 5);
Optional<Integer> firstSquareDivisibleByThree =
                    someNumbers.stream()
                                  .map(x - > x * x)
                                  .filter(x - > x % 3 == 8)
                                  .findFirst(); // 9
```

> `findFirst`와 `findAny`는 일반적으로 결과과 같으나 병렬성 때문에 둘이 존재한다. 병렬 스트림에서는 제약이 없는 findAny를 사용한다.

### 리듀싱

-	모든 스트림 요소를 처리해서 값으로 도출하는 것을 `리듀싱 연산`이라고 한다.

#### 요소의 합

```java
// sum 변수의 초기값 0
// 리스트의 모든 요소를 조합하는 연산
int sum = 0;
for (int x : numbers) {
  sum += x;
}

// 위 코드를 reduce를 이용하면...
int sum = numbers.stream().reduce(0, (a,b) -> a + b);

// 모든 요소 곱셈 적용시
int sum = numbers.stream().reduce(0, (a,b) -> a * b);
```

![요소의 합](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzMzJtQ19DdlpISW8)

##### 초기값 없음

-	초기값 미입력 가능하다. 단 Optional 객체를 반환한다.

```java
Optional<Integer> sum = numbers.stream().reduce((a,b) -> a + b);
```

#### 최댓값과 최솟값

```java
// 최대값
Optional<Integer> max = numbers.stream().reduce(Integer::max);

// 최소값
Optional<Integer> min = numbers.stream().reduce(Integer::min);
```

![최댓값과 최솟값](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzbkFRM2toRnJtY00)

### 전체 연산 요약

![전체 연산 요약](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzM3ZCNW9ybXQwdEk)

### 숫자형 스트림

#### 기본 특화 스트림

##### 숫자 스트림으로 매핑

```java
// reduce 메서드로 스트림 요소의 합 계산
// 칼로리 합계 계산
int calories = menu.stream()
                      .map(Dish::getCalories)
                      .reduce(0, Integer::sum);


/*
// 틀린 코드
Stream<Dish>는 sum이라는 연산 수행 불가
int calories = menu.stream()
                      .map(Dish::getCalories)
                      .sum();
*/                      

// mapTolnt, mapToDouble, mapToLong 사용시 가능
int calories = menu.stream()
                      .mapTolnt(Dish::getCalories)
                      .sum();
```

##### 객체 스트림으로 복원

-	boxed 메서드 이용

```java
IntStream intStream = menu.stream().mapTolnt(Dish::getCalories);
Stream<Integer> stream = intStream.boxed();
```

##### 기본값: OptionalInt

```java
Optionallnt maxCalories = menu.stream()
                    .mapTolnt(Dish::getCalories)
                    .max();

// 값이 없을 때 기본 최댓값을 명시적으로 설정
int max = maxCalories.orElse(1);
```

#### 숫자 범위

-	자바 8의 `IntStream`과 `LongStream`에서는 `range`와 `rangeClosed` 메서드를 제공.
-	range 는 시작값과 종료값 미포함.
-	rangeClosed 는 사작,종료값 포함.

```java
// 1부터 100까지의 짝수 스트림
IntStream evenNumbers = IntStream.rangeClosed(1,100).filter (n-> n % 2 == 0);
```

### 스트림 만들기

#### 값으로 스트림 만들기

```java
// 모든 문자열을 대문자로 변환 후 문자열 하나씩 출력
Stream<String> stream = Stream.of( "Java 8", "Lambdas", "In", "Action");
stream.map(String::toUpperCase).forEach(System.out::println);

// 스트림을 비울 수 있다.
Stream<String> emptyStream = Stream.empty();
```

#### 배열로 스트림 만들기

```java
int [] numbers = {2, 3, 5, 7, 11, 13};
int sum = Arrays.stream(numbers).sum();
```

#### 파일로 스트림 만들기

```java
long uniqueWords = 0;
try (Stream<String) lines = Files.lines(Paths .get("data.txt"), Charset.defaultCharset()))
{
  uniqueWords = lines.flatMap(line -> Arrays.stream(line.split(" ")))
                            .distinct()
                            .count();
}
catch (IOException e)
{
}
```

#### 함수로 무한 스트림 만들기

```java
// iterate
Stream.iterate(0, n -> n + 2)
                  .limit(10)
                  .forEach(System.out::println);

// generate
Stream.generate(Math::Random)
                  .limit(5)
                  .forEach(System.out::println);
```

### 요약

-	스트림 API를 이용하면 복잡한 데이터 처리 질의를 표현할 수 있다. [전체 연산 요약](#전체-연산-요약)은 자주 사용하는 스트림 연산을 보여준다.
-	filter, distinct, skip, limit 메서드로 스트림을 필터링하거나 자를 수 있다.
-	map, flatMap 메서드로 스트림의 요소를 추출하거나 변환할 수 있다.
-	findFirst, findAny 메서드로 스트림의 요소를 검색할 수 있다. allMatch, noneMatch, anyMatch 메서드를 이용해서 주어진 프레디케이트와 일치하는 요소를 스트림에서 검색할 수 있다.
-	이들 메서드는 쇼트서킷, 즉 결과를 찾는 즉시 반환하며, 전체 스트림을 처리하지는 않는다.
-	reduce 메서드로 스트림의 모든 요소를 반복 조합하며 값을 도출할 수 있다. 예를 들어 reduce로 스트림의 최댓값이나 모든 요소의 합계를 계산할 수 있다. filter, map 등은 상태를 저장하지 않는 `상태 없는 연산`이다. reduce 같은 연산은 값을 계산하는데 필요한 상태를 저장한다. sorted, distinct 등의 메서드는 새로운 스트림을 반환하기에 앞서 스트림의 모든 요서를 버퍼에 저장해야 한다. 이런 메서드를 `상태 있는 연산`이라고 부른다.
-	IntStream, DoubleStream, LongStream은 기본형 특화 스트림이다. 이들 연산은 각각의 기본형에 맞게 특화되어 있다.
-	컬렉션뿐 아니라 값, 배열, 파일, iterate와 generate 같은 메서드로도 스트림을 만들 수 있다.
-	크기가 정해지지 않은 스트림을 무한 스트림이라고 한다.
