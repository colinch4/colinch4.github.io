---
layout: post
title: "[typescript] 컴파일러 플래그를 사용하여 experimentalDecorators 설정하기"
description: " "
date: 2023-12-12
tags: [typescript]
comments: true
share: true
---

TypeScript는 JavaScript에 타입을 추가하는 강력한 도구입니다. 또한 데코레이터(Decorators)를 지원하여 클래스 및 클래스 멤버에 메타데이터를 추가할 수 있습니다. 그러나 decorator를 사용하기 위해서는 `experimentalDecorators` 플래그를 설정해야 합니다.

이 튜토리얼에서는 TypeScript 컴파일러 플래그를 사용하여 `experimentalDecorators`를 설정하는 방법에 대해 알아보겠습니다.

## 1. tsconfig.json 파일 생성 또는 열기

먼저 프로젝트 루트 디렉터리에 `tsconfig.json` 파일을 생성하거나 이미 있다면 엽니다.

```json
{
  "compilerOptions": {
    // 기타 옵션들...
  },
  "include": [
    // 포함할 파일 및 디렉터리 목록
  ]
}
```

## 2. experimentalDecorators 플래그 추가

`tsconfig.json` 파일의 `compilerOptions` 항목에 `experimentalDecorators` 플래그를 추가합니다.

```json
{
  "compilerOptions": {
    "experimentalDecorators": true,
    // 기타 옵션들...
  }
}
```

## 3. 프로젝트 재컴파일

이제 변경된 `tsconfig.json` 파일을 저장한 후, 프로젝트를 다시 컴파일하면 TypeScript는 `experimentalDecorators` 플래그를 설정하여 데코레이터를 사용할 수 있게 됩니다.

위의 단계를 따라 하여 TypeScript에서 데코레이터를 사용하기 위해 `experimentalDecorators` 플래그를 설정할 수 있습니다.

이제 데코레이터를 사용하여 클래스 또는 클래스 멤버에 메타데이터를 추가할 수 있습니다. 이를 통해 코드를 더 쉽게 이해하고 유지보수하는 데 도움을 받을 수 있습니다.

더 많은 TypeScript 컴파일러 플래그나 설정 옵션에 대해 알아보고 싶다면 [TypeScript 공식 문서](https://www.typescriptlang.org/tsconfig)를 참고하세요.