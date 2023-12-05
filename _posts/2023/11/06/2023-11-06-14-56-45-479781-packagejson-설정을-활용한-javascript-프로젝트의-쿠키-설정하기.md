---
layout: post
title: "Package.json 설정을 활용한 JavaScript 프로젝트의 쿠키 설정하기"
description: " "
date: 2023-11-06
tags: [package]
comments: true
share: true
---

쿠키는 웹 애플리케이션에서 클라이언트의 상태를 유지하기 위해 사용되는 작은 데이터 조각입니다. JavaScript를 사용하여 쿠키를 설정하고 관리하는 방법을 배워보겠습니다. 이를 위해 `cookie-parser` 패키지를 사용할 것입니다.

## 1. `cookie-parser` 패키지 설치

먼저, 프로젝트 디렉토리에서 `cookie-parser` 패키지를 설치합니다. 이 패키지는 Express.js에서 쿠키를 파싱하는 데 도움이 됩니다. 아래 명령을 실행하여 패키지를 설치하세요.

```shell
npm install cookie-parser
```

## 2. `package.json` 설정

이제 `package.json` 파일을 열어서 `scripts` 섹션에 다음과 같은 설정을 추가합니다.

```json
"scripts": {
  "start": "node index.js",
  "cookies": "node cookies.js"
}
```

위의 예시에서 `cookies` 스크립트는 쿠키를 설정하고 출력하는 역할을 합니다. 이제 `cookies.js` 파일을 생성하고 쿠키 설정 코드를 작성합니다.

## 3. `cookies.js` 파일 작성

`cookies.js` 파일에 다음 코드를 추가하여 쿠키 설정과 확인을 할 수 있습니다.

```javascript
const express = require('express');
const app = express();
const cookieParser = require('cookie-parser');

app.use(cookieParser());

app.get('/set-cookie', (req, res) => {
  res.cookie('username', 'john', { maxAge: 900000, httpOnly: true });
  res.send('Cookie set');
});

app.get('/get-cookie', (req, res) => {
  const username = req.cookies.username;
  res.send(`Username: ${username}`);
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
```

위의 코드는 Express.js를 사용하여 `/set-cookie` 엔드포인트에서 쿠키를 설정하고 `/get-cookie` 엔드포인트에서 쿠키를 확인하는 기능을 구현합니다.

## 4. 쿠키 설정 및 확인

터미널에서 아래 명령어를 실행하여 쿠키를 설정하고 확인할 수 있습니다.

```shell
npm run cookies
```

이제 `http://localhost:3000/set-cookie`에 접속하여 쿠키를 설정하고, `http://localhost:3000/get-cookie`에 접속하여 쿠키를 확인할 수 있습니다.

## 5. 마무리

이제 JavaScript 프로젝트에서 쿠키를 설정하는 방법을 배웠습니다. 쿠키를 사용하여 클라이언트의 상태를 유지하고 필요한 정보를 전달할 수 있습니다. `cookie-parser` 패키지를 통해 간편하게 쿠키를 관리할 수 있으므로, 이를 활용하여 웹 애플리케이션의 기능을 더욱 향상시킬 수 있습니다.

참고: [Express.js 공식 문서](https://expressjs.com/)