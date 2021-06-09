---
layout: post
title: "[Java8] 동작 파라미터화 코드 전달하기"
description: " "
date: 2021-06-09
tags: [Java8]
comments: true
share: true
---

동작 파라미터화 코드 전달하기
-----------------------------

목차
----

-	[변화하는 요구사항 대응하기](#변화하는-요구사항-대응하기)
	-	[첫 번째 시도: 녹색 사과 필터링](#첫-번째-시도-녹색-사과-필터링)
	-	[두 번째 시도: 색을 파라미터화](#두-번째-시도-색을-파라미터화)
-	[동작 파라미터화](#동작-파라미터화)
	-	[세 번째 시도: 추상적 조건으로 필터링](#세-번째-시도-추상적-조건으로-필터링)
-	[복잡한 과정 간소화](#복잡한-과정-간소화)
	-	[네 번째 시도: 익명 클래스 사용](#네-번째-시도-익명-클래스-사용)
	-	[다섯 번째 시도: 람다 표현식 사용](#다섯-번째-시도-람다-표현식-사용)
	-	[여섯 번째 시도: 리스트 형식으로 추상화](#여섯-번째-시도-리스트-형식으로-추상화)
-	[실전 예제](#실전-예제)
	-	[Comparator로 정렬하기](#comparator로-정렬하기)
	-	[Runnable로 코드 블록 실행하기](#runnable로-코드-블록-실행하기)
-	[요약](#요약)

### 변화하는 요구사항 대응하기

#### 첫 번째 시도: 녹색 사과 필터링

```java
List<Apple> inventory = Arrays.asList(new Apple(80,"green"), new Apple(155, "green"), new Apple(120, "red"));
```

```java
public static List<Apple> filterGreenApples(List<Apple> inventory){
    List<Apple> result = new ArrayList<>();
    for(Apple apple: inventory){
        if("green".equals(apple.getColor())){
            result.add(apple);
        }
    }
    return result;
}

// 실행 코드
List<Apple> greenApples = filterApplesByColor(inventory);
```

#### 두 번째 시도: 색을 파라미터화

-	개선 : 색을 파라미터화할 수 있도록 메서드에 파라미터를 추가.

```java
public static List<Apple> filterApplesByColor(List<Apple> inventory, String color){
    List<Apple> result = new ArrayList<>();
    for(Apple apple: inventory){
        if(apple.getColor().equals(color)){
            result.add(apple);
        }
    }
    return result;
}

// 실행 코드
List<Apple> greenApples = filterApplesByColor(inventory, "green");
List<Apple> redApples = filterApplesByColor(inventory, "red");
```

### 동작 파라미터화

-	사과의 어떤 속서에 기초해서 불린값을 반환(예를 들어 사과가 녹색인가? 150그램 이상인가?)하는 방법이 있다. 이와 같은 동작을 `프레디케이트(predicate)`라고 한다.

-	전략 디자인 패턴은 각 알고리즘을 캡슐화하는 알고리즘 패밀리를 정의해둔 다음에 런타임에 알고리즘을 선택하는 기법이다.

![사과를 선택하는 다양한 전략](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzd3h5MnFXd0QyUlE)

```java
interface ApplePredicate{
	public boolean test(Apple a);
}

static class AppleWeightPredicate implements ApplePredicate{
	public boolean test(Apple apple){
		return apple.getWeight() > 150;
	}
}

static class AppleColorPredicate implements ApplePredicate{
	public boolean test(Apple apple){
		return "green".equals(apple.getColor());
	}
}
```

#### 세 번째 시도: 추상적 조건으로 필터링

```java
public static List<Apple> filter(List<Apple> inventory, ApplePredicate p){
    List<Apple> result = new ArrayList<>();
    for(Apple apple : inventory){
        if(p.test(apple)){
            result.add(apple);
        }
    }
    return result;
}    

// 실행
List<Apple> heavyApples = filter(inventory, new AppleWeightPredicate());
List<Apple> redAndHeavyApples = filter(inventory, new AppleRedAndHeavyPredicate());
```

-	하지만 이 코드를 필터링하느라 많은 로직과 관계없는 코드가 추가되었다.  

![불필요한 코드](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzOW9BSU5OU1otV3c)

-	한 개의 파라미터, 다양한 동작

![한 개의 파라미터, 다양한 동작](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzelRyekQwMF9iRkU)

### 복잡한 과정 간소화

#### 네 번째 시도: 익명 클래스 사용

-	익명 클래스를 이용하면 코드의 양은 줄일 수 있지만, 모든 것이 해결 되는 것은 아니다.
-	반복되는 지저분한 코드 발생.

```java
List<Apple> redApples2 = filter(inventory, new ApplePredicate() {
    public boolean test(Apple a){
        return a.getColor().equals("red");
    }
});
```

#### 다섯 번째 시도: 람다 표현식 사용

```java
List<Apple> result = filter(inventory, (Apple apple) -> "red".equals(apple.getColor()));
```

#### 여섯 번째 시도: 리스트 형식으로 추상화

```java
public interface Predicate<T>{
    boolean test(T t);
}

public static <T> List<T> filter(List<T> list, Predicate<T> p) {
  List<T> result = new ArrayList<>();
  for(T e: list) {
    if(p.test(e)) {      
      result.add(e);
    }
  }
  return result;
}

List<Apple> redApples = filter(inventory, (Apple apple) -> "red".equals(apple.getColor()));
List<String> evenNumber = filter(numbers, (Integer i) -> i % 2 == 0);
```

### 실전 예제

#### Comparator로 정렬하기

```java
// java.util.Comparator
public interface Comparator<T> {
  public int compare(T o1 , T o2);
}
```

-	익명함수

```java
inventory.sort(new Comparator<Apple>() {
        public int compare(Apple o1, Apple o2) {
            return o1.getWeight().compareTo(o2.getWeight());
        };
});
```

-	람다 표현식

```java
inventory.sort( (Apple o1, Apple o2) -> o1.getWeight().compareTo(o2.getWeight()));
```

#### Runnable로 코드 블록 실행하기

```java
// java.lang.Runnable
public interface Runnable {
  public void run();
}
```

```java
Thread t = new Thread(new Runnable() {
  public void run() {
    System.out.println("Hello world");
  }
});
```

```java
Thread t = new Thread(() -> System.out.println("Hello world"));
```

### 요약

-	동작 파라미터화에서는 메서드 내부적으로 다양한 동작을 수행할 수 있도록 코드를 메서드 인수로 전달한다.
-	동작 파라미터화를 이용하면 변화하는 요구사항에 더 잘 대응할 수 있는 코드를 구현할 수 있으며 나중에 엔지니어링 비용을 줄일 수 있다.
-	코드 전달 기법을 이용하면 동작을 메서드의 인수로 전달할 수 있다. 하지만 자바8 이전에는 코드를 지저분하게 구현해야 했다. 익명 클래스로도 어느정도 코드를 깔끔하게 만들 수 있지만 자바 8에서는 인터페이스를 상속받아 여러 클래스를 구현해야 하는 수고를 없앨 수 있는 방법을 제공한다.
-	자바 API의 많은 메서드는 정렬, 스레드 등을 포함한 다양한 동작으로 파라미터화할 수 있다.
