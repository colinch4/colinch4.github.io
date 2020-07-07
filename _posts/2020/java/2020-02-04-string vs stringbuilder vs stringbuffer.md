---
layout: post
title: "StringBuffer, StringBuilder, String"
description: "Java의 String, StringBuffer, StringBuilder 에 대해 검색을 해보면 어떤 것이 성능이 좋은지, 장단점은 무엇인지에 대해 정리해놓은 글들을 많이 찾아볼 수 있습니다. 하지만 “왜?”, “어떻게?”를 구체적으로 설명하는 글은 없어서 MyStringBuilder를 직접 구현해보면서 알고리즘적으로 어떻게 다르게 구현되어있는지 정리했습니다."
date: 2020-02-04
tags: [java]
comments: true
share: true
---


> Java의 String, StringBuffer, StringBuilder 에 대해 검색을 해보면 어떤 것이 성능이 좋은지, 장단점은 무엇인지에 대해 정리해놓은 글들을 많이 찾아볼 수 있습니다. 하지만 “왜?”, “어떻게?”를 구체적으로 설명하는 글은 없어서 MyStringBuilder를 직접 구현해보면서 알고리즘적으로 어떻게 다르게 구현되어있는지 정리했습니다.

  

## String, StringBuffer, StringBuilder 특징 및 차이점

우선 Java에서 세 가지 클래스의 특징과 차이가 무엇인지 요약하자면, 세 가지 클래스는 모두 문자열을 처리하기 위한 클래스입니다. 문자열을 더하는 연산을 할 때 성능의 차이가 발생하는데 String 클래스가 StringBuffer, StringBuilder 보다 느리고 메모리 관리 측면에서도 큰 차이를 보입니다. 따라서 문자열의 더하기 연산을 이용할 때는 StringBuffer 혹은 StringBuilder 의 사용을 고려해봐야 합니다.

StringBuffer와 StringBuilder 는 기능이 동일하지만 한 가지 차이점이 존재합니다. 바로 동기화 처리 문제입니다.  
StringBuffer 는 동기화(synchronization)를 지원하여 멀티 스레드 환경에서 안전하게 동작하지만 StringBuilder 는 동기화를 지원하지 않습니다. 따라서 단일 스레드 환경에서는 StringBuilder 를, 멀티 스레드 환경에서는 StringBuilder를 사용하는 것이 권장됩니다. 굳이 두 클래스의 성능을 비교하자면 단일 스레드 환경에서 StringBuilder 가 StringBuffer 보다 빠르게 동작합니다.

  

## 문자열을 추가하는 연산에서 String가 느린 이유

String 클래스가 StringBuffer 혹은 StringBuilder 클래스보다 성능이 떨어지는 이유는 무엇일까요?  
String 클래스의  `immutable`  특성 때문입니다.  `immutable`  이란 변경할 수 없는, 불변의 라는 뜻으로 String 의 value 값은 한 번 생성되면 변경될 수 없습니다.

아래는 Java 8 API 문서의 String Class 설명의 일부분입니다.

> The String class represents character strings. All string literals in Java programs, such as “abc”, are implemented as instances of this class. Strings are constant; their values cannot be changed after they are created. String buffers support mutable strings. Because String objects are immutable they can be shared.

요약해보면, String 클래스는 문자열을 나타냅니다. 자바에서 “abc” 와 같은 모든 리터럴 문자열은 String의 인스턴스로 생성됩니다. 이는 상수이고 이 값은 한 번 생성되면 변경될 수 없습니다. thread safe 하기 때문에 여러 스레들이 공유하여 사용할 수 있습니다.

아래 코드를 살펴봅시다.

```
String a = "aa";
String b = new String("bb");

a = a + b;

```

> 참고로 a와 b의 초기화 방식을 다르게한 이유는 두 코드가 똑같이 동작한다는 것을 보여주기 위함입니다. 앞에서 모든 리터럴 문자열은 String 인스턴스로 생성된다고 했으니  `String a = "aa";`  는  `String a = new String("aa");`  와 같은 동작을 하는 코드가 됩니다.

