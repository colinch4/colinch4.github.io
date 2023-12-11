---
layout: post
title: "[typescript] 열거형(Enum)을 이용한 메소드 오버로딩(Method Overloading)"
description: " "
date: 2023-12-11
tags: [typescript]
comments: true
share: true
---

TypeScript는 JavaScript에 타입을 추가하는 정적 타입 언어로, 메소드 오버로딩과 같은 객체지향 프로그래밍 개념을 지원합니다. 이번 글에서는 TypeScript에서 `enum`을 사용하여 메소드 오버로딩을 구현하는 방법에 대해 살펴보겠습니다.

## Enum(열거형) 개념

`enum`은 연관된 상수 값을 정의할 때 사용되는 TypeScript의 데이터 형식입니다. 일반적으로 `enum`은 관련된 상수들을 논리적으로 그룹화하고 코드의 가독성을 높이는 데 사용됩니다.

예를 들어, 아래와 같이 HTTP 상태 코드를 열거형으로 정의할 수 있습니다:

```typescript
enum HttpStatusCode {
  OK = 200,
  BadRequest = 400,
  NotFound = 404,
  InternalServerError = 500
}
```

## 메소드 오버로딩

메소드 오버로딩은 동일한 이름의 메소드가 다른 매개변수 타입 또는 갯수에 따라 다르게 동작하도록 하는 것을 의미합니다. TypeScript는 이를 지원하여 하나의 함수에 여러 시그니처를 선언할 수 있게 합니다.

아래는 `enum`을 이용하여 HTTP 상태 코드를 다뤄야 하는 메소드를 오버로딩하는 예제입니다:

```typescript
class HttpRequestHandler {
  handleResponse(status: HttpStatusCode.OK): void;
  handleResponse(status: HttpStatusCode.BadRequest | HttpStatusCode.NotFound): void;
  handleResponse(status: HttpStatusCode): void {
    // status에 따른 동작 수행
    console.log("Handling response for status code: " + status);
  }
}
```

위의 코드에서 `HttpRequestHandler` 클래스의 `handleResponse` 메소드는 `HttpStatusCode` 열거형을 이용하여 오버로딩되었습니다. 첫 번째 오버로딩은 `OK` 상태 코드만을 처리하고, 두 번째 오버로딩은 `BadRequest`와 `NotFound` 상태 코드를 처리합니다.

## 결론

TypeScript의 `enum`을 이용한 메소드 오버로딩은 코드의 가독성을 높이고 유지보수를 용이하게 합니다. 이를 통해 다양한 상황에 따라 적절한 동작을 수행하는 메소드를 정의할 수 있습니다.

참고문헌: [TypeScript Handbook - Enums](https://www.typescriptlang.org/docs/handbook/enums.html)

위와 같이 TypeScript에서 `enum`을 활용하여 메소드 오버로딩을 구현할 수 있습니다. 이를 통해 코드의 가독성과 유지보수성을 향상시킬 수 있습니다.