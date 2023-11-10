---
layout: post
title: "React.forwardRef()를 활용하여 컴포넌트의 모달 창(Modal Popup) 기능을 구현하는 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: []
comments: true
share: true
---

React에서 모달 창은 매우 일반적인 요구사항입니다. 사용자의 인터랙션에 따라 모달을 열고 닫을 수 있도록 구현하는 것은 매우 중요합니다. 이번 글에서는 React.forwardRef()를 활용하여 컴포넌트의 모달 창 기능을 구현하는 방법에 대해 알아보겠습니다.

## 1. React.forwardRef()란?

React.forwardRef()는 React 16.3 이후 버전에서 도입된 기능으로, 함께 전달된 ref를 다른 컴포넌트로 전달하는 역할을 합니다. 기존에는 ref를 직접 사용하지 않고 컴포넌트 사이에서 데이터를 전달하기 위해 props로 전달하는 방식이 주로 사용되었습니다. 하지만 경우에 따라서 ref를 직접 사용해야 할 때가 있는데, 이때 React.forwardRef()를 사용할 수 있습니다.

## 2. 모달 컴포넌트 생성하기

먼저, 모달을 구현할 컴포넌트를 생성해야 합니다. 다음은 간단한 모달 컴포넌트의 예입니다.

```jsx
import React, { forwardRef, useImperativeHandle, useState } from 'react';

const Modal = forwardRef((props, ref) => {
  const [isOpen, setIsOpen] = useState(false);

  useImperativeHandle(ref, () => ({
    open: () => {
      setIsOpen(true);
    },
    close: () => {
      setIsOpen(false);
    }
  }));

  return (
    <div className={`modal ${isOpen ? 'open' : 'closed'}`}>
      {/* 모달 컨텐츠 */}
    </div>
  );
});
```

위의 코드에서는 useState 훅을 사용하여 모달의 상태를 관리합니다. setIsOpen 함수를 사용하여 모달을 열고 닫을 수 있습니다. 그리고 useImperativeHandle 훅을 사용하여 ref가 전달될 때 open()과 close() 함수를 호출할 수 있도록 합니다.

## 3. 모달 사용하기

이제 모달 컴포넌트를 사용해보겠습니다. 다음은 모달을 트리거하는 버튼을 포함하는 부모 컴포넌트의 예입니다.

```jsx
import React, { useRef } from 'react';

const ParentComponent = () => {
  const modalRef = useRef(null);

  const openModal = () => {
    modalRef.current.open();
  };

  const closeModal = () => {
    modalRef.current.close();
  };

  return (
    <div>
      <button onClick={openModal}>모달 열기</button>
      <button onClick={closeModal}>모달 닫기</button>
      <Modal ref={modalRef} />
    </div>
  );
};
```

위의 코드에서는 useRef 훅을 사용하여 모달 컴포넌트에 대한 ref를 생성합니다. openModal()과 closeModal() 함수에서는 모달의 open()과 close() 함수를 호출하여 모달을 열고 닫을 수 있도록 합니다. 그리고 Modal 컴포넌트를 ref 속성과 함께 추가하여 사용합니다.

## 4. 마무리

React.forwardRef()를 활용하여 모달 창 기능을 구현하는 방법에 대해 알아보았습니다. 이를 통해 다양한 상황에서 모달 창을 구현하는데 도움이 되길 바랍니다. 건강한 개발 환경에서 모달 창을 구현해보세요!

#React #모달