위의 두 줄의 코드가 실행되면 “aa”, “bb” 문자열에 대해 메모리가 할당되고 a, b 변수가 그 값을 각각 참조하게 됩니다.  
`a = a + b;`  이 실행된 후에는 어떻게 될까요?  
앞서 살펴본 바에 의하면 String 클래스는 immutable 하다. 값이 불변한다고 했습니다. a가 참조하고 있는 공간에 “aa” 대신에 “aabb” 라는 값으로 바꿔주는 것이 아니라 “aabb”에 대해 새로운 String 인스턴스를 생성하여 a가 참조하도록 합니다. 이전에 참조하던 “aa”는 쓰레기가 되고 나중에 가비지 컬렉션에 의해 처리됩니다. 바로 이런 이유 때문에 더 많은 시간과 메모리가 소요되는 것입니다. 연산을 많이 하면 할수록 이런 성능 차이는 더욱 심해집니다.

정말로 그렇게 동작하는지 코드로 살펴봅시다.

```
String a = "aa";
String b = new String("bb");

System.out.printf("a | value: %-4s, address: %s\n", a, a.hashCode());
System.out.printf("b | value: %-4s, address: %s\n", b, b.hashCode());

a = a + b;

System.out.printf("a | value: %-4s, address: %s\n", a, a.hashCode());
System.out.printf("b | value: %-4s, address: %s\n", b, b.hashCode());

```

```
$ java Example
a | value: aa  , address: 3104
b | value: bb  , address: 3136
a | value: aabb, address: 2986080
b | value: bb  , address: 3136

```

실행 결과를 살펴보면 처음에는 a에  `3104`라는 주소가 할당 됐는데 덧셈 연산 이후  `2986080`으로 새로운 메모리 공간이 할당된 것을 확인할 수 있습니다.

  

## StringBuffer, StringBuilder 와 비교한 String 클래스의 장점

StringBuffer와 StringBuilder이 String 보다 성능이 그렇게 좋다면 StringBuffer와 StringBuilder만 사용하지 왜 String를 사용하는지 의문이 듭니다. 당연히 String 만의 장점이 있고 Java에서 세 가지의 클래스를 따로 제공하는 이유가 있을 것입니다.

String 클래스는 immutable 속성을 가짐으로써 안전하다고 했습니다. 값이 변경되지 않기 때문에 여러 스레드가 데이터를 공유하더라도 동기화를 신경쓸 필요가 없이 안정성이 유지되는 장점이 있습니다. 그리고 StringBuffer, StringBuilder 클래스에서도 String 클래스를 이용합니다.  `toString()`  메소드의 경우 StringBuffer, StringBuilder의  `toString()`가 호출되면 해당 문자열에 대한 String 객체를 생성해서 반환합니다. 따라서 연산이 적게 사용되고, 문자열 값의 수정 없이 읽기가 많은 경우에는 String 클래스의 사용이 더 적절합니다.

  

## StringBuffer, StringBuilder가 String 보다 문자열 연산에서 좋은 성능을 보이는 방법

그렇다면 StringBuffer와 StringBuilder는 어떻게 구현되어 있길래 그렇게 많은 성능 차이를 보일까요?  
String 클래스가 덧셈 연산에서 좋지 않은 성능을 보이는 이유는 연산이 수행될 때마다 두 문자열을 모두 읽어 들이고 새로운 메모리에 복사하기 때문이었습니다. StringBuffer, StringBuilder 에서도 마찬가지로 문자열 복사를 하긴 하지만 가변 크기 배열을 이용해서 필요한 경우에만 문자열을 복사합니다.

> 배열의 크기를 무한정으로 지정할 수 없기 때문에 어느 클래스에서든 배열의 크기를 넘어서는 문자열을 합치려고 하면 문자열의 복사는 불가피합니다.

StringBuffer 와 StringBuilder 는 모두 AbstractStringBuilder 라는 추상 클래스를 상속 받아 구현되어있습니다.  
어떻게 구현되어있는지 간략히 알아봅시다.

### 맴버 변수

-   문자열 값을 저장하는 char형 배열  `value`
-   현재 문자열 크기의 값을 가지는 int형의  `count`

### append()

