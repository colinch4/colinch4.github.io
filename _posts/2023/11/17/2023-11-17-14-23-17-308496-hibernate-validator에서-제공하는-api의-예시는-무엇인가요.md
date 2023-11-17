---
layout: post
title: "[java] Hibernate Validator에서 제공하는 API의 예시는 무엇인가요?"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

Hibernate Validator는 Java Bean의 유효성 검사를 수행하기 위한 강력한 라이브러리입니다. 다양한 유효성 검사 규칙을 쉽게 정의하고 적용할 수 있어 개발자들에게 많은 편의를 제공합니다. 

다음은 Hibernate Validator에서 가장 많이 사용되는 API의 예시입니다:

1. `@NotNull`: 해당 필드가 Null이 아닌지 검사하는 애노테이션입니다. 예를 들어, 아래의 코드에서 `name` 필드는 Null이 아니어야 합니다.

```java
public class User {
    @NotNull(message = "이름은 Null일 수 없습니다.")
    private String name;
    
    // Getter and Setter
}
```

2. `@Size`: 문자열이나 컬렉션의 크기를 검사하는 애노테이션입니다. `min`과 `max` 속성을 사용하여 유효한 최소 및 최대 길이를 지정할 수 있습니다. 예를 들어, 아래의 코드에서 `name` 필드는 2자 이상 10자 이하여야 합니다.

```java
public class User {
    @Size(min = 2, max = 10, message = "이름은 2자 이상 10자 이하로 입력해야 합니다.")
    private String name;
    
    // Getter and Setter
}
```

3. `@Pattern`: 지정된 정규 표현식과 일치하는지를 확인하는 애노테이션입니다. 예를 들어, 아래의 코드에서 `email` 필드는 이메일 형식에 맞아야 합니다.

```java
public class User {
    @Pattern(regexp = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}", message = "올바른 이메일 형식이 아닙니다.")
    private String email;
    
    // Getter and Setter
}
```

이 외에도 Hibernate Validator는 다양한 유효성 검사 애노테이션을 제공하며, 개발자들은 필요에 따라 이러한 애노테이션을 조합하여 유효성 검사 규칙을 자유롭게 구성할 수 있습니다. 자세한 내용은 [Hibernate Validator 공식 문서](https://docs.jboss.org/hibernate/validator)를 참조하시기 바랍니다.