---
layout: post
title: "[java] 자바 애플리케이션에서의 XSS(Cross-Site Scripting) 공격 방어 기술"
description: " "
date: 2023-12-11
tags: [java]
comments: true
share: true
---

웹 애플리케이션은 사용자로부터 입력을 받고 이를 다시 웹 페이지에 표시하는 경우가 많습니다. 하지만 이는 보안 상 위험이 따를 수 있습니다. **XSS(Cross-Site Scripting)**는 악의적인 사용자가 웹 애플리케이션에 스크립트를 삽입하여 공격하는 기법입니다. 

자바 애플리케이션에서 XSS 공격을 방어하기 위한 몇 가지 기술이 있습니다. 이 포스트에서는 그 중 몇 가지를 살펴보겠습니다.

## 1. 입력 값의 검증

사용자로부터 입력을 받을 때, 입력값을 **검증**하여 유효한 형식과 범위 내에 있는지 확인해야 합니다. 입력 값이 스크립트를 포함하고 있는지 확인하여, 적절하지 않은 경우 에러 메시지를 표시하거나 입력을 거부하는 등의 조치를 취할 수 있습니다.

예를 들어, HTML과 JavaScript 태그를 필터링하여 사용자 입력에 포함된 스크립트를 방지할 수 있습니다.

```java
String input = userInput.replaceAll("<", "").replaceAll(">", "");
```

## 2. 출력 값의 이스케이프

웹 애플리케이션에서 사용자 입력값을 출력할 때는 적절한 **이스케이프** 처리를 해야합니다. 이스케이프 처리는 웹페이지에 사용자 입력값이 그대로 출력되는 것을 방지하며, 스크립트가 실행되지 않도록 합니다.

```java
String output = StringEscapeUtils.escapeHtml(input);
```

위 예제에서 `StringEscapeUtils.escapeHtml` 메서드는 Apache Commons Lang 라이브러리에서 제공하는 메서드로, HTML 코드를 이스케이프합니다.

## 3. Content Security Policy (CSP) 적용

**Content Security Policy (CSP)**를 이용하면 웹 페이지의 리소스가 로드될 때 허용되는 소스를 명시하여 XSS 공격을 방어할 수 있습니다. CSP를 설정하면 웹 애플리케이션에서 로드되는 스크립트와 스타일 등의 리소스가 신뢰할 수 있는 출처로부터 로드되도록 제한할 수 있습니다.

```html
<meta http-equiv="Content-Security-Policy" content="script-src 'self'">
```

위 예제에서 `script-src 'self'`는 동일 출처 정책을 적용하여 자체 출처에서만 스크립트를 로드하도록 설정하는 것입니다.

이와 같은 방어 기술을 조합하여 XSS 공격을 최소화할 수 있습니다. 그러나 완벽한 보안은 없으므로 계속해서 보안에 대한 고려가 필요합니다.

## 참고 자료
- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [Content Security Policy (CSP) - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)

위의 기술은 자바 애플리케이션에서 XSS 공격에 대비하기 위한 일부 방법들을 제시한 것입니다. 실제 적용 시 보다 다양한 상황과 요구에 맞게 적용해야 합니다.

내용을 참조하여 작성하였습니다.