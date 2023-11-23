---
layout: post
title: "[java] Java Play Framework에서의 테스트 더블(mock, stub) 사용 방법은 어떻게 되나요?"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Play Framework는 테스트 더블(mock, stub)을 사용하여 애플리케이션의 유닛 테스트를 작성하는 것을 지원합니다. 테스트 더블은 외부 의존성을 가지는 클래스나 서비스를 가짜로 대체하는 데 사용됩니다. 이를 통해 테스트 시간을 단축하고 테스트 케이스를 더 견고하게 만들 수 있습니다.

테스트 더블을 사용하기 위해서는 다음 단계를 따르면 됩니다.

1. Mockito 또는 EasyMock 같은 모킹 프레임워크를 사용합니다. 이러한 프레임워크는 Java에서 테스트 더블을 작성하는 데 도움이 됩니다. 

2. 의존성 주입(Dependency Injection)을 사용하여 외부 클래스 또는 서비스를 주입할 수 있도록 코드를 설계합니다. Play Framework의 경우, 주로 Guice를 사용하여 의존성 주입을 처리합니다.

3. 테스트 케이스에서 모킹 프레임워크를 사용하여 필요한 의존성을 모킹합니다. 모킹 프레임워크를 사용하여 해당 의존성을 호출하면 모킹한 대상으로 대체되어 값을 반환하거나 기대 동작을 설정할 수 있습니다.

아래는 Java Play Framework의 컨트롤러를 테스트하는 예제 코드입니다. Mockito를 사용하여 UserService 클래스를 모킹하는 방법을 보여줍니다.

```java
import org.junit.Test;
import org.mockito.Mockito;
import play.mvc.Http;
import play.mvc.Result;
import play.test.Helpers;

import static org.junit.Assert.assertEquals;
import static org.mockito.Mockito.when;

public class UserControllerTest {

    @Test
    public void testUserController() {
        // 모킹할 UserService 객체 생성
        UserService userServiceMock = Mockito.mock(UserService.class);

        // UserService의 메소드가 호출되었을 때 반환할 값을 설정
        when(userServiceMock.getUser(1)).thenReturn(new User("John", "Doe"));
        
        // 의존성 주입을 통해 UserService 객체를 주입
        UserController userController = new UserController(userServiceMock);

        // request 객체 생성
        Http.RequestBuilder request = Helpers.fakeRequest()
                .method("GET")
                .uri("/user/1");
        
        // 컨트롤러 테스트
        Result result = Helpers.route(request);
        
        // 반환된 결과 확인
        assertEquals(200, result.status());
        assertEquals("John", result.body().asJson().findPath("first_name").textValue());
        assertEquals("Doe", result.body().asJson().findPath("last_name").textValue());
    }
}
```

위 예제에서는 UserService 클래스를 모킹하여 getUser 메소드를 호출하면 모킹한 객체의 반환값을 받을 수 있게 설정했습니다. 이를 통해 UserController의 테스트 케이스를 작성하고 결과를 확인할 수 있습니다.

자세한 내용은 Mockito 또는 EasyMock의 공식 문서를 참조하시기 바랍니다.

참고 자료:
- [Mockito](https://site.mockito.org/)
- [EasyMock](https://easymock.org/)