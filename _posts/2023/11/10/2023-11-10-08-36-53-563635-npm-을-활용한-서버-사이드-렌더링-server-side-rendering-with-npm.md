---
layout: post
title: "npm 을 활용한 서버 사이드 렌더링 (Server-side rendering with npm)"
description: " "
date: 2023-11-10
tags: [npm]
comments: true
share: true
---

서버 사이드 렌더링은 프론트엔드 개발에서 매우 중요한 부분이다. 사용자가 웹 페이지에 접속할 때, 동적으로 데이터를 가져와서 렌더링하여 보여주는 것은 사용자 경험을 향상시키는데 도움을 준다. 이를 위해 npm을 활용한 서버 사이드 렌더링 기술을 소개하고자 한다.

## 서버 사이드 렌더링이란?

서버 사이드 렌더링은 클라이언트 사이드 렌더링과 대조적으로 서버에서 웹 페이지를 완전히 렌더링한 후에 클라이언트에게 전달하는 방식이다. 이렇게 서버에서 웹 페이지를 렌더링하는 것은 여러 가지 이점을 제공한다. 첫째, 검색 엔진 최적화를 향상시킬 수 있다. 검색 엔진은 웹 페이지의 내용을 이해하고 지수화하기 위해 HTML의 정적인 내용을 분석하는데, 클라이언트 사이드 렌더링 방식을 사용하면 검색 엔진이 정확한 정보를 수집하지 못할 수 있다. 둘째, 초기 로딩 시간을 줄일 수 있다. 서버 사이드 렌더링을 사용하면 사용자가 웹 페이지에 접속할 때 초기 렌더링이 이미 완료되어 있는 상태이기 때문에 화면이 빠르게 표시된다. 

## npm을 사용한 서버 사이드 렌더링

npm은 Node.js 프로젝트의 의존성 관리를 위한 패키지 매니저이다. npm을 사용하여 서버 사이드 렌더링을 구현하는 것은 상대적으로 간단하다. 다음은 npm을 사용하여 서버 사이드 렌더링을 하는 간단한 예제 코드이다.

```javascript
const express = require('express');
const ReactDOMServer = require('react-dom/server');
const App = require('./App');

const app = express();

app.get('/', (req, res) => {
  const html = ReactDOMServer.renderToString(<App />);
  res.send(html);
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

위의 예제 코드에서는 `express`와 `react-dom/server` 패키지를 사용하고 있다. `express`는 Node.js 기반의 웹 프레임워크로, 간단한 웹 서버를 생성하는 데 사용된다. `react-dom/server`는 React 애플리케이션을 서버 사이드에서 렌더링하기 위한 모듈이다. `App`은 렌더링할 React 컴포넌트를 의미한다.

이 예제 코드는 루트 경로(`/`)로 접속했을 때, `App` 컴포넌트를 렌더링하여 결과를 HTML 문자열로 변환하고, 이를 응답으로 보내는 간단한 서버를 생성한다.

## 결론

서버 사이드 렌더링은 웹 애플리케이션의 성능과 검색 엔진 최적화를 향상시키는데 도움이 되는 중요한 기술이다. npm을 활용하여 간단하게 서버 사이드 렌더링을 구현할 수 있다. 따라서, 프론트엔드 개발자는 서버 사이드 렌더링에 대한 이해와 활용을 고려해야 한다.

> 참고 자료:
> - Express - https://expressjs.com/
> - React - https://reactjs.org/
> - ReactDOMServer - https://reactjs.org/docs/react-dom-server.html

#tech #frontend