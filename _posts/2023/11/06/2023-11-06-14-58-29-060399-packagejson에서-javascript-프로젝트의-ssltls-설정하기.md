---
layout: post
title: "Package.json에서 JavaScript 프로젝트의 SSL/TLS 설정하기"
description: " "
date: 2023-11-06
tags: [package]
comments: true
share: true
---

자바스크립트 프로젝트를 개발하면서, 보안 연결을 위해 SSL/TLS (Secure Sockets Layer/Transport Layer Security) 설정을 적용해야 할 때가 있습니다. 이 설정은 클라이언트와 서버 간의 통신을 암호화하고 보호하기 위해 사용됩니다. 이번 블로그 포스트에서는 package.json 파일을 사용하여 JavaScript 프로젝트에서 SSL/TLS 설정을 어떻게 할 수 있는지 알아보겠습니다.

## package.json 파일에 SSL/TLS 설정 추가하기

1. 먼저, JavaScript 프로젝트의 루트 디렉토리에 있는 **package.json** 파일을 엽니다.

2. **scripts** 섹션 아래에 **start** 스크립트를 찾습니다. 만약 해당 스크립트가 없다면, 아래와 같이 추가합니다:
```json
"scripts": {
   "start": "node index.js"
}
```

3. **start** 스크립트 아래에 다음과 같은 환경 변수를 추가합니다:
```json
"scripts": {
   "start": "set HTTPS=true&& node index.js"
}
```

4. **start** 스크립트를 수정한 후, package.json 파일을 저장합니다.

## 서버 사이드에서 SSL/TLS 설정하기

1. JavaScript 프로젝트의 루트 디렉토리에 있는 **index.js** 파일을 엽니다.

2. **index.js** 파일의 맨 위에 다음과 같은 코드를 추가합니다:
```javascript
const https = require('https');
const fs = require('fs');

const options = {
   key: fs.readFileSync('path/to/private.key'),
   cert: fs.readFileSync('path/to/certificate.crt')
};

https.createServer(options, (req, res) => {
   // 서버 코드
}).listen(3000);
```
위의 코드에서, **path/to/private.key**와 **path/to/certificate.crt**는 서버의 개인 키와 인증서 파일의 경로를 나타냅니다. 이를 프로젝트에 맞게 수정하고 저장합니다.

## SSL/TLS 설정 확인하기

1. 터미널을 열고, 프로젝트의 루트 디렉토리로 이동합니다.

2. 다음 명령어를 실행하여 서버를 시작합니다:
```
npm start
```

3. 서버가 시작되면, 웹 브라우저에서 https://localhost:3000 (혹은 지정한 포트 번호)로 접속하여 SSL/TLS 설정이 제대로 동작하는지 확인합니다.

## 요약

이 글에서는 package.json 파일을 사용하여 JavaScript 프로젝트에서 SSL/TLS 설정하는 방법을 살펴보았습니다. package.json 파일에 HTTPS 변수를 설정한 후, 서버 사이드 코드에서 HTTPS 모듈을 사용하여 SSL/TLS 설정을 적용할 수 있습니다. 이를 통해 프로젝트의 보안을 강화할 수 있습니다.

**참고 자료:**
- [Node.js HTTPS 모듈 문서](https://nodejs.org/api/https.html)