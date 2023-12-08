---
layout: post
title: "[flutter] Swipeable Widget과 Animation Controller의 차이점"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Swipeable Widget과 Animation Controller는 Flutter 앱에서 애니메이션을 처리하는 데 사용됩니다. 이 두 가지 기술은 다른 목적을 가지고 있으며, 다음에서 자세히 살펴보겠습니다.

## Swipeable Widget

Swipeable Widget은 사용자의 스와이프 제스처에 반응하여 UI 요소를 이동하거나 삭제하는 데 사용됩니다. 이것은 주로 리스트 아이템을 스와이프하여 삭제하거나, 드래그하여 순서를 변경하는 등의 기능에 적합합니다.

예를 들어, 아래는 Swipeable Widget을 사용하여 리스트 아이템을 삭제하는 예시 코드입니다.

```dart
Swipeable(
  onSwipeLeft: () {
    // 왼쪽으로 스와이프했을 때 실행할 동작
    deleteItem();
  },
  child: ListTile(
    title: Text('리스트 아이템'),
  ),
)
```

## Animation Controller

Animation Controller는 **애니메이션을 제어**하고 **애니메이션 값의 변화를 추적**하는 데 사용됩니다. 화면 전환, 스케일 변환, 회전 등과 같은 애니메이션 효과를 구현할 때 Animation Controller를 사용하여 애니메이션 값의 변화를 추적합니다.

아래는 Animation Controller를 사용하여 애니메이션을 구현하는 예시 코드입니다.

```dart
AnimationController _controller;
Animation<double> _animation;

@override
void initState() {
  super.initState();
  _controller = AnimationController(
    vsync: this,
    duration: Duration(seconds: 1),
  );
  _animation = Tween(begin: 0.0, end: 1.0).animate(_controller);
  _controller.forward();
}
```

## 결론

Swipeable Widget과 Animation Controller는 각각 **사용자의 상호작용에 반익**하여 **UI 요소를 조작**하고, **애니메이션을 구현하고 제어**하는 데 사용됩니다. 이 두 가지 기술은 서로 다른 목적을 가지고 있으며, 예상되는 동작과 효과가 다르기 때문에 상황에 맞게 적절히 사용하여야 합니다.

더 많은 정보를 원하시면 [Flutter 공식 문서](https://flutter.dev/docs)를 참조하시기 바랍니다.