---
layout: post
title: "Package.json을 활용한 JavaScript 프로젝트의 테스트용 서버 설정하기"
description: " "
date: 2023-11-06
tags: [javascript, nodejs]
comments: true
share: true
---

Node.js 기반의 JavaScript 프로젝트를 개발할 때, 테스트용 서버를 설정하는 것은 중요한 단계입니다. 이를 위해 `package.json` 파일을 활용하여 서버를 설정할 수 있습니다. 이번 블로그 포스트에서는 `package.json`을 활용하여 JavaScript 프로젝트의 테스트용 서버를 설정하는 방법에 대해 알아보겠습니다.

## 1. `scripts` 필드 추가하기

먼저, `package.json` 파일을 열고 `scripts` 필드를 추가해야 합니다. 이 필드는 프로젝트에서 사용할 수 있는 여러 명령어를 정의하는 곳입니다. 아래와 같이 `"scripts"` 필드를 추가해주세요.

```json
{
  "name": "my-project",
  "version": "1.0.0",
  ...
  "scripts": {
    "start": "node server.js"
  },
  ...
}
```

위의 예시에서 `"start"` 스크립트는 `server.js` 파일을 실행하는 것을 정의하고 있습니다.

## 2. 테스트용 서버 파일 작성하기

이제 `server.js` 파일을 작성해야 합니다. 이 파일은 테스트용 서버의 역할을 하게 됩니다. 예를 들어, Express.js를 사용하여 HTTP 서버를 만들고 필요한 라우트와 미들웨어를 추가할 수 있습니다. 아래는 간단한 예시입니다.

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
```

위의 예시에서는 Express.js를 사용하여 루트 경로(`/`)로 접속했을 때 "Hello World!"라는 응답을 반환하는 간단한 서버를 작성하였습니다.

## 3. 테스트용 서버 실행하기

이제 터미널을 열고 다음 명령어를 실행하여 테스트용 서버를 실행할 수 있습니다.

```bash
npm start
```

위 명령어는 `package.json`의 `"start"` 스크립트를 실행하게 됩니다. 이 경우, `server.js` 파일을 실행하므로 테스트용 서버가 시작됩니다.

## 마무리

이제 `package.json` 파일을 활용하여 JavaScript 프로젝트의 테스트용 서버를 설정하는 방법에 대해 알아보았습니다. `scripts` 필드를 추가하여 실행할 스크립트를 정의하고, 테스트용 서버 파일을 작성하여 실행하는 방식입니다. 이를 통해 개발 중인 프로젝트를 쉽게 테스트할 수 있습니다.

더 자세한 내용은 [Express.js 공식 문서](https://expressjs.com/)를 참고하세요.

#javascript #nodejs