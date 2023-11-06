---
layout: post
title: "Package.json에서 JavaScript 프로젝트의 페이스북 연동 설정하기"
description: " "
date: 2023-11-06
tags: []
comments: true
share: true
---

페이스북 연동은 JavaScript 프로젝트에서 매우 중요한 요소입니다. 사용자 인증, 소셜 로그인 등 다양한 기능을 구현할 때 페이스북 API를 사용할 수 있습니다. 이를 위해 프로젝트의 Package.json 파일에서 페이스북 연동 설정을 할 수 있습니다. 

## 1. 페이스북 개발자 등록 및 앱 생성

페이스북 연동을 위해 먼저 페이스북 개발자 포털에 등록하고 앱을 생성해야 합니다. [https://developers.facebook.com](https://developers.facebook.com) 에 접속하여 개발자 계정을 만들고, 앱을 생성합니다. 

## 2. Package.json 파일 수정

Package.json 파일에서 페이스북 연동에 필요한 정보를 설정해야 합니다. 아래와 같이 "facebookAppId"와 "facebookAppSecret"을 추가해주세요. 

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "facebookAppId": "YOUR_APP_ID",
  "facebookAppSecret": "YOUR_APP_SECRET",
  "dependencies": {
    "react": "^16.13.1",
    "react-dom": "^16.13.1",
    "react-scripts": "3.4.1"
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```

위에서 "YOUR_APP_ID"와 "YOUR_APP_SECRET"에는 생성한 페이스북 앱의 앱 ID와 시크릿 키를 각각 입력해야 합니다.

## 3. 환경 변수 설정

Package.json 파일에서 페이스북 앱 ID와 시크릿 키를 직접 노출시키는 것은 보안상 좋지 않습니다. 따라서 환경 변수를 사용하여 민감한 정보를 보호해야 합니다.

이를 위해 `.env` 파일을 생성하고 아래와 같이 페이스북 앱 ID와 시크릿 키를 설정합니다. 파일 이름이 `.env`이므로 주의해주세요.

```
REACT_APP_FACEBOOK_APP_ID=YOUR_APP_ID
REACT_APP_FACEBOOK_APP_SECRET=YOUR_APP_SECRET
```

## 4. 연동 확인

이제 JavaScript 프로젝트에서 페이스북 연동을 사용할 수 있습니다. 예를 들어, 로그인 기능을 구현한다면 페이스북 SDK를 로드하고 페이스북 로그인 버튼을 추가할 수 있습니다. 자세한 연동 방법은 [페이스북 개발자 문서](https://developers.facebook.com/docs/javascript)에서 확인할 수 있습니다.

## 마무리

Package.json 파일을 통해 JavaScript 프로젝트에서의 페이스북 연동 설정을 쉽게 할 수 있습니다. 페이스북 API를 사용하여 다양한 기능을 구현하고 사용자 경험을 향상시킬 수 있습니다.