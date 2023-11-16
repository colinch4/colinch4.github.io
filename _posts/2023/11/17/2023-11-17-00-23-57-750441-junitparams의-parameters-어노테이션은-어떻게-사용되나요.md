---
layout: post
title: "[java] JUnitParams의 @Parameters 어노테이션은 어떻게 사용되나요?"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

`@Parameters` 어노테이션을 사용하여 매개변수 세트를 반환하는 메서드를 만들어야 합니다. 이 메서드는 `Iterable<Object[]>` 형식으로 선언되어야 하며, 각 매개변수 세트는 `Object[]` 배열로 표현됩니다. 각 매개변수 세트는 테스트 메서드에 전달될 것입니다.

예를 들어, 다음과 같이 `add` 메서드를 테스트하는 `CalculatorTest`라는 클래스가 있다고 가정해 봅시다.

```java
import junitparams.JUnitParamsRunner;
import junitparams.Parameters;
import org.junit.Test;
import org.junit.runner.RunWith;

@RunWith(JUnitParamsRunner.class)
public class CalculatorTest {

    @Test
    @Parameters
    public void testAdd(int a, int b, int expected) {
        Calculator calculator = new Calculator();
        int result = calculator.add(a, b);
        assertEquals(expected, result);
    }

    private Object[] parametersForTestAdd() {
        return new Object[]{
                new Object[]{2, 3, 5},
                new Object[]{0, 0, 0},
                new Object[]{-1, 1, 0}
        };
    }
}
```

`@Parameters` 어노테이션을 `testAdd` 메서드에서 사용하면 `parametersForTestAdd` 메서드가 매개변수 세트를 반환하는 메서드로 인식됩니다. 테스트 메서드는 해당 메서드에 정의된 매개변수 세트로 반복하여 실행됩니다. 위의 예제에서는 3개의 매개변수 세트를 사용하여 `add` 메서드를 테스트합니다.

JUnitParams의 `@Parameters` 어노테이션을 사용하면 동적으로 매개변수화된 테스트를 작성할 수 있으며, 다양한 테스트 시나리오를 다룰 수 있습니다. 추가적인 설정이나 어노테이션 파라미터를 사용하여 매개변수화된 테스트의 동작을 보다 세부적으로 제어할 수도 있습니다.