---
layout: post
title: "Package.json을 활용하여 JavaScript 프로젝트의 사진 업로드 설정하기"
description: " "
date: 2023-11-06
tags: []
comments: true
share: true
---

## 사진 업로드 라이브러리 설치하기
사진 업로드를 위해 먼저 필요한 라이브러리를 설치해야 합니다. Package.json 파일을 열고 `dependencies`에 다음과 같은 라이브러리를 추가합니다.

```json
{
  "dependencies": {
    "multer": "^1.4.2"
  }
}
```

위의 예시에서는 multer라는 사진 업로드를 처리해주는 라이브러리를 사용하였습니다. 이 라이브러리는 HTTP 요청에서 멀티파트(form-data) 데이터를 처리할 수 있습니다.

라이브러리를 설치하기 위해 터미널에서 아래 명령어를 실행합니다.

```bash
npm install
```

## 사진 업로드 설정하기
사진 업로드를 위해서는 Express 애플리케이션에서 multer를 설정해야 합니다. 이를 위해 Express 애플리케이션의 서버 파일에 다음과 같은 코드를 추가합니다.

```javascript
const express = require('express');
const multer = require('multer');

const app = express();

// 사진 업로드를 처리할 미들웨어 설정
const upload = multer({ dest: 'uploads/' })

app.post('/upload', upload.single('photo'), (req, res) => {
  // 업로드된 사진의 정보를 사용하여 처리하는 로직 추가
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

위의 예시에서는 `/upload` 엔드포인트에 POST 요청이 들어오면 multer를 이용하여 사진을 업로드하는 미들웨어를 실행합니다. `upload.single('photo')`는 한 개의 사진을 업로드하고자 할 때 사용되는 메서드입니다. `photo`는 업로드되는 파일의 필드 명을 나타냅니다.

## 실행 및 테스트
설정이 완료되면 프로젝트를 실행하여 사진 업로드 기능을 테스트할 수 있습니다. 터미널에서 아래 명령어를 실행합니다.

```bash
node app.js
```

서버가 정상적으로 실행되면 브라우저나 API 도구 등을 이용하여 `/upload` 엔드포인트로 POST 요청을 보내서 사진을 업로드해볼 수 있습니다.

이제 JavaScript 프로젝트에서 Package.json을 활용하여 사진 업로드를 설정하는 방법에 대해 알아보았습니다. Multer 라이브러리를 사용하여 쉽게 사진 업로드 기능을 구현할 수 있습니다.

## References
- [Multer GitHub Repository](https://github.com/expressjs/multer)