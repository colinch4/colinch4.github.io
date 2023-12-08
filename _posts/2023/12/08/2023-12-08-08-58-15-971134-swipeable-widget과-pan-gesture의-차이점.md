---
layout: post
title: "[flutter] Swipeable Widget과 Pan Gesture의 차이점"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

이번 포스트에서는 Flutter에서 Swipeable Widget과 Pan Gesture의 차이점에 대해 알아보겠습니다.

## Swipeable Widget

Swipeable Widget은 터치 제스처를 통해 사용자가 화면을 스와이프할 수 있는 기능을 제공하는 위젯입니다. 사용자는 Swipeable Widget을 드래그하여 원하는 동작을 수행할 수 있습니다. 예를 들어, 리스트 아이템을 스와이프하여 삭제하는 기능을 구현할 수 있습니다.

```dart
Swipeable(
  child: ListTile(title: Text('Swipe me')),
  onSwipeLeft: () => _deleteItem(),
  onSwipeRight: () => _editItem(),
);
```

## Pan Gesture

반면에 Pan Gesture는 화면에서 발생하는 터치 이벤트를 감지하여 해당 이벤트에 반응하는 기능을 구현할 때 사용됩니다. Pan Gesture를 사용하면 터치의 이동 방향 및 이동 거리에 따라 사용자 정의 동작을 수행할 수 있습니다. 예를 들어, 터치로 드래그한 위치에 따라 뷰를 이동시키는 동작을 구현할 수 있습니다.

```dart
GestureDetector(
  onPanUpdate: (details) {
    setState(() {
      _position += details.delta;
    });
  },
  child: Container(
    decoration: BoxDecoration(
      color: Colors.blue,
    ),
    child: Center(
      child: Text('Drag me'),
    ),
  ),
);
```

## 결론

Swipeable Widget은 사용자가 화면을 스와이프하는 동작을 감지하여 특정 동작을 수행하는 반면, Pan Gesture는 터치 이벤트의 이동 방향 및 거리에 따라 맞춤형 동작을 구현할 수 있습니다. 따라서, 두 기능은 서로 다른 사용 사례에 적합하며, 필요에 따라 적절히 선택하여 사용해야 합니다.

이상으로 Swipeable Widget과 Pan Gesture의 차이점에 대해 알아보았습니다. 감사합니다.

관련 참고자료:  
- [Swipeable Widget - Flutter API](https://api.flutter.dev/flutter/widgets/Swipeable-class.html)  
- [Pan Gesture - Flutter API](https://api.flutter.dev/flutter/widgets/GestureDetector-class.html)