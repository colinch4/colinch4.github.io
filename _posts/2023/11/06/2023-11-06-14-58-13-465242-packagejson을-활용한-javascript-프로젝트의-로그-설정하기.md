---
layout: post
title: "Package.json을 활용한 JavaScript 프로젝트의 로그 설정하기"
description: " "
date: 2023-11-06
tags: []
comments: true
share: true
---

좋은 로깅은 JavaScript 프로젝트를 디버깅하고 분석하는 데 매우 유용합니다. 이를 위해 Package.json 파일을 사용하여 로깅 설정을 구성할 수 있습니다. 이번 블로그 게시물에서는 JavaScript 프로젝트에서의 로그 설정 방법과 Package.json을 활용하는 방법을 알아보겠습니다.

## 1. 로그 라이브러리 설치하기

먼저, 로그를 다룰 수 있는 Node.js 라이브러리를 설치해야 합니다. 가장 널리 사용되는 로그 라이브러리 중 하나인 `winston` 라이브러리를 예시로 들어 설명하겠습니다. 아래 명령어를 사용하여 `winston` 라이브러리를 설치합니다.

```shell
npm install winston
```

## 2. 로그 설정 파일 작성하기

프로젝트의 루트 디렉토리에 `logging.json`과 같은 이름의 파일을 생성하여 로그 설정을 작성합니다. 이 파일은 Package.json 파일과 동일한 디렉토리에 위치해야 합니다.

```json
{
  "logs": {
    "console": {
      "level": "info",
      "format": "simple"
    },
    "file": {
      "level": "debug",
      "format": "json",
      "filename": "logs/application.log"
    }
  }
}
```

이 예시에서는 로그를 콘솔과 파일로 출력하는 두 가지 타입의 로그를 설정하였습니다. 콘솔 로그의 레벨은 `info`이고, 파일 로그의 레벨은 `debug`입니다. 로그 포맷은 각각 'simple'과 'json'으로 지정되었습니다.

## 3. Package.json에 로그 설정 추가하기

이제 Package.json 파일에 로그 설정을 추가해야 합니다. `"scripts"` 필드 아래에 `"logging"` 항목을 추가합니다.

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "scripts": {
    "start": "node index.js",
    "logging": "node logger.js"
  }
}
```

여기서 `"logging"`은 로그 설정 파일을 처리하는 스크립트인 `logger.js`를 실행하는 명령어입니다.

## 4. logger.js 파일 작성하기

이제 `logger.js` 파일을 생성하고 다음과 같이 작성합니다.

```javascript
const winston = require('winston');
const loggingConfig = require('./logging.json');

// 콘솔 로그 설정
const consoleLogger = winston.createLogger({
  level: loggingConfig.logs.console.level,
  format: winston.format[loggingConfig.logs.console.format](),
  transports: [new winston.transports.Console()]
});

// 파일 로그 설정
const fileLogger = winston.createLogger({
  level: loggingConfig.logs.file.level,
  format: winston.format[loggingConfig.logs.file.format](),
  transports: [new winston.transports.File({ filename: loggingConfig.logs.file.filename })]
});

// 사용 예시
consoleLogger.log('info', 'This is an info log');
fileLogger.log('debug', 'This is a debug log');
```

위 예시에서는 `winston` 라이브러리를 사용하여 로그 설정을 콘솔과 파일에 출력하는 로거를 생성합니다. 이 로거 인스턴스를 사용하여 로그를 출력할 수 있습니다.

## 결론

본 게시물에서는 Package.json 파일을 활용하여 JavaScript 프로젝트의 로그 설정을 구성하는 방법을 다루었습니다. 로깅은 프로젝트 디버깅 및 분석에 매우 유용하므로 로그 설정을 적절히 구성하여 프로젝트 개발 및 유지 관리에 도움이 되기를 바랍니다.

## 참고 자료

- [Winston 라이브러리 공식 문서](https://github.com/winstonjs/winston)