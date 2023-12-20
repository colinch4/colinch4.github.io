---
layout: post
title: "[kotlin] Mockito의 ArgumentMatchers를 활용한 코틀린 메서드 mocking 방법"
description: " "
date: 2023-12-20
tags: [kotlin]
comments: true
share: true
---

Mockito는 테스트에서 mocking을 쉽게 할 수 있도록 해주는 유용한 라이브러리입니다. Mockito의 ArgumentMatchers를 활용하면 특정 매개변수를 가진 메서드를 mocking할 수 있습니다.

이 블로그 포스트에서는 Kotlin과 Mockito의 ArgumentMatchers를 함께 사용하여 메서드 mocking하는 방법에 대해 알아보겠습니다.

## Mockito 및 ArgumentMatchers 추가

먼저, **build.gradle** 또는 **build.gradle.kts** 파일에 Mockito 및 ArgumentMatchers 의존성을 추가합니다.

```groovy
dependencies {
    testImplementation 'org.mockito:mockito-core:3.11.2'
    testImplementation 'org.mockito:mockito-inline:3.11.2'
}
```

또한 Kotlin에서 Mockito-Kotlin의 의존성도 추가할 수 있습니다.

```groovy
dependencies {
    testImplementation 'com.nhaarman.mockitokotlin2:mockito-kotlin:2.2.0'
}
```

이제 테스트 소스코드에 Mockito를 사용할 준비가 되었습니다.

## ArgumentMatchers를 사용한 메서드 mocking

다음은 Kotlin에서 ArgumentMatchers를 사용하여 메서드를 mocking하는 예제입니다.

```kotlin
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test
import org.mockito.Mockito.`when`
import org.mockito.kotlin.any
import org.mockito.kotlin.mock

interface Calculator {
    fun add(a: Int, b: Int): Int
}

class CalculatorService {
    fun performAddition(calculator: Calculator, a: Int, b: Int): Int {
        return calculator.add(a, b)
    }
}

class CalculatorServiceTest {
    @Test
    fun testPerformAddition() {
        // given
        val calculator = mock<Calculator>()
        val calculatorService = CalculatorService()

        `when`(calculator.add(any(), any())).thenReturn(10)  // ArgumentMatchers.any()

        // when
        val result = calculatorService.performAddition(calculator, 3, 7)

        // then
        assertEquals(10, result)
    }
}
```

이 예제에서는 Calculator 인터페이스와 CalculatorService 클래스를 테스트하는 방법을 보여줍니다. Mockito의 `when` 함수와 ArgumentMatchers의 `any()` 함수를 사용하여 `add` 메서드를 mocking하고, 이를 활용하여 `performAddition` 메서드를 테스트합니다.

## 마무리

이러한 방법을 사용하면 Mockito의 ArgumentMatchers를 활용하여 Kotlin에서 메서드 mocking을 쉽게할 수 있습니다. 테스트 주도 개발 및 유닛 테스트 작성 시에 유용하게 활용할 수 있으니, 필요한 경우 오픈소스 Mockito 및 Mockito-Kotlin의 공식 문서를 참고하시기 바랍니다.

Happy coding! 😊

[Mockito 공식 홈페이지](https://site.mockito.org/)
[Mockito-Kotlin Github 레포지토리](https://github.com/nhaarman/mockito-kotlin)