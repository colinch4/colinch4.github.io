---
layout: post
title: "Package.json을 사용하여 JavaScript 프로젝트의 쇼핑카트 설정하기"
description: " "
date: 2023-11-06
tags: [javascript]
comments: true
share: true
---

쇼핑카트는 많은 웹 애플리케이션에서 중요한 구성 요소입니다. 이번 가이드에서는 JavaScript 프로젝트에서 쇼핑카트를 설정하는 방법을 알아보겠습니다. 이를 위해 `package.json` 파일을 사용하여 종속성을 관리하고 설정할 것입니다.

## 1. 프로젝트 초기화

먼저, 프로젝트를 초기화해야 합니다. 프로젝트 폴더에서 터미널을 열고 다음 명령어를 실행하세요.

```shell
npm init
```

이 명령어는 새로운 `package.json` 파일을 생성해줍니다. 초기 설정은 여러분이 입력한 프로젝트에 대한 정보를 기반으로 생성됩니다.

## 2. Express와 필요한 패키지 설치

이제 쇼핑카트 구현에 필요한 의존성 패키지를 설치해야 합니다. 이 예제에서는 Express를 사용하여 간단한 웹 서버를 만들겠습니다. 터미널에서 다음 명령어를 실행하세요.

```shell
npm install express --save
```

위 명령을 실행하면 Express 패키지가 설치되고 `package.json` 파일의 `dependencies` 항목에 자동으로 추가됩니다.

## 3. 쇼핑카트 코드 작성

이제 쇼핑카트 코드를 작성해야 합니다. 예를 들어, `app.js` 파일에 다음과 같은 코드를 작성해봅시다.

```javascript
const express = require('express');
const app = express();

// 쇼핑카트에 아이템 추가
app.post('/cart/:item', (req, res) => {
  const item = req.params.item;
  console.log('아이템 추가:', item);
  res.send('아이템이 쇼핑카트에 추가되었습니다.');
});

// 쇼핑카트 보기
app.get('/cart', (req, res) => {
  console.log('쇼핑카트 보기');
  res.send('쇼핑카트를 보여줍니다.');
});

// 서버 시작
app.listen(3000, () => {
  console.log('서버가 http://localhost:3000 에서 실행 중입니다.');
});
```

위 코드에서 `/cart/:item` 경로에 POST 요청이 오면 쇼핑카트에 아이템을 추가하고, `/cart` 경로에 GET 요청이 오면 쇼핑카트를 보여줍니다.

## 4. 서버 실행

이제 쇼핑카트 서버를 실행해보겠습니다. 터미널에서 다음 명령어를 실행하세요.

```shell
node app.js
```

이제 웹 브라우저에서 `http://localhost:3000/cart/apple`에 접속해보세요. "아이템이 쇼핑카트에 추가되었습니다."라는 메시지가 보일 것입니다. 또한 `http://localhost:3000/cart`에 접속하면 "쇼핑카트를 보여줍니다."라는 메시지가 보일 것입니다.

## 5. 종속성 추가

추가적인 종속성을 설치해야 하는 경우, 터미널에서 다음 명령어를 사용하여 해당 패키지를 설치하세요.

```shell
npm install <패키지명> --save
```

이렇게 하면 `package.json` 파일의 `dependencies` 항목에 해당 패키지가 자동으로 추가됩니다.

## 정리

이제 JavaScript 프로젝트에서 쇼핑카트를 설정하는 방법을 알게 되었습니다. `package.json` 파일을 사용하여 종속성을 관리하고 필요한 패키지를 설치할 수 있습니다. Express를 사용하여 간단한 웹 서버를 만들고, 쇼핑카트 관련 기능을 구현할 수 있습니다. 이를 토대로 자신만의 쇼핑카트를 개발해보세요.

> 참고: [Express 공식 문서](https://expressjs.com/)
> #javascript #쇼핑카트