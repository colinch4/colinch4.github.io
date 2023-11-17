---
layout: post
title: "[java] Mockito의 Annotation인 @Mock, @InjectMocks, @Spy의 역할은 무엇인가?"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

- `@Mock`: `@Mock` 어노테이션은 목 객체를 생성하는데 사용됩니다. 목 객체는 실제 객체의 동작을 모방하여 테스트 동안 사용됩니다. `@Mock` 어노테이션이 선언된 필드는 `Mockito.mock()` 메소드를 통해 생성된 목 객체로 초기화됩니다. 이를 통해 테스트를 실행할 때 실제 객체 대신 목 객체를 사용할 수 있습니다.

- `@InjectMocks`: `@InjectMocks` 어노테이션은 테스트 대상 객체에 대한 의존성 주입을 담당합니다. 즉, 해당 객체의 필드 중 목 객체와 스파이 객체를 찾아 자동으로 주입해줍니다. `@InjectMocks` 어노테이션이 선언된 객체의 필드 중 `@Mock` 어노테이션이 선언된 필드는 해당 목 객체로 주입됩니다.

- `@Spy`: `@Spy` 어노테이션은 스파이 객체를 생성하는데 사용됩니다. 스파이 객체는 목 객체와 유사하지만, 일부 메소드의 실제 구현을 유지하면서 다른 메소드의 동작을 변경할 수 있습니다. `@Spy` 어노테이션이 선언된 필드는 `Mockito.spy()` 메소드를 통해 생성된 스파이 객체로 초기화됩니다. 따라서, 테스트 중 해당 객체를 사용할 때 실제 동작과 스파이 객체의 동작을 함께 확인할 수 있습니다.

이와 같이 Mockito의 `@Mock`, `@InjectMocks`, `@Spy` 어노테이션들은 테스트 코드에서 목 객체와 스파이 객체를 사용하기 위한 편리한 기능들을 제공합니다. 이를 통해 단위 테스트를 작성하고, 의존성 주입을 편리하게 처리할 수 있습니다.

```java
import org.mockito.Mock;
import org.mockito.InjectMocks;
import org.mockito.Spy;

public class ExampleTest {
    @Mock
    private ExampleService exampleServiceMock;

    @InjectMocks
    private ExampleController exampleController;

    @Spy
    private ExampleRepository exampleRepositorySpy;

    // 테스트 코드 작성
}
```

참고 문서:
- [Mockito 공식 문서](https://javadoc.io/static/org.mockito/mockito-core/3.2.4/org/mockito/Mockito.html)