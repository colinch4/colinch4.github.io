---
layout: post
title: "npm 을 활용한 PWA 개발 (Progressive Web App development with npm)"
description: " "
date: 2023-11-10
tags: []
comments: true
share: true
---

![PWA](https://example.com/pwa-image.jpg)

프로그레시브 웹앱(PWA)은 모바일 앱과 웹사이트의 기능을 결합한 사용자 친화적인 경험을 제공합니다. PWA는 기존의 웹사이트와 달리 오프라인 상태에서도 작동하며, 사용자의 홈 화면에 아이콘을 추가할 수 있습니다. 이번 글에서는 npm(npm - Node Package Manager)을 활용하여 PWA를 개발하는 방법에 대해 알아보겠습니다.

## npm 설치 및 프로젝트 초기화
PWA 개발을 위해 먼저 npm을 설치해야 합니다. 노드(Node.js)를 설치하고 나면 npm도 함께 설치됩니다. 설치가 완료되면 터미널에서 `npm -v` 명령어로 버전을 확인할 수 있습니다.

새로운 PWA 프로젝트를 시작하려면 터미널에서 다음의 명령어를 실행하여 프로젝트 디렉토리를 초기화합니다:
```shell
npm init
```

## 필수 패키지 설치
PWA 개발에 필요한 몇 가지 npm 패키지가 있습니다. 이 중에서 가장 중요한 패키지는 `workbox`입니다. `workbox`는 PWA의 오프라인 캐싱과 관련된 서비스 워커를 생성하고 관리하는 데 사용됩니다.

다음의 명령어를 사용하여 `workbox` 패키지를 설치합니다:
```shell
npm install workbox --save-dev
```

## 서비스 워커 등록
PWA에서 가장 중요한 요소는 서비스 워커(Service Worker)입니다. 서비스 워커는 브라우저의 백그라운드에서 실행되는 스크립트로, 오프라인 상태에서도 동작하는 기능을 구현합니다.

서비스 워커를 등록하려면 프로젝트의 루트에 `sw.js`라는 파일을 생성하고, 다음의 코드를 작성합니다:
```javascript
// sw.js
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open('my-cache').then((cache) => {
      return cache.addAll([
        '/',
        '/index.html',
        '/styles/style.css',
        '/scripts/app.js',
      ]);
    })
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});
```

위의 코드에서는 `install` 이벤트에서 캐시를 생성하고 필요한 파일들을 캐싱합니다. `fetch` 이벤트에서는 서비스 워커가 요청을 가로채고 캐시에 저장된 자원이 있는지 확인한 후, 없을 경우 네트워크에서 가져오도록 처리합니다.

## 서비스 워커 등록하기
HTML 파일의 `<head>` 태그 안에 다음의 코드를 추가하여 서비스 워커를 등록합니다:
```html
<!-- index.html -->
<script>
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/sw.js')
        .then((registration) => {
          console.log('Service Worker 등록 성공:', registration.scope);
        })
        .catch((error) => {
          console.log('Service Worker 등록 실패:', error);
        });
    });
  }
</script>
```

위의 코드에서는 먼저 브라우저가 서비스 워커를 지원하는지 확인한 후, 지원하면 `sw.js` 파일을 등록합니다. 등록이 성공하면 콘솔에 메시지가 출력됩니다.

## PWA 배포
PWA를 배포하기 위해 정적 파일들을 빌드해야 합니다. 이를 위해 `workbox` 패키지를 이용할 수 있습니다.

새로운 명령어를 추가해 `package.json` 파일의 `scripts` 항목을 다음과 같이 수정합니다:
```json
{
  "scripts": {
    "start": "your-start-command",
    "build": "your-build-command",
    "precache": "workbox generateSW"
  },
  "dependencies": {
    ...
  },
  "devDependencies": {
    ...
  }
}
```

프로젝트 루트에서 다음의 명령어를 실행하여 PWA를 빌드하고 필요한 파일들을 캐싱합니다:
```shell
npm run precache
```

배포된 PWA를 웹서버에 호스팅하여 기기에 설치된 앱처럼 사용할 수 있습니다. 배포된 PWA에 접속하고 오프라인 상태에서도 정상적으로 작동하는지 확인해보세요.

## 마치며
이번 글에서는 npm을 활용하여 프로그레시브 웹앱(PWA)을 개발하는 방법에 대해 알아보았습니다. npm을 이용하면 필요한 패키지를 쉽게 설치하고 관리할 수 있으며, 서비스 워커를 통해 오프라인 상태에서도 웹앱을 사용할 수 있게 만들 수 있습니다.

더 많은 PWA 개발에 대한 정보는 다음 자료를 참고하세요:
- [PWA 개발 문서](https://developer.mozilla.org/ko/docs/Web/Progressive_web_apps)
- [Workbox 문서](https://developers.google.com/web/tools/workbox)

#PWA #npm