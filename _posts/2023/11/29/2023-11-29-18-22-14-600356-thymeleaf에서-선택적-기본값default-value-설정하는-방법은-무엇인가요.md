---
layout: post
title: "[java] Thymeleaf에서 선택적 기본값(default value) 설정하는 방법은 무엇인가요?"
description: " "
date: 2023-11-29
tags: [java]
comments: true
share: true
---

Thymeleaf는 자바 기반의 웹 템플릿 엔진으로서 많은 유용한 기능을 제공합니다. 그 중 하나는 선택적 기본값 설정입니다. 선택적 기본값은 특정 변수의 값이 비어 있거나 null인 경우 사용할 기본값을 지정하는 것을 의미합니다. 

Thymeleaf에서 선택적 기본값을 설정하는 방법은 다음과 같습니다.

1. EL 표현식과 Thymeleaf의 if/else 문을 사용하여 기본값 설정하기:

```html
<p th:text="${(variable != null && variable != '') ? variable : 'Default Value'}"></p>
```

위의 예제에서는 `variable`이 비어 있거나 null이 아닌 경우 `variable`의 값을 출력하고, 그렇지 않은 경우에는 'Default Value'를 출력합니다.

2. Elvis 연산자( ?: )를 사용하여 기본값 설정하기:

```html
<p th:text="${variable ?: 'Default Value'}"></p>
```

위의 예제에서는 `variable`이 값이 존재할 경우 해당 값을 출력하고, 그렇지 않은 경우에는 'Default Value'를 출력합니다. Elvis 연산자는 변수가 null인 경우에만 기본값을 할당하는 간편한 방법입니다.

이러한 방식으로 Thymeleaf에서 선택적 기본값을 설정할 수 있습니다. 선택적 기본값을 지정함으로써 변수의 값이 없을 때 기본값을 사용하는 등의 로직을 처리할 수 있습니다.

더 자세한 내용은 [Thymeleaf 공식 문서](https://www.thymeleaf.org/doc/tutorials/3.0/usingthymeleaf.html#conditional-expressions)를 참고하시기 바랍니다.