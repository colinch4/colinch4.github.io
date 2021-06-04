---
layout: post
title: "[android] Effective java with Kotiln"
description: " "
date: 2021-06-04
tags: [android]
comments: true
share: true
---



#### item 3. 생성자에 매개 변수가 많다면 빌더를 고려해라 

```java
NutitionFacts cocCola = 
  new NutiritionFacts(240,8,100,0,35,27)
```

- 숫자들이 뜻하는 바를 알기 어려움
- 중간 필드만 기본값으로 처리 할 수 없음

Java 빈즈 패턴

```java
NutritionFacts cocaCola = new NutritionFacts();
cocaCola.setServingSize(240);
cocaCola.setSodium(35);
cocaCola.setCarbohydrate(27);
```

- 클래스를 불변으로 만들 수 없음
- 스레드 안정성 없음

```java
NutirionFacts cocaCola = new NutritionFacts
.Builder(240,8)
.calories(100)
.sodium(35)
.build();
```

- Builder 패턴을 만들기위한 Boilerplate 코드가 많다.

Kotiln 

```kotlin
class NutritionFacts{
  private val servingSize : Int,
  private val servings : Int,
  private val calories : Int = 0,
  private val fat : Int = 0,
  private val sodium : Int = 0,
  private val carbohydrate : Int = 0
}
```

```kotlin
val nutirtionFacts = NutirionFacts(
servingSize = 240,
servings = 8,
calories = 100,
fat = 0,
sodium = 35,
carbohydrate = 27
)
```



- private 생성자나 열거타입으로 싱글턴임을 보증하라.

```kotlin
object Elvis{
	fun leaveTheBuilding(){
		println("Whoa baby, i'm ouuta here");
	}
}
```

object 키워드로 싱글톤 객체를 간단히 생성

#### Item 4. 인스턴스화를 막으려거든 private 생성자를 사용하라. -> 인스턴스화를 막을 목적이 유틸클래스라면 Top Level function 을 사용하자.

#### Item 18.상속보다는 컴포지션을 사용하라.

```kotiln
class 
```

#### Item 19. 상속을 고려해 설계하고 문서화하라. 상속이 필요한 이유가 있을 때만 상속을 허용하라. -> 상속을 고려하고 문서화 하라 그러지 않았다면 상속을 금지하라.

#### Item 16. public 클래스에서는 public 필드가 접근자 메서드를 사용하라. -> 

```java
public class Point {
  private double x;
  private double y;
  
  public double getX() { return x;}
  public double getY() {return y;}
  
  public void setX(double x) {
    this.x = x;
  }
  public void setY(double y){
    this.y = y;
  }
}
```

- API 를 수정하지않고서는 표현을 바꿀수 없다.

- 불변식을 보장할 수 없다.

- 부수 작업을 수행할 수 없다.

- 캡슐화 이점을 제공하지 않는다.

- ```kotlin
  class Point {
    var x : Double = 0.0
    	get() {
        println("x")
        return field
      }
    var y : Double = 0.0
    	get(){
        println("y")
        return field
      }
  }
  ```

  

#### Item40  @Overide 를 일관되게 사용하라.

kotiln 은 override keyword를 이용하여 컴파일 에러 @Override 애너테이션을 달지않아도 오버라이딩 가능 하지만 코트린은 무조건 있어야되



- 가변객체
  - 임의의 복잡한상태에 놓일 수 있다.
  - 상태 전이를 정밀하게 문서로 남겨놓지않으면 가변 클래스는 믿고 쓰기 어려울수 있다. 
- 불변 객체
  - 객체 생성 이후 변하지않음
  - 스레드에 안전 동기화할 필요가 없다.

```java
private char ch = 'a';
private final char c = 'a';
```

```kotlin
private var character : Char = 'a'
private val character : Char = 'a'
```



final vs val

- final - 변수 선언 후에 , 선택적으로 붙이는 느낌
- val,var - 변수 선언 시 두개중에 하나로 결정해야함
  - 적어도 변수 선언시에 변경될만한 필드인지 한번 더 생각
  - 변경 여부를 잘 모르겠다면 일단 val

Kotiln List vs Java List(Kotinl MutableList)

- Kotiln List 에는 변경하는 메소드(add, addAll)가 정의되어 있지는 않음
- 실제 객체는 Mutable 이더라도 클라이언트에게 List로 노출된다면 해당 클라이언트로 하여금 내 List가 바뀌지 않도록 할 수 있다.

item 61 박싱된 기본 타입보다는 기본 타입을 사용하라.

기본 타입 vs 박싱된 기본 타입

- 박싱된 기본타입의 두 인스턴스는 값이 같아도 서로 다르게 식별 될 수 있다.
- 박싱된 기본 타입은 null을 가질 수있다.
- 기본 타입이 박싱된 기본 타입보다 시간과 메모리 사용에서 더욱 효율적

Kotlin에서 박싱된 기본 타입?

- Kotiln 에서는 기본타입이 없다.
- 컴파일 하는 과정에서 박싱된기본타입이 필요할때 Nullable,Generices 등 이 아니라면 기본 타입으로 컴파일한다.

```kotlin
val a : Int = 3 //private static final int a = 3
val b : Int? = 3 //@Nullable private static fianl Integer b = 
```

#### item 10,11,12

equals는 일반 규약을 지켜 재정의하라

equals를 재정의하려거든 hashCOde도 재정의하라

toString을 항상 재정의하라.

kotlin 에서는 기본적으로 equal, hasCode ,toString 을 만든다.

#### item 77

예외를 무시하지 마라.

```java
try {
  //구현 생략
} catch(Exception e){
  e.printStackTrace();
}
```

- 오류를 내재한 채 동작
- 문제의 원인과 아무상관 없는 곳에서 죽을 수 있다.
- 전파되게만 나둬도 디버깅 정보를 남긴채 프로그램이 신속하게 중단되게 할 수 있음

Checked Exception

- Try-catch 로 처리하거나 , 다시 throw 해야만 하는 Exception
- 단점
  - 복구가 불가능한 상황에서도 처리해야됨
  - 클라이언트에게 너무 자세한 오류정보를 제공
  - 수많은 개발자들이 처리하지 않고 무시함

Kotiln 에서는 

- Checked Excetpion 이없음
- 레퍼런스 페이지 - 여러가지 이육 ㅏ있지만, 예시로 든 것은 "예외를 무시하는 것" 

#### Item 88 지연 초기화는 신중히 사용하라

지연 초기화 

- 필드를 사용하는 시점에 초기화
  - 주로 필드 생성 비용이 비쌀때 사용한다.
- 책에서는,동기화로 인한 성능 저하를 문제로 삼음
- Kotiln 에서는 Delegated Properties(by lazy) 덕분에 쉽게 사용할 수 있음

```kotlin
val number by lazy {
	expensiveuFunction()
}
```

```kotlin
public enum class LazyThreadSafetyMode{
  SYNCHRONIZED,
  PUBLICATION,
  NONE,
}
fun <T> lazy(
mode : LazyThreadSafetyMode,
initializer : () -> T
)
```

- 사용시엔 동기화 수준을 최소화해서 사용하자.

#### Item 31 한정적 와일드카드를 사용해. API의 유연성을 높여라

//todo 