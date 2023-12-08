---
layout: post
title: "[flutter] AnimatedContainer의 duration 속성을 조절하여 애니메이션 속도 조절하기"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter 앱을 개발하다보면 화면 요소의 애니메이션을 사용할 때가 많습니다. 예를 들어, 화면에 요소를 추가하거나 제거할 때 부드러운 애니메이션을 적용하기 위해 `AnimatedContainer` 위젯을 사용할 수 있습니다. 이때, `duration` 속성을 조절하여 애니메이션의 속도를 커스터마이즈할 수 있습니다.

## AnimatedContainer란?

`AnimatedContainer`는 자식 위젯이 나타나거나 사라질 때 부드러운 애니메이션을 적용하는 Flutter 위젯입니다. 이 위젯을 사용하면 요소의 크기, 색상, 테두리 및 그림자를 부드럽게 변경할 수 있습니다.

## duration 속성 이해하기

`AnimatedContainer`의 `duration` 속성은 애니메이션이 실행되는 시간을 제어합니다. 기본적으로, 애니메이션의 기간을 정의하여 애니메이션의 속도를 조절하게 됩니다. 이때, duration은 `Duration` 클래스의 인스턴스여야 하며, 밀리초 단위로 작동합니다.

`AnimatedContainer`의 `duration` 속성을 변경하여 애니메이션의 속도를 높이거나 낮출 수 있습니다.

```dart
AnimatedContainer(
  duration: Duration(milliseconds: 500), // 애니메이션 속도를 높임
  // 나머지 속성들
)
```

```dart
AnimatedContainer(
  duration: Duration(milliseconds: 2000), // 애니메이션 속도를 낮춤
  // 나머지 속성들
)
```

## 결론

`AnimatedContainer`의 `duration` 속성을 조절하여 애니메이션의 속도를 커스터마이즈하는 방법을 배웠습니다. 이를 통해 앱의 UI를 더 부드럽게 만들고 사용자 경험을 향상시킬 수 있습니다.

참조: [Flutter AnimatedContainer Class](https://api.flutter.dev/flutter/widgets/AnimatedContainer-class.html)