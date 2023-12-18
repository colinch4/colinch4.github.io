---
layout: post
title: "[nodejs] SSR과 Client-side Rendering의 차이"
description: " "
date: 2023-12-19
tags: [nodejs]
comments: true
share: true
---

웹 개발에서 **Server-side Rendering(SSR)**과 **Client-side Rendering(CSR)**은 두 가지 주요한 방법론으로, 사용자에게 동적으로 생성된 콘텐츠를 제공하는 데 사용됩니다.

### Server-side Rendering(SSR)

**Server-side Rendering(SSR)**은 서버에서 완전한 HTML 페이지를 생성하여 클라이언트에게 전달하는 방식입니다. 서버에서 사용자의 요청에 따라 HTML 내용을 동적으로 렌더링하고 클라이언트에 제공합니다. 사용자가 웹 페이지를 요청할 때마다 새로운 HTML을 생성하므로 초기 로딩 속도는 느릴 수 있지만, 검색 엔진 최적화(SEO)에 유리합니다.

### Client-side Rendering(CSR)

**Client-side Rendering(CSR)**은 초기 페이지 로드시에 기본적인 HTML과 자바스크립트 파일만을 제공하고, 자바스크립트 파일을 통해 브라우저에서 동적으로 콘텐츠를 렌더링하는 방식입니다. 초기 로딩 시간이 빠르고, 웹 애플리케이션의 성능을 향상시킬 수 있지만, SEO 측면에서는 추가적인 대응이 필요합니다.

### SSR과 CSR의 차이

SSR과 CSR의 주요 차이점은, 페이지가 서버 측에서 렌더링되는지 클라이언트 측에서 렌더링되는지에 있습니다. **SSR**은 초기 로딩 시간이 느릴 수 있지만, 검색 엔진 최적화에 유리하고, **CSR**은 초기 로딩 시간이 빠르지만, SEO에 제약이 있을 수 있습니다.

물론, SSR과 CSR을 혼합하여 사용할 수도 있으며, 이는 "Hybrid Rendering"이라고도 불립니다.

따라서, 프로젝트의 성격과 요구사항에 따라 SSR과 CSR 중 어떤 방법을 채택할지 결정해야 합니다.

## 참고 자료

- Google Developers - [구글에서 쓸모있는 인덱스 가능한 페이지 만들기](https://developers.google.com/search/docs/advanced/guidelines/make-pwa-indexable)
- Vue.js 공식 문서 - [서버 사이드 렌더링(SSR)](https://ssr.vuejs.org/)
- React 공식 문서 - [서버 사이드 렌더링(SSR)](https://reactjs.org/docs/react-dom-server.html)