---
layout: post
title: "[java] Thymeleaf에서 기본값(default value) 설정의 방법은 무엇인가요?"
description: " "
date: 2023-11-29
tags: [java]
comments: true
share: true
---

Thymeleaf는 자바에서 HTML을 생성하기 위한 템플릿 엔진입니다. 기본값을 설정하는 방법은 다음과 같습니다:

1. 객체 속성을 통한 기본값 설정: 객체의 속성에 기본값을 설정하여 Thymeleaf에서 사용할 수 있습니다. 예를 들어, 다음과 같이 객체를 생성하고 속성에 기본값을 설정합니다.

```
public class User {
    private String name = "기본 사용자";
    // ...
}
```

2. Thymeleaf의 Elvis 연산자를 사용한 기본값 설정: Elvis 연산자인 `?:`를 사용하여 기본값을 설정할 수도 있습니다. Elvis 연산자는 표현식의 결과가 null이 아닌 경우 해당 값을 반환하고, null인 경우에만 오른쪽의 기본값을 반환합니다. 예를 들어, 다음과 같이 사용자 객체의 이름을 출력하는 예제에서 Elvis 연산자를 사용하여 기본값을 설정할 수 있습니다.

```
<span th:text="${user.name} ?: '기본 사용자'"></span>
```

위의 예제에서, `user.name`이 null이 아니라면 해당 값을 출력하고, null인 경우에만 `'기본 사용자'`라는 기본값을 출력합니다.

3. 컨트롤러에서 기본값 설정: 컨트롤러에서 Thymeleaf에서 사용할 변수를 모델에 추가할 때 기본값을 설정할 수도 있습니다. 예를 들어, 다음과 같은 컨트롤러 메서드에서 `user`라는 변수를 모델에 추가할 때 기본값을 설정할 수 있습니다.

```
@GetMapping("/user")
public String getUser(Model model) {
    User user = ...; // 사용자 정보를 가져오는 코드
    model.addAttribute("user", user != null ? user : new User("기본 사용자"));
    return "user";
}
```

위의 예제에서, 컨트롤러는 사용자 정보를 가져오는데 실패한 경우에는 기본값으로 `new User("기본 사용자")`를 설정하여 모델에 추가합니다.

위의 방법 중에서 해당 상황에 맞는 방법을 선택하여 Thymeleaf에서 기본값을 설정할 수 있습니다. Thymeleaf를 사용하면서 페이지에 기본값을 설정하는 것은 매우 유용한 기능 중 하나입니다.