---
layout: post
title: "Package.json을 사용하여 JavaScript 프로젝트의 웹 소켓 설정하기"
description: " "
date: 2023-11-06
tags: [package]
comments: true
share: true
---

## 목차
- [개요](#개요)
- [package.json 파일 생성](#packagejson-파일-생성)
- [websocket 라이브러리 설치](#websocket-라이브러리-설치)
- [WebSocket 설정 추가](#websocket-설정-추가)
- [실행 및 테스트](#실행-및-테스트)
- [참고 자료](#참고-자료)

## 개요
JavaScript로 웹 소켓(WebSocket)을 사용하여 양방향 통신을 구현할 때, 프로젝트의 패키지 관리를 위해 package.json 파일을 사용하는 것이 일반적입니다. 이 글에서는 package.json 파일을 사용하여 JavaScript 프로젝트에 웹 소켓 설정을 추가하는 방법을 알아보겠습니다.

## package.json 파일 생성
우선, 프로젝트 폴더의 루트 디렉토리에 package.json 파일을 생성해야 합니다. 다음 명령어를 사용하여 package.json 파일을 생성할 수 있습니다:

```bash
npm init -y
```

위 명령어를 실행하면 기본적인 package.json 파일이 생성됩니다.

## websocket 라이브러리 설치
WebSocket을 사용하기 위해서는 먼저 해당 기능을 제공하는 라이브러리를 설치해야 합니다. 가장 인기 있는 WebSocket 라이브러리인 `ws`를 설치하기 위해 아래 명령어를 실행합니다:

```bash
npm install ws
```

위 명령어를 실행하면 `ws` 라이브러리가 프로젝트에 설치됩니다.

## WebSocket 설정 추가
package.json 파일을 열고, "dependencies" 항목 아래에 다음과 같이 "websocket" 항목을 추가해주세요:

```json
"dependencies": {
  "ws": "^8.0.0"
}
```

위 설정 코드에서 `"^8.0.0"`은 `ws` 라이브러리의 버전을 지정하는 부분으로, 버전은 필요에 따라 변경할 수 있습니다.

## 실행 및 테스트
이제 프로젝트를 실행하고 웹 소켓을 테스트할 준비가 되었습니다. 프로젝트에서 WebSocket을 사용하기 위해 필요한 작업을 진행하고, WebSocket 서버와 클라이언트 코드를 작성한 뒤 실행해보세요.

위 방법으로 WebSocket 설정을 추가하고 실행하면, JavaScript 프로젝트에서 웹 소켓을 이용한 양방향 통신을 구현할 수 있습니다.

## 참고 자료
- [npm 공식 문서](https://docs.npmjs.com/)
- [WebSocket API 문서](https://developer.mozilla.org/ko/docs/Web/API/WebSocket)
- [ws 라이브러리 GitHub 저장소](https://github.com/websockets/ws)