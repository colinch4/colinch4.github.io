---
layout: post
title: "[flutter] 플러터(Flutter) 개발에서 상태 관리를 위해 Redux를 사용하면 왜 라이브러리(Flutter Hooks)를 함께 사용하나요?"
description: " "
date: 2023-12-04
tags: [flutter]
comments: true
share: true
---

이런 문제를 해결하기 위해 Flutter Hooks라는 라이브러리를 사용합니다. Flutter Hooks는 플러터에서 함수형 프로그래밍 스타일을 사용할 수 있게 해주는 라이브러리로, 간단하고 효율적인 상태 관리를 가능하게 합니다. Redux와 함께 사용되면 Redux 액션과 리듀서를 작성하는 대신, Hooks를 사용해 상태를 직접 업데이트하고 관리할 수 있습니다.

Flutter Hooks를 사용하면 코드의 가독성과 유지 보수성을 향상시킬 수 있습니다. Redux의 복잡성을 줄이고, 간결하고 직관적인 코드를 작성할 수 있습니다. 또한 Redux에서 어려운 개념들을 배우고 적용하는 시간을 단축시킬 수 있습니다. 따라서 Redux와 Flutter Hooks를 함께 사용하면, 플러터 앱의 상태 관리를 효율적으로 처리할 수 있습니다.

참고 자료:
- Redux: https://redux.js.org/
- Flutter Hooks: https://pub.dev/packages/flutter_hooks