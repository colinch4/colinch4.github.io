---
layout: post
title: "[kotlin] Mocking과 Stubbing의 차이점과 코틀린 Mockito에서의 활용"
description: " "
date: 2023-12-20
tags: [kotlin]
comments: true
share: true
---

Mocking과 Stubbing은 테스트 주도 개발(Test-driven development, TDD)에서 중요한 역할을 하는데, 이 두 가지 개념을 이해하고 이를 코틀린 Mockito에서 어떻게 활용하는지 알아보겠습니다.

## Table of Contents
1. [Mocking과 Stubbing](#mocking과-stubbing)
2. [코틀린 Mockito에서의 활용](#코틀린-mockito에서의-활용)
3. [결론](#결론)

## Mocking과 Stubbing

**Mocking**은 테스트에서 외부 의존성을 모의(mock)하는 것을 의미합니다. 즉, 실제 객체를 대체하여 테스트할 수 있도록 동작을 제어하는 것입니다. `Mockito`와 같은 목(Mock) 객체를 사용하여 외부 의존성을 대체하고 모의 객체로써의 행동을 정의할 수 있습니다.

반면 **Stubbing**은 특정 메서드의 반환 값을 고정하는 것으로, 메서드가 호출될 때 항상 동일한 값을 반환하도록 하는 것입니다. 이를 통해 특정 상황에서의 테스트를 보다 쉽게 할 수 있습니다.

## 코틀린 Mockito에서의 활용

코틀린에서는 `Mockito` 라이브러리를 활용하여 Mocking과 Stubbing을 할 수 있습니다. 객체의 메서드가 호출될 때 정해진 값을 반환하도록 하는 것은 Stubbing입니다. 아래의 예시를 통해 코틀린 Mockito에서의 활용법을 알아봅시다.

예를 들어, `UserService` 클래스를 테스트하는 경우:
```kotlin
val userService = mock(UserService::class.java)

`when`(userService.findById(1)).thenReturn(User(id = 1, name = "John"))
`when`(userService.findById(2)).thenReturn(null)

val user1 = userService.findById(1)
val user2 = userService.findById(2)

assertNotNull(user1)
assertNull(user2)
```

위의 예시에서 `userService.findById(1)`이 호출될 때는 `User(id = 1, name = "John")`을 반환하도록 Stubbing을 정의하고, `userService.findById(2)`이 호출될 때는 null을 반환하도록 Stubbing을 정의했습니다.

## 결론

Mocking과 Stubbing은 테스트 주도 개발에서 중요한 요소이며, 코틀린 Mockito를 통해 효과적으로 활용할 수 있습니다. 이를 통해 외부 의존성을 쉽게 모의하고, 원하는 값을 반환하여 테스트할 수 있습니다.

참고 문헌:
- Mockito Kotlin DSL: https://javadoc.io/doc/org.mockito/mockito-core/latest/org/mockito/kotlin/index.html