---
layout: post
title: "[java] JUnitParams를 활용한 TDD(Test-driven development) 방법은 어떻게 되나요?"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

JUnitParams를 활용한 TDD 방법을 설명하기 위해 간단한 예제를 사용해보겠습니다. 아래는 `Calculator` 클래스의 `add()` 메서드를 TDD 방식으로 개발하는 과정입니다.

1. 먼저, `Calculator` 클래스를 작성합니다.

```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
}
```

2. 이제 `CalculatorTest` 클래스를 작성하여 `add()` 메서드를 테스트합니다.

```java
import junitparams.JUnitParamsRunner;
import junitparams.Parameters;
import org.junit.Test;
import org.junit.runner.RunWith;

import static org.junit.Assert.assertEquals;

@RunWith(JUnitParamsRunner.class)
public class CalculatorTest {
    private Calculator calculator = new Calculator();

    @Test
    @Parameters({
            "0, 0, 0",
            "1, 2, 3",
            "-1, -1, -2",
            "10, -5, 5"
    })
    public void testAdd(int a, int b, int expected) {
        assertEquals(expected, calculator.add(a, b));
    }
}
```

3. `@RunWith(JUnitParamsRunner.class)` 어노테이션을 사용하여 JUnitParamsRunner를 실행합니다.

4. `@Parameters` 어노테이션을 사용하여 테스트에 사용될 매개변수를 정의합니다. 각 매개변수는 콤마(,)로 구분되며, 첫 번째 매개변수는 `a`, 두 번째 매개변수는 `b`, 세 번째 매개변수는 `expected`로 사용됩니다.

5. `testAdd()` 메서드에서 `assertEquals()`를 사용하여 예상 결과값과 실제 결과값을 비교합니다.

이렇게 JUnitParams를 활용하여 TDD 방법을 적용할 수 있습니다. 이를 통해 다양한 조건에 대한 테스트를 간편하게 작성하고, 코드의 변경에 따른 영향을 빠르게 확인할 수 있습니다.

참고 자료:
- [JUnitParams GitHub 레포지토리](https://github.com/Pragmatists/JUnitParams)
- [JUnitParams 홈페이지](http://www.junitparams.com/)