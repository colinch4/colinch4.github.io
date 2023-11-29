---
layout: post
title: "[java] PowerMock의 Mockito Extension 사용 방법"
description: " "
date: 2023-11-29
tags: [java]
comments: true
share: true
---

PowerMock은 Mockito와 함께 사용되는 Java 테스트 도구로, 전통적인 Mockito로는 테스트하기 어려운 코드에 대해서도 모의 객체(Mock Object) 기반의 유연하고 강력한 테스트를 제공합니다. Mockito 스타일의 API를 사용하여 PowerMock을 통합하기 위해 PowerMockito라는 Mockito 확장이 제공됩니다.

이 글에서는 PowerMockito의 주요 기능 중 하나인 Mockito Extension을 사용하는 방법을 알아보겠습니다.

### 1. 의존성 추가

PowerMockito를 사용하기 위해 먼저 의존성을 추가해야 합니다. Maven을 사용하는 경우 pom.xml에 다음과 같은 의존성을 추가합니다:

```xml
<dependency>
    <groupId>org.powermock</groupId>
    <artifactId>powermock-module-junit4</artifactId>
    <version>{PowerMock 버전}</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.powermock</groupId>
    <artifactId>powermock-api-mockito2</artifactId>
    <version>{PowerMock 버전}</version>
    <scope>test</scope>
</dependency>
```

### 2. Mockito에서 PowerMockito로 전환

이제 Mockito에서 PowerMockito로 전환해야 합니다. Mockito의 `@RunWith` 애노테이션을 `PowerMockRunner`로 변경하고, Mockito의 `@PrepareForTest` 애노테이션을 사용하여 각각의 테스트 클래스에서 PowerMockito를 초기화해야 할 클래스를 지정합니다.

```java
@RunWith(PowerMockRunner.class)
@PrepareForTest({ClassToMock.class}) // PowerMockito 초기화 대상 클래스
public class MyTestClass {

    @Test
    public void myTest() {
        // 테스트 코드 작성
    }
}
```

### 3. PowerMockito 사용하기

PowerMockito는 Mockito와 함께 다양한 테스트 시나리오를 처리할 수 있는 강력한 기능을 제공합니다. 다음은 PowerMockito에서 제공하는 몇 가지 주요 기능의 예시입니다.

**3.1. 정적 메소드 모의**

PowerMockito를 사용하여 정적 메소드의 리턴 값을 모의할 수 있습니다.

```java
PowerMockito.mockStatic(ClassWithStaticMethods.class);
PowerMockito.when(ClassWithStaticMethods.staticMethod()).thenReturn(expectedValue);
```

**3.2. Private 메소드 모의**

PowerMockito를 사용하여 private 메소드의 리턴 값을 모의할 수 있습니다.

```java
ClassToMock spy = PowerMockito.spy(new ClassToMock());
PowerMockito.when(spy, "privateMethod").thenReturn(expectedValue);
```

**3.3. 생성자 모의**

PowerMockito를 사용하여 생성자를 모의하고, 생성자에서 리턴하는 객체를 모의할 수 있습니다.

```java
ClassToMock mock = PowerMockito.mock(ClassToMock.class);
PowerMockito.whenNew(ClassToMock.class).withNoArguments().thenReturn(mock);
```

### 마무리

이제 PowerMockito를 사용하여 Mockito 테스트에 더 많은 유연성과 기능을 추가할 수 있게 되었습니다. PowerMockito의 강력한 기능을 활용하여 복잡한 코드와 의존성을 가진 클래스에 대한 테스트를 보다 쉽게 작성할 수 있습니다.

더 자세한 내용은 PowerMockito 공식 문서를 참조하시기 바랍니다.

참조:
- [PowerMock official documentation](https://powermock.github.io/)
- [Mockito official documentation](https://javadoc.io/doc/org.mockito/mockito-core/latest/index.html)