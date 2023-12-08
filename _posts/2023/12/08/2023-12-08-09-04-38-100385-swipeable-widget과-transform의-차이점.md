---
layout: post
title: "[flutter] Swipeable Widget과 Transform의 차이점"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

이 글에서는 **Swipeable Widget**과 **Transform**이라는 **Flutter**에서 사용되는 두 가지 다른 기능에 대해 알아보겠습니다. **Swipeable Widget**과 **Transform**은 둘 다 화면 요소를 조작하거나 변형하는 데 사용되지만, 각각의 특징과 사용 사례가 다릅니다.

## Swipeable Widget

**Swipeable Widget**은 사용자가 화면에서 터치하여 스와이프할 수 있는 기능을 구현할 때 사용됩니다. 이를 통해 리스트나 카드와 같은 요소들을 드래그하여 특정 동작을 수행할 수 있습니다. 예를 들어, 이메일 앱에서 이메일을 스와이프하여 삭제 또는 보관하는 동작을 구현할 때 **Swipeable Widget**이 사용될 수 있습니다.

다양한 설정을 통해 사용자가 화면을 어떻게 스와이프할 수 있는지를 지정하고, 스와이프 동작에 대한 반응을 설정할 수 있습니다.

```dart
Swipeable(
  child: ListTile(
    title: Text('Swipe me'),
  ),
  onSwipeLeft: () {
    // Perform action when swiped left
  },
  onSwipeRight: () {
    // Perform action when swiped right
  },
);
```

## Transform

**Transform**은 화면 요소의 위치, 크기 또는 회전을 변경할 때 사용됩니다. 이를 통해 화면 요소를 자유롭게 변형하거나 애니메이션 효과를 적용할 수 있습니다. 예를 들어, 이미지를 확대/축소하거나 회전시킬 때 **Transform**이 사용될 수 있습니다.

```dart
Transform(
  transform: Matrix4.translationValues(100.0, 0.0, 0.0),
  child: Text('Hello'),
);
```

## 결론

**Swipeable Widget**과 **Transform**은 각각 터치 동작에 대한 반응과 화면 요소의 변형에 사용됩니다. **Swipeable Widget**은 사용자의 터치에 반응하여 특정 동작을 수행하고, **Transform**은 화면 요소의 위치나 모양을 변형시킬 수 있습니다. 올바른 상황에 맞게 적절히 사용하여 Flutter 앱을 더욱 효과적으로 구현할 수 있습니다.