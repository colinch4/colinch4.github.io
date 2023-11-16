---
layout: post
title: "[java] JUnitParams와 Apache Commons를 함께 사용하는 방법은 어떻게 되나요?"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

JUnitParams는 JUnit에서 매개변수화된 테스트를 작성할 수 있도록 도와주는 라이브러리입니다. Apache Commons는 자주 사용되는 유틸리티 기능을 제공하는 라이브러리입니다. 이 두 라이브러리를 함께 사용하면 유연하고 강력한 테스트 케이스를 작성할 수 있습니다.

먼저, Maven 또는 Gradle을 사용하여 JUnitParams와 Apache Commons를 프로젝트에 추가해야 합니다. 이를 위해 프로젝트의 의존성 파일에 다음과 같은 항목을 추가해주세요.

Maven:
```xml
<dependency>
    <groupId>pl.pragmatists</groupId>
    <artifactId>JUnitParams</artifactId>
    <version>1.1.1</version>
    <scope>test</scope>
</dependency>

<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.12.0</version>
</dependency>
```

Gradle:
```groovy
testImplementation 'pl.pragmatists:JUnitParams:1.1.1'
implementation 'org.apache.commons:commons-lang3:3.12.0'
```

의존성을 추가한 후, JUnitParams를 사용하여 매개변수화된 테스트 케이스를 작성할 수 있습니다. 아래는 예제 코드입니다.

```java
import static org.junit.Assert.assertEquals;
import junitparams.JUnitParamsRunner;
import junitparams.Parameters;
import org.apache.commons.lang3.StringUtils;
import org.junit.Test;
import org.junit.runner.RunWith;

@RunWith(JUnitParamsRunner.class)
public class StringUtilsTest {
    
    @Test
    @Parameters({
        "hello, 5",
        "world, 5",
        "JUnitParams, 12"
    })
    public void testStringLength(String input, int expectedLength) {
        int actualLength = StringUtils.length(input);
        assertEquals(expectedLength, actualLength);
    }
    
}
```

위의 예제는 JUnitParams의 `@Parameters` 어노테이션을 사용하여 입력과 예상 결과를 제공합니다. Apache Commons의 `StringUtils.length` 메서드를 테스트하며, 입력 문자열의 길이를 예상결과와 비교하여 테스트합니다.

JUnitParams와 Apache Commons를 함께 사용하면 다양한 입력 값을 테스트하는 데 더욱 유연성을 가질 수 있습니다. 필요한 경우 추가적인 테스트 케이스를 `@Parameters` 어노테이션을 사용하여 작성하고, Apache Commons의 다른 유틸리티 메서드를 테스트에 활용할 수 있습니다.

더 자세한 내용은 JUnitParams와 Apache Commons의 공식 문서를 참조하시기 바랍니다.

- JUnitParams: https://github.com/Pragmatists/JUnitParams
- Apache Commons: https://commons.apache.org/