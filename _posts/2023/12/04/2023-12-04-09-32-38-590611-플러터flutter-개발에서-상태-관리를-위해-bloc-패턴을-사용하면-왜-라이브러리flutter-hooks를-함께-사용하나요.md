---
layout: post
title: "[flutter] 플러터(Flutter) 개발에서 상태 관리를 위해 BLoC 패턴을 사용하면 왜 라이브러리(Flutter Hooks)를 함께 사용하나요?"
description: " "
date: 2023-12-04
tags: [flutter]
comments: true
share: true
---

플러터(Flutter) 개발에서 상태 관리는 매우 중요한 측면입니다. 개발자는 애플리케이션의 상태를 관리하고 UI 갱신을 적절하게 처리해야 합니다. 이러한 작업을 수행하기 위해 BLoC (Business Logic Component) 패턴을 사용하는 것은 매우 효과적입니다.

BLoC 패턴은 상태(데이터)와 UI 분리를 강조하며, 비즈니스 로직을 추상화하여 재사용 가능한 컴포넌트를 만들 수 있게 해줍니다. 하지만 BLoC 패턴으로 상태 관리를 하는 경우에는 몇 가지 불편한 점이 있을 수 있습니다.

첫째, BLoC의 상태를 별도로 관리하기 때문에 상태를 업데이트하려면 불변성을 유지하고 상태를 복사하는 작업이 필요합니다. 둘째, BLoC로 상태를 변경할 때마다 UI를 업데이트하기 위해 Stream과 BlocBuilder 또는 StreamBuilder와 같은 위젯을 사용해야 합니다. 이는 비교적 복잡한 코드를 작성하게 됩니다.

이러한 이유로 Flutter 개발자들은 BLoC 패턴과 함께 Flutter Hooks 라이브러리를 사용하기 시작했습니다. Flutter Hooks는 React의 Hooks 개념을 Flutter로 가져와서 상태 관리를 훨씬 간단하고 직관적으로 처리할 수 있도록 도와줍니다.

Flutter Hooks는 StatefulWidget을 사용하지 않고도 상태를 관리할 수 있는 useState 및 useMemo등의 훅을 제공합니다. 이를 통해 상태 변경과 UI 갱신을 더 간단하게 처리할 수 있습니다. 예를 들어, useState 훅을 사용하면 몇 줄의 코드로 상태를 생성하고 변경할 수 있습니다.

```dart
var count = useState(0);
```

또한, useEffect 훅을 사용하여 위젯이 생성되거나 특정 상태가 변경될 때 원하는 동작을 수행할 수 있습니다. useMemo 훅은 계산 비용이 큰 작업을 수행할 때 캐싱하여 중복 계산을 피할 수 있게 해줍니다.

이 외에도 Flutter Hooks는 다양한 훅을 제공하여 다른 상태 관리 문제를 해결할 수 있습니다. 예를 들면 useStream, useFuture, useValueListenable 등이 있습니다.

따라서, BLoC 패턴과 함께 Flutter Hooks를 사용하면 상태 관리 작업을 훨씬 효율적으로 처리할 수 있습니다. BLoC은 비즈니스 로직을 추상화하고 재사용 가능한 컴포넌트를 만드는 데 도움을 주고, Flutter Hooks는 상태 관리를 훨씬 간편하게 만들어 줍니다. 이 두 기술의 조합은 플러터 개발에서 상태 관리의 완벽한 조합이라고 할 수 있습니다.

### 참고 자료
- [Flutter Hooks 공식 문서](https://pub.dev/packages/flutter_hooks)
- [BLoC 패턴 소개](https://bloclibrary.dev/#/coreconcepts)
- [React Hooks 소개](https://reactjs.org/docs/hooks-intro.html)