---
layout: post
title: "[react] 생명주기 메서드 중 shouldComponentUpdate를 사용하는 이유는 무엇인가요?"
description: " "
date: 2023-12-22
tags: [react]
comments: true
share: true
---

컴포넌트가 다시 렌더링되기 전에 shouldComponentUpdate를 통해 현재 프롭스와 상태를 이전 프롭스와 상태와 비교하여 실제로 변경이 있는지를 판단할 수 있습니다. 변경이 없는 경우에는 불필요한 렌더링을 방지하여 성능을 향상시킬 수 있습니다.

따라서 shouldComponentUpdate를 사용하여 업데이트가 필요한 경우에만 렌더링되도록 설정함으로써 컴포넌트의 성능을 최적화할 수 있습니다.

```jsx
shouldComponentUpdate(nextProps, nextState) {
  // 현재 프롭스와 상태와 다음 프롭스와 상태를 비교하여 업데이트 필요 여부 판단
  // true를 반환하면 렌더링, false를 반환하면 렌더링하지 않음
}
```

더 자세한 내용은 React 공식 문서의 "shouldComponentUpdate()" 섹션을 참고할 수 있습니다. [React 공식 문서 - shouldComponentUpdate()](https://ko.reactjs.org/docs/react-component.html#shouldcomponentupdate)