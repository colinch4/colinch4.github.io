---
layout: post
title: "Package.json에서 JavaScript 프로젝트 실행 스크립트 작성하기"
description: " "
date: 2023-11-06
tags: [package]
comments: true
share: true
---

JavaScript 프로젝트를 관리하기 위해 `package.json` 파일을 사용하는 것은 일반적인 관행입니다. `package.json` 파일은 프로젝트의 종속성 관리뿐만 아니라 스크립트 실행에도 사용됩니다. 이 글에서는 `package.json` 파일의 `scripts` 필드를 사용하여 JavaScript 프로젝트의 실행 스크립트를 작성하는 방법을 알아보겠습니다.

### `scripts` 필드 소개

`package.json` 파일의 `scripts` 필드에는 프로젝트의 실행 스크립트를 작성할 수 있습니다. 이 필드에 작성된 스크립트는 `npm run` 명령어를 사용하여 실행할 수 있습니다.

```json
"scripts": {
  "start": "node index.js",
  "test": "mocha"
}
```

위 예시에서는 `start` 스크립트가 `node index.js` 명령어를 실행하고, `test` 스크립트는 `mocha` 명령어를 실행합니다. 이렇게 작성된 스크립트는 `npm run start` 또는 `npm run test` 명령어를 통해 실행할 수 있습니다.

### `scripts` 필드에 스크립트 작성하기

실행 스크립트를 작성할 때에는 사용하는 툴 또는 명령어의 이름을 스크립트 이름으로 사용하는 것이 일반적입니다. 예를 들어, Babel을 사용하여 ES6 코드를 변환한다면 스크립트 이름을 `build`로 작성하는 것이 좋습니다.

```json
"scripts": {
  "build": "babel src -d dist"
}
```

위 예시에서는 `npm run build` 명령어를 실행하면 `babel src -d dist` 명령어가 실행됩니다. 이 명령어는 `src` 폴더의 파일을 `dist` 폴더로 Babel을 통해 변환합니다.

### 스크립트에 매개변수 사용하기

스크립트는 매개변수를 사용하여 보다 동적인 동작을 할 수 있습니다. 매개변수는 `$npm_config_` 접두사를 붙여 사용할 수 있습니다.

```json
"scripts": {
  "start": "node server.js",
  "start:dev": "nodemon server.js",
  "start:prod": "node server.js --production"
}
```

위 예시에서 `start:prod` 스크립트는 `--production` 옵션을 사용하여 서버를 실행합니다. 매개변수를 통해 다양한 실행 환경에서 스크립트를 사용할 수 있습니다.

### 스크립트 실행 순서 설정하기

여러 개의 스크립트를 순서대로 실행하기 위해서는 `&&` 연산자를 사용할 수 있습니다.

```json
"scripts": {
  "build": "webpack && babel src -d dist"
}
```

위 예시에서 `build` 스크립트는 `webpack` 명령어가 실행된 후에 `babel src -d dist` 명령어가 실행됩니다.

### 추가적인 스크립트 예시

아래는 자주 사용되는 다른 스크립트 예시입니다.

```json
"scripts": {
  "test": "mocha",
  "lint": "eslint src",
  "start": "node server.js",
  "start:dev": "nodemon server.js",
  "start:prod": "node server.js --production"
}
```

- `test`: 테스트 스크립트로 Mocha를 실행합니다.
- `lint`: ESLint를 사용하여 소스 코드를 검사합니다.
- `start`: 서버를 실행합니다.
- `start:dev`: 개발 모드에서 서버를 실행합니다.
- `start:prod`: 프로덕션 모드에서 서버를 실행합니다.

### 마무리

이제 `package.json` 파일의 `scripts` 필드를 사용하여 JavaScript 프로젝트의 실행 스크립트를 작성하는 방법을 알게 되었습니다. 이를 통해 프로젝트의 관리와 개발 효율성을 높일 수 있습니다. 추가적인 정보는 [공식 npm 문서](https://docs.npmjs.com/cli/v7/using-npm/scripts)를 참고해주세요.