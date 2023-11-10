---
layout: post
title: "Package.json 설정을 활용한 JavaScript 프로젝트의 CORS 설정"
description: " "
date: 2023-11-06
tags: [Package]
comments: true
share: true
---

CORS (Cross-Origin Resource Sharing)는 웹 애플리케이션에서 다른 도메인에서 리소스를 요청할 수 있도록 하는 메커니즘입니다. JavaScript 프로젝트에서 CORS를 설정하는 방법 중 하나는 package.json 파일을 사용하는 것입니다. 이를 통해 간편하게 CORS를 구성할 수 있습니다.

## package.json 파일 수정

package.json 파일을 열고 "scripts" 섹션에 "start" 스크립트를 찾습니다. 일반적으로 이 스크립트는 프로젝트를 실행하는 데 사용됩니다. 해당 줄에 `--open` 플래그를 추가하여 개발 서버를 열 때 CORS를 활성화할 수 있습니다. 아래 예시를 참고하세요.

```json
"scripts": {
  "start": "react-scripts start --open"
}
```

위의 예시는 React 프로젝트를 기준으로 작성되었습니다. 다른 프레임워크나 라이브러리를 사용하는 경우 해당 스크립트에 맞게 수정하면 됩니다.

## CORS 설정 확인

개발 서버를 다시 실행하고 브라우저에서 프로젝트를 로드합니다. 개발 도구의 Network 탭을 열고 리소스 요청을 확인합니다. 요청 헤더에 "Access-Control-Allow-Origin"이 포함되어 있으면 CORS가 정상적으로 설정된 것입니다.

### Reference

- [Create React App - Integrating with an API Backend](https://create-react-app.dev/docs/proxying-api-requests-in-development/#configuring-the-proxy-manually)