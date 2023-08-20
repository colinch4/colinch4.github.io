---
layout: post
title: "자바 어노테이션 ( Annotation )"
description: "@ <-- 요놈은 기본적으로 컴파일러에게 이게 어노테이션이다라고 알린다. @ 마크 다음에 오는 문자는 해당 어노테이션의 이름이고 여기서는 Entity !!! 자바 어노테이션은 값을 세팅할수있는 요소들을 가질수있는데 속성이나 파라미터 쯤이라고 볼수있지."
date: 2020-04-09 14:34
tags: [java]
comments: true
share: true
---


## **1. 자바 어노테이션 기본 문법**

  

## Annotation 이름

기본적으로 요렇게 생김
```java
@Entity  
```
`@` <-- 요놈은 기본적으로 컴파일러에게 이게 어노테이션이다라고 알린다.

@ 마크 다음에 오는 문자는 해당 어노테이션의 이름이고 여기서는 "Entity" !!!

###   

### Annotation 요소 (Element)

자바 어노테이션은 값을 세팅할수있는 요소들을 가질수있는데 속성이나 파라미터 쯤이라고 볼수있지.
```java
@Entity(tableName = "vehicles")  
```
위에서는 tableName 이라는 이름의 요소를 하나 가지고있다는뜻이야. 값은 "vehicles" 이군.

물론 아래와 같이 여러개의 요소를 가질수도있어.
```java
@Entity(tableName = "vehicles", primaryKey = "id") 
```
하나만 요소로 가질 경우 다음과 같이 짧게 줄여 쓸수도있지.
```java
@InsertNew("yes") 
```
##   

## Annotation 선언위치(Placement)

어노테이션은 클래스, 인터페이스, 메소드, 메소드 파라미터, 필드, 지역변수 위에 위치할수있어.

아래는 클래스 위에 선언되어있는 것이고
```java
@Entity
public class Vehicle {
}
```
위에 말했다시피 @로 시작하고 이름은 Entity 야. Entity 어노테이션은 그냥 내가 만든 어노테이션이고 현재 별 의미 없어. :-)

  

아래 예는 모든 선언 위치에 어노테이션(주석)을 넣어봤어 함 봐바~

