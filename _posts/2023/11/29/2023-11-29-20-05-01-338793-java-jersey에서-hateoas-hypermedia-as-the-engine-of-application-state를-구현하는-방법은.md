---
layout: post
title: "[java] Java Jersey에서 HATEOAS (Hypermedia as the Engine of Application State)를 구현하는 방법은?"
description: " "
date: 2023-11-29
tags: [java]
comments: true
share: true
---

HATEOAS는 RESTful API 디자인에서 매우 중요한 개념으로, 클라이언트가 서버로부터 받은 응답을 기반으로 현재 상태와 가능한 다음 단계를 이해하고 동적으로 상호작용 할 수 있도록 돕는다.

Java Jersey는 HATEOAS를 구현하기 위한 몇 가지 유용한 라이브러리와 기능을 제공한다. 먼저, `jersey-hateoas` 라이브러리를 사용하여 HATEOAS 기능을 추가할 수 있다.

`jersey-hateoas`  라이브러리를 Maven 또는 Gradle 프로젝트의 종속성으로 추가한다. 

```xml
<dependency>
    <groupId>org.glassfish.jersey.ext</groupId>
    <artifactId>jersey-hateoas</artifactId>
    <version>2.34</version>
</dependency>
```

다음으로, `Link` 클래스를 사용하여 링크를 생성하고 응답에 포함시킬 수 있다. `Link.fromMethod()` 메서드를 사용하면 특정 메서드와 연결된 링크를 생성할 수 있다.

```java
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.Link;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

@Path("/example")
@Produces(MediaType.APPLICATION_JSON)
public class ExampleResource {

    @GET
    public Response getExample() {
        Link link = Link.fromMethod(ExampleResource.class, "anotherMethod")
                .rel("next")
                .build();

        return Response.ok()
                .link(link)
                .entity("Example Response")
                .build();
    }

    @GET
    @Path("/another")
    public Response anotherMethod() {
        // Some logic
        return Response.ok()
                .entity("Another Response")
                .build();
    }
}
```

위의 예제에서는 `/example` 경로로 GET 요청이 들어올 때 `getExample()` 메서드가 호출되며, 이 메서드는 `Link`를 생성하여 응답에 포함시킨다. 생성된 링크는 `rel("next")`를 통해 다음 동작과 연결되었다는 의미를 나타낸다.

또한, `/example/another` 경로로 GET 요청이 들어오면 `anotherMethod()` 메서드가 호출되며, 해당 메서드는 다음 동작을 수행한 후 응답을 반환한다.

응답은 JSON 형식으로 반환되며, 포함된 링크를 통해 클라이언트는 가능한 다음 단계에 대한 정보를 얻을 수 있다.

이제 Java Jersey에서 HATEOAS를 구현하는 방법에 대해 알게 되었다. 이를 활용하여 RESTful API를 보다 동적이고 유연하게 만들 수 있다.

---
**참고자료:**
- [Jersey Hateoas User Guide](https://eclipse-ee4j.github.io/jersey/)
- [Jersey Hateoas GitHub](https://github.com/eclipse-ee4j/jersey)