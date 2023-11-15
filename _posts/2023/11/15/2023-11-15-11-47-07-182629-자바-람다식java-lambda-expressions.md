---
layout: post
title: "[java] 자바 람다식(Java lambda expressions)"
description: " "
date: 2023-11-15
tags: [java]
comments: true
share: true
---

자바 8부터 람다식이라고 불리는 새로운 기능이 도입되었습니다. 람다식은 간결하고 효율적인 자바 코드를 작성하는 데 도움을 주는 강력한 도구입니다. 이 글에서는 자바 람다식에 대해 알아보고 실제 사용 예시를 살펴보겠습니다.

## 람다식이란?

람다식은 익명 함수를 간결한 구문으로 표현한 것으로, 메소드를 하나의 식으로 표현하는 방법입니다. 간단하게 말하면 람다식은 메소드를 간략화하여 표현하는 것입니다. 람다식의 기본적인 구조는 다음과 같습니다.

```
(parameter) -> { body }
```

(parameter)는 메소드에서 사용될 매개변수를 나타내며, ->는 매개변수와 메소드 바디를 연결하는 화살표입니다. { body }에는 메소드의 구현 내용이 들어갑니다.

## 람다식의 장점

람다식을 사용하면 다음과 같은 장점을 얻을 수 있습니다.

1. 간결한 코드 작성: 불필요한 부분을 제거하고 직관적인 코드 작성이 가능합니다.
2. 익명 함수: 이름이 없는 함수이기 때문에 재사용이 필요하지 않은 경우에 유용합니다.
3. 코드 가독성 향상: 메소드의 구현을 람다식으로 표현하면 코드의 의도를 명확히 표현할 수 있습니다.

## 람다식의 사용 예시

다음은 자바에서 람다식을 사용하는 간단한 예시입니다.

```java
public class LambdaExample {
    public static void main(String[] args) {
        // 기존 인터페이스를 람다식으로 구현
        MyInterface myInterface = () -> System.out.println("Hello, Lambda!");
        myInterface.sayHello();
        
        // 람다식을 매개변수로 전달
        printMessage(() -> System.out.println("Printing a message from a lambda expression!"));
    }
    
    interface MyInterface {
        void sayHello();
    }
    
    private static void printMessage(Printable printable) {
        printable.print();
    }
    
    interface Printable {
        void print();
    }
}
```

위의 예시에서는 먼저 MyInterface라는 인터페이스를 정의하고, 람다식을 사용하여 이 인터페이스를 구현합니다. 그리고 printMessage 메소드에서 Printable 인터페이스를 매개변수로 받아 람다식을 호출하여 메세지를 출력합니다.

## 결론

이렇듯 자바의 람다식은 간결한 문법으로 메소드를 표현하는 강력한 기능입니다. 람다식을 사용하면 코드의 가독성을 향상시키고, 작업을 간소화하여 생산성을 높일 수 있습니다.

더 많은 정보를 원한다면 다음 자료를 참고하시기 바랍니다:

- Oracle 자바 문서: [람다식 (Java Lambda Expressions)](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html)