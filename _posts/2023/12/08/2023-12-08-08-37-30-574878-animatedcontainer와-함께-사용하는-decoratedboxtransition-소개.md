---
layout: post
title: "[flutter] AnimatedContainer와 함께 사용하는 DecoratedBoxTransition 소개"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

애니메이션은 사용자 경험을 향상시키는 데 중요한 역할을 합니다. Flutter에서는 애니메이션을 쉽게 구현할 수 있는 다양한 방법을 제공합니다. 이번 글에서는 `AnimatedContainer` 위젯과 함께 사용하는 `DecoratedBoxTransition`에 대해 알아보겠습니다.

## AnimatedContainer 소개

`AnimatedContainer`는 자식 위젯을 자동으로 애니메이션화하는 떠오르는 애니메이션, 크기 변화, 색상 변경 등을 지원하는 위젯입니다. `AnimatedContainer`를 사용하면 사용자 인터랙션에 따라 부드러운 애니메이션 효과를 쉽게 추가할 수 있습니다.

예를 들어 다음과 같이 코드를 작성할 수 있습니다.

```dart
AnimatedContainer(
  duration: Duration(seconds: 1),
  curve: Curves.fastOutSlowIn,
  color: _selected ? Colors.blue : Colors.red,
  child: Container(width: 200, height: 200),
)
```

## DecoratedBoxTransition 소개

`DecoratedBoxTransition`는 부모 위젯의 `decoration` 속성을 애니메이션화하는 데 사용됩니다. 색상, 그림자, 모서리 둥글게 등 `BoxDecoration`의 속성을 부드럽게 전환할 수 있습니다.

`DecoratedBoxTransition`는 `Animation<double>`을 사용하여 애니메이션을 제어합니다. 필요한 경우 `DecorationTween`을 사용하여 시작값과 끝값을 지정할 수 있습니다.

```dart
DecoratedBoxTransition(
  position: _controller.drive(decoration),
  child: const FlutterLogo(size: 200),
)
```

## AnimatedContainer와 DecoratedBoxTransition를 함께 활용하기

`AnimatedContainer`와 `DecoratedBoxTransition`를 결합하여 부드러운 애니메이션 효과를 더욱 풍부하게 만들 수 있습니다. 예를 들어, 사용자가 버튼을 선택했을 때 `AnimatedContainer`와 `DecoratedBoxTransition`를 함께 사용하여 부모 위젯의 `decoration` 속성을 애니메이션화할 수 있습니다.

```dart
AnimatedContainer(
  duration: Duration(seconds: 1),
  curve: Curves.fastOutSlowIn,
  decoration: decoration,
  child: DecoratedBoxTransition(
    position: _controller.drive(decoration),
    child: const FlutterLogo(size: 200),
  ),
),
```

이렇게 `AnimatedContainer`와 `DecoratedBoxTransition`를 결합하여 부드러운 애니메이션 효과를 구현할 수 있습니다.

## 마무리

이번 글에서는 `AnimatedContainer`와 `DecoratedBoxTransition`을 함께 사용하여 부드러운 애니메이션 효과를 구현하는 방법에 대해 알아보았습니다. 이러한 기술을 활용하면 Flutter 앱의 사용자 경험을 향상시키는 데 도움이 될 것입니다.

더 많은 정보가 필요하다면 [공식 Flutter 문서](https://flutter.dev/docs)를 참고하세요.