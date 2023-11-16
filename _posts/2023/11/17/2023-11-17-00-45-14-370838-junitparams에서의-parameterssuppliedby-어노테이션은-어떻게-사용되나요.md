---
layout: post
title: "[java] JUnitParams에서의 @ParametersSuppliedBy 어노테이션은 어떻게 사용되나요?"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

@ParametersSuppliedBy 어노테이션은 테스트 메서드 위에 작성되며, 매개변수를 제공하는 클래스를 지정하기 위해 사용됩니다. 예를 들어, 다음과 같이 사용할 수 있습니다:

```java
@RunWith(JUnitParamsRunner.class)
public class MyTest {

    @Test
    @ParametersSuppliedBy(MyParametersProvider.class)
    public void myTestMethod(Object param) {
        // Test logic here
    }
}
```

위 코드에서는 MyParametersProvider 클래스로부터 매개변수를 제공받는 myTestMethod 메서드를 정의하고 있습니다. MyParametersProvider 클래스는 JUnitParams에서 제공하는 ParametersProvider 인터페이스를 구현해야 합니다.

```java
public class MyParametersProvider implements ParametersProvider {

    @Override
    public Object[] getParameters() {
        // 매개변수로 사용할 값을 반환하는 로직을 구현
    }
}
```

MyParametersProvider 클래스에서는 getParameters 메서드를 구현하여 매개변수로 사용할 값을 반환해야 합니다.

이렇게 @ParametersSuppliedBy 어노테이션을 사용하여 JUnitParams에서 매개변수 제공자를 지정하면, 해당 제공자에서 반환하는 매개변수를 가지고 테스트 메서드를 실행할 수 있습니다. 이를 통해 테스트 케이스의 다양한 매개변수 조합을 손쉽게 작성할 수 있습니다.

참고 문서:
- [JUnitParams GitHub 페이지](https://github.com/Pragmatists/JUnitParams)
- [JUnitParams 문서](https://pragmatists.github.io/JUnitParams/)
- [JUnitParams 예제](https://www.baeldung.com/junit-params)