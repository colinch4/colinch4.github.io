---
layout: post
title: "[java] Mockito의 ArgumentCaptor 사용 예시"
description: " "
date: 2023-12-18
tags: [java]
comments: true
share: true
---

Mockito는 자바에서 Mock 객체를 만들고 행위를 검증하는 데 사용되는 인기있는 테스트 라이브러리입니다. ArgumentCaptor는 Mockito에서 매개변수를 캡처하고 검증하는 데 사용되는 유용한 도구입니다. 이 포스트에서는 Mockito의 ArgumentCaptor를 사용하여 테스트 더블(Mock 객체)의 메서드 호출 및 매개변수를 검증하는 방법을 살펴보겠습니다.

## ArgumentCaptor란 무엇인가요?

ArgumentCaptor는 Mockito에서 제공하는 기능으로, 메서드 호출 시 전달된 매개변수를 캡처하여 나중에 해당 값들을 검증하는 데 사용됩니다. 즉, ArgumentCaptor를 사용하면 메서드 호출 시 전달된 매개변수를 쉽게 검증할 수 있습니다.

## 사용 예시

다음은 ArgumentCaptor를 사용하여 Mock 객체의 메서드 호출 및 매개변수를 검증하는 간단한 예시입니다.

### 예시 코드

```java
import static org.mockito.Mockito.*;

import org.junit.Test;
import org.mockito.ArgumentCaptor;

public class ExampleTest {
    
    @Test
    public void testSomething() {
        // Mock 객체 생성
        SomeClass mock = mock(SomeClass.class);

        // 테스트 대상 호출 (여기서는 SomeClass의 메서드를 호출하는 가정)
        // 예를 들어 mock.someMethod("argument");
        
        // ArgumentCaptor 생성
        ArgumentCaptor<String> argumentCaptor = ArgumentCaptor.forClass(String.class);
        
        // verify를 통해 메서드 호출 및 매개변수 검증
        verify(mock).someMethod(argumentCaptor.capture());
        
        // 캡처된 매개변수 가져오기
        String capturedArgument = argumentCaptor.getValue();
        
        // 캡처된 매개변수와 기대값 비교
        assertEquals("argument", capturedArgument);
    }
}
```

위의 예시 코드에서는 `mock` 객체를 생성하고 `verify`를 통해 해당 메서드 호출과 매개변수를 검증하고 있습니다. 또한 `ArgumentCaptor`를 사용하여 `capture()` 메서드를 호출하여 전달된 매개변수를 캡처하고, `getValue()`를 통해 캡처된 매개변수를 가져오고 있습니다.

## 결론

이를 통해 Mockito의 ArgumentCaptor를 사용하여 Mock 객체의 메서드 호출 및 매개변수를 간단하게 검증하는 방법을 살펴보았습니다. ArgumentCaptor는 테스트 코드에서 특히 매개변수에 따라 동작이 달라지는 경우 유용하게 활용될 수 있습니다. Mockito 공식 문서와 추가 자료를 참고하여 더 많은 정보를 얻을 수 있습니다.

참고: [Mockito 공식 문서](https://javadoc.io/doc/org.mockito/mockito-core/latest/org/mockito/ArgumentCaptor.html)