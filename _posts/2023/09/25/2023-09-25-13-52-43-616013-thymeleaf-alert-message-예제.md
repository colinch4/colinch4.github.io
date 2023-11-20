---
layout: post
title: "thymeleaf alert message 예제"
description: " "
date: 2023-09-25
tags: [java]
comments: true
share: true
---

이번 예제에서는 Thymeleaf를 사용하여 웹 애플리케이션에서 알림 메시지를 표시하는 방법을 살펴보겠습니다.

1. 우선, `pom.xml` 파일에 Thymeleaf 의존성을 추가합니다.

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>
```

2. 컨트롤러 클래스에서 알림 메시지를 처리하는 메소드를 작성합니다.

```java
@Controller
public class MyController {

    @GetMapping("/showMessage")
    public String showMessage(Model model) {
        model.addAttribute("message", "알림 메시지 예제입니다.");
        return "showMessage";
    }
}
```

3. 알림 메시지를 표시할 HTML 템플릿 파일을 작성합니다. 파일 이름은 `showMessage.html`로 하겠습니다.

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>알림 메시지 예제</title>
</head>
<body>
    <div th:if="${message}" class="alert alert-success">
        <strong>알림 메시지:</strong> <span th:text="${message}"></span>
    </div>
</body>
</html>
```

4. 웹 애플리케이션에서 `/showMessage` 경로로 접근하면 알림 메시지가 표시됩니다.

위의 예제에서는 `"알림 메시지 예제입니다."`라는 메시지를 `Model` 객체에 추가하여 Thymeleaf 템플릿에서 사용합니다. 이후, `div` 요소를 통해 해당 메시지를 표시하며, `th:if` 속성을 사용하여 메시지가 존재하는 경우에만 표시합니다.

Thymeleaf를 사용하여 알림 메시지를 표시하는 방법에 대해 간단한 예제를 소개해드렸습니다. 웹 애플리케이션에서 다양한 유형의 알림 메시지를 표시하는 경우, 이 예제를 참고하여 활용하시면 됩니다.

#Thymeleaf #알림메시지