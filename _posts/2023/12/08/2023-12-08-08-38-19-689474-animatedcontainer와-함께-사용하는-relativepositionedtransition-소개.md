---
layout: post
title: "[flutter] AnimatedContainer와 함께 사용하는 RelativePositionedTransition 소개"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

## 서론
Flutter에서 UI 요소를 애니메이션화하는 것은 매우 중요합니다. 애니메이션을 추가하면 앱이 더 동적이고 흥미로워 보입니다. 이번 블로그 글에서는 AnimatedContainer와 함께 사용되는 RelativePositionedTransition을 소개하고, 어떻게 사용하는지 알아보겠습니다.

## AnimatedContainer 소개
`AnimatedContainer`는 Flutter에서 사용할 수 있는 매우 강력한 애니메이션 위젯 중 하나입니다. 이 위젯은 `duration`, `curve`, `color`, `margin`, `padding` 등의 속성을 변경할 때 애니메이션을 적용할 수 있습니다. 예를 들어, 컨테이너의 높이와 너비를 변경하거나 색상을 변경할 때 부드러운 애니메이션 효과를 적용할 수 있습니다.

```dart
AnimatedContainer(
  duration: Duration(seconds: 1),
  width: _isExpanded ? 200 : 100,
  height: _isExpanded ? 200 : 100
);
```

## RelativePositionedTransition 소개
`RelativePositionedTransition`은 부모 위젯에 상대적인 위치에 애니메이션을 적용하는 데 사용됩니다. 일반적으로 `Stack` 위젯 내에서 사용됩니다. 이 위젯을 사용하면 상대적인 위치에 애니메이션을 쉽게 적용할 수 있습니다.

```dart
Stack(
  children: <Widget>[
    RelativePositionedTransition(
      rect: RelativeRectTween(
        begin: RelativeRect.fromLTRB(0, 0, 100, 100),
        end: RelativeRect.fromLTRB(100, 100, 200, 200),
      ).animate(_animationController),
      child: Container(
        color: Colors.blue,
      ),
    ),
  ],
)
```

## AnimatedContainer와 RelativePositionedTransition 함께 사용하기
`AnimatedContainer`와 `RelativePositionedTransition`을 함께 사용하면 상대적인 위치에 애니메이션하면서 컨테이너 속성(크기, 색상 등)을 애니메이션화하는 효과를 쉽게 구현할 수 있습니다.

```dart
Stack(
  children: <Widget>[
    AnimatedContainer(
      duration: Duration(seconds: 1),
      width: _isExpanded ? 200 : 100,
      height: _isExpanded ? 200 : 100,
    ),
    RelativePositionedTransition(
      rect: RelativeRectTween(
        begin: RelativeRect.fromLTRB(0, 0, 100, 100),
        end: RelativeRect.fromLTRB(100, 100, 200, 200),
      ).animate(_animationController),
      child: Container(
        color: Colors.blue,
      ),
    ),
  ],
)
```

## 마무리
`AnimatedContainer`와 `RelativePositionedTransition`은 Flutter에서 UI 요소를 애니메이션화하는 데 매우 유용한 기능입니다. 이러한 기능을 활용하여 앱의 사용자 경험을 향상시키고, 더 매력적인 UI를 디자인할 수 있을 것입니다.

참고: [Flutter 애니메이션 공식 문서](https://flutter.dev/docs/development/ui/animations)