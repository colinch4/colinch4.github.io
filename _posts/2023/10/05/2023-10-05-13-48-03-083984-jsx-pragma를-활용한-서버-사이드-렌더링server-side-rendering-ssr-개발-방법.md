---
layout: post
title: "JSX pragma를 활용한 서버 사이드 렌더링(Server-Side Rendering, SSR) 개발 방법"
description: " "
date: 2023-10-05
tags: []
comments: true
share: true
---

서버 사이드 렌더링(Server-Side Rendering, SSR)은 웹 애플리케이션의 성능과 검색 엔진 최적화를 개선하기 위해 사용되는 기술입니다. SSR은 서버에서 웹 페이지의 초기 렌더링을 수행하여 완전한 HTML을 클라이언트로 보내고, 이후 클라이언트 측에서는 JavaScript를 사용하여 상호작용을 추가하는 방식입니다. JSX pragma를 사용하여 서버 사이드 렌더링을 개발하는 방법에 대해 알아보겠습니다.

## 1. Babel 설정을 통해 JSX pragma 설정하기

첫 번째 단계는 Babel 설정을 통해 JSX pragma를 설정하는 것입니다. JSX pragma란 React 컴포넌트를 렌더링하기 위해 사용할 함수를 지정하는 것을 말합니다.

Babel 설정 파일인 `.babelrc` 또는 `babel.config.js` 파일에서 다음과 같이 `pragma` 속성을 추가합니다:

```javascript
{
  "presets": [
    ["@babel/preset-env", {
      "targets": {
        "node": "current"
      }
    }],
    "@babel/preset-react"
  ],
  "plugins": [
    ["@babel/plugin-transform-react-jsx", {
      "pragma": "customCreateElement"
    }]
  ]
}
```

위의 예제에서는 `customCreateElement`라는 함수를 JSX pragma로 지정하고 있습니다. JSX pragma 함수는 React 컴포넌트의 createElement 함수 역할을 수행합니다. 

## 2. JSX pragma 함수 구현하기

다음으로, JSX pragma 함수를 구현해야 합니다. 이 함수는 React 컴포넌트를 렌더링하는 역할을 합니다. 예를 들어, 다음과 같이 JSX pragma 함수를 작성할 수 있습니다:

```javascript
function customCreateElement(component, props, ...children) {
  // 컴포넌트와 props를 사용하여 서버에서 HTML을 생성하는 로직을 작성
  // ...

  // 생성된 HTML 반환
  return html;
}
```

위의 예제에서는 `customCreateElement` 함수가 컴포넌트, props 및 자식 요소를 사용하여 서버에서 HTML을 생성하는 로직을 작성하도록 구현되어 있습니다.

## 3. 서버에서 JSX pragma 사용하기

서버에서 JSX pragma를 사용하는 방법은 다음과 같습니다. 예를 들어, Node.js에서 Express와 함께 사용한다고 가정해봅시다:

```javascript
import React from 'react';
import { renderToString } from 'react-dom/server';
import App from './App';

app.get('/', (req, res) => {
  const html = renderToString(<App />); // JSX pragma 함수(customCreateElement)를 사용한 렌더링

  res.send(html);
});
```

위의 예제에서는 Express 앱의 `/` 경로로 GET 요청이 오면, JSX pragma 함수를 사용하여 `App` 컴포넌트를 문자열로 변환하고 이를 클라이언트에 반환합니다.

## 4. 클라이언트에서 JavaScript로 상호작용 추가하기

서버에서 초기 렌더링을 처리할 때 이미 서버에서 생성된 HTML을 사용하기 때문에 클라이언트 측에서는 JavaScript로 추가적인 상호작용을 구현할 수 있습니다. 이를 위해, 클라이언트에서 React 컴포넌트를 다시 렌더링하는 방법을 이해해야 합니다.

```javascript
import React from 'react';
import { hydrate } from 'react-dom';
import App from './App';

hydrate(<App />, document.getElementById('root')); // 클라이언트에서 초기 렌더링을 위해 hydrate 함수 사용
```

위의 예제에서는 `hydrate` 함수를 사용하여 클라이언트 측에서 초기 렌더링을 처리합니다. 이 함수는 서버에서 생성된 HTML과 클라이언트에서 생성된 HTML을 일치시키기 위해 사용됩니다.

## 마무리

JSX pragma를 활용한 서버 사이드 렌더링(SSR)은 웹 애플리케이션의 성능을 개선하고 검색 엔진 최적화를 향상시킬 수 있는 강력한 기술입니다. 이번 글에서는 JSX pragma를 설정하고 서버에서 사용하는 방법을 알아보았습니다. SSR은 복잡한 웹 애플리케이션에서 특히 유용하며, 이를 통해 사용자 경험을 개선할 수 있습니다.

#React #SSR