(뭐 큰 역할을 하는건 아니지만 우리가 항상 사용하는 // 요런 주석으로써의 의미는 있다고 볼수있지 )
```java
**@Entity** public class Vehicle { **@Persistent** protected String vehicleName = null; **@Getter** public String getVehicleName() {
        return this.vehicleName;
    }

    public void setVehicleName(**@Optional** vehicleName) {
        this.vehicleName = vehicleName;
    }

    public List addVehicleNameToList(List names) { **@Optional** List localNames = names;

        if(localNames == null) {
            localNames = new ArrayList();
        }
        localNames.add(getVehicleName());

        return localNames;
    }

} 
```
  

## 자바에서 기본적으로 제공되는 어노테이션

-   @Deprecated
-   @Override
-   @SuppressWarnings

### @Deprecated

이 어노테이션은 , 해당 클래스/메소드 등은 더이상 지원하지 않으니 or 만들고 나니깐 별로 안좋은

부분이 많거나, 더 좋은 해결법이 생겼으니 사용하지 마시라는 의미야. 그럼에도 불구하고 네가 그걸

쓴다면 자바 컴파일러는 귀신같이 알아내서 경고 메세지를 날려줄것이지.

(@Deprecated 주석때문에 컴파일러가 알아차릴수있는거라는 말)
```java
@Deprecated
public class MyComponent {

}
```
### @Override

이 어노테이션은 슈퍼클래스에 대해 오버라이드 되었다는걸 알려줘. 따라서 만약 함수가

슈퍼클래스와 매칭되지 않았으면 에러를 날려주지. (컴파일러 만드는 사람들이 에러를 감지하기

편하겠지?) 아래 예를 봅시다~
```java
public class MySuperClass {

    public void doTheThing() {
        System.out.println("Do the thing");
    }
}


public class MySubClass extends MySuperClass{

    @Override
    public void doTheThing() {
        System.out.println("Do it differently");
    }
}
```
### 물론 이 어노테이션을 사용하는게 강제는 아니지만 , 사용하는게 좋을꺼야. 만약 슈퍼클래스가  
  
변경되었는데 그걸 모르고 자식클래스에서 오버라이딩한 클래스를 그대로 냅두면, 의도가  
  
깨져버리고 우리는 그 사실도 모른채 퇴근을 하겠지~ 만약 @Override 를 선언해뒀다면  
  
바로 에러로 알려주고 네가 수정한후에 편한마음으로 컴백홈하게 도와줄꺼야

### @SuppressWarnings

이 어노테이션은 해당 메소드에 대해서 compiler suppress warnings (컴파일러 경고 억제?)을

만들어. 예를들어 어떤 코드가 경고메세지를 수천개씩 쏟아내는데, 그게 보기싫을때 입막음

시켜버리는거야 조용히~
```java
@SuppressWarnings
public void methodWithWarning() {


}
```
##   

## 개인용 어노테이션 만들기

  

개인적으로 사용할 어노테이션을 만드는것이 가능하며 어노테이션은 클래스나 인터페이스처럼

자신의 파일에 정의된다. 다음 예를 보자.
```java
**@interface** MyAnnotation {

    String       value();
    String       name();
    int            age();
    String[]    newNames();

} 
```
위의 어노테이션은  **4개의 요소**를 가지고있고 이름은 `MyAnnotation` 이다.

`**@interface**  키워드`를 주목하라 이것은 자바컴파일러에게 이놈이 어노테이션 정의라는걸 알려준다.

요소들은 인터페이스에서의 함수 정의와 유사하다. 자바 기본요소들을 모두 사용할수있고 , 배열도 사용가능하다. (복잡객체사용은 불가능)

  

위에서 정의한 어노테이션을 사용해 보자.
```java
@MyAnnotation(
    value="123",
    name="Jakob",
    age=37,
    newNames={"Jenkov", "Peterson"}
)
public class MyClass {


} 
```
위에 보다시피 각각의 요소에 나만의 값을 지정했다. 후에 프레임워크에서 이 값을 파싱해서 필요한 정보를 알아낼것이다. 물론 님 스스로 리플렉션을 통해 저 어노테이션을 분석해서 사용할수도 있을테고~

* 저런 주석을 달아놓으면 나중에 클래스별로 그루핑을 할때 사용하거나 어떤 클래스/함수는 어떤것(URL 따위들) 과 매핑 같은것에 사용할수 있을거라는 생각을 잠시 해보자. 함수이름이 달라져도 어노테이션만 같으면 자동 매핑해줄수있지 않겠는가

  

### 요소(Element)디폴트 값

요소에 기본값을 설정할수 있다. 아래 예를 보자.
```java
@interface MyAnnotation {

    String   value() **default "";**

    String   name();
    int      age();
    String[] newNames();

} 
```
디폴트값을 설정해두면 아래와 같이 사용할때 값을 넣지 않아도 된다. (아예 보이지도 않음)
```java
@MyAnnotation(
    name="Jakob",
    age=37,
    newNames={"Jenkov", "Peterson"}
)
public class MyClass {


}
```
###   
@Retention - 네이버 사전 : (어떤 것을 잃지 않는) 보유[유지])

얼마나 오랫동안 어노테이션 정보가 유지되는지 설정할수있다.

  

SOURCE : 어노테이션 정보가 컴파일시 사라짐, 바이트코드에서는 존재하지 않음.

(example: @Override, @SuppressWarnings)

CLASS : 클래스 파일에 존재하고 컴파일러에 의해 사용가능, 가상머신(런타임)에서는 사라짐.

RUNTIME : 실행시 어노테이션 정보가 가상 머신에 의해서 참조 가능.  **자바리플렉션에 의해 사용**

  

아래 예를 보자.
```java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

@Retention(RetentionPolicy.RUNTIME)

@interface MyAnnotation {

    String   value() default "";

}
```
  

### @Target

자신이 만든 어노테이션이 사용되게될 자바 요소를 지정할수있다. 아래 예를 보자.
```java
import java.lang.annotation.ElementType;
import java.lang.annotation.Target;

@Target({ElementType.METHOD})
public @interface MyAnnotation {

    String   value();
} 
```
위처럼 만들면 메소드에서만 사용가능한 어노테이션을 정의할수있다.아래와 같이 타겟을 정할수있다.

-   ElementType.ANNOTATION_TYPE
-   ElementType.CONSTRUCTOR
-   ElementType.FIELD
-   ElementType.LOCAL_VARIABLE
-   ElementType.METHOD
-   ElementType.PACKAGE
-   ElementType.PARAMETER
-   ElementType.TYPE

### @Inherited

The `@Inherited` 어노테이션은 이 어노테이션을 사용한 슈퍼클래스를 상속한 서브클래스에서도  
해당 어노테이션을 갖도록 한다.
```java
java.lang.annotation.Inherited

@Inherited
public @interface MyAnnotation {

} 

@MyAnnotation
public class MySuperClass { ... } 

public class MySubClass extends MySuperClass { ... } 
```
`MySubClass` 클래스는 `@MyAnnotation 을 상속한다.`

