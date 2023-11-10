---
layout: post
title: "React Concurrent Mode의 자바스크립트 UI 컴포지션 패턴"
description: " "
date: 2023-11-09
tags: [ConcurrentMode]
comments: true
share: true
---

React Concurrent Mode는 React 18에서 새롭게 도입된 기능으로, 사용자에게 더 나은 성능과 사용자 경험을 제공하기 위한 목적으로 개발되었습니다. 이러한 모드에서는 비동기적으로 UI를 렌더링하여 멈추지 않는 사용자 경험을 제공할 수 있게 합니다. 이 패턴은 이전의 React에서 사용되던 동기적인 UI 컴포지션 패턴과는 다른 방식으로 작동합니다.

## 동기적인 UI 컴포지션 패턴

React에서는 기본적으로 동기적인 UI 컴포지션 패턴을 사용합니다. 이 패턴은 컴포넌트가 렌더링되는 동안 다른 작업을 중단시키지 않고 한 번에 한 작업씩 순차적으로 처리합니다. 이것은 대부분의 경우에는 문제가 되지 않으며 사용자에게 부드러운 사용자 경험을 제공할 수 있지만, 복잡한 UI나 무거운 작업을 처리해야 할 때는 성능 문제가 발생할 수 있습니다.

## React Concurrent Mode의 이점

React Concurrent Mode는 동기적인 컴포지션 패턴의 한계를 극복하기 위해 비동기적인 방식으로 작동합니다. 이 모드에서는 여러 작업이 동시에 실행되도록 스케줄링되어 UI의 능력을 최대한 활용할 수 있습니다. 이러한 비동기 작업 스케줄링은 성능을 향상시키고 사용자가 멈추지 않는 반응형 경험을 제공합니다.

## React Concurrent Mode의 자바스크립트 UI 컴포지션 패턴

React Concurrent Mode에서는 자바스크립트의 체계적인 UI 컴포지션 패턴을 이용하여 비동기적인 UI 작업을 처리합니다. 이 패턴은 React에서 제공하는 `Suspense` 컴포넌트와 `useTransition` 훅을 활용하여 구현됩니다. `Suspense` 컴포넌트를 사용하여 특정 리소스가 로딩될 때까지 대체 UI를 표시하고, `useTransition` 훅을 사용하여 UI 전환을 부드럽게 처리할 수 있습니다.

```javascript
import { Suspense, useTransition } from 'react';

function App() {
  const [startTransition] = useTransition();

  function handleClick() {
    startTransition(() => {
      // 비동기 작업 실행
    });
  }

  return (
    <div>
      <button onClick={handleClick}>비동기 작업 시작</button>
      <Suspense fallback={<div>로딩 중...</div>}>
        {/* 비동기 작업 결과를 보여주는 UI */}
      </Suspense>
    </div>
  );
}
```

위의 코드는 React Concurrent Mode에서 자바스크립트 UI 컴포지션 패턴을 구현한 예시입니다. `useTransition` 훅을 사용하여 비동기 작업을 시작하고, `Suspense` 컴포넌트를 사용하여 로딩 중인 동안의 대체 UI를 표시합니다. 비동기 작업이 완료되면 결과를 보여주는 UI가 렌더링됩니다.

## 마무리

React Concurrent Mode는 더 나은 사용자 경험과 성능을 제공하기 위해 도입된 기능입니다. 새로운 자바스크립트 UI 컴포지션 패턴을 사용하여 비동기적인 UI 작업을 처리하며, 이를 통해 멈추지 않는 반응형 경험을 제공할 수 있습니다. 계속해서 React의 발전에 주목해보고 새로운 패턴을 적용하여 향상된 UI 개발을 경험해보세요.

## 참조

- [React 공식 문서 - Concurrent Mode](https://reactjs.org/docs/concurrent-mode-intro.html)