---
layout: post
title: "[java] Apache Commons Lang 을 사용하여 객체가 null 인지 체크하는 방법"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

Java 프로젝트에서 객체가 null인지 체크하는 것은 매우 중요합니다. Null 포인터 예외를 방지하기 위해 객체의 유효성을 확인하는 것은 안전성을 높이고 코드의 신뢰성을 향상시킵니다. Apache Commons Lang 라이브러리는 객체의 null 체크를 쉽게 수행할 수 있는 유용한 기능을 제공합니다.

## Apache Commons Lang이란?

Apache Commons Lang은 Apache 재단에서 제공하는 유틸리티 라이브러리로, Java 개발자가 자주 사용하는 다양한 작업을 보조해주는 클래스와 메서드를 제공합니다. Null 체크 뿐만 아니라 문자열 처리, 날짜 및 시간 처리, 배열 조작 등 다양한 기능을 제공합니다.

## Apache Commons Lang을 사용하여 객체가 null인지 체크하는 방법

Apache Commons Lang의 `ObjectUtils` 클래스의 `isNull` 메서드를 사용하여 객체가 null인지 체크할 수 있습니다. 아래 예제 코드를 참고하세요.

```java
import org.apache.commons.lang3.ObjectUtils;

public class NullCheckExample {
    public static void main(String[] args) {
        String text = null;

        if (ObjectUtils.isNull(text)) {
            System.out.println("객체는 null입니다.");
        } else {
            System.out.println("객체는 null이 아닙니다.");
        }
    }
}
```

위의 예제에서는 `ObjectUtils.isNull` 메서드를 사용하여 `text` 객체가 null인지 체크합니다. `text` 객체가 null이면 "객체는 null입니다."라는 메시지를 출력하고, null이 아닌 경우 "객체는 null이 아닙니다."라는 메시지를 출력합니다.

## 결론

Apache Commons Lang의 `ObjectUtils` 클래스를 사용하면 객체가 null인지 쉽게 체크할 수 있습니다. 이를 통해 안전한 프로그래밍을 할 수 있고, NullPointerException을 방지할 수 있습니다. Apache Commons Lang 라이브러리의 다른 유용한 기능도 함께 활용하면 프로젝트의 효율성을 향상시킬 수 있습니다.

참고 링크:
- Apache Commons Lang: [https://commons.apache.org/proper/commons-lang/](https://commons.apache.org/proper/commons-lang/)