---
layout: post
title: "React Concurrent Mode의 DOM 조작 방식과 최적화 전략"
description: " "
date: 2023-11-09
tags: []
comments: true
share: true
---

React Concurrent Mode는 React 18부터 도입된 기능으로, 사용자 경험을 향상시키기 위해 React 애플리케이션의 성능을 개선하는 방법을 제공합니다. Concurrent Mode에서는 DOM 조작 방식도 이전과 다르게 변경되었습니다.

일반적으로 React는 Virtual DOM과 Reconciliation 알고리즘을 사용하여 변경된 부분만 업데이트하는 방식으로 DOM 조작을 합니다. 하지만 Concurrent Mode에서는 이러한 동기적인 업데이트 방식을 비동기적으로 처리합니다.

비동기적 업데이트는 React의 Scheduler가 호출 스택을 사용하여 작업을 세분화하고 우선순위에 따라 조절함으로써 앱의 반응성을 높입니다. 이렇게 함으로써 사용자 인터랙션 중에 우선순위가 높은 작업을 먼저 처리하고, 사용자 경험을 향상시킬 수 있습니다.

# React Concurrent Mode의 최적화 전략

React Concurrent Mode에서 업데이트를 최적화하기 위해 몇 가지 전략을 사용할 수 있습니다.

## 1. Suspense 사용

React Suspense는 아직 렌더링되지 않은 컴포넌트에 대해 로딩 상태를 처리하고, 필요한 데이터가 준비될 때까지 대기하는 기능을 제공합니다. 이를 사용하여 비동기적으로 데이터를 로딩하거나 코드 스플리팅을 수행할 수 있습니다. Suspense를 사용하면 사용자에게 로딩 인디케이터를 보여주고, 데이터가 준비되면 자동으로 업데이트할 수 있습니다.

## 2. Memoization 활용

React Memoization 기능을 활용하여 컴포넌트의 불필요한 리렌더링을 방지할 수 있습니다. 이를 통해 성능을 향상시킬 수 있습니다. Memoization은 이전에 계산한 값을 캐시하여 같은 인자로 호출될 때 이전에 계산한 값을 다시 사용하는 것을 의미합니다. 이를 활용하여 컴포넌트의 props나 상태가 변경되지 않으면 리렌더링하지 않도록 설정할 수 있습니다.

React Concurrent Mode는 생산성과 성능을 더욱 향상시키는 많은 기능과 최적화 전략을 제공합니다. 위에서 소개한 방법 외에도 애플리케이션의 구조에 따라 다양한 최적화 전략을 적용할 수 있습니다. Concurrent Mode를 사용하여 React 애플리케이션의 성능을 개선해보세요!

[React 공식 문서](https://reactjs.org/docs/concurrent-mode-intro.html)를 참조하면 더 많은 세부 정보를 확인할 수 있습니다.

#react #reactconcurrent