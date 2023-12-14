---
layout: post
title: "[java] try-finally 문과 try-catch-finally 문의 차이점은 무엇인가요?"
description: " "
date: 2023-12-14
tags: [java]
comments: true
share: true
---

**try-finally** 문은 예외가 발생하든 발생하지 않든 반드시 실행되는 코드 블록을 정의합니다. 이는 예외가 발생하더라도 반드시 자원을 해제하거나 정리해야 하는 경우에 유용합니다.

```java
FileInputStream inputStream = null;
try {
    inputStream = new FileInputStream("file.txt");
    // 파일에서 데이터를 읽는 코드
} finally {
    if (inputStream != null) {
        inputStream.close();  // 자원 해제
    }
}
```

**try-catch-finally** 문은 예외가 발생할 경우 이를 처리하는 catch 블록을 추가로 포함합니다. 예외 처리를 위해 추가적인 로직을 수행해야 하는 경우에 사용됩니다.

```java
try {
    // 예외가 발생할 수 있는 코드
} catch (IOException e) {
    // IOException 예외 처리
} finally {
    // 어떠한 경우에도 실행되어야 하는 코드
}
```

따라서, **try-catch-finally** 문은 예외 처리까지 추가적으로 다룰 수 있고, **try-finally** 문은 단순히 자원을 해제하거나 정리하는 데에 적합합니다.