---
layout: post
title: "[java] Apache Velocity와 RESTful API 템플릿 처리 방법"
description: " "
date: 2023-12-21
tags: [java]
comments: true
share: true
---

Apache Velocity는 Java 언어로 작성된 오픈소스 템플릿 엔진입니다. 이 템플릿 엔진을 사용하여 RESTful API의 응답을 동적으로 생성하고 전송하는 방법을 알아보겠습니다.

## Apache Velocity란?

Apache Velocity는 Apache Software Foundation에서 개발된 템플릿 엔진으로, 표준 Java 클래스와 함께 사용되어 동적으로 웹 페이지나 다른 텍스트 문서를 생성할 수 있게 해줍니다. API 응답의 템플릿화에 많이 사용되며, JSON, XML, HTML과 같은 형식으로 데이터를 동적으로 채울 수 있습니다.

## Velocity 템플릿 작성

Velocity 템플릿은 텍스트 문서 안에 Velocity 문법을 사용하여 동적으로 데이터를 삽입할 수 있습니다. 아래는 JSON 응답을 생성하는 예시입니다.

```java
{
  "name": "$name",
  "age": $age
}
```

위 코드에서 `$name`과 `$age`는 Velocity 문법을 사용하여 동적으로 삽입될 데이터를 나타냅니다.

## RESTful API에서 Velocity 템플릿 처리

RESTful API에서 Apache Velocity를 사용하여 템플릿을 처리하려면, 먼저 프로젝트에 Velocity 라이브러리를 추가해야 합니다. Maven을 사용하는 경우, `pom.xml` 파일에 다음 의존성을 추가합니다.

```xml
<dependency>
    <groupId>org.apache.velocity</groupId>
    <artifactId>velocity-engine-core</artifactId>
    <version>2.2</version>
</dependency>
```

그런 다음, Velocity를 사용하여 응답을 생성하고 전송할 수 있습니다. 아래는 간단한 RESTful API 엔드포인트에서 Velocity 템플릿을 사용하는 예시입니다.

```java
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.VelocityEngine;

...

VelocityEngine velocityEngine = new VelocityEngine();
velocityEngine.init();

Template template = velocityEngine.getTemplate("response.vm");

VelocityContext context = new VelocityContext();
context.put("name", "John Doe");
context.put("age", 30);

StringWriter writer = new StringWriter();
template.merge(context, writer);

String response = writer.toString();

// 전송 로직 (예: HTTP 응답으로 전송)
```

위 코드에서 `response.vm`은 Velocity 템플릿 파일의 이름이며, 해당 파일에는 JSON 응답 템플릿이 정의되어 있어야 합니다.

이와 같이 Apache Velocity를 사용하여 RESTful API의 응답을 동적으로 생성하고 전송할 수 있습니다.

참고:
- [Apache Velocity 공식 사이트](https://velocity.apache.org/)
- Baillie, J. (2003). "Velocity: A Java-based Template Engine" in *JDJ*. [Online]. Available: https://velocity.apache.org/