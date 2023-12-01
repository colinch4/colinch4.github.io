---
layout: post
title: "[javascript] Vue.js와 JWT(Jason Web Token)의 사용법"
description: " "
date: 2023-12-01
tags: [javascript]
comments: true
share: true
---

## 소개

Vue.js는 현재 가장 인기있는 프론트엔드 JavaScript 프레임워크 중 하나입니다. JWT는 웹 애플리케이션에서 사용자 인증과 권한 부여를 위한 토큰 기반 인증 방식 중 하나입니다. 이 글에서는 Vue.js와 JWT를 함께 사용하는 방법에 대해 알아보겠습니다.

## JWT란 무엇인가요?

JWT는 클라이언트-서버 간에 정보를 안전하게 전송하기 위해 사용되는 토큰 기반 인증 방식입니다. 토큰은 사용자의 인증 정보와 함께 서명되어 있어 변조를 방지할 수 있습니다. JWT는 JSON 형식으로 표현되며, 토큰에는 발급자, 사용자 정보, 만료 시간 등의 데이터가 포함될 수 있습니다.

## Vue.js에서 JWT 사용하기

Vue.js에서 JWT를 사용하기 위해서는 다음과 같은 단계를 따라야 합니다.

### 1. JWT 라이브러리 설치

먼저, Vue.js 프로젝트에 JWT 라이브러리를 설치해야 합니다. `jsonwebtoken`이라는 라이브러리는 JWT를 생성하고 검증하는데 도움을 주는 편리한 기능을 제공합니다. NPM을 사용하여 다음 명령어를 실행하여 라이브러리를 설치할 수 있습니다:

```bash
$ npm install jsonwebtoken
```

### 2. JWT 생성하기

사용자가 로그인 후, Vue.js 프론트엔드는 JWT를 생성해야 합니다. 생성된 토큰은 서버로 전송되고, 서버에서는 해당 토큰을 검증하여 인증 및 권한 부여를 수행합니다.

다음은 Vue.js에서 JWT를 생성하는 예제 코드입니다:

```javascript
import jwt from 'jsonwebtoken';

const user = {
  id: 123,
  username: 'johndoe',
  role: 'admin'
};

const secretKey = 'mysecretkey';

const token = jwt.sign(user, secretKey);
```

위 예제에서 `jwt.sign` 함수를 사용하여 사용자 객체와 비밀 키를 전달하여 JWT를 생성합니다.

### 3. JWT 검증하기

Vue.js에서 JWT를 검증하기 위해서는 서버로부터 받은 토큰을 검증해야 합니다. 이를 위해 서버에서 제공하는 API를 호출해야 합니다. 서버 측에서는 JWT를 검증한 후, 유효한 경우 서버로부터 데이터를 반환합니다.

다음은 Vue.js에서 JWT를 검증하는 예제 코드입니다:

```javascript
import jwt from 'jsonwebtoken';

const token = '...'; // 서버로부터 전달받은 토큰

const secretKey = 'mysecretkey';

jwt.verify(token, secretKey, (err, decoded) => {
  if (err) {
    // 토큰이 유효하지 않은 경우
    console.error(err);
  } else {
    // 토큰이 유효한 경우, 디코딩된 사용자 정보를 사용하여 작업 수행
    console.log(decoded);
  }
});
```

위 예제에서 `jwt.verify` 함수를 사용하여 토큰을 검증합니다. 검증이 성공하면 디코딩된 사용자 정보를 콘솔에 출력합니다.

## 결론

Vue.js와 JWT를 함께 사용하면 안전하고 효율적인 사용자 인증 및 권한 부여를 구현할 수 있습니다. Vue.js에서 JWT를 생성하고 검증하는 방법에 대해 알아보았습니다. 추가적으로 JWT를 저장하고 관리하는 방법, JWT를 사용한 API 호출 등을 공부하여 보다 실용적인 애플리케이션을 구현할 수 있습니다.

## 참고문서

- [JWT 공식 사이트](https://jwt.io/)
- [Vue.js 공식 사이트](https://vuejs.org/)
- [jsonwebtoken 라이브러리](https://www.npmjs.com/package/jsonwebtoken)