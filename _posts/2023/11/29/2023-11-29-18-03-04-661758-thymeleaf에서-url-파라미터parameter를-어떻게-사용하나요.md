---
layout: post
title: "[java] Thymeleaf에서 URL 파라미터(parameter)를 어떻게 사용하나요?"
description: " "
date: 2023-11-29
tags: [java]
comments: true
share: true
---

Thymeleaf를 사용하여 웹 애플리케이션을 개발 중이고, URL 파라미터를 사용해야 할 때가 있을 겁니다. URL 파라미터는 주로 쿼리 스트링(query string) 형태로 전달되며, 매개변수로 사용자의 입력값을 받거나 페이지 간에 데이터를 전달할 때 사용됩니다.

Thymeleaf에서 URL 파라미터를 사용하려면 다음과 같은 방법을 사용할 수 있습니다.

```java
<a th:href="@{/path/to/page(param=${value})}">Link</a>
```

위의 코드에서, `@{}` 형식을 사용하여 링크 URL을 작성합니다. `{}` 안에는 컨트롤러의 경로와 파라미터를 지정할 수 있습니다. 위의 예시에서는 `/path/to/page`를 컨트롤러 경로로 지정하고, `param`이라는 파라미터에 `value` 값을 전달하고 있습니다.

Thymeleaf는 URL을 생성할 때 자동으로 URL 인코딩을 수행하므로, 값에 공백이나 특수 문자가 포함되어 있다면 문제 없이 처리됩니다.

이렇게 작성된 링크를 클릭하면, 해당 페이지로 이동하면서 URL 파라미터가 전달됩니다. 컨트롤러에서는 `@RequestParam` 어노테이션을 사용하여 해당 파라미터를 받아올 수 있습니다.

```java
@GetMapping("/path/to/page")
public String getPage(@RequestParam("param") String value) {
    // 파라미터 값 사용
    return "page";
}
```

위의 예제에서는 `@RequestParam` 어노테이션을 사용하여 `param`이라는 이름의 파라미터를 `value` 매개변수로 받아오고 있습니다. 받아온 파라미터 값을 사용하여 페이지를 처리하고, 해당 페이지를 반환합니다.

Thymeleaf에서 URL 파라미터를 사용하는 방법에 대해 간단하게 소개해드렸는데요. 이를 통해 웹 애플리케이션에서 URL 파라미터를 활용할 수 있고, 사용자의 입력값을 받아오거나 페이지 간에 데이터를 전달할 수 있게 됩니다.

더 자세한 내용은 Thymeleaf 공식 문서(https://www.thymeleaf.org/)를 참고하시면 도움이 될 것입니다.