---
layout: post
title: "[javascript] AMD(Asynchronous Module Definition)와 CommonJS 모듈의 차이점은 무엇인가요?"
description: " "
date: 2023-12-18
tags: [javascript]
comments: true
share: true
---

1. **로딩 방식:**
   - AMD는 비동기 로딩을 지원하므로 브라우저 환경에서 주로 사용됩니다. 모든 종속성이 로드되면 콜백이 실행됩니다.
   - CommonJS는 동기식 로딩 모델을 따르며, 모듈이 필요할 때마다 필요한 모듈을 동기적으로 로드합니다. 이는 주로 Node.js와 같은 서버 환경에서 사용됩니다.

2. **문법:**
   - AMD는 `define` 함수를 사용하여 모듈을 정의하고, `require` 함수를 사용하여 종속성을 가져옵니다.
   - CommonJS는 `require` 함수를 사용하여 모듈을 가져오고, `module.exports` 및 `exports` 객체를 사용하여 모듈을 정의합니다.

3. **환경:**
   - AMD는 주로 브라우저에서 사용되며, 모듈 로딩의 비동기적 특성을 고려하여 설계되었습니다.
   - CommonJS는 주로 서버 측 JavaScript 환경에서 사용되며, 파일 시스템 및 네트워크와 같은 동기적인 작업을 다룹니다.

따라서 환경(브라우저 또는 서버)과 로딩 방식(동기 또는 비동기)에 따라 두 모듈 시스템 중 하나를 선택할 수 있습니다.