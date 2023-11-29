---
layout: post
title: "[java] Thymeleaf에서 전역 메시지(global message)를 어떻게 사용하나요?"
description: " "
date: 2023-11-29
tags: [java]
comments: true
share: true
---

전역 메시지를 사용하기 위해서는 다음의 단계를 따릅니다:

1. 프로젝트에 messages.properties 파일을 만듭니다.
2. messages.properties 파일에 전역 메시지를 작성합니다. 예를 들어, 다음과 같이 작성할 수 있습니다:

```properties
welcome.message=환영합니다!
error.email.invalid=유효하지 않은 이메일 주소입니다.
```

3. 템플릿 파일에서 전역 메시지를 사용하려면, namespace를 선언해야 합니다. 다음과 같은 네임스페이스를 추가합니다:

```html
<html xmlns:th="http://www.thymeleaf.org">
...
</html>
```

4. 템플릿 파일에서 전역 메시지를 사용하고 싶은 곳에 다음과 같이 작성합니다:

```html
<p th:text="#{welcome.message}"></p>
```

위의 코드는 messages.properties 파일에서 `welcome.message` 키에 해당하는 값을 출력합니다.

이와 같이 전역 메시지를 사용하면 템플릿 파일 간에 일관성을 유지하고, 변경 사항을 쉽게 관리할 수 있습니다. Thymeleaf에서 전역 메시지 사용 방법을 포함하여 더 많은 내용은 [Thymeleaf 공식 문서](https://www.thymeleaf.org/doc/articles/springmvcaccessdata.html#accessing-merging-contextual-information-localized-messages)를 참조하십시오.