---
layout: post
title: "[javascript] Next.js에서의 디자인 토큰(PDS, Pattern Design System) 사용 방법은 어떤 것이 있나요?"
description: " "
date: 2023-11-24
tags: [javascript]
comments: true
share: true
---

Next.js는 React 기반의 프레임워크로, 디자인 토큰(PDS, Pattern Design System)을 사용하여 일관된 디자인을 구현할 수 있습니다. PDS는 스타일, 컴포넌트, 레이아웃 등과 같은 디자인 요소를 일관되게 관리하는 시스템입니다.

PDS를 Next.js 프로젝트에 적용하는 방법에는 여러 가지가 있습니다. 간단한 예제 코드를 통해 설명해보겠습니다.

1. 디자인 토큰 작성하기

가장 먼저, 디자인 토큰을 작성해야 합니다. 이는 PDS를 적용하고자 하는 스타일과 컴포넌트에 대한 속성들을 정의한 것입니다. 예를 들어, `colors.js`라는 파일에 다음과 같은 코드를 작성할 수 있습니다.

```javascript
const colors = {
  primary: '#FF0000',
  secondary: '#00FF00',
  // 추가적인 디자인 토큰들...
};

export default colors;
```

2. 스타일 적용하기

디자인 토큰을 작성한 후, 해당 스타일을 사용하고자 하는 컴포넌트에 적용할 수 있습니다. 예를 들어, `Button` 컴포넌트에 `colors.js`에서 정의한 `primary` 색상을 적용하려면 다음과 같이 작성할 수 있습니다.

```javascript
{% raw %}
import React from 'react';
import colors from './colors';

const Button = () => {
  return (
    <button style={{ backgroundColor: colors.primary }}>Click me</button>
  );
};

export default Button;
{% endraw %}
```

3. 컴포넌트 사용하기

적용한 스타일을 가진 컴포넌트를 다른 곳에서 사용할 수 있습니다. 예를 들어, `App` 컴포넌트에서 `Button` 컴포넌트를 사용하려면 다음과 같이 작성할 수 있습니다.

```javascript
import React from 'react';
import Button from './Button';

const App = () => {
  return (
    <div>
      <h1>Welcome to my Next.js app</h1>
      <Button />
    </div>
  );
};

export default App;
```

위와 같이 설정하면, `Button` 컴포넌트는 `colors.js`에서 정의한 `primary` 색상을 가지게 됩니다.

Next.js에서의 PDS(Pattern Design System) 사용 방법에 대해 예시를 통해 설명해 보았습니다. PDS를 통해 일관된 디자인을 유지하고 개발 생산성을 높일 수 있습니다.

참고자료:
- Next.js 공식 문서: [https://nextjs.org/](https://nextjs.org/)
- React 공식 문서: [https://reactjs.org/](https://reactjs.org/)