---
layout: post
title: "[flutter] AnimatedContainer와 함께 사용하는 RotationTransition 소개"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

어플리케이션을 개발하다 보면 사용자에게 더 흥미로운 경험을 제공하기 위해 애니메이션을 사용해야 하는 경우가 많습니다. **Flutter**에서 `AnimatedContainer`와 `RotationTransition`을 함께 사용하면 UI 요소의 크기와 각도를 부드럽게 변경하면서 사용자에게 보다 더 흥미로운 화면을 제공할 수 있습니다.

## AnimatedContainer란?

`AnimatedContainer`는 애니메이션이 적용된 컨테이너로, 크기나 배경색 등 여러 속성이 변경될 때 동안 애니메이션을 전환할 수 있습니다. 이를 통해 UI가 부드럽게 변화하면서 사용자의 시각적인 경험을 향상시킬 수 있습니다.

```dart
AnimatedContainer(
  duration: Duration(seconds: 1),
  width: _isExpanded ? 200 : 100,
  height: _isExpanded ? 200 : 100,
  color: _isExpanded ? Colors.blue : Colors.green,
  curve: Curves.fastOutSlowIn,
  child: Center(child: Text('Hello, Flutter!')),
)
```

위 예제에서 `_isExpanded`가 `true`일 때, `AnimatedContainer`의 너비와 높이는 200이 되고 배경색은 파란색으로 변경됩니다. 그리고 `_isExpanded`가 `false`일 때는 너비와 높이가 100으로, 배경색은 초록색으로 변경됩니다. 

## RotationTransition이란?

`RotationTransition`은 자식 위젯을 회전하는 간단한 방법을 제공하는 위젯입니다. 이를 사용하여 UI 요소를 회전하거나 사용자 상호작용에 따라 동적인 회전 애니메이션을 만들 수 있습니다.

```dart
RotationTransition(
  turns: _animation,
  child: Container(
    width: 100,
    height: 100,
    color: Colors.red,
  ),
)
```

위 코드에서 `_animation`은 0부터 1까지의 값으로 회전 각도를 나타냅니다. 따라서 `_animation`이 1인 경우 자식 위젯은 360도 회전합니다.

## AnimatedContainer와 RotationTransition 함께 사용하기

`AnimatedContainer`의 크기 및 속성을 변경하고 `RotationTransition`을 사용하여 요소를 회전함으로써 UI에서 더욱 동적인 효과를 만들 수 있습니다.

```dart
bool _isRotated = false;

AnimatedContainer(
  duration: Duration(seconds: 1),
  width: _isRotated ? 200 : 100,
  height: _isRotated ? 200 : 100,
  color: _isRotated ? Colors.blue : Colors.green,
  curve: Curves.fastOutSlowIn,
  child: RotationTransition(
    turns: _animation,
    child: Center(child: Text('Hello, Flutter!')),
  ),
)
```

위의 예제에서 `_isRotated`가 `true`일 때, `AnimatedContainer`의 크기가 커지면서 배경색도 파란색으로 변경되고, 텍스트는 회전하면서 화면에 표시됩니다. `_isRotated`가 `false`일 때는 반대로 작아지고 초록색으로 변경됩니다.

이제 `AnimatedContainer`와 `RotationTransition`을 함께 사용하여 애니메이션을 적용하고 UI에 동적인 효과를 부여하는 방법을 알아보았습니다. 이러한 기술은 풍부한 사용자 경험을 제공하고 앱을 흥미롭고 매력적으로 만드는데 도움이 될 것입니다.

더 많은 정보를 원하시면 [Flutter 공식 문서](https://flutter.dev/docs)를 참조하세요.