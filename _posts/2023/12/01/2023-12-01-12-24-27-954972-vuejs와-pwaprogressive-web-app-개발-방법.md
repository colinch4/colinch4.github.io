---
layout: post
title: "[javascript] Vue.js와 PWA(Progressive Web App) 개발 방법"
description: " "
date: 2023-12-01
tags: [javascript]
comments: true
share: true
---

## 목차
- [Vue.js 소개](#vuejs-소개)
- [PWA란?](#pwa란)
- [Vue.js와 PWA 개발 방법](#vuejs와-pwa-개발-방법)
  - [Vue CLI 설치](#vue-cli-설치)
  - [PWA 설정](#pwa-설정)
  - [Service Worker 등록](#service-worker-등록)
- [결론](#결론)

## Vue.js 소개 <a id="vuejs-소개"></a>
Vue.js는 사용자 인터페이스를 구축하기 위한 자바스크립트 프레임워크입니다. 가볍고 유연한 구조로 간단한 웹 페이지부터 복잡한 웹 애플리케이션까지 다양한 프로젝트에 사용됩니다. Vue.js는 MVVM(Model-View-ViewModel) 패턴을 기반으로 하며, 데이터와 뷰를 쉽게 바인딩하여 화면을 업데이트하는 것을 도와줍니다.

## PWA란? <a id="pwa란"></a>
Progressive Web App(PWA)는 웹과 네이티브 앱의 장점을 결합한 형태의 웹 애플리케이션입니다. PWA는 웹 기술을 사용하여 오프라인 상태에서도 작동하고, 앱 아이콘을 설치하고 알림을 받는 등 네이티브 앱과 유사한 경험을 제공합니다.

## Vue.js와 PWA 개발 방법 <a id="vuejs와-pwa-개발-방법"></a>

### Vue CLI 설치 <a id="vue-cli-설치"></a>
Vue CLI는 Vue.js 프로젝트를 생성하고 관리하기 위한 도구입니다. 다음 명령어를 사용하여 Vue CLI를 설치합니다:

```javascript
npm install -g @vue/cli
```

### PWA 설정 <a id="pwa-설정"></a>
Vue CLI로 생성한 프로젝트에서 PWA를 사용하도록 설정해야 합니다. 프로젝트 루트 디렉토리에서 다음 명령어를 실행합니다:

```javascript
vue add @vue/pwa
```

명령어를 실행하면 PWA Plugin이 설치되고 자동으로 PWA 설정 파일이 생성됩니다.

### Service Worker 등록 <a id="service-worker-등록"></a>
PWA는 Service Worker를 사용하여 오프라인 상태에서 작동하는 기능을 제공합니다. Service Worker는 브라우저의 백그라운드에서 실행되며, 웹 페이지와 상호작용하여 네트워크 요청을 가로채고 캐싱하는 등의 역할을 수행합니다.

Vue CLI로 생성한 프로젝트에는 이미 기본 Service Worker 파일이 포함되어 있습니다. 프로젝트 루트의 `src` 폴더에 있는 `service-worker.js` 파일에서 Service Worker를 커스터마이징할 수 있습니다.

Service Worker를 등록하려면 `main.js` 파일에 다음 코드를 추가합니다:

```javascript
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/service-worker.js')
    .then(function(registration) {
      console.log('Service Worker registered with scope:', registration.scope);
    }).catch(function(error) {
      console.log('Service Worker registration failed:', error);
    });
}
```

이제 프로젝트를 빌드하고 서버에 배포하면 Vue.js로 개발한 PWA가 완성됩니다.

## 결론 <a id="결론"></a>
Vue.js와 PWA는 웹 애플리케이션 개발에 새로운 가능성을 열어주는 기술입니다. Vue CLI를 사용하여 Vue.js 프로젝트를 생성한 후 PWA 설정을 추가하여 간단하게 PWA를 개발할 수 있습니다. Service Worker를 등록하여 오프라인 상태에서도 사용자에게 원활한 경험을 제공할 수 있습니다.

## 참고 자료
- [Vue.js 공식 사이트](https://vuejs.org/)
- [Vue CLI 공식 사이트](https://cli.vuejs.org/)
- [PWA(Portland Web App) 공식 사이트](https://web.dev/progressive-web-apps/)