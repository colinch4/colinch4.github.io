---
layout: post
title: "[java] JUnitParams를 활용한 API Mocking 방법은 어떻게 되나요?"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

API Mocking을 위해서는 외부 API 호출을 대신하는 Mock 객체를 생성해야 합니다. JUnitParams를 사용하여 파라미터화된 테스트를 작성하면, Mock 객체를 테스트의 인자로 전달할 수 있습니다.

먼저, JUnitParams를 프로젝트에 추가해야 합니다. Maven을 사용하는 경우, `pom.xml` 파일에 다음 종속성을 추가합니다:

```xml
<dependency>
    <groupId>pl.pragmatists</groupId>
    <artifactId>JUnitParams</artifactId>
    <version>{버전}</version>
    <scope>test</scope>
</dependency>
```

Mockito를 함께 사용하여 Mock 객체를 생성하고 설정할 수 있습니다. Mockito 또한 Maven 종속성에 추가해야 합니다. `pom.xml` 파일에 다음 종속성을 추가합니다:

```xml
<dependency>
    <groupId>org.mockito</groupId>
    <artifactId>mockito-core</artifactId>
    <version>{버전}</version>
    <scope>test</scope>
</dependency>
```

이제 API Mocking을 위한 테스트 클래스를 작성해보겠습니다. 아래는 예시 코드입니다:

```java
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.runners.MockitoJUnitRunner;

import static junitparams.JUnitParamsRunner.$;
import static org.junit.Assert.assertEquals;
import static org.mockito.Mockito.when;

@RunWith(MockitoJUnitRunner.class)
public class APIMockingTest {

    @Mock
    private ExternalAPIClient externalAPIClient;

    @InjectMocks
    private APIService apiService;

    @Test
    @Parameters(method = "getMockedResponseParams")
    public void testApiCall(MockedResponse mockedResponse) {
        // Mock 객체의 동작 설정
        when(externalAPIClient.getData()).thenReturn(mockedResponse.getResponse());

        // 테스트할 API 호출
        String result = apiService.getDataFromExternalAPI();

        // 예상 결과와 실제 결과 비교
        assertEquals(mockedResponse.getExpectedResult(), result);
    }

    private Object[] getMockedResponseParams() {
        return $(
            $(new MockedResponse("Mock API Response", "Mock API Response")),
            $(new MockedResponse("Another Mock Response", "Another Mock Response"))
        );
    }

    private static class MockedResponse {
        private String response;
        private String expectedResult;

        private MockedResponse(String response, String expectedResult) {
            this.response = response;
            this.expectedResult = expectedResult;
        }

        // Getter, Setter 메서드 생략
    }
}
```

위의 코드에서 `ExternalAPIClient`는 외부 API와 상호 작용하는 클라이언트를 나타내며 `APIService`는 API를 호출하는 서비스입니다. `ExternalAPIClient`를 Mock 객체로 설정하여 `apiService`의 동작을 테스트할 수 있습니다.

`@Mock` 애노테이션은 Mock 객체를 생성하고 `@InjectMocks` 애노테이션은 `APIService`에 Mock 객체를 주입합니다. `@RunWith(MockitoJUnitRunner.class)`는 Mockito를 JUnit에 통합하여 Mock 객체를 관리하는 러너를 사용하도록 설정합니다.

`@Parameters` 애노테이션을 사용하여 파라미터화된 테스트를 작성할 수 있습니다. `getMockedResponseParams` 메서드는 MockedResponse 객체의 배열을 반환하는 메서드입니다. 테스트 메서드에 `MockedResponse` 객체를 인자로 전달하여 각각의 테스트 케이스에 대해 다른 Mock 객체를 사용할 수 있습니다.

위의 예제는 API Mocking을 JUnitParams와 Mockito를 활용하여 수행하는 방법을 보여주고 있습니다. 이를 참고하여 프로젝트에서 필요한 Mock 테스트를 작성해보세요. Mockito와 JUnitParams 문서를 참조하면 더 자세한 정보를 얻을 수 있습니다.

참고 문서:
- [JUnitParams](https://github.com/Pragmatists/JUnitParams)
- [Mockito](https://site.mockito.org/)