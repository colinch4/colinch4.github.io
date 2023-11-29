---
layout: post
title: "[java] Thymeleaf에서 서버 사이드 유효성 검사(server-side validation)를 어떻게 수행하나요?"
description: " "
date: 2023-11-29
tags: [java]
comments: true
share: true
---

1. 유효성 검사를 수행할 객체를 만듭니다. 이 객체는 유효성을 검사할 필드를 가지고 있어야 합니다. 예를 들어, 회원 가입 폼을 작성하는 경우, 이름, 이메일, 비밀번호 등의 필드가 있을 수 있습니다.

2. 컨트롤러에서 폼을 제출하고 유효성 검사를 수행하는 메서드를 작성합니다. 이 메서드는 @PostMapping 어노테이션으로 지정된 경로와 연결되어야 합니다.

```
@PostMapping("/register")
public String registerUser(@Validated MyForm form, BindingResult result) {
    if (result.hasErrors()) {
        // 유효성 검사 실패 시, 오류 처리 로직을 작성합니다.
        return "register";
    }
    // 유효성 검사 통과 시, 회원 가입 로직을 실행합니다.
    return "redirect:/";
}
```

3. 폼 객체에 @Validated 어노테이션을 추가하여 유효성 검사를 활성화합니다.

```
public class MyForm {
    @NotBlank
    private String name;
  
    @Email
    private String email;
  
    // Getter와 Setter 생략
}
```

4. Thymeleaf 템플릿에서 유효성 검사 결과를 표시할 수 있습니다. 예를 들어, 다음과 같이 필드 오류 메시지를 표시할 수 있습니다.

```html
<form th:object="${form}" th:action="@{/register}" method="post">
    <div>
        <label for="name">이름:</label>
        <input type="text" id="name" th:field="*{name}" required>
        <div th:if="${#fields.hasErrors('name')}" th:errors="*{name}"></div>
    </div>
    <!-- 다른 필드들도 유사한 방법으로 표시합니다. -->
    <button type="submit">가입하기</button>
</form>
```

이렇게 하면 Thymeleaf에서 서버 사이드 유효성 검사를 수행할 수 있습니다.

참고 자료:
- Thymeleaf 공식 문서(https://www.thymeleaf.org/doc/tutorials/3.0/thymeleafspring.html#validation-and-error-handling)
- Spring Framework 공식 문서(https://docs.spring.io/spring-framework/docs/current/spring-framework-reference/web.html#mvc-ann-validation)