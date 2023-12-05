---
layout: post
title: "Package.json 설정을 활용한 JavaScript 프로젝트의 템플릿 엔진 설정"
description: " "
date: 2023-11-06
tags: [package]
comments: true
share: true
---

템플릿 엔진은 JavaScript 프로젝트에서 HTML, CSS, JavaScript 등을 동적으로 생성하는 데 사용되는 도구입니다. 이러한 템플릿 엔진을 사용하기 위해서는 프로젝트의 `package.json` 파일을 설정해야 합니다. 이 포스트에서는 `package.json` 설정을 통해 템플릿 엔진을 설정하는 방법에 대해 알아보겠습니다.

## Express와 EJS를 사용한 예시

1. 먼저, Express 프레임워크와 EJS(Effective JavaScript)를 설치해야 합니다. 아래의 명령어를 사용하여 설치합니다:

```shell
npm install express ejs
```

2. `package.json` 파일을 열고, `"dependencies"` 항목 아래에 다음과 같이 `"express"`와 `"ejs"`를 추가합니다:

```json
"dependencies": {
  "express": "^4.17.1",
  "ejs": "^3.1.6"
}
```

3. 프로젝트 루트 디렉토리에 `views` 디렉토리를 생성하고, 그 안에 `index.ejs` 파일을 생성합니다:

```ejs
<!DOCTYPE html>
<html>
  <head>
    <title>템플릿 엔진 예시</title>
  </head>
  <body>
    <h1>Hello, <%= name %>!</h1>
  </body>
</html>
```

4. Express 애플리케이션을 설정하고, EJS 템플릿 엔진을 사용하도록 `app.js` 파일을 업데이트합니다:

```javascript
const express = require('express');
const app = express();
const port = 3000;

app.set('view engine', 'ejs'); // EJS를 템플릿 엔진으로 설정
app.set('views', path.join(__dirname, 'views')); // views 디렉토리를 템플릿 파일의 기본 위치로 설정

app.get('/', (req, res) => {
  res.render('index', { name: 'World' }); // index.ejs 템플릿 렌더링
});

app.listen(port, () => {
  console.log(`서버가 http://localhost:${port} 에서 실행 중입니다.`);
});
```

5. 프로젝트를 실행하고 브라우저에서 `http://localhost:3000`을 엽니다. 화면에 "Hello, World!"라는 문구가 표시되어야 합니다.

## 결론

이제 JavaScript 프로젝트에서 템플릿 엔진을 설정하는 방법을 알게 되었습니다. `package.json` 파일을 활용하여 필요한 의존성을 설치하고, Express와 EJS를 함께 사용하여 동적인 웹 페이지를 생성할 수 있습니다.

# References
- [Express 공식 문서](https://expressjs.com/)
- [EJS 공식 문서](https://ejs.co/)