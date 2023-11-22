---
layout: post
title: "[javascript] Redux의 선택적인 리렌더링(Optimized Rendering) 방법은?"
description: " "
date: 2023-11-22
tags: [javascript]
comments: true
share: true
---

Redux는 상태 관리 라이브러리로, React와 함께 많이 사용됩니다. 그러나 큰 규모의 애플리케이션에서는 Redux의 성능 문제가 발생할 수 있습니다. 특히, 매번 상태 업데이트 시 전체 컴포넌트 트리를 다시 렌더링하는 경우 성능 저하가 발생할 수 있습니다.

이를 해결하기 위해 Redux는 선택적인 리렌더링(Optimized Rendering) 방법을 제공합니다. Redux는 상태 업데이트 후 변경된 부분만 다시 렌더링되도록 하는 방법을 제공합니다. 이를 통해 불필요한 리렌더링을 피하고 성능을 향상시킬 수 있습니다.

다음은 Redux에서 선택적인 리렌더링을 구현하는 방법입니다.

1. connect 함수의 mapStateToProps 파라미터를 사용합니다. 이 파라미터는 현재 상태를 매핑하여 컴포넌트에 전달합니다. 포함된 상태가 변경될 때만 컴포넌트가 다시 렌더링됩니다.

2. connect 함수의 ownProps 파라미터를 사용하여 특정 속성이 변경될 때에만 컴포넌트를 리렌더링할 수 있습니다. 이는 성능 향상에 큰 도움이 됩니다.

3. shouldComponentUpdate 메서드를 사용하여 리렌더링을 제어할 수 있습니다. 이 메서드는 다음 상태와 현재 상태를 비교하여 리렌더링 여부를 결정합니다. 변경되지 않은 경우 리렌더링을 건너뛰게 됩니다.

4. PureComponent 또는 React.memo를 사용하여 순수한 컴포넌트를 만들 수 있습니다. 이러한 컴포넌트는 얕은 비교를 수행하여 변경 여부를 판단하므로, 변경되지 않은 경우에는 리렌더링되지 않습니다.

Redux의 선택적인 리렌더링 방법을 사용하면 상태 변경 시 성능을 획기적으로 개선할 수 있습니다. 이를 통해 애플리케이션의 성능을 최적화할 수 있습니다.

참고 자료:
- Redux 공식 문서: https://redux.js.org/recipes/state-array#optimizing-performance