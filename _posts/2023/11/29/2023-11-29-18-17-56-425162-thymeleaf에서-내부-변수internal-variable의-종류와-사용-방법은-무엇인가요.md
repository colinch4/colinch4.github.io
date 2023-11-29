---
layout: post
title: "[java] Thymeleaf에서 내부 변수(internal variable)의 종류와 사용 방법은 무엇인가요?"
description: " "
date: 2023-11-29
tags: [java]
comments: true
share: true
---

Thymeleaf은 Java 기반의 템플릿 엔진으로, 웹 애플리케이션 개발에서 인기있게 사용되고 있습니다. Thymeleaf의 강력한 기능 중 하나는 내부 변수를 사용하여 템플릿 로직을 더욱 유연하게 만들 수 있다는 것입니다. 이번 글에서는 Thymeleaf에서 사용할 수 있는 내부 변수의 종류와 사용 방법에 대해 알아보겠습니다.

내부 변수는 Thymeleaf 템플릿에서 사용할 수 있는 기본적인 변수들을 의미합니다. 다음은 Thymeleaf에서 사용할 수 있는 내부 변수의 종류입니다:

1. #ctx: 컨텍스트 변수로서, 사용자 정의 프로퍼티와 HTTP 요청 속성에 접근할 수 있습니다. 예를 들어, #ctx.session.userId는 세션에서 사용자 ID를 가져올 수 있습니다.
2. #vars: 현재 폼의 데이터 바인딩 변수에 접근할 수 있는 변수입니다.
3. #root: 뷰 데이타의 최상위 객체에 접근할 수 있는 변수입니다.
4. #request: HTTP 요청 속성에 접근할 수 있는 변수입니다.
5. #response: HTTP 응답 속성에 접근할 수 있는 변수입니다.
6. #locale: 현재 사용자의 로케일에 접근할 수 있는 변수입니다.

내부 변수를 사용하는 방법은 간단합니다. Thymeleaf 템플릿에서는 내부 변수를 사용할 때 "#" 기호를 붙여서 사용합니다. 예를 들어, #ctx.application.name은 컨텍스트 변수인 application의 name 속성에 접근하는 것을 의미합니다.

아래는 내부 변수를 사용하는 Thymeleaf 템플릿의 예시입니다:

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<body>

    <h1 th:text="${#ctx.application.name}">Default title</h1>

    <p th:text="${#root.posts[0].title}">Default post title</p>

</body>
</html>
```

위의 예시에서는 #ctx.application.name을 사용하여 컨텍스트 변수의 name 속성 값을 출력하고, #root.posts[0].title을 사용하여 최상위 객체의 posts 리스트에서 첫 번째 게시물의 title을 출력합니다.

내부 변수를 사용하여 Thymeleaf 템플릿을 유연하게 구성할 수 있으며, 웹 개발에서 많은 도움을 줄 수 있는 강력한 기능입니다.

더 자세한 정보를 원하신다면, Thymeleaf 공식 문서 [링크](https://www.thymeleaf.org/doc/tutorials/2.1/usingthymeleaf.html#standard-expression-syntax)를 참고하시기 바랍니다.