---
layout: post
title: "Package.json을 활용하여 JavaScript 프로젝트의 초기 설정 자동화하기"
description: " "
date: 2023-11-06
tags: []
comments: true
share: true
---

JavaScript 프로젝트를 시작할 때는 기본적인 설정들을 직접 해주어야 합니다. 이러한 작업은 번거롭고 반복적일 수 있습니다. 이러한 문제를 해결하기 위해 **Package.json** 파일을 사용하여 JavaScript 프로젝트의 초기 설정을 자동화할 수 있습니다.

## Package.json이란?

**Package.json**은 JavaScript 프로젝트의 metadata와 의존성(dependency) 정보를 포함하는 파일입니다. 이 파일은 프로젝트를 초기화하고 관리하는 데 사용됩니다.

## Package.json 사용하기

1. 프로젝트 디렉토리에서 터미널을 엽니다.
2. `npm init` 명령어를 실행하여 프로젝트 초기화를 시작합니다.
3. 몇 가지 프로젝트 정보를 입력하고 엔터를 눌러 파일을 생성합니다.
4. 생성된 Package.json 파일에서 프로젝트에 필요한 설정을 추가하거나 수정합니다.

## 의존성(dependency) 설치하기

Package.json 파일에는 프로젝트에 필요한 외부 라이브러리를 명시할 수 있습니다. 
이를 통해 개발자들은 별도로 패키지를 다운로드하거나 관리하지 않아도 됩니다.

1. 터미널에서 `npm install <package-name>` 명령어를 실행하여 필요한 패키지를 설치합니다.
2. 설치한 패키지는 Package.json 파일의 dependencies 항목에 자동으로 추가됩니다.

**예시:**

```
"dependencies": {
  "express": "^4.17.1",
  "axios": "^0.21.1",
  "lodash": "^4.17.21"
}
```

## 스크립트(script) 실행하기

Package.json 파일을 사용하여 JavaScript 프로젝트에 스크립트를 추가하고 실행할 수도 있습니다.

1. Package.json 파일의 scripts 항목에 스크립트를 추가합니다.

**예시:**

```
"scripts": {
  "start": "node server.js",
  "test": "jest"
}
```

2. 터미널에서 `npm run <script-name>` 명령어를 사용하여 스크립트를 실행합니다.

## 결론

Package.json은 JavaScript 프로젝트의 초기 설정을 자동화하기 위해 유용한 도구입니다. 해당 파일을 사용하면 개발자들은 프로젝트의 의존성 관리, 스크립트 실행 등을 편리하게 수행할 수 있습니다.

---

#### 참고 자료
- [npm Documentation](https://docs.npmjs.com/cli/v7/configuring-npm/package-json)
- [Understanding package.json](https://www.sitepoint.com/package-json-node-js/)