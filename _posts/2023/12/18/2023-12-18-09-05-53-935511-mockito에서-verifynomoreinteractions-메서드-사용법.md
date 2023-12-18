---
layout: post
title: "[java] Mockito에서 verifyNoMoreInteractions() 메서드 사용법"
description: " "
date: 2023-12-18
tags: [java]
comments: true
share: true
---

Mockito는 자바에서 유닛 테스트를 작성하기 위한 인기있는 목(mock) 프레임워크 중 하나입니다. Mockito를 사용하면 모의 객체(mock objects)를 만들고 조작하여 테스트하는 데 도움이 됩니다.

`verifyNoMoreInteractions()` 메서드는 Mockito에서 사용되는 중요한 메서드 중 하나로, 특정 모의 객체에 대한 상호 작용 검증을 완료한 후 해당 모의 객체와 관련된 추가적인 상호 작용이 발생하지 않았음을 검증합니다.

## 사용법

다음은 `verifyNoMoreInteractions()` 메서드의 기본적인 사용법입니다.

```java
// given
SomeClass mockObject = mock(SomeClass.class);

// when
// ... 모의 객체를 사용하는 동작 수행 ...

// then
verify(mockObject).someMethod(someArgument);
verifyNoMoreInteractions(mockObject);
```

위의 코드에서 `verify(mockObject).someMethod(someArgument)`는 `mockObject`에 대한 `someMethod` 호출을 검증하는 부분이고, `verifyNoMoreInteractions(mockObject)`는 해당 모의 객체에 대해 추가적인 상호 작용이 발생하지 않음을 검증하는 부분입니다.

## 주의사항

`verifyNoMoreInteractions()`를 사용할 때 몇 가지 주의사항이 있습니다.
- `verifyNoMoreInteractions()`를 호출하는 이전에 다른 `verify()` 메서드를 사용하여 상호 작용을 검증해야 합니다.
- 같은 메서드에 대해 여러 번 호출하는 경우 각 호출에 대해 `verify()` 후에 `verifyNoMoreInteractions()`를 사용해야 합니다.

`verifyNoMoreInteractions()`는 모의 객체와 관련된 추가적인 상호 작용을 방지하여 테스트의 일관성과 예측 가능성을 향상시킵니다.

더 많은 정보나 예제 코드는 Mockito 공식 문서를 참고하실 수 있습니다: [Mockito 공식 문서](https://javadoc.io/doc/org.mockito/mockito-core/latest/org/mockito/Mockito.html#2)