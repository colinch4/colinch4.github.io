---
layout: post
title: "[javascript] 실행 컨텍스트 스택(execution context stack)이란 무엇인가?"
description: " "
date: 2023-12-14
tags: [javascript]
comments: true
share: true
---

JavaScript의 실행 컨텍스트 스택은 코드가 실행될 때 생성되는 개별 실행 컨텍스트가 쌓여 있는 스택입니다. 각 실행 컨텍스트는 해당 코드의 실행에 필요한 정보를 담고 있습니다.

### 실행 컨텍스트란?

*실행 컨텍스트*는 코드가 실행될 때 생성되고 실행될 때 필요한 여러 정보를 담고 있는 객체입니다. 각 실행 컨텍스트 안에는 변수, 객체 및 함수의 선언 및 실행 정보가 저장됩니다.

### 실행 컨텍스트 스택 작동 방식

1. **전역 실행 컨텍스트**: 코드가 실행될 때 가장 먼저 생성되는 실행 컨텍스트입니다.
2. **함수 실행 컨텍스트**: 함수가 호출될 때마다 해당 함수의 실행 컨텍스트가 스택에 추가됩니다.
3. **현재 실행 중인 함수의 실행 컨텍스트**: 스택의 맨 위에 위치한 실행 컨텍스트입니다.

### 실행 컨텍스트 스택의 역할

- 코드 실행 중에 변수, 함수 및 객체에 접근할 수 있도록 환경을 제공합니다.
- 스코프 체인과 클로저를 통해 변수 및 함수에 대한 접근을 가능하게 합니다.
- 스택 상단의 실행 컨텍스트에서 현재 실행 중인 코드의 실행을 관리합니다.

이러한 방식으로 실행 컨텍스트 스택은 JavaScript 코드의 실행 흐름을 관리하며, 함수 호출 및 변수, 객체, 함수의 스코프 관리를 담당합니다.

### 참고 자료
1. [JavaScript 실행 컨텍스트와 클로저](https://velog.io/@thms200/JavaScript%EC%9D%98-%EC%8B%A4%ED%96%89-%EC%BB%A8%ED%85%8D%EC%8A%A4%ED%8A%B8-%EC%8A%A4%ED%83%9D) (한국어)
2. [Understanding Execution Context and Execution Context Stack in JavaScript](https://frontnet.co.kr/191) (영어)