### @Documented

`@Documented` 어노테이션이 지정된 대상의 JavaDoc 에 이 어노테이션의 존재를 표기하도록 지정.
```java
java.lang.annotation.Documented

@Documented
public @interface MyAnnotation {

} 

@MyAnnotation
public class MySuperClass { ... }
```


## **2. 자바 어노테이션 이야기**

##   

## 2-1. 왜 어노테이션인가?

  

어노테이션은 J2SE 5 에 이미 소개되어졌고 , 중요한 탄생 이유는 프로그래머에게 그들의 코드에 대한 메타데이터를 자신의 코드에 직접적으로 기술할수있는것을 제공하기위함이다. 어노테이션이 만들어지기전에 프로그래머가 자신의 코드를 기술하는 방법은 transient 키워드를 사용한다던가, 주석(comments) 를 통하여, 인터페이스를 이용등등 중구난방이었다.그리고 여러타입의 어플리케이션에서 코드를 기술하는 메커니즘은 주로 XML 이 사용되어졌는데 이것은 그리 좋은 방법은 아닌게 코드와 XML (XML 은 코드가 아니다) 사이에 디커플링이 발생되고 이것은 어플리케이션을 유지보수하기 힘들게 한다.

  

자바 스펙에서 어노테이션은 다음에서 나타내 지고 있다 :

