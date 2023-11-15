---
layout: post
title: "[java] 자바 예외 처리(Java exception handling)"
description: " "
date: 2023-11-15
tags: [java]
comments: true
share: true
---

자바 프로그래밍에서 예외 처리는 중요한 개념입니다. 예외 처리는 예측할 수 없는 상황이 발생했을 때 프로그램의 비정상적인 종료를 방지할 수 있습니다. 이번 블로그 포스트에서는 자바에서 예외 처리하는 방법에 대해 알아보겠습니다.

## 예외(Exception)란?

예외는 프로그램이 실행 중에 발생하는 문제 또는 오류입니다. 이러한 예외는 런타임 시 발생할 수 있으며, 프로그램이 예상하지 못한 방식으로 동작할 수 있습니다. 예외는 자바에서 발생한는 다양한 상황을 나타낼 수 있으며, 예를 들면 다음과 같습니다.

- 사용자의 잘못된 입력
- 파일을 찾을 수 없음
- 0으로 나누기 등

자바는 이러한 예외 상황을 처리할 수 있는 예외 처리 메커니즘을 제공합니다.

## 예외 처리 방법

자바에서 예외를 처리하는 방법은 크게 두 가지입니다.

### 1. 예외 던지기(Throwing Exceptions)

예외 던지기는 예외가 발생했을 때, 해당 예외를 호출한 곳에게 전달하는 방식입니다. 예외를 던질 때는 `throw` 키워드를 사용합니다. 예시 코드를 살펴보겠습니다.

```java
public void divide(int num1, int num2) throws ArithmeticException {
    if (num2 == 0) {
        throw new ArithmeticException("0으로 나눌 수 없습니다.");
    }
    int result = num1 / num2;
    System.out.println("결과: " + result);
}
```

위의 코드에서 `divide` 메서드는 `num2`가 0일 경우 `ArithmeticException`을 던집니다. 이렇게 예외를 던진다면 메서드를 호출한 곳에서 예외를 처리해야 합니다.

### 2. 예외 처리하기(Try-Catch Blocks)

예외 처리하기는 예외가 발생했을 때, 예외를 잡아서 처리하는 방식입니다. `try-catch` 블록을 사용하여 예외를 처리합니다. 예시 코드를 살펴보겠습니다.

```java
public void divide(int num1, int num2) {
    try {
        if (num2 == 0) {
            throw new ArithmeticException("0으로 나눌 수 없습니다.");
        }
        int result = num1 / num2;
        System.out.println("결과: " + result);
    } catch (ArithmeticException e) {
        System.out.println("예외 발생: " + e.getMessage());
    }
}
```

위의 코드에서 `try` 블록 안에서 예외가 발생할 가능성이 있는 코드를 작성하고, `catch` 블록에서 예외를 처리하는 코드를 작성합니다. 예외가 발생하면 해당 블록이 실행되고, 예외를 처리할 수 있는 로직이 호출됩니다.

## 예외 처리의 이점

예외 처리는 프로그램의 안정성과 신뢰성을 향상시키는 중요한 요소입니다. 예외 처리를 통해 프로그램이 예상치 못한 상황에서도 적절한 대응을 할 수 있습니다. 이를 통해 프로그램에 발생하는 오류를 예측하고 처리할 수 있습니다.

## 마무리

자바에서 예외 처리는 프로그램의 신뢰성을 높이기 위해 반드시 사용해야 하는 중요한 요소입니다. 이번 포스트에서는 예외 처리의 개념과 예외를 처리하는 방법에 대해 알아보았습니다. 예외 처리를 통해 안정적이고 오류가 적은 프로그램을 작성할 수 있습니다.

더 많은 자세한 정보는 자바 공식 문서를 참고해 주세요.

- [Java Exception Handling](https://docs.oracle.com/javase/tutorial/essential/exceptions/index.html)

감사합니다!