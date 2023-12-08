---
layout: post
title: "[flutter] AnimatedContainer와 함께 사용하는 TweenAnimationBuilder 소개"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter에서 UI 요소의 애니메이션을 쉽게 구현할 수 있는 여러 가지 방법이 있습니다. 이 중에서도 **AnimatedContainer**와 **TweenAnimationBuilder**는 많이 사용되는 방법 중 하나입니다. 

## AnimatedContainer와는 어떻게 사용되나요?

**AnimatedContainer**는 일반적인 Container와 유사하지만, 속성들이 변경될 때 자동으로 애니메이션을 생성하여 부드러운 효과를 줄 수 있습니다. 이를 통해 UI의 변화를 부드럽게 표현할 수 있습니다.

```
```dart
AnimatedContainer(
  duration: Duration(seconds: 1),
  width: _isOpened ? 200 : 100,
  height: _isOpened ? 200 : 100,
  color: _isOpened ? Colors.blue : Colors.red,
  child: Center(child: Text('AnimatedContainer')),
),
```
```

위 코드를 보면, **AnimatedContainer**가 **_isOpened** 변수의 값에 따라 width, height, color 등의 속성을 부드럽게 변경하고 있습니다.

## TweenAnimationBuilder는 무엇인가요?

**TweenAnimationBuilder**는 UI 요소의 애니메이션을 구현하기 위해 사용되는 위젯 중 하나로, 상태값을 변화시키는 방법을 제공합니다. 주로 커스텀 애니메이션을 구현할 때 유용하게 사용됩니다. 

예를 들어, 숫자가 증가할 때 애니메이션 효과를 줄 수 있는데, 이때 **TweenAnimationBuilder**가 유용합니다.

```
```dart
TweenAnimationBuilder(
  duration: Duration(seconds: 1),
  tween: _colorTween,
  builder: (_, Color color, __) {
    return Container(
      width: 200,
      height: 200,
      color: color,
      child: Center(child: Text('TweenAnimationBuilder')),
    );
  },
),
```
```

위 코드에서 **_colorTween**은 ColorTween 객체로, 애니메이션 동안 색상을 부드럽게 변화시킬 수 있습니다.

따라서, **AnimatedContainer**는 속성의 변화에 따라 자동으로 애니메이션을 생성하고, **TweenAnimationBuilder**는 커스텀 애니메이션을 쉽게 구현할 수 있도록 해줍니다. 이 두 가지 방법을 적절하게 활용하면 다양한 UI 애니메이션을 구현할 수 있습니다.

## 요약

이 글에서는 Flutter에서 UI 애니메이션을 구현하는 데 자주 사용되는 **AnimatedContainer**와 **TweenAnimationBuilder**에 대해 알아보았습니다. 각각의 특징과 사용 방법을 살펴보고, 간단한 예제를 통해 애니메이션 구현 방법을 알아보았습니다.

## 참고 자료

- [Flutter AnimatedContainer](https://api.flutter.dev/flutter/widgets/AnimatedContainer-class.html)
- [Flutter TweenAnimationBuilder](https://api.flutter.dev/flutter/widgets/TweenAnimationBuilder-class.html)