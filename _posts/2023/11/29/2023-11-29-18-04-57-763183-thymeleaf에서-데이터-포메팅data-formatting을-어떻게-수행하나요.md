---
layout: post
title: "[java] Thymeleaf에서 데이터 포메팅(data formatting)을 어떻게 수행하나요?"
description: " "
date: 2023-11-29
tags: [java]
comments: true
share: true
---

Thymeleaf에서는 데이터를 사용자 친화적인 형식으로 표현하기 위해 데이터 포맷팅 기능을 제공합니다. 데이터 포맷팅을 사용하면 날짜, 시간, 숫자 등의 데이터를 원하는 형식으로 변환할 수 있습니다.

Thymeleaf에서 데이터 포맷팅을 수행하는 방법은 다음과 같습니다:

1. 날짜 포맷팅

```
<span th:text="${#dates.format(dateValue, 'yyyy-MM-dd')}"></span>
```

위의 예제에서는 `dateValue`라는 변수를 `yyyy-MM-dd` 형식으로 포맷팅하여 출력합니다. #dates.format 메소드를 사용하여 원하는 날짜 포맷을 지정할 수 있습니다.

2. 숫자 포맷팅

```
<span th:text="${#numbers.formatInteger(numberValue, '#,###')}"></span>
```

위의 예제에서는 `numberValue`라는 변수를 `#,###` 형식으로 포맷팅하여 출력합니다. #numbers.formatInteger 메소드를 사용하여 숫자 포맷을 지정할 수 있습니다.
   

3. 메시지 포맷팅

```
<span th:text="#{message.key}"></span>
```

위의 예제에서는 `message.key`라는 메시지 키를 사용하여 메시지를 포맷팅하여 출력합니다. 이때 메시지 키는 properties 파일에 정의되어 있어야 합니다.

Thymeleaf의 데이터 포맷팅 기능을 사용하여 데이터를 원하는 형식으로 변환하여 출력할 수 있습니다. 세부적인 포맷팅 기능에 대한 자세한 내용은 Thymeleaf 공식 문서를 참조하시기 바랍니다.

참조: [Thymeleaf 공식 문서](https://www.thymeleaf.org/doc/tutorials/3.0/usingthymeleaf.html#expression-basics-formatting-output)