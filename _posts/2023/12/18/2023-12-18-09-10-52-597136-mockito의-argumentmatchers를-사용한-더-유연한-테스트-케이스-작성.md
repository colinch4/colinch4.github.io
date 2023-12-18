---
layout: post
title: "[java] Mockito의 ArgumentMatchers를 사용한 더 유연한 테스트 케이스 작성"
description: " "
date: 2023-12-18
tags: [java]
comments: true
share: true
---

Mockito는 자바에서 유닛 테스트를 작성할 때 도움이 되는 인기있는 mocking 프레임워크입니다. **ArgumentMatchers**는 Mockito에서 사용되는 강력한 기능 중 하나로, 메서드 호출에 전달되는 매개변수를 유연하게 검증할 수 있는 도구입니다.

## ArgumentMatchers 소개

Mockito의 **ArgumentMatchers**를 사용하면 특정 매개변수 값 또는 매개변수의 일부를 일치시키는 유연한 방법으로 메서드 호출을 검증할 수 있습니다. 이를 통해 테스트 케이스를 더 유연하게 작성할 수 있습니다.

예를 들어, 특정 객체의 메서드 호출이 특정 매개변수로 호출되는지를 확인하는 경우, ArgumentMatchers를 사용하여 일치 조건을 지정할 수 있습니다. 또한, 정확한 값보다는 특정 범위나 유형의 매개변수를 갖는 메서드 호출을 확인할 수도 있습니다.

## ArgumentMatchers 사용 예시

아래는 Mockito의 ArgumentMatchers를 사용하여 유연한 테스트 케이스를 작성하는 예시입니다.

```java
import static org.mockito.ArgumentMatchers.*;

// mock 객체 생성
List<String> mockedList = mock(List.class);

// 매개변수가 "test"인 경우에만 호출을 확인
when(mockedList.contains(argThat(s -> s.equals("test")))).thenReturn(true);

// 호출 확인
assertThat(mockedList.contains("test")).isTrue();
assertThat(mockedList.contains("hello")).isFalse();
```

위 예시에서는 `ArgumentMatchers.argThat()`를 사용하여 람다 표현식을 이용해 "test" 매개변수를 갖는 메서드 호출을 확인합니다.

## 결론

Mockito의 **ArgumentMatchers**는 유연하고 강력한 mocking 도구로, 테스트 작성을 보다 편리하고 효율적으로 만들어줍니다. 이를 통해 테스트 케이스를 작성할 때 불필요한 제약을 줄이고 더 유연한 검증을 수행할 수 있습니다.

---

참고 문헌:
- Mockito 문서: [Mockito 공식 문서](https://javadoc.io/static/org.mockito/mockito-core/3.9.0/org/mockito/Mockito.html)
- Baeldung: [Mockito Argument Matchers](https://www.baeldung.com/mockito-argument-matchers)