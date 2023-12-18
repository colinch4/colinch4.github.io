---
layout: post
title: "[javascript] Nuxt.js에서의 CSS 프레임워크(Vuetify, Bulma 등) 사용 방법은?"
description: " "
date: 2023-12-19
tags: [javascript]
comments: true
share: true
---

**Vuetify를 Nuxt.js에서 사용하는 방법:**

1. 먼저, Nuxt.js 프로젝트를 생성합니다.
2. 다음으로, Vuetify를 설치합니다.
    ```shell
    npm install vuetify
    ```
3. Nuxt.js 설정 파일(nuxt.config.js)에서 다음과 같이 Vuetify 플러그인을 등록합니다.
    ```javascript
    // nuxt.config.js
    export default {
      buildModules: [
        '@nuxtjs/vuetify'
      ],
      vuetify: {
        /* Vuetify 옵션 설정 */
      }
    }
    ```
4. 이제 Vuetify를 사용하여 컴포넌트를 만들고 스타일링할 수 있습니다.

**Bulma를 Nuxt.js에서 사용하는 방법:**

1. 먼저, Nuxt.js 프로젝트를 생성합니다.
2. 다음으로, Bulma를 설치합니다.
    ```shell
    npm install bulma
    ```
3. Nuxt.js 설정 파일(nuxt.config.js)에서 다음과 같이 Bulma CSS 파일을 추가합니다.
    ```javascript
    // nuxt.config.js
    export default {
      css: [
        'bulma/css/bulma.css'
      ]
    }
    ```
4. 이제 Bulma를 사용하여 컴포넌트를 만들고 스타일링할 수 있습니다.

이제, Vuetify 또는 Bulma를 사용하여 Nuxt.js 애플리케이션을 개발할 수 있게 되었습니다. 각 CSS 프레임워크의 공식 문서 및 예제를 참고하여 보다 전문적으로 스타일링할 수 있습니다.

참고 자료:
- Vuetify 공식 문서: [https://vuetifyjs.com](https://vuetifyjs.com)
- Bulma 공식 문서: [https://bulma.io](https://bulma.io)