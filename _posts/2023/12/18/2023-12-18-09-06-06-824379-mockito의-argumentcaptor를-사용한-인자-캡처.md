---
layout: post
title: "[java] Mockito의 ArgumentCaptor를 사용한 인자 캡처"
description: " "
date: 2023-12-18
tags: [java]
comments: true
share: true
---

Mockito는 자바에서 유닛 테스트를 위해 모의 객체(Mock Objects)를 생성하고 사용하는 데 도움을 주는 인기 있는 테스트 라이브러리 중 하나입니다. 여기서는 Mockito의 `ArgumentCaptor`를 사용하여 메소드 호출 시 전달된 인자를 캡처하는 방법에 대해 알아보겠습니다.

## `ArgumentCaptor`란?

`ArgumentCaptor`는 Mockito에서 제공하는 기능으로, 모의 객체를 사용할 때 메소드 호출 시 전달된 매개변수를 캡처하는 데 사용됩니다. 이를 통해 모의 객체에 대한 특정 메소드 호출 시 전달된 인자를 검증하거나 후속 동작에서 활용할 수 있습니다.

## 사용법

다음은 `ArgumentCaptor`를 사용하여 메소드 호출 시 전달된 인자를 캡처하는 간단한 예제입니다.

```java
import static org.mockito.Mockito.*;

// 모의 객체 생성
List<String> mockedList = mock(List.class);

// 모의 객체를 사용한 메소드 호출
mockedList.add("Mockito");

// ArgumentCaptor 생성
ArgumentCaptor<String> argument = ArgumentCaptor.forClass(String.class);
// 메소드 호출 시 전달된 인자를 캡처
verify(mockedList).add(argument.capture());

// 캡처된 값 검증
assertEquals("Mockito", argument.getValue());
```

위 예제에서는 `List` 인터페이스의 `add` 메소드 호출 시 전달된 문자열을 `ArgumentCaptor`를 사용하여 캡처하고, 후속에서 해당 인자를 검증하는 과정을 보여줍니다.

`ArgumentCaptor.forClass()` 메소드를 사용하여 캡처할 인자의 타입을 지정하고, `capture()` 메소드를 통해 실제로 인자를 캡처합니다. 캡처된 값은 `getValue()` 메소드를 통해 가져올 수 있습니다.

## 마무리

`ArgumentCaptor`를 사용하면 모의 객체를 사용한 메소드 호출 시 전달된 인자를 쉽게 캡처하고 검증할 수 있습니다. 이를 통해 유닛 테스트를 작성하고 각 메소드로 전달된 인자에 대한 검증을 보다 효과적으로 할 수 있습니다.

모의 객체와 `ArgumentCaptor`를 적절히 활용하여 코드의 품질을 높이고 유지보수성을 개선하는 데 도움이 될 것입니다. Mockito 공식 문서 및 예제를 참고하여 실제 프로젝트에 적용해 보는 것을 권장합니다.

참고 문헌:
- [Mockito 공식 문서](https://javadoc.io/doc/org.mockito/mockito-core/latest/index.html)
- [Mockito GitHub 저장소](https://github.com/mockito/mockito)