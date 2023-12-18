---
layout: post
title: "[java] Mockito의 Argument Matchers 기능"
description: " "
date: 2023-12-18
tags: [java]
comments: true
share: true
---

Mockito는 Java용 mocking 프레임워크로, 메서드 호출 및 객체 상호작용을 시뮬레이션하기 위해 사용됩니다. Mockito를 사용하면 테스트를 작성할 때 가짜 객체를 만들어 실제 객체를 대체하여 테스트할 수 있습니다. Mockito의 Argument Matchers 기능은 특정 메서드 호출에 전달되는 매개변수를 비교하거나 확인하는 방법을 제공합니다.

## Argument Matchers란?

Argument Matchers는 Mockito에서 메서드 호출에 전달된 매개변수를 검증하는 데 사용되는 기능입니다. 이를 통해 메서드 호출에 대한 매개변수의 형식과 값을 확인할 수 있습니다. Argument Matchers를 사용하여 특정 값이나 형식의 매개변수가 메서드 호출에 전달되는지 확인할 수 있습니다.

## Argument Matchers 사용하기

```java
// 예제: 인자 매처를 사용하여 메서드 호출 검증
List<String> mockedList = mock(List.class);

// anyString()을 사용하여 임의의 문자열이 전달되는지 확인
when(mockedList.get(anyInt())).thenReturn("element");

// 2를 전달하는 것을 확인
verify(mockedList).get(eq(2));
```

위의 예제에서 `anyInt()`와 `eq(2)`는 Argument Matchers의 예시입니다. `anyInt()`는 임의의 정수가 전달되는지 확인하고, `eq(2)`는 2가 전달되는지를 확인합니다.

## Argument Matchers 종류

다양한 종류의 Argument Matchers가 있습니다. 가장 흔하게 사용되는 몇 가지는 다음과 같습니다:
- `anyInt()`: 임의의 정수
- `eq(value)`: 주어진 값과 일치하는 매개변수
- `anyString()`: 임의의 문자열
- `anyObject()`: 임의의 객체
- `isNull()`: null 값
- `notNull()`: null이 아닌 값

## 결론

Mockito의 Argument Matchers를 사용하면 테스트 중에 특정 메서드 호출에 전달되는 매개변수를 검증할 수 있습니다. 이를 통해 효율적이고 신뢰할 수 있는 테스트를 작성할 수 있습니다.

더 많은 정보를 원하시거나 추가적인 기능에 대해 알고 싶다면 Mockito 공식 문서를 참조해보세요.

[Mockito 공식 문서](https://javadoc.io/doc/org.mockito/mockito-core/latest/index.html)