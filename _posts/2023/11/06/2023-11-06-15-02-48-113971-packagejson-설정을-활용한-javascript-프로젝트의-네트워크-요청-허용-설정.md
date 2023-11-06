---
layout: post
title: "Package.json 설정을 활용한 JavaScript 프로젝트의 네트워크 요청 허용 설정"
description: " "
date: 2023-11-06
tags: [javascript, cors]
comments: true
share: true
---

JavaScript 프로젝트를 개발할 때, 종종 서버와의 네트워크 요청이 필요합니다. 이때, 브라우저의 보안 정책에 따라 CORS (Cross-Origin Resource Sharing) 에러가 발생할 수 있습니다. 이러한 문제를 해결하기 위해, 프로젝트의 Package.json 파일을 사용하여 네트워크 요청을 허용할 수 있습니다.

## Package.json 파일 수정

1. 프로젝트 루트 디렉토리에서 Package.json 파일을 엽니다.
2. `"scripts"` 키를 찾습니다. 만약 없다면, 새로 생성합니다.
3. `"scripts"` 키 아래에 `"start"` 키를 만듭니다.
4. `"start"` 키의 값으로 `"NODE_OPTIONS='--enable-source-maps --inspect-brk'"` 를 설정합니다.
5. 이제 프로젝트가 CORS 에러 없이 네트워크 요청을 할 수 있습니다.

예시:

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "scripts": {
    "start": "NODE_OPTIONS='--enable-source-maps --inspect-brk' react-scripts start"
  },
  ...
}
```

## 프로젝트 실행

Package.json 파일을 수정한 뒤, 해당 프로젝트를 실행하기 위해 다음 명령어를 사용합니다.

```bash
npm start
```

이제 프로젝트의 네트워크 요청은 CORS 에러 없이 서버로 전송될 것입니다.

## 참고 자료

- [MDN Web Docs - 코스(CORS) 에러 처리하기](https://developer.mozilla.org/ko/docs/Web/HTTP/CORS)
- [NPM Documentation - Scripts](https://docs.npmjs.com/cli/v7/using-npm/scripts)

#javascript #cors