---
layout: post
title: "[java] JUnitParams에서의 Parameterized Test는 무엇인가요?"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

파라미터화된 테스트는 같은 테스트 시나리오를 다양한 입력값으로 실행하여 테스트의 유연성과 재사용성을 높히는 방법입니다. 이를 통해 테스트 코드를 간결하게 작성하고, 다양한 테스트 케이스를 한번에 실행해 볼 수 있습니다.

JUnitParams에서의 Parameterized Test 작성 방법은 크게 두 가지입니다. 첫 번째 방법은 `@RunWith` 어노테이션을 통해 `JUnitParamsRunner`를 설정하는 것입니다. 이러한 설정을 통해 클래스에 파라미터화된 테스트 메서드를 작성할 수 있습니다.

두 번째 방법은 `@Parameters`와 `@Test` 어노테이션을 사용하여 파라미터화된 테스트 메서드를 작성하는 것입니다. `@Parameters` 어노테이션은 새로운 데이터 세트를 생성하는 메서드를 가리키며, `@Test` 어노테이션은 파라미터화된 테스트 메서드를 가리킵니다.

아래는 JUnitParams를 사용한 Parameterized Test의 예시 코드입니다:

```java
@RunWith(JUnitParamsRunner.class)
public class MyParameterizedTest {

    @Test
    @Parameters({"2, 3, 5", "4, 6, 10", "10, 0, 10"})
    public void testAdd(int num1, int num2, int expected) {
        int result = Calculator.add(num1, num2);
        assertEquals(expected, result);
    }
}
```
위의 예시 코드에서 `@Parameters` 어노테이션을 사용하여 `testAdd` 메서드에 데이터 세트를 정의하고 있습니다. 이렇게 정의된 데이터 세트는 각각 `num1`, `num2`, `expected`라는 변수에 바인딩되어 테스트가 실행됩니다.

이와 같이 JUnitParams의 Parameterized Test를 사용하면 다양한 입력값을 사용하여 테스트를 실행할 수 있으므로, 테스트 코드를 보다 유연하고 간결하게 작성할 수 있습니다.