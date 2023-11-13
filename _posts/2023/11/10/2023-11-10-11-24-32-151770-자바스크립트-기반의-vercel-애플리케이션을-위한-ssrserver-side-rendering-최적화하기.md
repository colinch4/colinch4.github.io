---
layout: post
title: "자바스크립트 기반의 Vercel 애플리케이션을 위한 SSR(Server Side Rendering) 최적화하기"
description: " "
date: 2023-11-10
tags: [Vercel]
comments: true
share: true
---

## 서버 사이드 렌더링(SSR)의 이점

서버 사이드 렌더링(SSR)은 클라이언트 측에서 렌더링되는 전통적인 웹 애플리케이션과 달리, 서버에서 렌더링되어 클라이언트에게 전달되는 방식입니다. SSR은 여러 가지 이점을 제공합니다.

1. 검색 엔진 최적화(SEO): SSR은 웹 페이지 컨텐츠를 서버에서 생성하기 때문에 검색 엔진이 쉽게 페이지를 색인할 수 있습니다.
2. 초기 로딩 시간 최적화: SSR은 초기 렌더링을 서버에서 처리하기 때문에 사용자가 페이지를 더 빨리 볼 수 있습니다.
3. 더 나은 사용자 경험: SSR은 초기 페이지로드 이후에도 빠른 네비게이션 및 상호 작용을 제공하여 사용자 경험을 향상시킵니다.

## Vercel을 사용한 SSR 설정

Vercel은 간단하고 편리한 사용을 제공하는 서버리스 배포 플랫폼입니다. Vercel은 자체 SSR 설정을 지원하며, JavaScript 기반 애플리케이션에 대한 SSR 최적화를 수행하는 데 필요한 도구와 기능을 제공합니다.

1. **Vercel 프로젝트 생성**: Vercel 웹사이트에서 프로젝트를 생성하고 저장소에 연결합니다.

2. **Vercel 설정**: Vercel 설정 파일(vercel.json)에서 `functions` 섹션을 추가하고 SSR을 위한 함수 경로를 지정합니다.

    ```json
    {
      "functions": {
        "api/**/*.{ts,tsx}": {
          "runtime": "@vercel/node",
          "memory": 512
        }
      }
    }
    ```

3. **서버리스 함수 작성**: 서버리스 함수를 작성하여 SSR 로직을 구현합니다. 이 함수는 클라이언트 요청에 대한 렌더링된 페이지를 반환합니다. 예를 들어, 다음과 같은 함수를 작성할 수 있습니다.

    ```javascript
    import { renderToString } from 'react-dom/server';
    import App from './App';

    export default async function handler(req, res) {
      const appHtml = renderToString(<App />);
      const html = `
        <!DOCTYPE html>
        <html>
        <head>
          <title>My SSR App</title>
        </head>
        <body>
          <div id="root">${appHtml}</div>
        </body>
        </html>
      `;
      res.setHeader('Content-Type', 'text/html');
      res.status(200).send(html);
    }
    ```

4. **Vercel로 배포**: Vercel CLI 또는 Vercel 웹사이트를 통해 애플리케이션을 배포합니다.

## SSR 최적화 팁

SSR을 사용하면 애플리케이션 성능과 사용자 경험을 향상시킬 수 있습니다. 다음은 SSR을 최적화하는 몇 가지 팁입니다.

1. **캐싱 활용**: SSR은 동적으로 페이지를 생성하므로 매 요청마다 렌더링하는 것은 비효율적입니다. 렌더링 결과를 캐싱하여 불필요한 렌더링을 피할 수 있습니다.

2. **비동기 데이터 로딩**: SSR을 통해 페이지를 서버에서 렌더링할 때, 필요한 데이터를 비동기적으로 불러올 수 있습니다. 이를 통해 초기 로딩 속도를 향상시킬 수 있습니다.

3. **번들 최적화**: SSR 애플리케이션의 번들 사이즈를 최적화하는 것은 성능 향상에 중요합니다. 필요한 모듈만 번들에 포함시키고, 코드 스플리팅과 같은 기법을 사용하여 필요한 모듈을 지연 로딩할 수 있습니다.

SSR은 JavaScript 기반 애플리케이션을 최적화하는 데 매우 유용한 기술입니다. Vercel을 사용하면 간단하게 SSR을 구현하고 최적화할 수 있습니다. 이러한 SSR 최적화 팁을 적용하여 애플리케이션의 성능을 향상시키고 사용자 경험을 개선해보세요.

**참고 문서**: [Vercel 공식 문서](https://vercel.com/docs/serverless-functions/introduction)