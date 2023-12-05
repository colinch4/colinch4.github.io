---
layout: post
title: "Package.json을 활용한 JavaScript 프로젝트의 사전 컴파일 설정하기"
description: " "
date: 2023-11-06
tags: [package]
comments: true
share: true
---

JavaScript 프로젝트를 시작할 때, 종종 사전 컴파일(pre-compile) 단계를 거치는 것이 유용합니다. 이를 통해 코드를 최적화하고 트랜스파일하거나 번들링할 수 있습니다. 이 글에서는 Package.json 파일을 사용하여 JavaScript 프로젝트의 사전 컴파일 설정을 하는 방법에 대해 알아보겠습니다.

## Package.json 파일 생성하기

먼저, 프로젝트 루트 디렉토리에 Package.json 파일을 생성해야 합니다. 이를 위해서는 터미널을 열고 다음 명령어를 실행합니다:

```
npm init
```

실행하면 프로젝트에 대한 정보를 입력할 수 있는 대화형 프롬프트가 표시됩니다. 이 프롬프트를 따라가며 프로젝트에 대한 정보를 입력한 후, Package.json 파일이 생성됩니다.

## 사전 컴파일 도구 설치하기

사전 컴파일을 위해 사용할 도구를 설치해야 합니다. 예를 들어, Babel을 사용하여 ES6 코드를 ES5로 트랜스파일한다고 가정해봅시다. 이 경우에는 다음 명령어를 사용하여 Babel을 설치합니다:

```
npm install --save-dev @babel/core @babel/preset-env
```

위 명령어를 실행한 후, Package.json 파일의 `devDependencies` 항목에 Babel 관련 패키지가 추가됩니다.

## 사전 컴파일 스크립트 추가하기

사전 컴파일을 실행하기 위해 Package.json 파일에 스크립트를 추가해야 합니다. 이를 위해 Package.json 파일을 열고, `"scripts"` 항목 아래에 사전 컴파일을 실행할 명령어를 추가합니다. Babel을 사용하는 경우, 다음과 같이 `"build"` 스크립트를 추가할 수 있습니다:

```json
"scripts": {
  "build": "babel src -d dist"
}
```

위 예시에서는 `babel` 명령어를 사용하여 `src` 폴더의 파일들을 `-d` 옵션을 통해 `dist` 폴더로 트랜스파일하도록 설정하였습니다. 필요에 따라 이 명령어를 수정하여 원하는 동작을 설정할 수 있습니다.

사전 컴파일 스크립트를 추가한 후, 터미널에서 다음 명령어를 실행하여 사전 컴파일을 실행할 수 있습니다:

```
npm run build
```

위 명령어를 실행하면 설정한 스크립트가 실행되어 코드가 사전 컴파일됩니다.

## 결론

Package.json 파일을 활용하여 JavaScript 프로젝트의 사전 컴파일 설정을 효과적으로 할 수 있습니다. 위에서는 Babel을 예시로 들었지만, 다른 사전 컴파일 도구를 사용하는 경우에도 비슷한 방식으로 설정할 수 있습니다. 이를 통해 프로젝트를 더욱 효율적으로 관리하고 개발할 수 있습니다.

관련 참고 자료:
- Babel 공식 문서: https://babeljs.io/
- npm 공식 문서: https://docs.npmjs.com/