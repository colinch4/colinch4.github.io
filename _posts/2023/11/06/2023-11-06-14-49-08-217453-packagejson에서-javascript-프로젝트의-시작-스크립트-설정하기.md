---
layout: post
title: "Package.json에서 JavaScript 프로젝트의 시작 스크립트 설정하기"
description: " "
date: 2023-11-06
tags: []
comments: true
share: true
---

JavaScript 프로젝트를 개발할 때, package.json 파일은 프로젝트의 구성 요소와 설정 정보를 담고 있는 중요한 파일입니다. 이 파일을 사용하여 프로젝트의 시작 스크립트를 설정할 수 있습니다. 시작 스크립트는 프로젝트를 실행할 때 자동으로 실행되는 스크립트를 가리킵니다. 

### package.json 파일 생성하기

먼저, 새로운 JavaScript 프로젝트를 생성하고 해당 디렉토리로 이동합니다. 프로젝트 디렉토리에서 명령줄을 열고 다음 명령어를 실행하여 package.json 파일을 생성합니다.

```shell
npm init
```

위 명령을 실행하면 프로젝트의 이름, 버전, 설명 등 다양한 정보를 입력하는 프롬프트가 표시됩니다. 필요한 정보를 입력한 후에는 package.json 파일이 생성됩니다.

### 시작 스크립트 설정하기

package.json 파일을 열고, "scripts" 항목을 찾습니다. 이 항목은 프로젝트의 시작 스크립트와 관련된 정보를 담고 있습니다. 시작 스크립트는 "scripts" 항목 내의 "start" 속성에 설정됩니다.

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "express": "^4.17.1"
  }
}
```

위 예시에서는 "start" 스크립트를 "node index.js"로 설정하였습니다. 이는 프로젝트를 실행할 때 "index.js" 파일이 자동으로 실행된다는 의미입니다.

### 프로젝트 실행하기

package.json 파일을 저장한 후 명령줄에서 다음 명령어를 실행하여 프로젝트를 실행할 수 있습니다.

```shell
npm start
```

npm start 명령을 실행하면 설정된 시작 스크립트가 실행되어 프로젝트가 시작됩니다.

### 마치며

이렇게 package.json 파일을 사용하여 JavaScript 프로젝트의 시작 스크립트를 설정할 수 있습니다. 시작 스크립트를 설정하여 프로젝트를 편리하게 실행할 수 있으며, 추가로 사용할 수 있는 다양한 스크립트를 설정할 수도 있습니다.

### 참고 자료

- [npm 공식 문서 - package.json](https://docs.npmjs.com/cli/v7/configuring-npm/package-json)
- [npm 공식 문서 - scripts](https://docs.npmjs.com/cli/v7/using-npm/scripts)