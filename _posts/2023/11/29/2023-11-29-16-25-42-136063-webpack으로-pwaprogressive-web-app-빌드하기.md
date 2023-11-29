---
layout: post
title: "[javascript] Webpack으로 PWA(Progressive Web App) 빌드하기"
description: " "
date: 2023-11-29
tags: [javascript]
comments: true
share: true
---

웹 개발에서 PWA(Progressive Web App)는 점점 더 중요해지고 있는 개념입니다. PWA는 모바일 앱처럼 동작하며, 사용자에게 앱을 다운로드하거나 설치할 필요 없이 웹 브라우저에서 바로 사용할 수 있는 혁신적인 기술입니다. 

이번 글에서는 PWA를 웹팩(Webpack)으로 빌드하는 방법을 알아보겠습니다. 웹팩은 모듈 번들러로, 여러 모듈을 가져와 하나의 번들로 묶어주는 역할을 합니다.

## 1. 프로젝트 설정

먼저 프로젝트를 생성하고 필요한 종속성을 설치해야 합니다. 아래의 명령어를 사용하여 프로젝트를 초기화하고 웹팩과 관련된 패키지를 설치합니다.

```bash
npm init -y
npm install webpack webpack-cli --save-dev
```

## 2. 웹팩 설정 파일 생성

다음으로, 프로젝트 루트 디렉토리에 웹팩 설정 파일(`webpack.config.js`)을 생성합니다. 이 설정 파일은 웹팩이 어떻게 동작해야 하는지 정의합니다.

```javascript
const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
};
```

위의 코드는 `./src/index.js` 파일을 진입점(entry)으로 설정하고, 번들된 파일 이름은 `bundle.js`로 설정하며, 번들된 파일이 저장될 경로는 `./dist`로 설정합니다.

## 3. Service Worker 구성

PWA를 구현하기 위해선 Service Worker를 사용해야 합니다. Service Worker는 백그라운드에서 작동되는 스크립트이며, 브라우저와의 통신을 처리하고 사용자 경험 개선에 필요한 기능을 제공합니다.

다음은 `sw.js`라는 파일을 생성하고, 아래의 코드를 추가합니다.

```javascript
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open('my-cache').then((cache) => {
      return cache.addAll([
        '/',
        '/index.html',
        '/styles.css',
        '/script.js',
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

위의 코드는 설치 이벤트(`install`)가 발생하면, 정적 파일들(`index.html`, `styles.css`, `script.js`)을 캐싱합니다. 그리고 `fetch` 이벤트가 발생하면, 캐시된 정적 파일이 있는 경우 해당 파일을 반환하고, 없는 경우 원본 서버에서 가져온 뒤 응답합니다.

## 4. 웹팩 빌드

이제 웹팩을 사용하여 프로젝트를 빌드할 차례입니다. 아래의 명령어를 실행하여 웹팩을 실행하고 번들 파일을 생성합니다.

```bash
npx webpack --mode production
```

위의 명령어에서 `--mode` 옵션은 프로덕션 모드로 웹팩을 실행하라는 의미입니다. 이를테면 압축된 번들 파일을 생성하거나, CSS 파일을 번들에 포함시킬 수 있습니다.

## 5. PWA 빌드 완료

이제 PWA를 웹팩으로 빌드한 후, 빌드된 파일을 웹 서버에 올리면 됩니다. 이를테면, [GitHub Pages](https://pages.github.com/)를 사용하여 간단히 배포할 수 있습니다.

이제 웹 브라우저에서 해당 URL로 이동하여 PWA를 확인할 수 있습니다.

## 결론

웹팩을 사용하여 PWA를 빌드하는 방법을 알아보았습니다. 웹팩은 모듈 번들링을 통해 여러 모듈을 하나의 번들로 묶어주는 역할을 담당하고, Service Worker를 이용하여 PWA의 핵심 기능을 구현할 수 있습니다. 결국, 웹팩을 통해 PWA를 빌드하여 사용자에게 좋은 웹 경험을 제공할 수 있습니다.