---
layout: post
title: "[typescript] 타입 가드를 사용한 DTO(Data Transfer Object) 검사"
description: " "
date: 2023-12-08
tags: [typescript]
comments: true
share: true
---

## 개요
프로그래밍에서 데이터 전송 객체(DTO)는 데이터를 서로 다른 시스템 간에 전송하기 위한 객체입니다. 이러한 DTO를 사용할 때, 해당 객체의 유효성을 검사하는 것이 중요합니다. 타입스크립트에서는 타입 가드를 사용하여 DTO의 유효성을 검사할 수 있습니다. 이 블로그 포스트에서는 타입 가드를 활용하여 타입스크립트에서 DTO의 유효성을 검사하는 방법에 대해 알아보겠습니다.

## 타입 가드를 사용한 DTO 검사
타입 가드를 사용하여 DTO를 검사하는 방법은 간단합니다. 먼저, DTO에 대한 타입을 정의하고 해당 타입에 대한 타입 가드 함수를 작성합니다. 예를 들면 아래와 같습니다.

```typescript
type UserDTO = {
  id: number;
  username: string;
  email: string;
}

function isUserDTO(obj: any): obj is UserDTO {
  return typeof obj.id === 'number' &&
         typeof obj.username === 'string' &&
         typeof obj.email === 'string';
}
```

위 예제에서 `UserDTO`는 사용자 정보를 나타내는 DTO이고, `isUserDTO` 함수는 해당 DTO의 유효성을 검사하는 타입 가드 함수입니다. 이제 `isUserDTO` 함수를 사용하여 DTO를 검사할 수 있습니다.

```typescript
function processUser(user: any) {
  if (isUserDTO(user)) {
    // user 객체가 유효한 UserDTO일 경우 처리 로직 작성
  } else {
    // user 객체가 유효하지 않은 경우 에러 처리 로직 작성
  }
}
```

위의 `processUser` 함수에서는 `isUserDTO` 함수를 사용하여 입력된 `user` 객체의 유효성을 검사하고, 유효한 경우에는 해당 객체에 대한 처리 로직을 작성하고, 그렇지 않은 경우에는 에러 처리 로직을 작성합니다.

## 결론
타입 가드를 사용하여 타입스크립트에서 DTO의 유효성을 검사하는 것은 코드의 안정성을 높이는 데 도움이 됩니다. DTO를 사용하는 애플리케이션에서 유효성 검사를 통해 잘못된 데이터 전송을 방지하고, 안정성 있는 코드를 유지할 수 있습니다.

이러한 타입 가드를 통한 DTO의 유효성 검사는 타입스크립트에서 안정적인 데이터 전송을 위한 중요한 기술입니다.

## 참고 자료
- TypeScript Handbook: [Type Guards](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#using-type-predicates)
- MDN Web Docs: [Type guards and type assertions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)