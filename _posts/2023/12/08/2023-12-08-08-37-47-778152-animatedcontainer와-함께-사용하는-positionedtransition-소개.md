---
layout: post
title: "[flutter] AnimatedContainer와 함께 사용하는 PositionedTransition 소개"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter 앱을 개발하다보면 화면 전환과 같이 애니메이션을 적용해야 하는 경우가 많이 있습니다. *Flutter*에서는 *AnimatedContainer*와 *PositionedTransition*을 결합하여 다양한 애니메이션을 쉽게 구현할 수 있습니다.

이번 글에서는 *AnimatedContainer*와 *PositionedTransition*을 함께 사용하여 화면 전환 애니메이션을 구현하는 방법에 대해 알아보겠습니다.

## 1. AnimatedContainer

[*AnimatedContainer*](https://api.flutter.dev/flutter/widgets/AnimatedContainer-class.html)는 *Container* 위젯과 유사하지만, 속성 변경 시 자연스러운 애니메이션 효과를 제공하는 위젯입니다. 크기, 색상, 모서리 반경 등을 애니메이션화할 수 있어 화면 전환 애니메이션에 유용하게 활용됩니다.

다음은 *AnimatedContainer*의 가장 기본적인 예제입니다.

```dart
AnimatedContainer(
  duration: Duration(seconds: 1),
  color: _isToggled ? Colors.blue : Colors.red,
  height: _isToggled ? 100.0 : 200.0,
  width: _isToggled ? 100.0 : 200.0,
  child: //...,
)
```

위 코드에서 `_isToggled` 값을 변경할 때마다 *AnimatedContainer*는 새로운 크기와 색상으로 자연스러운 애니메이션을 적용합니다.

## 2. PositionedTransition

[*PositionedTransition*](https://api.flutter.dev/flutter/widgets/PositionedTransition-class.html)은 여러 개의 *Positioned* 위젯을 사용하여 애니메이션을 적용할 수 있는 위젯으로, 일반적으로 *Stack* 위젯과 함께 사용됩니다. 위젯의 위치를 애니메이션화할 때 유용하게 활용할 수 있습니다.

다음은 *PositionedTransition*을 사용한 예제입니다.

```dart
PositionedTransition(
  rect: _animation.drive(
    CurveTween(curve: Curves.ease),
  ).drive(
    Tween<Rect>(
      begin: Rect.fromLTRB(0, 0, 100, 100),
      end: Rect.fromLTRB(100, 100, 200, 200),
    ),
  ),
  child: Container(
    color: Colors.blue,
  ),
)
```

이 예제에서는 `_animation`을 사용하여 위치를 변경하면서 자연스러운 애니메이션을 적용합니다.

## 3. AnimatedContainer와 PositionedTransition 함께 사용하기

*AnimatedContainer*와 *PositionedTransition*을 함께 사용하면 화면 전환 애니메이션을 더욱 다채롭고 효과적으로 구현할 수 있습니다. 예를 들어, 화면 전환 시 요소의 크기와 위치를 동시에 애니메이션화할 수 있습니다.

다음은 *AnimatedContainer*와 *PositionedTransition*을 함께 사용한 예제입니다.

```dart
Stack(
  children: <Widget>[
    PositionedTransition(
      rect: _animation.drive(
        CurveTween(curve: Curves.ease),
      ).drive(
        Tween<Rect>(
          begin: Rect.fromLTRB(0, 0, 100, 100),
          end: Rect.fromLTRB(100, 100, 200, 200),
        ),
      ),
      child: AnimatedContainer(
        duration: Duration(seconds: 1),
        color: _isToggled ? Colors.blue : Colors.red,
        height: _isToggled ? 100.0 : 200.0,
        width: _isToggled ? 100.0 : 200.0,
      ),
    ),
  ],
)
```

위 코드에서 *PositionedTransition*과 *AnimatedContainer*를 함께 사용하여 위치와 크기를 애니메이션화할 수 있습니다.

## 결론

*Flutter*에서 *AnimatedContainer*와 *PositionedTransition*을 함께 사용하여 화면 전환 애니메이션을 구현하는 방법에 대해 알아보았습니다. 이를 통해 다양한 애니메이션 효과를 더 쉽게 적용할 수 있고, 사용자에게 더욱 즐거운 앱 경험을 제공할 수 있습니다.

더 많은 정보는 [Flutter 공식 문서](https://flutter.dev/docs)를 참고하시기 바랍니다.