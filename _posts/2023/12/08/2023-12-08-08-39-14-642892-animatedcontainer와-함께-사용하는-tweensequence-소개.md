---
layout: post
title: "[flutter] AnimatedContainer와 함께 사용하는 TweenSequence 소개"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter 앱을 개발하다보면 UI 요소의 애니메이션을 추가하고 싶을 때가 많습니다. `AnimatedContainer`는 UI 요소의 속성을 부드럽게 변화시키는 데 도움을 주는데, 이때 `Tween`과 `TweenSequence`를 사용하여 애니메이션을 더욱 다채롭고 복잡하게 만들 수 있습니다. 이번 포스트에서는 `AnimatedContainer`와 함께 사용하는 `TweenSequence`에 대해 알아보겠습니다.

## 1. AnimatedContainer란?

`AnimatedContainer`는 UI 요소의 크기, 색상, 패딩 등을 부드럽게 애니메이션시키는 Flutter 위젯입니다. 이를 사용하면 UI 요소의 변화를 자연스럽게 만들 수 있어 사용자 경험을 더욱 향상시킬 수 있습니다.

```dart
AnimatedContainer(
  duration: Duration(seconds: 1),
  width: _width,
  height: _height,
  color: _color,
  padding: _padding,
  child: _child,
);
```

위 예제는 `AnimatedContainer`의 간단한 사용 예시입니다. `duration` 속성을 통해 애니메이션 속도를 조절할 수 있고, `width`, `height`, `color`, `padding` 등의 속성을 변경함으로써 애니메이션을 만들 수 있습니다.

## 2. Tween과 TweenSequence

`Tween`은 애니메이션의 시작과 끝 값 사이의 보간(interpolation)을 정의하는 객체입니다. 이를 사용하여 값을 부드럽게 변화시키는데 유용하게 활용할 수 있습니다. 

```dart
Tween(begin: 0.0, end: 1.0)
```

`TweenSequence`는 여러 개의 `Tween`을 순차적으로 실행하여 복잡한 애니메이션을 만들 수 있도록 도와줍니다. 각 `Tween`에는 해당 애니메이션의 시작 시간과 종료 시간을 정의하여 한 번에 여러 애니메이션을 실행할 수 있습니다.

```dart
TweenSequence(
  <TweenSequenceItem<double>>[
    TweenSequenceItem(tween: Tween(begin: 0.0, end: 100.0), weight: 40.0),
    TweenSequenceItem(tween: Tween(begin: 100.0, end: 200.0), weight: 60.0),
  ],
)
```

위 예제는 `TweenSequence`를 사용하여 애니메이션을 여러 단계로 나누어 정의한 것입니다.

## 3. AnimatedContainer와 TweenSequence 함께 사용하기

`AnimatedContainer`와 `TweenSequence`를 함께 사용하면 UI 요소의 애니메이션을 더욱 다채롭고 복잡하게 만들 수 있습니다. 예를 들어, UI 요소의 크기와 색상을 동시에 애니메이션시키는 등의 효과를 만들어낼 수 있습니다.

```dart
TweenSequence(
  <TweenSequenceItem<Color>>[
    TweenSequenceItem(tween: ColorTween(begin: Colors.red, end: Colors.blue), weight: 50.0),
    TweenSequenceItem(tween: ColorTween(begin: Colors.blue, end: Colors.green), weight: 50.0),
  ],
).animate(_controller)
  ..addListener(() {
    setState(() {
      _color = _colorAnimation.value;
      _height = _heightAnimation.value;
    });
  });
```

위 예제에서 `_controller`는 AnimationController로, `addListener`를 통해 애니메이션 값이 변할 때마다 `setState`를 호출하여 UI를 업데이트합니다.

`AnimatedContainer`와 `TweenSequence`를 함께 사용하여 다채로운 애니메이션 효과를 만들어낼 수 있으며, 앱의 사용자 경험을 향상시킬 수 있게됩니다.

이상으로 `AnimatedContainer`와 `TweenSequence`에 대한 간략한 소개였습니다. 자세한 내용은 [공식 문서](https://api.flutter.dev/flutter/animation/Tween-sequence.html)를 참고하시기 바랍니다.