---
layout: post
title: "[flutter] Swipeable Widget과 Value Listenable의 차이점"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

양 끝에서 좌우로 스와이프할 수 있는 **Swipeable Widget**은 사용자 인터페이스(UI)와 상호작용하는 데 유용합니다. 반면에, **Value Listenable**은 값을 감지하여 인터페이스를 업데이트하거나 알림하는 데 사용됩니다.

## Swipeable Widget

**Swipeable Widget**은 스와이프 동작을 관리하는 편리한 방법을 제공합니다. 사용자가 위젯을 스와이프할 때, `onSwipeLeft` 및 `onSwipeRight`와 같은 이벤트 핸들러를 지정하여 해당 이벤트가 발생할 때 수행할 작업을 정의할 수 있습니다.

아래는 Flutter에서 Swipeable Widget을 사용한 간단한 예시 코드입니다.

```dart
Swipeable(
  onSwipeLeft: () {
    // 왼쪽으로 스와이프할 때 수행할 작업
  },
  onSwipeRight: () {
    // 오른쪽으로 스와이프할 때 수행할 작업
  },
  child: Container(
    // 스와이프 가능한 컨텐츠
  ),
)
```

## Value Listenable

**Value Listenable**은 값이 변할 때 알림을 받는 데 사용됩니다. 이는 값의 변화에 따라 인터페이스를 동적으로 업데이트하는 데 유용합니다. 예를 들어, 값이 변경될 때마다 UI를 다시 그릴 수 있습니다.

Flutter에서 Value Listenable을 사용하는 예시 코드는 다음과 같습니다.

```dart
ValueNotifier<int> count = ValueNotifier<int>(0);

ValueListenableBuilder(
  valueListenable: count,
  builder: (context, value, child) {
    return Text('$value');
  },
);
```

이 코드는 `ValueListenableBuilder`를 사용하여 `count`가 변경될 때마다 값을 업데이트하는 간단한 예시입니다.

## 결론

**Swipeable Widget**은 사용자의 상호작용을 관리하고, **Value Listenable**은 값의 변화를 감지하여 이에 대한 반응을 처리합니다. 각각의 기능은 고유한 상황에 따라 유용하게 활용됩니다.

참고 자료: 
- Flutter Swipeable Widget: https://api.flutter.dev/flutter/widgets/Swipeable-class.html
- Flutter Value Listenable: https://api.flutter.dev/flutter/widgets/ValueListenableBuilder-class.html