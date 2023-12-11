---
layout: post
title: "[typescript] 타입스크립트와 Jest를 사용하여 예외 처리(Exception Handling)를 테스트하는 방법"
description: " "
date: 2023-12-11
tags: [typescript]
comments: true
share: true
---

예외 처리는 소프트웨어 개발에서 중요한 부분 중 하나입니다. 타입스크립트와 Jest를 이용하여 코드에서 발생하는 예외를 효과적으로 테스트하는 방법을 살펴보겠습니다.

## 타입스크립트와 Jest 설정

먼저, 타입스크립트 프로젝트에 Jest를 설정합니다. `package.json` 파일에 jest를 설치합니다.

```json
"devDependencies": {
  "jest": "^27.0.6",
  "@types/jest": "^27.0.1",
  "ts-jest": "^27.0.3"
}
```

`tsconfig.json` 파일에 아래와 같이 `esModuleInterop` 옵션을 설정합니다.

```json
{
  "compilerOptions": {
    "esModuleInterop": true
  }
}
```

Jest 설정 파일(`jest.config.js`)을 프로젝트 루트 디렉토리에 생성하고 아래와 같이 설정합니다.

```javascript
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
};
```

## 예외 처리 테스트 작성

이제, 예외 처리를 테스트하는 함수를 작성합니다. 아래는 `throwError` 함수를 테스트하는 예제입니다. 

```typescript
function throwError(): void {
  throw new Error("Something went wrong");
}

describe("Exception handling", () => {
  it("should throw error", () => {
    expect(() => throwError()).toThrowError("Something went wrong");
  });
});
```

위의 예제에서 `throwError` 함수를 호출했을 때 예외가 발생하는지를 테스트하고, 발생한 예외가 정확히 예상한 메시지를 가지고 있는지를 확인합니다.

## 예외 처리 테스트 실행

테스트를 실행하여 예외 처리가 올바르게 동작하는지 확인합니다. 아래 명령어로 Jest를 실행할 수 있습니다.

```bash
npx jest
```

## 결론

이제 타입스크립트와 Jest를 사용하여 예외 처리를 효과적으로 테스트하는 방법을 알아보았습니다. 이를 통해 안정적인 소프트웨어를 개발하는 데 도움이 될 것입니다.

참고 자료:
- [Jest 공식 문서](https://jestjs.io/docs/getting-started)
- [타입스크립트 핸드북](https://www.typescriptlang.org/docs/handbook/intro.html)

**Happy coding!**