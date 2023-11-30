---
layout: post
title: "[java] Apache Commons Collections의 테스트 및 디버깅 방법"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 Java 언어를 사용하여 컬렉션 프레임워크를 쉽게 구현할 수 있도록 도와주는 유용한 라이브러리입니다. 이 라이브러리를 사용하면 다양한 유형의 데이터 구조를 관리하고 조작할 수 있습니다. 하지만 이 라이브러리를 사용할 때 테스트와 디버깅은 중요한 과정입니다. 이 글에서는 Apache Commons Collections를 테스트하고 디버깅하는 방법에 대해 알아보겠습니다.

## 1. 테스트 작성하기

Apache Commons Collections를 사용한 코드를 테스트하기 위해서는 JUnit과 같은 테스트 프레임워크를 사용하는 것이 좋습니다. 테스트 케이스를 작성하여 각각의 기능을 테스트할 수 있습니다. 테스트 케이스는 예상된 결과와 실제 결과를 비교하고, 예외가 발생하는지 확인하는 등의 검증 작업을 진행합니다.

예를 들어, `ArrayList`와 `LinkedList`를 사용하여 Apache Commons Collections의 `MultiMap`을 테스트하는 경우 다음과 같이 테스트 케이스를 작성할 수 있습니다:

```java
import org.apache.commons.collections4.MultiMap;
import org.apache.commons.collections4.map.MultiValueMap;
import org.junit.Test;

import static org.junit.Assert.*;

public class MultiMapTest {

    @Test
    public void testPutAndGet() {
        MultiMap<String, Integer> multiMap = new MultiValueMap<>();

        multiMap.put("key1", 1);
        multiMap.put("key1", 2);
        multiMap.put("key2", 3);

        assertEquals(2, multiMap.get("key1").size());
        assertEquals(1, multiMap.get("key2").size());
    }

    @Test(expected = UnsupportedOperationException.class)
    public void testUnsupportedOperation() {
        MultiMap<String, Integer> multiMap = new MultiValueMap<>();
        multiMap.put("key1", 1);

        multiMap.get("key1").add(2); // UnsupportedOperationException 발생
    }

}
```

위의 예시에서는 `MultiMap`의 `put` 및 `get` 기능을 테스트하고, 예외가 발생하는 경우에 대한 테스트도 포함되어 있습니다.

## 2. 디버깅하기

Apache Commons Collections를 사용한 코드에서 문제가 발생할 경우 디버깅은 매우 유용한 도구입니다. IDE(통합 개발 환경)를 사용하여 디버깅 모드로 코드를 실행하면, 코드의 흐름을 따라가며 변수의 값을 확인하고 오류를 찾을 수 있습니다.

또한, Apache Commons Collections는 로그를 출력하기 위해 SLF4J와 같은 로깅 프레임워크를 지원합니다. 로그를 적절하게 설정하면 실행 중인 코드의 동작을 추적할 수 있으며, 오류 발생 시 로그를 통해 원인을 파악하는 데 도움이 됩니다.

다음은 SLF4J를 사용하여 로그를 출력하는 예시 코드입니다:

```java
import org.apache.commons.collections4.MultiMap;
import org.apache.commons.collections4.map.MultiValueMap;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ExampleClass {

    private static final Logger LOGGER = LoggerFactory.getLogger(ExampleClass.class);

    public static void main(String[] args) {
        MultiMap<String, Integer> multiMap = new MultiValueMap<>();

        // 로그 출력
        LOGGER.debug("Creating MultiMap");

        multiMap.put("key1", 1);
        multiMap.put("key1", 2);
        multiMap.put("key2", 3);

        LOGGER.debug("MultiMap: {}", multiMap);
    }
}
```

위의 예시 코드에서 `LOGGER.debug()`를 사용하여 원하는 로그를 출력할 수 있습니다. 로그의 레벨을 설정하여 출력할 로그의 수준을 조절할 수도 있습니다.

## 참고 자료

- Apache Commons Collections 공식 문서: [https://commons.apache.org/proper/commons-collections/](https://commons.apache.org/proper/commons-collections/)
- JUnit 공식 문서: [https://junit.org/junit5/](https://junit.org/junit5/)
- SLF4J 공식 문서: [http://www.slf4j.org/](http://www.slf4j.org/)