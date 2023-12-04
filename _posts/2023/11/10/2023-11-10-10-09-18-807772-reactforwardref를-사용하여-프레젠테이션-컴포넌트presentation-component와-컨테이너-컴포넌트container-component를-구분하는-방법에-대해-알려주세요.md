---
layout: post
title: "React.forwardRef()를 사용하여 프레젠테이션 컴포넌트(Presentation Component)와 컨테이너 컴포넌트(Container Component)를 구분하는 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [reactjs]
comments: true
share: true
---

React에서 컴포넌트를 개발하는 동안 Presentation Component와 Container Component를 구분하는 것은 중요한 과정입니다. Presentation Component는 주로 UI 요소를 표현하고, Container Component는 데이터 플로우를 관리하고 상태를 업데이트합니다. 이러한 구분은 코드의 모듈화와 유지 보수를 용이하게 해줍니다.

이러한 구분을 위해 React.forwardRef()를 사용할 수 있습니다. React.forwardRef()는 ref 전달을 통해 하위 컴포넌트에 접근할 수 있는 기능을 제공합니다.

## Presentation Component 작성하기
Presentation Component는 UI 렌더링을 담당합니다. ref를 받는 기능은 필요하지 않으므로 일반 함수형 컴포넌트로 작성할 수 있습니다.

```jsx
import React from "react";

const PresentationComponent = ({ props }) => {
  // UI 컴포넌트의 코드 작성
  return (
    <div>
      <h1>{props.title}</h1>
      <p>{props.description}</p>
    </div>
  );
};

export default PresentationComponent;
```

## Container Component 작성하기
Container Component는 Presentation Component를 감싸고, 로직 및 데이터 처리를 담당합니다. React.forwardRef()를 사용하여 ref 전달을 지원해야 합니다.

```jsx
import React from "react";
import PresentationComponent from "./PresentationComponent";

const ContainerComponent = React.forwardRef((props, ref) => {
  // 로직 및 데이터 처리
  const handleClick = () => {
    // 클릭 이벤트 핸들러 로직 작성
  };

  return (
    <div onClick={handleClick} ref={ref}>
      <PresentationComponent {...props} />
    </div>
  );
});

export default ContainerComponent;
```

## 사용법
Container Component를 사용하는 부모 컴포넌트에서 ref를 생성하고, 해당 ref를 Container Component에 전달할 수 있습니다.

```jsx
import React, { useRef, useEffect } from "react";
import ContainerComponent from "./ContainerComponent";

const ParentComponent = () => {
  const containerRef = useRef(null);

  useEffect(() => {
    // ref를 통한 Container Component 내부 DOM에 접근 가능
    console.log(containerRef.current);
  }, []);

  return (
    <div>
      <ContainerComponent ref={containerRef} props={...} />
    </div>
  );
};
```

Presentation Component와 Container Component의 구분은 코드의 가독성과 유지 보수를 향상시킬 수 있습니다. React.forwardRef()를 사용하여 ref 전달을 지원하면서, 역할에 맞게 컴포넌트를 관리할 수 있습니다.

#React #강좌