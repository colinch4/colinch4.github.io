---
layout: post
title: "React.forwardRef()를 사용하여 SSR과 CSR을 함께 지원하는 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: []
comments: true
share: true
---

React.forwardRef()는 React 컴포넌트에서 ref를 전달하기 위해 사용되는 함수입니다. 이 함수를 사용하면 Server Side Rendering(SSR) 및 Client Side Rendering(CSR)을 함께 지원하는 방법을 구현할 수 있습니다.

## SSR과 CSR의 차이점

SSR은 서버에서 초기 렌더링을 수행하고 클라이언트에 HTML을 반환하는 방식입니다. 이에 반해, CSR은 클라이언트에서 JavaScript를 이용하여 동적으로 컴포넌트를 렌더링하는 방식입니다.

SSR의 장점은 초기 로딩 시간을 단축하고 검색 엔진 최적화(SEO)를 향상시킬 수 있다는 것입니다. 하지만 CSR은 보다 동적이고 대화형인 사용자 경험을 제공할 수 있습니다.

## React.forwardRef()를 사용한 방법

React.forwardRef()는 ref를 통해 하위 컴포넌트에 접근할 수 있도록 해줍니다. SSR과 CSR을 함께 지원하기 위해서는 다음과 같은 방법을 사용할 수 있습니다:

1. 공통된 로직을 갖는 컴포넌트를 작성합니다.
2. React.forwardRef() 함수를 사용하여 ref를 전달할 수 있는 Wrapper 컴포넌트를 작성합니다.
3. 해당 Wrapper 컴포넌트를 SSR 및 CSR 시에 사용하도록 설정합니다.

```jsx
import React, { forwardRef } from 'react';

// 공통된 로직을 갖는 컴포넌트
const CommonComponent = forwardRef((props, ref) => {
  // ref를 사용하여 하위 컴포넌트에 접근할 수 있도록 함
  return <div ref={ref}>Hello World</div>;
});

// SSR 및 CSR 시에 사용될 Wrapper 컴포넌트
const WrapperComponent = (props) => {
  // ref를 전달하기 위해 빈 객체를 생성
  const ref = React.createRef();

  if (typeof window !== 'undefined') {
    // CSR 시에만 ref를 할당
    props.innerRef.current = ref.current;
  }

  return <CommonComponent ref={ref} />;
};

// SSR 및 CSR 시에 사용할 ref 변수
const ref = { current: null };

// SSR 및 CSR 시에 사용할 컴포넌트 렌더링
ReactDOM.render(<WrapperComponent innerRef={ref} />, document.getElementById('root'));
```

위의 예제 코드에서는 CommonComponent라는 공통된 로직을 갖는 컴포넌트를 작성하고, WrapperComponent라는 Wrapper 컴포넌트를 만들어 React.forwardRef()를 사용하여 ref를 전달하고 있습니다. WrapperComponent는 SSR 및 CSR 시에 사용되며, innerRef를 통해 ref 접근이 가능합니다.

이렇게 구현하면 SSR과 CSR을 함께 지원할 수 있으며, ref를 통해 하위 컴포넌트에 접근할 수 있습니다.

## 결론

React.forwardRef()를 사용하여 SSR과 CSR을 함께 지원하는 방법을 알아보았습니다. 공통된 로직을 갖는 컴포넌트를 작성하고, React.forwardRef()를 사용하여 ref를 전달하고 Wrapper 컴포넌트를 생성하는 것으로 SSR과 CSR을 함께 사용할 수 있습니다. 이를 통해 개발자는 웹 애플리케이션의 성능과 사용자 경험을 향상시킬 수 있습니다.

#React #React.forwardRef