---
layout: post
title: "Package.json 설정을 사용하여 JavaScript 프로젝트의 에러 핸들링하기"
description: " "
date: 2023-11-06
tags: [package]
comments: true
share: true
---

에러 핸들링은 JavaScript 프로젝트에서 매우 중요한 부분입니다. 이를 효과적으로 처리하기 위해서는 패키지 의존성 및 관리를 포함하여 적절한 설정이 필요합니다. 이 기사에서는 `package.json` 파일을 사용하여 JavaScript 프로젝트의 에러 핸들링을 설정하는 방법을 소개하겠습니다.

## package.json 파일 설정하기

1. 프로젝트 루트 폴더에서 `package.json` 파일을 엽니다.

2. `scripts` 항목에 `start` 명령어를 추가합니다. 에러 핸들링에 사용될 스크립트를 등록할 수 있습니다.
   ```json
   "scripts": {
     "start": "node server.js"
   }
   ```

3. `dependencies` 나 `devDependencies` 에 에러 핸들링에 필요한 패키지를 추가합니다. 주로 사용되는 패키지에는 `express` 와 `dotenv` 등이 있습니다.
   ```json
   "dependencies": {
     "express": "^4.17.1"
   },
   "devDependencies": {
     "dotenv": "^10.0.0"
   }
   ```

4. 에러 핸들링을 위해 필요한 환경 변수들을 `.env` 파일에 설정합니다. `.env` 파일은 프로젝트 루트 폴더에 생성하며, 필요한 환경 변수들을 키-값 형태로 정의합니다.
   ```
   PORT=3000
   DB_USERNAME=admin
   DB_PASSWORD=password
   ```

## 에러 핸들링 스크립트 작성하기

모든 에러 핸들링 로직을 `server.js` 파일에 작성합니다. 주요한 에러 핸들링을 위해 다음과 같은 스크립트들을 추가할 수 있습니다.

```javascript
// 필요한 패키지를 가져옵니다.
const express = require('express');
const dotenv = require('dotenv');

// .env 파일을 로드합니다.
dotenv.config();

// Express 앱을 생성합니다.
const app = express();

// 에러 처리 미들웨어를 등록합니다.
app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).send('Internal Server Error');
});

// 서버를 실행합니다.
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
```

위의 스크립트에서 `app.use()` 함수는 에러를 처리하는 미들웨어를 등록합니다. 이를 통해 발생한 모든 에러는 콘솔에 로깅되고 클라이언트에는 "Internal Server Error" 메시지가 전송됩니다.

## 프로젝트 실행하기

프로젝트를 실행하기 전, 다음 명령을 사용하여 필요한 패키지들을 설치해야 합니다.
```bash
npm install
```

프로젝트를 실행하기 위해 다음 명령을 실행합니다.
```bash
npm start
```

이제 JavaScript 프로젝트에서 에러 핸들링을 설정하는 방법을 알게 되었습니다. `package.json` 파일을 사용하여 프로젝트 설정을 관리하면 개발 과정에서 에러를 효과적으로 처리할 수 있습니다.

> 참고 자료:
> - [Express.js 공식 문서](https://expressjs.com/)
> - [dotenv 라이브러리](https://www.npmjs.com/package/dotenv)