---
layout: post
title: "[typescript] 컴파일러 플래그를 사용하여 strictPropertyInitialization 설정하기"
description: " "
date: 2023-12-12
tags: [typescript]
comments: true
share: true
---

## 1. `strictPropertyInitialization` 옵션 활성화

먼저, TypeScript 설정 파일(`tsconfig.json`)에서 `strictPropertyInitialization` 옵션을 활성화해야 합니다. 

```json
{
  "compilerOptions": {
    "strictPropertyInitialization": true
  }
}
```

이렇게 설정하면 컴파일러가 클래스 내의 모든 프로퍼티가 선언과 동시에 초기화되었는지 확인합니다.

## 2. 프로퍼티 초기화하기

클래스 내의 프로퍼티를 선언할 때 초기값을 반드시 제공해야 합니다.

```typescript
class Example {
  public name: string = ''; // 초기값을 제공
  public age!: number; // 느낌표(!)를 사용하여 나중에 값이 할당됨을 명시
}
```

위의 예시에서 `name` 프로퍼티는 초기값을 제공하였고, `age` 프로퍼티는 나중에 값을 할당할 것임을 느낌표(!)로 명시했습니다.

이렇게 하면 컴파일러가 `strictPropertyInitialization` 규칙을 준수한다고 판단하여 경고나 오류를 피할 수 있습니다.

`strictPropertyInitialization` 설정을 사용하면 초기화되지 않은 프로퍼티로 인한 잠재적인 오류를 방지할 수 있으므로 TypeScript 프로젝트에서 안정성을 높일 수 있습니다.

더 많은 정보는 TypeScript 공식 문서의 [strictPropertyInitialization](https://www.typescriptlang.org/tsconfig#strictPropertyInitialization) 섹션을 참고하세요.