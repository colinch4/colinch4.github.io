---
layout: post
title: "[java] Mockito에서 Argument Matcher를 사용하는 방법은?"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

`org.mockito.Matchers` 클래스에는 다양한 Argument Matcher 메소드가 제공됩니다. 예를 들어 `any()`, `eq()`, `isNull()`, `isNotNull()` 등이 있습니다. 이러한 메소드를 사용하여 특정 인자를 검증할 수 있습니다.

아래는 Mockito로 Argument Matcher를 사용하는 간단한 예시입니다.

```java
import static org.mockito.Mockito.*;

// Mock 객체 생성
List<String> mockList = mock(List.class);

// Argument Matcher를 사용하여 메소드 호출 검증
when(mockList.get(anyInt())).thenReturn("Hello"); // 인자로 어떤 정수를 전달해도 "Hello"를 반환하도록 설정

// 검증
assertEquals("Hello", mockList.get(1));
assertEquals("Hello", mockList.get(2));

// 호출 횟수 검증
verify(mockList, times(2)).get(anyInt());
```

위의 예제에서는 `get()` 메소드에 대해 Argument Matcher `anyInt()`를 사용하여 어떤 정수 인자를 전달해도 "Hello"를 반환하도록 설정했습니다. 그리고 `get()` 메소드를 호출한 후 반환값을 검증하고, 호출 횟수를 검증했습니다.

Argument Matcher를 사용할 때는 주의할 점이 있습니다. Argument Matcher를 사용하는 경우 원하는 동작을 정확하게 지정하기 위해 모든 매개변수에 Matcher를 적용해야 합니다. 그렇지 않으면 Mockito에서 예외를 발생시킵니다.

더 많은 정보를 얻고 싶다면 Mockito 공식 문서를 참조하는 것이 좋습니다. Mockito의 Argument Matcher 기능은 테스트 케이스 작성을 훨씬 유연하고 간결하게 만들어줍니다.

**참고 자료:**
- [Mockito 공식 문서](https://javadoc.io/doc/org.mockito/mockito-core/latest/org/mockito/Matchers.html)