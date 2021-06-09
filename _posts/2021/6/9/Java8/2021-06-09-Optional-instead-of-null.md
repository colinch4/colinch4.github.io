---
layout: post
title: "[Java8] null 대신 Optional"
description: " "
date: 2021-06-09
tags: [Java8]
comments: true
share: true
---

null 대신 Optional
------------------

### 값이 없는 상황을 어떻게 처리할까?

#### null 때문에 발생하는 문제

-	에러의 근원이다.
-	코드를 어지럽힌다.
-	아무 의미가 없다.
-	자바 철학에 위배된다.
-	형식 시스템에 구멍을 만든다.

### Optional 클래스 소개

![Optional 클래스 소개](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzamtQLUltekcwems)

### Optional 적용 패턴

#### Optional 객체 만들기

-	빈 Optional

```java
Optional<Car> optCar = Optional.empty();
```

-	null이 아닌 값으로 Optional 만들기

```java
Optional<Car> optCar = Optional.of(car);
```

-	null값으로 Optional 만들기

```java
Optional<Car> optCar = Optional.ofNullable(car);
```

#### 맵으로 Optional의 값을 추출하고 변환하기

```java
// 기존 코드
String name = null;
if(insurance != null) {
  name = insurance.getName();
}

// Optional 사용 코드
Optional<Insurance> optlnsurance = Optional .ofNullable(insurance);
Optional<String> name = optlnsurance.map(Insurance::getName);
```

#### flatMap으로 Optional 객체 연결

```java
Optional<Person> optPerson = Optional.of(person);
Optional<String> name =
    optPerson.map(Person::getCar)
        .map(Car::getlnsurance)
        .map(Insurance::getName);
```

-	위 코드는 컴파일되지 않는다. map 연산의 결과는 Optional<Optional<Car>> 형식의 객체다.

-	다음과 같이 구현해야 한다.

```java
public String getCarlnsuranceName(Optional<Person> person) {
  return person.flatMap(Person::getCar)
               .flatMap(Car::getlnsurance)
               .map(Insurance::getName)
               .orElse("Unknown");
}
```

-	따라서 flatMap 연산으로 Optional을 평준화한다. 평준화 과정이란 이론적으로 두 Optional을 합치는 기능을 수행하면서 둘 중 하나라도 null이면 빈 Optional을 생성하는 연산이다.

![Optional](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzNHBNNWFHbWotRGM)

### Optional 클래스의 메서드

![Optional 클래스의 메서드](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzaW1HZlJEblRoVmc)

### 요약

-	역사적으로 프로그래밍 언어에서는 null 레퍼런스로 값이 없는 상황을 표현해왔다.
-	자바 8에서는 값이 있거나 없음을 표현할 수 있는 클래스 java.util.Optional<T>를 제공한다.
-	팩토리 메서드 Optional.empty, Optional.ofNullable, Optional.of 등을 이용해서 Optional 객체를 만들 수 있다.
-	Optional 클래스는 스트림과 비슷한 연산을 수행하는 map, flatMap, filter 등의 메서드를 제공한다.
-	Optional로 값이 없는 상황을 적절하게 처리하도록 강제할 수 있다. 즉, Optional로 예상치 못한 null 예외를 방지할 수 있다.
-	Optional을 활용하면 더 좋은 API를 설계할 수 있다. 즉, 사용자는 메서드의 시그너처만 보고도 Optional값이 사용되거나 반환되는지 에측할 수 있다.
