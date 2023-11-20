---
layout: post
title: "[java] TestNG와 Mock 객체(Mockito, EasyMock 등)를 활용한 유닛 테스트"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

이번 포스트에서는 Java 개발자들에게 널리 사용되는 TestNG 유닛 테스트 프레임워크와 Mock 객체를 활용한 테스트에 대해 알아보겠습니다.

## 1. TestNG 소개

TestNG는 Java 언어를 위한 강력한 테스트 프레임워크로, JUnit과 비슷한 목적으로 만들어졌지만 몇 가지 추가 기능을 제공합니다. TestNG는 테스트를 구성하고 실행하기 위한 다양한 어노테이션과 구성요소를 제공하여 개발자들이 유연하고 강력한 테스트 케이스를 작성할 수 있도록 도와줍니다.

## 2. Mock 객체 소개

Mock 객체는 테스트 시에 실제 객체를 대신하여 사용되는 가짜 객체입니다. 이 가짜 객체를 사용하여 의존하는 객체와의 상호작용을 시뮬레이션하고, 테스트 중에 원하는 동작을 강제할 수 있습니다. Mock 객체를 사용하면 외부 의존성을 없애고 테스트를 보다 격리된 환경에서 실행할 수 있으며, 테스트의 안정성과 신뢰성을 높일 수 있습니다.

## 3. TestNG와 Mock 객체의 사용 예시

### 3.1 Mockito를 사용한 Mock 객체 생성 예시

Mockito는 인기있는 Mock 객체 프레임워크 중 하나로, 간편하게 Mock 객체를 생성하고 사용할 수 있습니다. 아래는 Mockito를 사용하여 Mock 객체를 생성하고 메소드 호출을 검증하는 예시 코드입니다.

```java
import static org.mockito.Mockito.*;

// Mock 객체 생성
List<String> mockList = mock(List.class);

// Mock 객체의 메소드 호출 검증
mockList.add("test");
verify(mockList).add("test");
```

### 3.2 TestNG와 Mockito를 함께 사용하는 예시

아래는 TestNG와 Mockito를 함께 사용하여 유닛 테스트를 작성하는 예시 코드입니다.

```java
import static org.mockito.Mockito.*;
import org.testng.annotations.Test;

public class MyServiceTest {

  @Test
  public void testMyService() {
    // Mock 객체 생성
    SomeDependency mockDependency = mock(SomeDependency.class);

    // Mock 객체의 동작 설정
    when(mockDependency.doSomething()).thenReturn("mock result");

    // 테스트할 서비스 객체 생성
    MyService myService = new MyService(mockDependency);

    // 서비스 객체의 메소드 호출 및 결과 검증
    String result = myService.doSomething();
    assertEquals(result, "mock result");
    verify(mockDependency).doSomething();
  }
}
```

위의 코드에서는 `MyService`라는 클래스를 테스트하고 있습니다. `MyService`는 `SomeDependency`라는 외부 의존성을 가지고 있습니다. 이 의존성을 Mock 객체로 대체하여 원하는 동작을 강제하고, `MyService`의 동작을 테스트할 수 있습니다.

## 4. 마무리

TestNG와 Mock 객체(Mockito, EasyMock 등)를 활용한 유닛 테스트는 Java 개발자들에게 매우 유용한 방법입니다. TestNG의 강력한 기능과 Mock 객체의 격리된 테스트 환경은 안정적이고 신뢰성 있는 테스트를 작성할 수 있게 해줍니다. 개발자들은 이러한 기술을 활용하여 더 효과적으로 소프트웨어를 개발하고 유지보수할 수 있습니다.

### 참고자료
- [TestNG 공식 사이트](https://testng.org/doc/)
- [Mockito 공식 사이트](https://site.mockito.org/)
- [EasyMock 공식 사이트](https://easymock.org/)