---
layout: post
title: "[javascript] Parcel에서 Styled-Components를 사용하는 방법은?"
description: " "
date: 2023-11-22
tags: [javascript]
comments: true
share: true
---

Styled-Components는 React 애플리케이션에서 스타일링을 위해 널리 사용되는 라이브러리입니다. 이 글에서는 Parcel 번들러를 사용하여 Styled-Components를 설정하는 방법을 알아보겠습니다.

## 1. 프로젝트 설정

먼저, 프로젝트 디렉토리에서 다음 명령을 사용하여 Parcel을 설치합니다:

```bash
npm install --save-dev parcel-bundler
```

그리고 `index.html` 파일을 생성하고 다음 내용을 추가합니다:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Parcel + Styled-Components</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="./index.js"></script>
  </body>
</html>
```

## 2. React 및 Styled-Components 설치

다음으로 React와 Styled-Components를 설치합니다:

```bash
npm install react react-dom styled-components
```

## 3. React 애플리케이션 생성

`src` 디렉토리에 `App.js` 파일을 생성하고 다음 내용을 추가합니다:

```javascript
import React from "react";
import styled from "styled-components";

const StyledHeading = styled.h1`
  color: blue;
`;

const App = () => {
  return <StyledHeading>Hello, Styled-Components!</StyledHeading>;
};

export default App;
```

## 4. Parcel 설정

프로젝트 루트 디렉토리에 `index.js` 파일을 생성하고 다음 내용을 추가합니다:

```javascript
import React from "react";
import ReactDOM from "react-dom";
import App from "./src/App";

ReactDOM.render(<App />, document.getElementById("root"));
```

그리고 `package.json` 파일을 열고 `scripts` 섹션에 다음 내용을 추가합니다:

```json
"scripts": {
  "start": "parcel index.html"
}
```

## 5. 애플리케이션 실행

터미널에서 다음 명령을 실행하여 애플리케이션을 실행합니다:

```bash
npm start
```

Parcel은 `src` 폴더의 `index.js` 파일을 번들링하고 개발 서버를 실행하여 애플리케이션을 자동으로 업데이트합니다. 브라우저에서 `http://localhost:1234`로 이동하면 `Hello, Styled-Components!`를 볼 수 있습니다.

## 결론

이제 Parcel과 Styled-Components를 함께 사용하는 방법을 알게 되었습니다. 이러한 조합을 사용하면 효율적이고 유연한 방식으로 React 애플리케이션을 스타일링할 수 있습니다. 자유롭게 다양한 스타일을 실험해보고 컴포넌트를 더욱 재사용 가능하게 만들기 위해 Styled-Components의 다양한 기능을 활용해보세요.

---

## 참고 자료

- [Styled-Components 공식 문서](https://styled-components.com/)
- [Parcel 공식 문서](https://parceljs.org/)