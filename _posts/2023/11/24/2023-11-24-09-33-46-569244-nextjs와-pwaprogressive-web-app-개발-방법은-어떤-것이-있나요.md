---
layout: post
title: "[javascript] Next.js와 PWA(Progressive Web App) 개발 방법은 어떤 것이 있나요?"
description: " "
date: 2023-11-24
tags: [javascript]
comments: true
share: true
---

# Next.js와 PWA(Progressive Web App) 개발 방법

## 개요
Next.js는 React 기반의 프레임워크로, 서버 사이드 렌더링과 정적 파일 생성 등의 기능을 제공합니다. PWA는 웹 앱을 모바일 앱과 유사한 경험을 제공하는 방식으로 개발하는 방법입니다. Next.js와 PWA를 함께 사용하는 방법을 알아보겠습니다.

## 1. Manifest 파일 생성
PWA를 구현하기 위해 먼저 Manifest 파일을 생성해야 합니다. Manifest 파일은 웹 앱의 외부 링크를 지정하고, 아이콘과 앱 이름 등의 정보를 제공합니다. Manifest 파일은 `public` 폴더에 저장되어야 합니다.

```javascript
// public/manifest.json

{
  "name": "My Next.js PWA",
  "short_name": "NextPWA",
  "start_url": "/",
  "display": "standalone",
  "theme_color": "#ffffff",
  "background_color": "#ffffff",
  "icons": [
    {
      "src": "/android-chrome-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/android-chrome-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
```

## 2. Service Worker 설정
Service Worker는 PWA를 오프라인에서 작동할 수 있도록 도와주는 JavaScript 파일입니다. Next.js에서는 `next-offline` 패키지를 사용하여 Service Worker를 설정할 수 있습니다.

```shell
npm install @zeit/next-offline
```

```javascript
// next.config.js

const withOffline = require('next-offline')

module.exports = withOffline({
  /* next-offline configuration options here */
})
```

## 3. PWA 설정 추가
`withOffline` 설정을 추가한 후, `next.config.js` 파일을 수정하여 PWA 관련 설정을 추가해야 합니다.

```javascript
// next.config.js

module.exports = {
  /* Next.js configuration options here */

  pwa: {
    dest: 'public',
    runtimeCaching: [
      {
        urlPattern: /^https?.*/,
        handler: 'NetworkFirst',
        options: {
          cacheName: 'offlineCache',
          expiration: {
            maxEntries: 200
          }
        }
      }
    ]
  }
}
```

## 4. PWA 메타 태그 추가
`<head>` 태그 내에 PWA와 관련된 메타 태그를 추가해야 합니다.

```javascript
// pages/_document.js

import Document, { Html, Head, Main, NextScript } from 'next/document'

class MyDocument extends Document {
  render() {
    return (
      <Html>
        <Head>
          <meta name="viewport" content="width=device-width, initial-scale=1" />
          <link rel="manifest" href="/manifest.json" />
          <meta name="theme-color" content="#ffffff" />
        </Head>
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    )
  }
}

export default MyDocument
```

## 5. 프로덕션 빌드 및 실행
위 단계까지 완료했다면, 다음 명령어를 사용하여 Next.js 앱을 프로덕션 빌드하고 실행할 수 있습니다.

```shell
npm run build
npm start
```

이제 Next.js 앱은 PWA로 작동하며, 사용자는 오프라인에서 앱을 사용할 수 있습니다.

## 결론
Next.js와 PWA를 함께 사용하여 웹 앱을 개발하는 방법을 살펴보았습니다. 이를 통해 사용자는 오프라인에서 앱을 사용할 수 있으며, 웹 앱과 모바일 앱의 경험을 융합할 수 있습니다. 자세한 내용은 [Next.js 공식 문서](https://nextjs.org/docs)와 [PWA 공식 문서](https://developers.google.com/web/progressive-web-apps)를 참고하시기 바랍니다.