-   [JSR 175 A metadata facility for the Java programming Language](https://www.jcp.org/aboutJava/communityprocess/final/jsr175/index.html)
-   [JSR 250 Common Annotations for the Java Platform](https://jcp.org/en/jsr/detail?id=250)

##   

## 2-2. 소개

  

어노테이션을 나타내는(설명해주는) 가장 좋은 단어는 메타데이터이다. (자신의 정보를 담고있는 데이타) .

자바 어노테이션은 코드메타데이타이다.

  

그것은 코드 그 자신에 대한 정보를 담고있다.어노테이션은 패키지,클래스,메소드,변수,파라미터등에서 사용될수있으며 자바 8 부터는 코드의 거의모든 부분에서 사용될수있다. 이것은 타입 어노테이션으로 불려지는데 아래에 살펴보겠다.

  

어노테이션이 적용된 "코드" 는 직접적으로 그들의 "어노테이션" 으로부터 영향받아지지는 않고 단지 서드 시스템에 그것(주석) 에 대한 정보를 제공한다.

  

어노테이션은 런타임에 활용할수있기도하며, 단지 소스레벨에서만 사용가능하게도 만들수있다.

##   

## 2-3. Consumers (소비자)

  

어노테이션의 목적이 정확히 먼지, 어떻게 사용되는지 이해하는건 쉽지 않다, 그것들은 어떠한 기능적 로직을 가지고 있지 않으며 , 코드에 영향을 미치지 않는다. 어노테이션이 뭘 할까?

이것을 위한 설명으로 난 어노테이션 컨슈머스라고 말하는게 있는데 , 이것들은 시스템이나 서드파티 어플리케이션 (스프링같은) 으로서 어노테이션이 적용된 코드를 어노테이션 정보로부터 의존적인 여러가지 행동을 취한다.

예를들어 자바 빌트인 어노테이션경우에는 소비자는 자바가상머신(JVM) 이며 어노테이션이 적용된 코드를 실행한다. 사용자 정의 어노테이션의 경우의 예로는 JUnit, Spring 등이 있다.

그리고 소비자는 코드에서부터 어노테이션을 분석하기위해 자바 리플렉션을 이용한다.

##   

## 2-4. 유즈 케이스

어노테이션은 다양한 목적으로 사용되는데 대표적으로는

-   **컴파일러를 위한 정보제공 :** Java 8 `@FunctionalInterface` , @supresswarnings
-   **자동 문서 작성 :** generate reports automatically like Jenkins, Jira or Teamcity.
-   **코드 자동 생성 :** A good example of this is the JAXB library.
-   **런타임 프로세싱 :** testing (Junit), dependency injection (Spring), logging (Log4J) ,data access (Hibernate) etc.

##   

## 2-5. Java 8 에서 어노테이션

  

Java 8 은 여러가지 훌륭한 기능을 가지고 왔는데 어노테이션 프레임워크도 발전되었다.

다음 예예를 통해 확인해 보도록 하자.

`@Repeatable`:

```java
/**
 * Container for the {@link CanBeRepeated} Annotation containing a list of values
*/
@Retention( RetentionPolicy.RUNTIME )
@Target( ElementType.TYPE_USE )
public @interface RepeatedValues
{
    CanBeRepeated[] value();
}

Afterwards, we create the annotation itself and we mark it with the Meta annotation @Repeatable:

@Retention( RetentionPolicy.RUNTIME )
@Target( ElementType.TYPE_USE )
@Repeatable( RepeatedValues.class )
public @interface CanBeRepeated
{
    String value();
}

Finally we can see how to use it (repeatedly) in a given class:

@CanBeRepeated( "the color is green" )
@CanBeRepeated( "the color is red" )
@CanBeRepeated( "the color is blue" )
public class RepeatableAnnotated
{
}

If we would try to do the same with a non repeatable annotation:

@Retention( RetentionPolicy.RUNTIME )
@Target( ElementType.TYPE_USE )
public @interface CannotBeRepeated
{
    String value();
}

@CannotBeRepeated( "info" )
/*
 * if we try repeat the annotation we will get an error: Duplicate annotation of non-repeatable type
 *
 * @CannotBeRepeated. Only annotation types marked
 *
 * @Repeatable can be used multiple times at one target.
 */

// @CannotBeRepeated( "more info" )
public class RepeatableAnnotatedWrong
{
}

We would get an error from the compiler like:

Duplicate annotation of non-repeatable type
Since Java 8 is also possible to use annotations within types. That is anywhere you can use a type, including the new operator, castings, implements and throws clauses. Type Annotations allow improved analysis of Java code and can ensure even stronger type checking. The following examples clarify this point:

@SuppressWarnings( "unused" )
public static void main( String[] args )
{
    // type def
    @TypeAnnotated
    String cannotBeEmpty = null;

    // type
    List<@TypeAnnotated String> myList = new ArrayList<String>();

    // values
    String myString = new @TypeAnnotated String( "this is annotated in java 8" );
}

// in method params
public void methodAnnotated( @TypeAnnotated int parameter )
{
    System.out.println( "do nothing" );
}


All this was not possible until Java 8.

@FunctionalInterface: this annotation indicates that the element annotated is going to be a functional interface. A functional interface is an interface that has just one abstract method (not a default one). The compiler will handle the annotated element as a functional interface and will produce an error if the element does not comply with the needed requirements. Here is an example of functional interface annotation:
// implementing its methods
@SuppressWarnings( "unused" )
MyCustomInterface myFuncInterface = new MyCustomInterface()
{
    @Override
    public int doSomething( int param )
    {
        return param * 10;
    }
};

// using lambdas
@SuppressWarnings( "unused" )
    MyCustomInterface myFuncInterfaceLambdas = ( x ) -> ( x * 10 );
}

@FunctionalInterface
interface MyCustomInterface
{
/*
 * more abstract methods will cause the interface not to be a valid functional interface and
 * the compiler will thrown an error:Invalid '@FunctionalInterface' annotation;
 * FunctionalInterfaceAnnotation.MyCustomInterface is not a functional interface
 */
    // boolean isFunctionalInterface();
    int doSomething( int param );
}

This annotation can be applied to classes, interfaces, enums and annotations and it is retained by the JVM and available in Run time. Here is its declaration:

@Documented
 @Retention(value=RUNTIME)
 @Target(value=TYPE)
public @interface FunctionalInterface
```
  

##   

## 2-6. Retrieving 어노테이션

  

자바 리플렉션 API 는 여러가지 메소드를 포함한다. 그 메소드들은 런타임에 클래스,메소드등으로부터

어노테이션 정보를 얻을수있게 한다. 그것을 통해서 스프링같은 서드파티 프레임워크는 클래스들을

조작할수있게 된다.

  

저런 모든 메소드들을 포함한 인터페이스는 [AnnotatedElement](http://docs.oracle.com/javase/7/docs/api/java/lang/reflect/AnnotatedElement.html) 이며 대표적으로 다음과 같다.

-   `getAnnotations()`**:** 주어진 엘리먼트가 가지고있는 모든 어노테이션을 배열로 가져온다.
-   `isAnnotationPresent(annotation)`**:** 엘리먼트가 어노테이션을 가지고있는지 체크한다.
-   `getAnnotation(class)`**:** 파라미터로 넘겨진 엘리먼트에 대한 단일 어노테이션을 가져온다.

This class is implementing by `java.lang.Class`, `java.lang.reflect.Method` and `java.lang.reflect.Field` among others, so can be used basically with any kind of Java element.

Now we are going to see an example of how to read the annotations present in a class or method using the methods listed above:

We write a program that tries to read all the annotations present in a class and its methods (we use for this example the classes defined before):

```java
public static void main( String[] args ) throws Exception
{
    Class<AnnotatedClass> object = AnnotatedClass.class;
    // 클래스로부터 모든 어노테이션을 가져온다.
    Annotation[] annotations = object.getAnnotations();
    for( Annotation annotation : annotations )
    {
        System.out.println( annotation );
    }

    // 어노테이션이 존재하는지 체크한다.
    if( object.isAnnotationPresent( CustomAnnotationClass.class ) ) 
    {
        // 원하는 엘리먼트의 어노테이션을 가져온다.
        Annotation annotation = object.getAnnotation( CustomAnnotationClass.class );
        System.out.println( annotation );
    }

    // 클래스내에 있는 모든 메소드들에 대해 어노테이션을 확인한다. 
    for( Method method : object.getDeclaredMethods() )
    {
        if( method.isAnnotationPresent( CustomAnnotationMethod.class ) )
        {
            Annotation annotation = method.getAnnotation( CustomAnnotationMethod.class );
            System.out.println( annotation );
        }
    }
}

The output of this program would be:

@com.danibuiza.javacodegeeks.customannotations.CustomAnnotationClass(getInfo=Info, author=danibuiza, date=2014-05-05)
@com.danibuiza.javacodegeeks.customannotations.CustomAnnotationClass(getInfo=Info, author=danibuiza, date=2014-05-05)
@com.danibuiza.javacodegeeks.customannotations.CustomAnnotationMethod(author=friend of mine, date=2014-06-05, description=annotated method)
@com.danibuiza.javacodegeeks.customannotations.CustomAnnotationMethod(author=danibuiza, date=2014-06-05, description=annotated method)
```

In the program above we can see the usage of the method `getAnnotations()` in order to retrieve all annotations for a given object (a method or a class). We also showed how to check if an specific annotation is present and to retrieve it in positive case using the methods `isAnnotationPresent()` and `getAnnotation()`.


## 3. 자바 리플렉션으로 어노테이션 다루기

  

**자바 리플렉션을 사용함으로서 런타임에 자바클래스에 정의되있는 어노테이션 정보에 접근할수있다.**

##   

## 클래스 어노테이션

  
```java
Class aClass = TheClass.class;
Annotation[] annotations = aClass.getAnnotations();

for(Annotation annotation : annotations){
    if(annotation instanceof MyAnnotation){
        MyAnnotation myAnnotation = (MyAnnotation) annotation;
        System.out.println("name: " + myAnnotation.name());
        System.out.println("value: " + myAnnotation.value());
    }
} 
```
요렇게 접근가능하다:
```java
Class aClass = TheClass.class;
Annotation annotation = aClass.getAnnotation(MyAnnotation.class);

if(annotation instanceof MyAnnotation){
    MyAnnotation myAnnotation = (MyAnnotation) annotation;
    System.out.println("name: " + myAnnotation.name());
    System.out.println("value: " + myAnnotation.value());
}
```
##   

## Method 어노테이션

  
```java
public class TheClass {
  @MyAnnotation(name="someName",  value = "Hello World")
  public void doSomething(){}
} 
```
요렇게 접근가능하다:
```java
Method method = ... //obtain method object
Annotation[] annotations = method.getDeclaredAnnotations();

for(Annotation annotation : annotations){
    if(annotation instanceof MyAnnotation){
        MyAnnotation myAnnotation = (MyAnnotation) annotation;
        System.out.println("name: " + myAnnotation.name());
        System.out.println("value: " + myAnnotation.value());
    }
} 
```
요렇게도 접근가능하다:
```java
Method method = ... // obtain method object
Annotation annotation = method.getAnnotation(MyAnnotation.class);

if(annotation instanceof MyAnnotation){
    MyAnnotation myAnnotation = (MyAnnotation) annotation;
    System.out.println("name: " + myAnnotation.name());
    System.out.println("value: " + myAnnotation.value());
} 
```
##   

## Parameter 어노테이션

  
```java
public class TheClass {
  public static void doSomethingElse(
        @MyAnnotation(name="aName", value="aValue") String parameter){
  }
} 
```
요렇게 접근가능하다:
```java
Method method = ... //obtain method object
Annotation[][] parameterAnnotations = method.getParameterAnnotations();
Class[] parameterTypes = method.getParameterTypes();

int i=0;
for(Annotation[] annotations : parameterAnnotations){
  Class parameterType = parameterTypes[i++];

  for(Annotation annotation : annotations){
    if(annotation instanceof MyAnnotation){
        MyAnnotation myAnnotation = (MyAnnotation) annotation;
        System.out.println("param: " + parameterType.getName());
        System.out.println("name : " + myAnnotation.name());
        System.out.println("value: " + myAnnotation.value());
    }
  }
} 
```
`Method.getParameterAnnotations()` 메소드는 2차원 배열을 리턴한다는걸 주목하라.

그것은 메소드파라미터 각각의 어노테이션 배열을 포함한다.

  

## Field 어노테이션

  
```java
public class TheClass {

  @MyAnnotation(name="someName",  value = "Hello World")
  public String myField = null;
} 
```
요렇게 접근가능하다:
```java
Field field = ... //obtain field object
Annotation[] annotations = field.getDeclaredAnnotations();

for(Annotation annotation : annotations){
    if(annotation instanceof MyAnnotation){
        MyAnnotation myAnnotation = (MyAnnotation) annotation;
        System.out.println("name: " + myAnnotation.name());
        System.out.println("value: " + myAnnotation.value());
    }
} 
```
요렇게도 접근가능하다:
```java
Field field = ... // obtain method object
Annotation annotation = field.getAnnotation(MyAnnotation.class);

if(annotation instanceof MyAnnotation){
    MyAnnotation myAnnotation = (MyAnnotation) annotation;
    System.out.println("name: " + myAnnotation.name());
    System.out.println("value: " + myAnnotation.value());
}
```
  

  

  

----------

  

**Annotation & Reflection 예제**

  

* 메타 annotation type

  
1.@documented : 이 어노테이션을 자바독이나 유사한 도구로 문서화되어져야하는데 사용  
  

하는 엘리먼트를 지칭  
  

2.@Target : 어노테이션 타입이 수용할 수 있는 많은 프로그램 엘리먼트를 지칭  
  

3.@Inherited : 자동으로 상속받는 어노테이션 타입을 지칭  
  

4.@Retention : 어노테이션된 타입이 얼마나 지속되는가를 지칭  
  
  
[메소드에 지정할 어노테이션 정보들을 정의해놓은 인터페이스]  

```java
package com.journaldev.annotations;  
  
import java.lang.annotation.Documented;  
import java.lang.annotation.ElementType;  
import java.lang.annotation.Inherited;  
import java.lang.annotation.Retention;  
import java.lang.annotation.RetentionPolicy;  
import java.lang.annotation.Target;  
  
  
@Documented  
@Target(ElementType.METHOD)  
@Inherited  
@Retention(RetentionPolicy.RUNTIME)  
public @interface MethodInfo {  
 String author() default "Pankaj";  
 String date();  
 int revision() default 1;  
 String comments();  
}  
```
  
[어노테이션을 적용한 메소드들이 정의되어 있는 클래스 예]  

```java
package com.journaldev.annotations;  
  
import java.io.FileNotFoundException;  
import java.util.ArrayList;  
import java.util.List;  
  
public class AnnotationExample {  
 public static void main(String[] arg) {  
 }  
 @Override  
 @MethodInfo(comments = "deprecated method",  
    date = "Nov 17 2012",  
    revision=1)  
 public String toString() {  
  return "Overriden toString method";  
 }  
   
 @Deprecated  
 @MethodInfo(comments = "deprecated method",  
    date = "Nov 17 2012")  
 public static void oldMethod() {  
  System.out.println("old method, don't use it.");  
 }  
   
 @SuppressWarnings({"unchecked", "deprecation"})  
 @MethodInfo(author = "Pankaj",  
    comments = "Main method",  
    date = "Nov 17 2012",  
    revision = 10)  
 public static void genericsTest() throws FileNotFoundException {  
  List list = new ArrayList();  
  list.add("abc");  
  oldMethod();  
 }  
}  
```
  
[Reflection을 사용하여 어노테이션 정보를 분석하는 클래스 :  
  

테스트 클래스로 클래스의 모든 메소드를 로드하고, 그 메소드 중에 어노테이션 인터페이스  
  

에 정의된 어노테이션을 마킹한 각 메소드에 한해서만 이하 작업을 수행.]  
  

1.해당 메소드의 모든 어노테이션을 출력.  
  

2.해당 메소드의 어노테이션 정보를 새 어노테이션 인터페이스 변수에 담고  
  

그 변수에서 어노테이션 값이 사용자가 지정한 값을 가지고 있다면 해당메소드 출력.  

```java
package com.journaldev.annotations;  
  
import java.lang.annotation.Annotation;  
import java.lang.reflect.Method;  
  
public class AnnotationParsing {  
 public static void main(String[] args) {  

  try {  
   for(Method method :    AnnotationParsing.class.getClassLoader()  
                                         .loadClass(("com.journaldev.annotations.AnnotationExample"))  
                                         .getMethods()) {  

     if(method.isAnnotationPresent(com.journaldev.annotations.MethodInfo.class)) {  
      try {  
       //iterates all the annotations available in the method  
       for(Annotation anno : method.getDeclaredAnnotations()) {  
        System.out.println("Annotation in Method" +method+ " : " +anno);  
       }  
       MethodInfo methodAnno = method.getAnnotation(MethodInfo.class);  
       if(methodAnno.revision()==1) {  
        System.out.println("Method with revision no 1 = " +method);  
       }  
         
      } catch (Throwable ex) {  
       ex.printStackTrace();  
      }  
     }  
   }  
  } catch (SecurityException | ClassNotFoundException e) {  
   e.printStackTrace();  
  }  
 }  
}  
```


## 4. 스프링 설정 : 어노테이션 vs XML

  

MyBean.java 가 XML/어노테이션/자바 컨피그레이션을 통해 어떻게 객체로 만들어지는지 살펴보도록하자.

## **( 1 ) XML 을 통한 설정**

**Beans:**

스프링 컨테이너 안에 만들고싶은 자바 클래스들 ("benas") 이다. 두번째 빈은 첫번째 빈을 DI 받고 있다.

**MyBean.java**
```java
package com.hmkcode.spring.beans;
 
public class MyBean {
 
    private String name;
 
    public String getName() {
        return name;
    }
 
    public void setName(String name) {
        this.name = name;
    }
 
    @Override
    public String toString() {
        return "MyBean [name=" + name + "]";
    }
 
}
```
**AnotherBean.java**
```java
package com.hmkcode.spring.beans;
 
public class AnotherBean {
 
    private MyBean myBean;
 
    public MyBean getMyBean() {
        return myBean;
    }
 
    public void setMyBean(MyBean myBean) {
        this.myBean = myBean;
    }
 
    @Override
    public String toString() {
        return "AnotherBean [myBean=" + myBean + "]";
    }   
}
```

**XML 설정 :**

src/main/resources/config/**XMLConfig.xml**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans  xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd">
<bean  id="myBean"  class="com.hmkcode.spring.beans.MyBean">
<property  name="name"  value="xmlBean"  />
</bean>
<bean  id="anotherBean"  class="com.hmkcode.spring.beans.AnotherBean">
<property  name="myBean"  ref="myBean"  />
</bean>
</beans>
```

**위의 설정은 아래와 동등하다.**

```java
MyBean myBean = new MyBean(); 
myBean.setName("xmlBean");

AnotherBean anotherBean = new AnotherBean();
anotherBean.setMyBean(mybean);
```

**Run:**
```java
package com.hmkcode;

import org.springframework.context.ApplicationContext;

import org.springframework.context.support.ClassPathXmlApplicationContext;

import com.hmkcode.spring.beans.AnotherBean;

import com.hmkcode.spring.beans.MyBean;

public class App

{

public static void main( String[] args )

{

ApplicationContext ctxXML = new ClassPathXmlApplicationContext("config/XMLConfig.xml");

AnotherBean anotherBean = (AnotherBean) ctxXML.getBean("anotherBean");

System.out.println( anotherBean);

}

}
```
**Output**:
```java
AnotherBean [myBean=MyBean [name=xmlBean]]
```

## **( 2 ) 어노테이션 기반 설정**

**Beans + Annotation:**
-   **MyBean.java**

-   **@Component**(value=“myBean2″) : this will enable Spring to detect this bean when scanning and instantiate a bean named “**myBean2**“
-   **@Value**(value=“AnnotationBean”) : this equivalent to mybean2.setName(“AnnotationBean”);

```java
package com.hmkcode.spring.beans;

import org.springframework.beans.factory.annotation.Value;

import org.springframework.stereotype.Component;

@Component(value="myBean2")

public class MyBean {

private String name;

public String getName() {

return name;

}

@Value(value="AnnotationBean")

public void setName(String name) {

this.name = name;

}

@Override

public String toString() {

return "MyBean [name=" + name + "]";

}

}
```


-   **AnotherBean.java**

-   **@Component**(value=“anotherBean”) : this will enable Spring to detect this bean when scanning and instantiate a bean named “anotherBean”
-   **@Autowired**  **@Qalifier**(“myBean2″): this equivalent to anotherBean.setMyBean(mybean2)


```java

package com.hmkcode.spring.beans;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.beans.factory.annotation.Qualifier;

import org.springframework.stereotype.Component;

@Component(value="anotherBean")

public class AnotherBean {

private MyBean myBean;

public MyBean getMyBean() {

return myBean;

}

@Autowired

@Qualifier("myBean2")

public void setMyBean(MyBean myBean) {

this.myBean = myBean;

}

@Override

public String toString() {

return "AnotherBean [myBean=" + myBean + "]";

}

}
```

**XML 설정:** _**(annotation 이 사용가능하도록)**_

_단지 어노테이션을 활성화 하기위해 XML 이 필요하다. XML 안에 따로 <bean> 같은 태그를 사용하지 않았다._

-   **XMLConfig-Annotation.xml**

```xml
<?xml version="1.0" encoding="UTF-8"?>

<beans  xmlns="http://www.springframework.org/schema/beans"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

xmlns:context="http://www.springframework.org/schema/context"

xsi:schemaLocation="http://www.springframework.org/schema/beans

http://www.springframework.org/schema/beans/spring-beans.xsd

http://www.springframework.org/schema/context

http://www.springframework.org/schema/context/spring-context.xsd">

<context:component-scan  base-package="com.hmkcode.spring.beans"/>

<!-- The use of <context:component-scan> implicitly enables the functionality of <context:annotation-config> -->

</beans>
```

**Run:**

```java

package com.hmkcode;

import org.springframework.context.ApplicationContext;

import org.springframework.context.support.ClassPathXmlApplicationContext;

import com.hmkcode.spring.beans.AnotherBean;

public class App

{

public static void main( String[] args )

{

ApplicationContext ctxAnnotation = new ClassPathXmlApplicationContext("config/XMLConfig-Annotation.xml");

AnotherBean anotherBean = (AnotherBean) ctxAnnotation.getBean("anotherBean");

System.out.println( anotherBean);

}

}
```

**Output:**

```java

AnotherBean [myBean=MyBean [name=AnnotationBean]]
```

## **( 3 ) 자바를 이용한 설정 (XML 제거됨)**

**Beans:**

-   **MyBean.java**
  
```java

package com.hmkcode.spring.beans;

import org.springframework.beans.factory.annotation.Value;

public class MyBean {

private String name;

public String getName() {

return name;

}

@Value(value="JavaConfigBean")

public void setName(String name) {

this.name = name;

}

@Override

public String toString() {

return "MyBean [name=" + name + "]";

}

}

```

**AnotherBean.java**

```java

package com.hmkcode.spring.beans;

import org.springframework.beans.factory.annotation.Autowired;

public class AnotherBean {

private MyBean myBean;

public MyBean getMyBean() {

return myBean;

}

@Autowired

public void setMyBean(MyBean myBean) {

this.myBean = myBean;

}

@Override

public String toString() {

return "AnotherBean [myBean=" + myBean + "]";

}

}

```

**Cofiguration:**

```java

package com.hmkcode.spring.config;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import com.hmkcode.spring.beans.AnotherBean;
import com.hmkcode.spring.beans.MyBean;

@Configuration

public class JavaConfig {

@Bean

public MyBean myBean(){

return new MyBean();

}

@Bean(name = "anotherBean2")

public AnotherBean anotherBean(){

return new AnotherBean();

}

}

```

**Run:**

```java

package com.hmkcode;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import com.hmkcode.spring.beans.AnotherBean;
import com.hmkcode.spring.config.JavaConfig;

public class App

{

public static void main( String[] args )

{

ApplicationContext ctxJavaConfig = new AnnotationConfigApplicationContext(JavaConfig.class);

AnotherBean anotherBean = (AnotherBean) ctxJavaConfig.getBean("anotherBean2");

System.out.println( anotherBean);

}

}
```

**Output:**

```java

AnotherBean [myBean=MyBean [name=JavaConfigBean]]

```

**AnnotationConfigApplicationContext 분석**

```java

@Configuration  
public class AnnotatedHelloConfig{  
@bean  
public AnnotatedHello annotatedHello(){  
return new AnnotatedHello();

}

}

....

ApplicationContext ctx=new **AnnotationConfigApplicationContext**(AnnotatedHelloConfig.class);

AnnotatedHello  hello =ctx.getBean("annotatedHello", AnnotatedHello .class);

```
위의 코드는 @Configuration 으로 <beans> 를 대신하고  
@bean 으로 자바코드에 의한 빈등록을 하게 해주는 예이다.

AnnotationConfigApplicationContext 을 이용하여 설정 클래스를 입력받은후에  
getBean 메소드를 통하여 내부의 특정 객체를 가져오는 소스이다.

  

**Reference**

**http://tutorials.jenkov.com/java-reflection/annotations.html**

**http://tutorials.jenkov.com/java/annotations.html**

**http://www.javacodegeeks.com/2014/11/java-annotations-tutorial.html**

**http://hmkcode.com/spring-configuration-xml-annotation-java/**
