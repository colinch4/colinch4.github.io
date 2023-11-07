---
layout: post
title: "Suspense를 사용하여 코드 스플리팅(Code splitting)을하는 방법은?"
description: " "
date: 2023-11-07
tags: []
comments: true
share: true
---

1. 동적으로 로딩할 컴포넌트를 선택합니다. 예를 들어, `import` 문을 사용하여 로드해야 할 컴포넌트를 가져옵니다.

```jsx
const MyComponent = React.lazy(() => import('./MyComponent'));
```

2. Suspense 컴포넌트를 사용하여 로딩 상태를 관리합니다. Suspense 컴포넌트는 로딩 중일 때 표시할 fallback 컴포넌트를 설정할 수 있습니다.

```jsx
function App() {
  return (
    <div>
      <Suspense fallback={<div>Loading...</div>}>
        <MyComponent />
      </Suspense>
    </div>
  );
}
```

3. 코드를 번들링하여 사용할 때 로딩 시간을 최적화합니다. 웹팩(Webpack)의 경우, `optimization.splitChunks` 속성을 사용하여 번들을 자동으로 분할할 수 있습니다. 다음 예제는 웹팩 설정 파일에 `splitChunks`를 사용하는 방법입니다.

```javascript
module.exports = {
  // ...

  optimization: {
    splitChunks: {
      chunks: 'all',
    },
  },
};
```

위의 단계를 따르면, Suspense를 사용하여 코드 스플리팅을 구현할 수 있습니다. 컴포넌트가 사용되는 시점에서 해당 컴포넌트가 동적으로 로드되고, 로딩 중일 때는 fallback 컴포넌트를 표시합니다. 이를 통해 초기 번들 크기를 줄이고 웹 애플리케이션의 성능을 향상시킬 수 있습니다.

참고 자료:
- React 공식 문서: [Code-Splitting](https://ko.reactjs.org/docs/code-splitting.html)
- Webpack 공식 문서: [Code Splitting](https://webpack.js.org/guides/code-splitting/)