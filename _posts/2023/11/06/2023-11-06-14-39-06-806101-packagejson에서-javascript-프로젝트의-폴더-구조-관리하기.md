---
layout: post
title: "Package.json에서 JavaScript 프로젝트의 폴더 구조 관리하기"
description: " "
date: 2023-11-06
tags: [Package]
comments: true
share: true
---

JavaScript 프로젝트를 개발할 때 폴더 구조를 잘 관리하는 것은 매우 중요합니다. 이는 프로젝트의 구성요소들을 체계적으로 분류하고 유지 보수하기 쉽게 만들어줍니다. Package.json 파일은 npm(노드 패키지 매니저)에서 프로젝트의 의존성을 관리하기 위해 사용되는 파일입니다. 이 파일을 활용하여 JavaScript 프로젝트의 폴더 구조를 관리하는 방법에 대해 알아보겠습니다.

### 1. Package.json 파일 생성하기

먼저, 프로젝트의 루트 폴더에 명령 프롬프트 또는 터미널을 열고 다음 명령을 실행하여 Package.json 파일을 생성합니다.
```bash
npm init
```

이 명령을 실행하면 몇 가지 질문이 나오는데, 프로젝트의 이름이나 버전 등을 입력하면 됩니다. 입력을 완료하면 Package.json 파일이 생성됩니다.

### 2. 폴더 구조 설계

JavaScript 프로젝트의 폴더 구조는 프로젝트의 크기와 요구사항에 따라 다를 수 있지만, 일반적으로 다음과 같은 구조를 추천합니다.

```plaintext
- src
  - components
  - pages
  - utils
- public
- tests
- dist
```

- `src`: 소스 코드 파일들을 저장하는 폴더입니다.
  - `components`: 재사용 가능한 컴포넌트 파일들을 저장하는 폴더입니다.
  - `pages`: 프로젝트의 각 페이지에 대한 파일들을 저장하는 폴더입니다.
  - `utils`: 유틸리티 함수나 도우미 파일들을 저장하는 폴더입니다.
- `public`: 정적 파일들 (예: HTML, CSS, 이미지 등)을 저장하는 폴더입니다.
- `tests`: 테스트 파일들을 저장하는 폴더입니다.
- `dist`: 프로젝트 번들 파일이 생성되는 폴더입니다.

### 3. Package.json 파일 수정하기

Package.json 파일을 열어서 `scripts` 항목을 수정하여 프로젝트의 특정 명령어들을 실행할 수 있도록 설정할 수 있습니다. 예를 들어, 다음과 같이 설정할 수 있습니다.

```json
{
  "scripts": {
    "start": "node src/index.js",
    "test": "mocha tests",
    "build": "babel src -d dist"
  }
}
```

위의 설정을 추가하면 다음과 같이 각 명령어를 실행할 수 있습니다.

- `npm start`: 프로젝트를 실행합니다.
- `npm test`: 테스트를 실행합니다.
- `npm run build`: 소스 코드를 번들링하여 dist 폴더에 저장합니다.

### 4. 의존성 관리하기

Package.json 파일의 `dependencies` 항목에서 프로젝트가 의존하는 외부 패키지들을 관리할 수 있습니다. 예를 들어, lodash 패키지를 사용하고 있다면 다음과 같이 추가할 수 있습니다.

```json
{
  "dependencies": {
    "lodash": "^4.17.21"
  }
}
```

위의 예시에서 `"lodash": "^4.17.21"`는 lodash 패키지의 버전 4.17.21 이상을 의존성으로 설정한다는 의미입니다. 

### 마무리

Package.json 파일을 효과적으로 활용하여 JavaScript 프로젝트의 폴더 구조를 관리하는 방법에 대해 알아보았습니다. 자주 사용되는 폴더들을 구성하고, scripts 항목을 수정하여 편리하게 프로젝트를 관리할 수 있습니다. 이를 토대로 프로젝트 개발을 시작해보세요!

---
Reference:

- [npm Documentation](https://docs.npmjs.com/)