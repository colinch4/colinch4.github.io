---
layout: post
title: "[flutter] Swipeable Widget과 Custom Painter의 차이점"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter 앱을 개발하다 보면 UI를 만들기 위해 Swipeable Widget과 Custom Painter를 사용하는 경우가 많습니다. 이 두 가지 방법 간에는 어떤 차이가 있는지 살펴보겠습니다.

## Swipeable Widget

Swipeable Widget은 사용자가 뷰를 터치하여 스와이프할 수 있는 기능을 제공합니다. 리스트 항목을 삭제하거나 수정하는 등의 동작을 할 때 많이 사용됩니다. Swipeable Widget은 사용자 상호작용에 반응하여 터치 동작을 인식하고 처리할 수 있습니다. 예를 들어, `Dismissible`나 `Slidable`와 같은 위젯을 사용하여 스와이프할 때 나타나는 액션을 정의할 수 있습니다.

```dart
Slidable(
  actionPane: SlidableDrawerActionPane(),
  actionExtentRatio: 0.25,
  child: ListTile(
    ...
  ),
  actions: <Widget>[
    IconSlideAction(
      caption: 'Archive',
      ...
    ),
  ],
  secondaryActions: <Widget>[
    IconSlideAction(
      caption: 'More',
      ...
    ),
  ],
);
```

## Custom Painter

반면에 Custom Painter는 화면을 그리는 데 사용됩니다. 이를 사용하여 직접 그림을 그릴 수 있고, 주로 그래프, 차트 또는 복잡한 사용자 지정 그래픽을 만드는 데 사용됩니다. Custom Painter를 사용하면 `CustomPaint` 위젯과 함께 `CustomPainter` 클래스를 구현하여 원하는 그림을 그릴 수 있습니다.

```dart
class MyPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    ...
  }

  @override
  bool shouldRepaint(CustomPainter oldDelegate) {
    return false;
  }
}
```

## 결론

Swipeable Widget은 사용자 상호작용에 응답하여 스와이프 동작을 처리하는 데 주로 사용되며, Custom Painter는 화면에 그래픽을 그리는 데 사용됩니다. 이 두 가지 방법은 서로 다른 목적과 사용 사례를 가지고 있으며, 개발자는 앱의 요구에 맞는 방법을 선택하여 구현할 수 있습니다.

위의 내용을 요약하면 Swipeable Widget은 사용자 상호작용에 반응하여 스와이프 동작을 처리하고, Custom Painter는 화면에 그래픽을 그립니다.

참고: https://flutter.dev/docs/cookbook/gestures/dismissible

[flutter]: flutter
[dart]: dart