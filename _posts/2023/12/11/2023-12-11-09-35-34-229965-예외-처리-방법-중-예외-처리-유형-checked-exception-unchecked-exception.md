---
layout: post
title: "[java] 예외 처리 방법 중 예외 처리 유형 (Checked Exception, Unchecked Exception)"
description: " "
date: 2023-12-11
tags: [java]
comments: true
share: true
---

자바에서 예외 처리는 프로그램의 안정성을 유지하고 예외 상황에 대비하는 데 중요한 역할을 합니다. 자바에서 예외는 크게 *Checked Exception*과 *Unchecked Exception* 두 가지 유형으로 나눌 수 있습니다.

## Checked Exception (확인 예외)

Checked Exception은 **RuntimeException** 클래스를 상속하지 않는 예외로, 컴파일 시에 반드시 예외 처리 코드를 작성해야 합니다. 즉, 예외를 발생시키는 코드를 사용하는 메서드에서 `try-catch`나 `throws`를 사용하여 예외를 처리하도록 강제하는 예외 유형입니다.

예를 들어, **IOException**이나 **ClassNotFoundException**과 같은 입출력 관련 예외들이 Checked Exception에 해당됩니다.

```java
public void readFile(String fileName) throws IOException {
    // 파일 읽기 코드
}
```

## Unchecked Exception (미확인 예외)

Unchecked Exception은 **RuntimeException** 클래스를 상속하는 예외로, 컴파일러가 예외 처리에 대한 확인을 수행하지 않습니다. 따라서 개발자가 직접 예외 처리를 하지 않아도 되며, 선택적으로 예외 처리를 할 수 있습니다.

예를 들어, **NullPointerException**이나 **ArrayIndexOutOfBoundsException**과 같은 런타임 시 발생하는 예외들이 Unchecked Exception에 해당됩니다.

```java
public void divide(int num1, int num2) {
    if (num2 == 0) {
        throw new ArithmeticException("Division by zero!");
    } else {
        int result = num1 / num2;
    }
}
```

## 결론

Checked Exception과 Unchecked Exception은 예외를 다루는 방식과 예외 처리의 필요성에서 차이가 있습니다. 프로그램의 안정성과 예외 상황에 대한 대비를 위해 각 유형에 맞는 적절한 예외 처리 방식을 사용하는 것이 중요합니다.

이상으로 자바에서의 예외 처리 유형에 대한 간략한 설명을 마치도록 하겠습니다.

자료 참고: [Oracle Java Tutorials](https://docs.oracle.com/javase/tutorial/essential/exceptions/)

---