StringBuffer, StringBuilder에서는 + 연산 대신  `append()`  라는 함수를 이용합니다.  
value에 사용되지 않고 남아있는 공간에 새로운 문자열이 들어갈 정도의 크기가 있다면 그대로 삽입합니다. 그렇지 않다면 value 배열의 크기를 두배로 증가시키면서 기존의 문자열을 복사하고 새로운 문자열을 삽입합니다.

### 예시

예를들어 살펴봅시다.

1.  `StringBuilder sb = new StringBuilder();`
    -   StringBuilder 를 생성할 때 capacity를 지정하지 않으면 기본 16으로 설정됩니다.
    -   따라서 value 의 크기는 16, 값은 비어있게 되고,
    -   count는 0으로 초기화 됩니다.
2.  `sb.append("first string");`
    -   “first string” 이라는 문자열의 크기는 12이고 value는 비어있으므로 수용공간 16보다 작으므로 아무런 문자열의 복사 없이 바로 추가됩니다.
    -   value 의 값은 “first string” 이 되고,
    -   count는 12로 갱신됩니다.

4.  `sb.append("+second string");`
    -   “second string” 의 크기는 14. value 에 남아 있는 공간이 4 밖에 되지 않으므로 배열의 크기를 늘려줘야 합니다.
    -   value 의 크기를 두배(32)로 늘리고 기존의 문자열을 복사합니다. 새로운 문자열까지 더해주면 value 값은 “first string+second string”이 됩니다.
    -   count는 26으로 갱신됩니다.

실제로는 위의 설명보다 조금 더 복잡하게 구현되어있지만 핵심적인 부분은 동일합니다.  
이런식으로 StringBuffer와 StringBuilder는 문자열의 더하더라도 매번 문자열을 복사할 필요가 없어서 성능을 높일 수 있습니다.

  

## MyStringBuilder

위에서 설명한 방법을 이용하여 StringBuilder 의 핵심적인 부분만 간단히 구현해봤습니다. 매우 간단한 코드이지만 이것만으로도 String 과 비교했을 때의 성능 차이를 확인해 볼 수 있습니다.

```
import java.util.ArrayList;
import java.util.Arrays;

class MyStringBuilder {
    int count = 0;
    char[] value;

    public MyStringBuilder(String string) {
        value = new char[string.length() + 16];
        string.getChars(0, string.length(), value, 0);
        count = string.length();
    }

    @Override
    public String toString() {
        return new String(value, 0, count);
    }

    public void append(String string) {
        int oldCount = count;
        count = oldCount + string.length();
        if(count > value.length)
            value = Arrays.copyOf(value, value.length * 2);
        string.getChars(0, string.length(), value, oldCount);
    }

    public static void main(String[] args) {
        long startTime = 0;
        long endTime = 0;

        String string = new String("abc");
        StringBuilder stringBuilder = new StringBuilder("abc");
        MyStringBuilder myStringBuilder = new MyStringBuilder("abc");

        startTime = System.nanoTime();
        for (int i=0; i<10000; i++) {
            string += "abc" + i;
        }
        endTime = System.nanoTime();

        System.out.println("String 실행 시간          : " + (endTime - startTime));

        startTime = System.nanoTime();
        for (int i=0; i<10000; i++) {
            stringBuilder.append("abc");
        }
        endTime = System.nanoTime();

        System.out.println("StringBuilder 실행 시간   : " + (endTime - startTime));

        startTime = System.nanoTime();
        for (int i=0; i<10000; i++) {
            myStringBuilder.append("abc");
        }
        endTime = System.nanoTime();

        System.out.println("MyStringBuilder 실행 시간 : " + (endTime - startTime));
    }
}

```

### 실행 결과

```
$ java MyStringBuilder
String 실행 시간          : 744113349
StringBuilder 실행 시간   : 438078
MyStringBuilder 실행 시간 : 976512

```

  

## 참고자료

-   [Java 8 String Class Document](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)
-   [Java 8 StringBuilder Source code](http://grepcode.com/file/repository.grepcode.com/java/root/jdk/openjdk/6-b14/java/lang/StringBuilder.java)
-   [http://xxxelppa.tistory.com/57](http://xxxelppa.tistory.com/57)

